#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Use full functions"""

import fileinput
from pathlib import Path
import configparser
import logging
import os
import re
import shlex
import shutil
from collections import OrderedDict as OD
from datetime import datetime as dt
from distutils.dir_util import copy_tree
from getpass import getuser
from os.path import join as pjoin
from subprocess import call

import pkg_resources
import tabulate
import yaml

from . import DATEFMT, PREVIOUS_REVS_DIR, REVISIONS, SETTINGS, CONFDIR

logger = logging.getLogger("pproj")

DEFAULT_META = {
    "title": "Quotation",
    "subtitle": "Decompression Training",
    "papersize": "a4",
    "geometry": "margin=3cm",
    "documentclass": "article",
    "author": getuser(),
    "coverpage": True,
    "myref": "MyReference",
    "otherref": "*NA*",
    "lof": True,
    "lot": True,
    "toc": True,
    "numbersections": True,
    "linkcolor": "magenta",
    "pandoc-latex-admonition": [
        {
            "color": "firebrick",
            "classes": ["admonition", "warning"],
            "nobreak": False,
            # 'margin': -4,
            # 'innermargin': 5
        },
        {
            "color": "green",
            "classes": ["tip"],
            "nobreak": False,
            # 'margin': -4,
            # 'innermargin': 5
        },
        {
            "color": "gray",
            "classes": ["note"],
            "nobreak": False,
            # 'margin': -4,
            # 'innermargin': 5
        },
    ],
}


def _load_yaml(metafile):
    with open(metafile, "r") as yamlfile:
        lines = yamlfile.readlines()
    # first, get rid of "---"
    cleaned = []
    for line in lines:
        if line.startswith("---"):
            continue
        cleaned.append(line)
    yamldata = "\n".join(cleaned)
    data = yaml.safe_load(yamldata)
    return data


def _dump_yaml(metafile, data, default_flow_style=False):
    with open(metafile, "w") as yamlfile:
        yamlfile.write("---\n")
        yamlfile.write(
            (yaml.dump(data, width=80, default_flow_style=default_flow_style))
        )
        yamlfile.write("---\n")


def create_makefile(where, config):
    with open(
        pkg_resources.resource_filename("pandocproj.data", "makefile"), "r"
    ) as fh:
        data = fh.read()
    data = data.replace("PANDOC_BIN=!!\n", f"PANDOC_BIN={config['pandoc_bin']}\n")
    data = data.replace("MATHJAX_URL=!!\n", f"MATHJAX_URL={config['mathjax_url']}\n")
    data = data.replace(
        "PANDOC_FILTERS_PATH=!!\n",
        f"PANDOC_FILTERS_PATH={config['pandoc_filters_path']}\n",
    )

    with open(where / "makefile", "w") as fh:
        fh.write(data)


PANDOC_TPL = r"""

"""

REV = re.compile(r"^revision:\s*(\d+)")


def get_settings_conf(projdir):
    metafile = pjoin(projdir, SETTINGS)
    data = _load_yaml(metafile)
    return data


def get_revisions_conf(projdir):
    metafile = pjoin(projdir, REVISIONS)
    data = _load_yaml(metafile)
    return data


def get_mdfile_conf(projdir, mix_settings=True):
    conf = {}
    if mix_settings:
        conf.update(get_settings_conf(projdir))

    conf.update(_read_file_yaml(get_filename(projdir)))
    return conf


def get_revisions_info(projdir, rev=None, check_isfile=True):
    """parse revisions.yaml to get use full info"""
    data = get_revisions_conf(projdir)
    fname = data["filename"]
    if rev is None:
        # get latest revision (current one)
        rev = data["revision"]
    current_file = "{fname}_r{rev:02d}.md".format(fname=fname, rev=rev)
    if check_isfile and not os.path.isfile(pjoin(projdir, current_file)):
        raise ValueError("File %s does not exist" % current_file)
    return current_file, rev, data["revisions"]


def get_filename(projdir, rev=None):
    current_file, rev, revisions = get_revisions_info(
        projdir, rev=rev, check_isfile=False
    )
    return current_file
    data = get_revisions_conf(projdir)


def switch_ext(filename, ext):
    return os.path.splitext(filename)[0] + ext


def rollback(projdir, datefmt):
    """rollback to previous version"""
    metafile = pjoin(projdir, REVISIONS)
    data = _load_yaml(metafile)
    filename = data["filename"]
    current_rev = data["revision"]
    target_rev = current_rev - 1
    print("rollback from %d to %d" % (current_rev, target_rev))
    # ------------------------------------------------------------------------
    # handle files
    ARCHIVES = pjoin(projdir, PREVIOUS_REVS_DIR, str(target_rev))
    current_md = filename + "_r%.2d" % current_rev + ".md"
    call(["make", "clean"])
    # shutil.rmtree('fig')
    # shutil.rmtree('.fig')
    # os.remove('makefile')
    os.remove(current_md)
    copy_tree(ARCHIVES, ".")
    shutil.rmtree(ARCHIVES)
    return current_rev, target_rev


def commit(projdir, datefmt):
    """upgrade to new version"""
    # ------------------------------------------------------------------------
    # read `meta.yaml` to get current informations for commit
    mdfile_conf = get_mdfile_conf(projdir)  # MD + .settings.yaml
    revisions = get_revisions_conf(projdir)
    filename = revisions["filename"]
    current_rev = revisions["revision"]
    current_date = revisions["date"]
    # ------------------------------------------------------------------------
    # update REVISIONS current data
    target_rev = current_rev + 1
    revisions["revision"] = target_rev
    revisions["date"] = dt.strftime(dt.now(), datefmt)
    revisions["revisions"] += [
        {
            "rev": current_rev,
            "author": mdfile_conf["author"],
            "date": current_date,
            "comment": mdfile_conf["revision_description"],
        }
    ]

    # ------------------------------------------------------------------------
    # create new file
    old_filename = filename + "_r%.2d" % current_rev + ".md"
    new_filename = filename + "_r%.2d" % target_rev + ".md"
    shutil.copy(old_filename, new_filename)
    # archive old file
    ARCHIVES = pjoin(projdir, PREVIOUS_REVS_DIR, str(current_rev))
    os.makedirs(ARCHIVES, exist_ok=True)

    for ext in (
        ".md",
        ".pdf",
        ".html",
        ".docx",
        ".rtf",
        ".odt",
        ".epub",
        ".tex",
    ):
        fname = os.path.splitext(old_filename)[0] + ext
        if os.path.isfile(fname):
            shutil.move(fname, ARCHIVES)
    # also copy `fig`, yaml files and makefile
    _projdir = Path(projdir)
    if (_projdir / "fig").exists():
        shutil.copytree("fig", pjoin(ARCHIVES, "fig"))
    if (_projdir / "static").exists():
        shutil.copytree("static", pjoin(ARCHIVES, "static"))
    shutil.copytree(".style", pjoin(ARCHIVES, ".style"))
    shutil.copy("makefile", ARCHIVES)
    shutil.copy(REVISIONS, ARCHIVES)
    shutil.copy(SETTINGS, ARCHIVES)
    _dump_yaml(pjoin(projdir, REVISIONS), revisions)
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
    _dump_revisions_table(new_filename, _revisions)
    return current_rev, target_rev


def _read_file_yaml(mdfile):
    """because some data may be stored in MD file itself,
    this method provides a way to read them
    """
    # From http://pandoc.org/MANUAL.html#extension-pandoc_title_block
    #
    # A YAML metadata block is a valid YAML object, delimited by a line of
    # three hyphens (---) at the top and a line of three hyphens (---) or three
    # dots (...) at the bottom. A YAML metadata block may occur anywhere in the
    # document, but if it is not at the beginning, it must be preceded by a
    # blank line.

    # this means that we cannot be sure we are in a YAML block as long as we
    # didn't check the closing block line
    yaml_datas = []  # {starting_line: [lines]}
    IN_YAML = False
    with open(mdfile, "r") as fh:
        for i, line in enumerate(fh):
            if line.strip() == "---" and not IN_YAML:
                # ------------------------------------------------------------
                # Suspect YAML block beginning
                yaml_lines = []
                IN_YAML = True
                logger.debug("suspect YAML starting at line %d", i)
            elif IN_YAML and (line.strip() == "---" or line.strip() == "..."):
                # ------------------------------------------------------------
                # end of suspected YAML block
                IN_YAML = False
                logger.debug("suspect YAML stopping at line %d", i)
                try:
                    yaml_data = yaml.safe_load("\n".join(yaml_lines))
                    logger.debug("yaml keys: %s", yaml_data.keys())
                except Exception as exc:
                    # not a regular Yaml block
                    logger.warning(exc)
                    logger.debug("not a valid YAML block")
                    continue
                else:
                    # regular yaml block
                    yaml_datas.append(yaml_data)
            elif IN_YAML:
                # ------------------------------------------------------------
                # regular lines of yaml block
                yaml_lines.append(line)
    # concatenate...
    yaml_datas = yaml_datas[::-1]
    if len(yaml_datas) > 0:
        inline_conf = yaml_datas.pop(0)
        for d in yaml_datas:
            inline_conf.update(d)
        return inline_conf
    return {}


def _dump_revisions_table(filename, revisions):
    """given a revisions dict, dump a table in all *.md files"""
    # turn list of dicts into dict made of lists
    # get all keys (columns)
    table = {"rev": 0, "date": 1, "author": 2, "comment": 3}
    table = OD(sorted(table.items(), key=lambda t: t[1]))
    for k, v in table.items():
        table[k] = []
    # sort revisions
    revisions = sorted(revisions, key=lambda x: int(x["rev"]))
    for rev in revisions:
        for k, v in rev.items():
            table[k].append(v)
    table_str = tabulate.tabulate(table, headers="keys")

    IN_REVISIONS = False
    for line in fileinput.FileInput(filename, inplace=1):
        if "BEGIN REVISIONS" in line:
            IN_REVISIONS = True
            print(line, end="\n")
            print(table_str, end="\n")
            print("\nTable: Document Revisions. {#tbl:_rev_}")
            print("", end="\n")
            continue
        elif "END REVISIONS" in line:
            IN_REVISIONS = False
            print(line, end="")
            continue
        if not IN_REVISIONS:
            print(line, end="")
        else:
            # skip all the lines
            continue


def getconf(profile):
    """read pproj config file"""
    config = configparser.ConfigParser()
    config.read(CONFDIR / "config.ini")
    return config[profile]


def new_project(args):
    """creates a new project"""
    conf = DEFAULT_META.copy()
    if args.author is not None:
        conf["author"] = args.author
    for arg in ("lof", "lot", "toc", "sections_nb"):
        conf[arg] = getattr(args, arg)
    dir_ = Path(args.dir).resolve()
    filename = args.filename
    if not filename:
        filename = dir_.name
    # force extension to ".md"
    fname, ext = os.path.splitext(filename)
    if ext and ext != ".md":
        logger.warning('force extension to ".md"')
    filename = fname + "_r00.md"
    root_filename = fname  # FIXME: probably useless to add extension
    conf["myref"] = fname
    if args.interactive:
        for k, v in conf.items():
            if isinstance(v, bool):
                coerce = _bool
                within = "yn"
                default = "y"
            else:
                coerce = type(v)
                within = None
                default = v
            conf[k] = _ask(k, coerce=coerce, within=within, default=default)
        # --------------------------------------------------------------------
        # abstract or not abstract?
        is_abstract = _ask("Create an abstract?", "y", within="yn", coerce=_bool)
        if not is_abstract:
            # clean pandoc tpl
            conf.pop("abstract")
    bootstrap_conf = dict(getconf(profile=args.profile).items())
    # ------------------------------------------------------------------------
    # create dir
    shutil.copytree(CONFDIR / bootstrap_conf["bootstrap_dir"], dir_)
    # dir_.mkdir()
    meta_yaml = dir_ / SETTINGS
    _dump_yaml(meta_yaml, conf)
    # ------------------------------------------------------------------------
    # default revisions.yaml
    conf2 = {}
    date = dt.strftime(dt.now(), DATEFMT)
    conf2["filename"] = root_filename
    conf2["revision"] = 0
    conf2["revisions"] = []  # no committed revision
    meta_yaml = dir_ / REVISIONS
    _dump_yaml(meta_yaml, conf2)
    # ------------------------------------------------------------------------
    # create pandoc document
    shutil.copytree(CONFDIR / bootstrap_conf["style"], dir_ / ".style")
    # "templates" -> ".style"
    # rename dir_/pandoc_tpl.md
    shutil.move(dir_ / "pandoc_tpl.md", dir_ / filename)
    # -------------------------------------------------------------------------
    # copy makefile
    create_makefile(where=dir_, config=bootstrap_conf)
    # ------------------------------------------------------------------------
    # init file
    source = args.from_file
    if source:
        source = os.path.join(os.getcwd(), source)
        # override filename with source content
        cmd = "make --directory={} source MD_SOURCE={} MD_TARGET={}".format(
            dir_, source, filename
        )
        call(shlex.split(cmd))
        print(dir_)
        # ---------------------------------------------------------------------
        # now, add default yaml header block
        target = Path(dir_) / filename
        block = """
---
revision_description: inital release
---


<!--PANDOC MANUAL: http://pandoc.org/MANUAL.html-->

\newpage


Document Revisions
==================

The following revisions have been issued:

<!--BEGIN REVISIONS-->
<!--END REVISIONS-->

<!-- end of header -->

"""
        with open(target, "r") as fh:
            lines = fh.read()
        lines = block + lines
        with open(target, "w") as fh:
            fh.write(lines)


def _bool(value):
    if value.lower() in ("y", "yes", 1, "1", "true", True):
        return True
    return False


def _ask(question, default=None, coerce=str, within=None):
    """interactively ask some questions"""
    if default:
        question = question + " [%s]" % default
    while True:
        ans = input(question + ": ")
        if not ans and default:
            ans = default
        # ------------------------------------------------------------------------
        # check within
        if within and ans not in within:
            print("answer shall be within %s" % list(within))
            continue
        # ------------------------------------------------------------------------
        # check type
        try:
            ans = coerce(ans)
        except Exception as exc:
            logger.debug(exc)
            print('cannot coerce var "%s" to %s' % (ans, coerce))
        else:
            break
    return ans
