#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""

import argparse
from pathlib import Path
import os
import shlex
import shutil
import sys
import tempfile
import time
from datetime import datetime as dt
from os.path import join as pjoin
from pprint import pformat
from subprocess import call, check_output

try:
    from selenium import webdriver

    BROWSER = None
    IS_SELENIUM = True
except Exception as exc:
    import webbrowser

    print("ERR: no selenium. Try conda install geckodriver")
    IS_SELENIUM = False


from . import (
    DATEFMT,
    PREVIOUS_REVS_DIR,
    REVISIONS,
    SETTINGS,
    __email__,
    __version__,
    logger,
)
from .utils import _dump_revisions_table, _dump_yaml, getconf
from .utils import commit as _commit
from .utils import (
    get_filename,
    get_mdfile_conf,
    get_revisions_conf,
    get_revisions_info,
    new_project,
)
from .utils import rollback as _rollback
from .utils import switch_ext


PANDOC_EXECS = [
    "/usr/bin/pandoc",
    "/opt/anaconda/bin/pandoc",
    "/opt/anaconda3/bin/pandoc",
]
for b in PANDOC_EXECS:
    if os.path.isfile(b):
        PANDOC_BIN = b
        PANDOC_VERSION = check_output(shlex.split("%s --version" % b)).decode()
        PANDOC_VERSION = PANDOC_VERSION.split("\n")[0]
        break
else:
    logger.warning("no binary found for pandoc")


def general(args):
    if args.version is True:
        print("PandocProj %s" % __version__)
        print("%s" % __email__)
        print("****")
        print("Install Path:   %s" % os.path.split(os.path.realpath(__file__))[0])
        print("Python exec:    %s" % sys.executable)
        print("Python version: %s" % sys.version.split("\n")[0])
        print("Pandoc exec:    %s" % PANDOC_BIN)
        print("Pandoc version: %s" % PANDOC_VERSION)
        return


def commit(args):
    """wrapper for _commits(projdir, datefmt)"""
    projdir = args.dir
    prepro(args)
    _commit(projdir, DATEFMT)


def rollback(args):
    """wrapper for _rollback(projdir, datefmt)"""
    projdir = args.dir
    datefmt = DATEFMT
    _rollback(projdir, datefmt)


def prepro(args):
    projdir = args.dir
    curfile, current_rev, revisions = get_revisions_info(projdir)
    logger.info("Preprocessing current file: %s" % curfile)
    # ------------------------------------------------------------------------
    # override 'revision_description' recovered from md file
    mdfile_conf = get_mdfile_conf(projdir)
    for k, v in mdfile_conf.items():
        v = str(v)
        logger.debug("**%s**:%s" % (k, v.replace("\n", "")))
    rev_description = get_mdfile_conf(projdir).get("revision_description", "XXX")
    logger.info('rev description from MD: "%s"' % rev_description)
    rev_date = get_mdfile_conf(projdir).get("date", dt.strftime(dt.now(), DATEFMT))
    author = get_mdfile_conf(projdir).get("author", "???")
    revisions = get_revisions_conf(projdir)
    # get latest revision and update 'comment'
    revisions["date"] = rev_date
    logger.info("dump %s" % pformat(revisions))
    _dump_yaml(pjoin(projdir, REVISIONS), data=revisions)
    _revisions = revisions["revisions"].copy()
    # add current revision data
    _revisions.append(
        {
            "rev": revisions["revision"],
            "date": revisions["date"],
            "author": mdfile_conf["author"],
            "comment": mdfile_conf["revision_description"],
        }
    )
    _dump_revisions_table(curfile, _revisions)


def pdfdiff(args):
    projdir = args.dir
    prepro(args)
    # ------------------------------------------------------------------------
    # current file data
    current_file, current_rev, revisions = get_revisions_info(projdir)
    current_dir = "."
    # ------------------------------------------------------------------------
    # previous file data    # negative reference is relative to current rev
    available_revs = [r["rev"] for r in revisions]
    previous_rev = args.previous_rev
    if previous_rev < 0:
        previous_rev = current_rev + previous_rev
    if previous_rev not in available_revs:
        raise ValueError("Revision %d does not exist" % previous_rev)
    previous_file = get_filename(projdir, previous_rev)
    previous_dir = pjoin(PREVIOUS_REVS_DIR, str(previous_rev))
    # ------------------------------------------------------------------------
    # generate `.tex` files
    call(["make", "-C", previous_dir, "tex"])
    call(["make", "tex"])
    mda = pjoin(current_dir, current_file)
    mdb = pjoin(previous_dir, previous_file)
    texa = switch_ext(mda, ".tex")
    texb = switch_ext(mdb, ".tex")

    difftex = get_revisions_conf(projdir)["filename"]  # root filename
    difftex += "_diff.tex"
    diffpdf = switch_ext(difftex, ".pdf")
    latexdiffargs = ["latexdiff", "--type=%s" % args.type]
    latexdiffargs += ["--floattype=IDENTICAL", "--graphics-markup=none"]
    latexdiffargs += [texb, texa]
    cmd = " ".join(latexdiffargs)
    print(cmd)
    diff = check_output(latexdiffargs)
    with open(difftex, "w") as fh:
        fh.write(diff.decode())
    # finally, generate diff pdf
    tmp = tempfile.mkdtemp()
    pdfargs = ["latexmk", "-pdf", "-synctex=1", "-output-directory=%s" % tmp, difftex]
    try:
        call(pdfargs)
    except Exception as exc:
        logger.exception(exc)
        logger.info('an error occured. Check "%s" dir', tmp)
        logger.info('command was "%s"', " ".join(pdfargs))
    else:
        logger.info("results are in %s", tmp)
    shutil.copy(pjoin(tmp, diffpdf), switch_ext(mda, ".pdf"))
    # clean
    for file_ in (texa, texb, difftex):
        os.remove(file_)


def _find_files(path):
    files = [f for f in os.listdir(path)]
    return dict(
        [
            (f, os.path.getmtime(f))
            for f in files
            if os.path.splitext(f)[-1] in (".md", ".pdc", ".pandoc")
        ]
    )


def _get_output(tmpdir, input):
    fname = os.path.split(input)[-1]
    fname = os.path.splitext(fname)[0] + ".html"
    fpath = os.path.join(tmpdir, fname)
    return fpath


def _refresh_browser(file, refresh_only=False, anchor="@"):
    """opens or refresh html static file"""
    if not IS_SELENIUM:
        logger.warning("selenium is not installed")
        webbrowser.open(file, new=0)
        return
    url = "file://" + file + "#%s" % anchor
    if BROWSER.current_url != url:
        BROWSER.get(url)
    if refresh_only:
        try:
            BROWSER.refresh()
            logger.info("refreshed browser")
        except:
            logger.info(f"loading {url}")
            BROWSER.get(url)
    else:
        logger.info(f"loading {url}")
        BROWSER.get(url)


def servei(args):
    """serve MD file in local dir, based on inotify"""
    import tempfile
    import inotify.adapters

    if IS_SELENIUM:
        global BROWSER
        BROWSER = webdriver.Firefox()
    cwd = Path(os.path.abspath(os.path.curdir))
    anchor = args.anchor
    master_md_file = args.master_md_file
    if not master_md_file:
        master_md_file = guess_master_md_file(cwd).relative_to(cwd)
    else:
        master_md_file = Path(master_md_file)
    if not anchor:
        anchor = "@"
    with tempfile.TemporaryDirectory(prefix="PPROJ") as tmpdir:
        print("serving from %s into %s" % (cwd, tmpdir))
        target = Path(tmpdir) / cwd.name
        _output = _get_output(target, master_md_file)
        shutil.copytree(cwd, target, symlinks=True)
        i = inotify.adapters.InotifyTree(str(cwd))
        keep_events = {"IN_MODIFY", "IN_CREATE", "IN_DELETE"}
        watched_extensions = {
            ".md",
            ".jpg",
            ".yaml",
            ".yml",
            ".png",
            ".svg",
            ".latex",
            ".css",
            ".csv",
        }
        cmd = ["make", "-C", target, "html"]
        check_output(cmd)
        _refresh_browser(_output, refresh_only=False, anchor=anchor)
        for event in i.event_gen(yield_nones=False):
            # synchronize changed file
            (_, type_names, path, filename) = event
            path = Path(path)
            relpath = path.relative_to(cwd)
            src = path / filename
            _target = target / relpath / filename
            type_names = set(type_names) & keep_events
            if type_names and src.suffix in watched_extensions:
                if type_names == {"IN_DELETE"} and _target.exists():
                    _target.unlink()
                if src.exists():
                    shutil.copy(src, _target)
                # trigger compilation
                check_output(cmd)
                # refresh web browser
                _refresh_browser(_output, refresh_only=True, anchor=anchor)


def guess_master_md_file(dir):
    dir = Path(dir)
    suspects = list(dir.glob(f"{dir.name}_r*.md"))
    return suspects[0]


def version(args):
    filters = (
        "panflute",
        "pandoc_eqnos",
        "pandoc_fignos",
        "pantable",
        "pandoc_tablenos",
        "pandoc_latex_admonition",
        "tabulate",
        "selenium",
        "inotify",
    )
    import pkg_resources
    from pandocproj import __version__

    print(40 * "=")
    print(f"pandocproj: {__version__}")
    print(40 * "=")
    print("external dependancies:")

    # -------------------------------------------------------------------------
    # get pandoc version
    pandoc_bin = getconf(args.profile)["pandoc_bin"]
    pv = check_output([pandoc_bin, "--version"])
    pv = pv.decode().split("\n")[0].split()[-1]
    print(f"  * pandoc: {pv} ({pandoc_bin})")

    for modulename in filters:
        try:
            version = pkg_resources.get_distribution(modulename).version
            prefix = ""
        except pkg_resources.DistributionNotFound:
            version = "missing!"
            prefix = "ERROR: "
        print(f"  * {prefix}{modulename}: {version}")


def parse_args(args):
    """parse arguments from CLI"""
    parser = argparse.ArgumentParser(description="Pandoc Project.")
    parser.add_argument(
        "-v", "--version", action="store_true", help="Show Version and exit"
    )
    parser.add_argument("-p", "--profile", default="DEFAULT", help="profile name")
    parser.set_defaults(process=general)
    subparsers = parser.add_subparsers(help="sub-command help")
    # ------------------------------------------------------------------------
    # pproj serve
    parser_serve = subparsers.add_parser("serve", help="serve source file as HTML")
    parser_serve.add_argument("-a", "--anchor", type=str, help="anchor to follow")
    parser_serve.add_argument(
        "-m",
        "--master-md-file",
        type=str,
        help="master markdown file to trigger compilation on",
    )
    parser_serve.set_defaults(process=servei)
    # -------------------------------------------------------------------------
    # pproj version
    parser_version = subparsers.add_parser("version", help="version informations")
    parser_version.set_defaults(process=version)
    # ------------------------------------------------------------------------
    # pproj init
    parser_init = subparsers.add_parser("init", help="create a project")
    parser_init.add_argument("dir", type=str, help="path to new project")
    parser_init.add_argument("--filename", type=str, help="name of the tracked file")
    parser_init.add_argument("-a", "--author", type=str, help="Author's name")
    parser_init.add_argument(
        "--lof", action="store_true", help="include list of figures"
    )
    parser_init.add_argument(
        "--lot", action="store_true", help="include list of tables"
    )
    parser_init.add_argument(
        "--toc", action="store_true", help="include table of content"
    )
    parser_init.add_argument(
        "-n", "--sections-nb", action="store_true", help="numer sections"
    )
    parser_init.add_argument(
        "-i", "--interactive", action="store_true", help="additional settings"
    )
    parser_init.add_argument(
        "-f",
        "--from-file",
        type=str,
        help="import file as initial content",
        default=None,
    )
    parser_init.set_defaults(process=new_project)
    # ------------------------------------------------------------------------
    # pproj commit
    parser_commit = subparsers.add_parser("commit", help="commit and upgrade revision")
    parser_commit.add_argument(
        "-d", "--dir", default=".", type=str, help="Project path"
    )
    parser_commit.set_defaults(process=commit)
    # ------------------------------------------------------------------------
    # pproj rollback
    parser_rollback = subparsers.add_parser(
        "rollback", help="rollback to previous revision"
    )
    parser_rollback.add_argument(
        "-d", "--dir", default=".", type=str, help="Project path"
    )
    parser_rollback.set_defaults(process=rollback)
    # ------------------------------------------------------------------------
    # pproj prepro
    parser_prepro = subparsers.add_parser("prepro", help="prepro to previous revision")
    parser_prepro.add_argument(
        "-d", "--dir", default=".", type=str, help="Project path"
    )
    parser_prepro.set_defaults(process=prepro)
    # ------------------------------------------------------------------------
    # pproj pdfdiff
    parser_pdfdiff = subparsers.add_parser(
        "pdfdiff", help="pdfdiff to previous revision"
    )
    parser_pdfdiff.add_argument(
        "-d", "--dir", default=".", type=str, help="Project path"
    )
    parser_pdfdiff.add_argument(
        "-r", "--previous-rev", default=-1, type=int, help="Base revision"
    )
    parser_pdfdiff.add_argument(
        "-t",
        "--type",
        type=str,
        default="CHANGEBAR",
        help=(
            "Change highlights settings."
            " One within {UNDERLINE CTRADITIONAL TRADITIONAL CFONT"
            " FONTSTRIKE INVISIBLE CHANGEBAR CCHANGEBAR CULINECHBAR"
            " CFONTCBHBAR BOLD PDFCOMMENT}"
        ),
    )
    parser_pdfdiff.set_defaults(process=pdfdiff)
    # ========================================================================
    # return default func
    # ========================================================================
    return parser.parse_args(args)


def main(args=None):
    """The main routine."""
    if not args:
        # from command line
        args = parse_args(sys.argv[1:])
    else:
        # from test cases
        args = parse_args(args)
    if args.version:
        general(args)
        return
    return args.process(args)


if __name__ == "__main__":
    main()
