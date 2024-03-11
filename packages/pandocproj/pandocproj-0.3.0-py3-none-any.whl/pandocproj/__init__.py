# -*- coding: utf-8 -*-

"""Top-level package for PandocProj."""
import logging
from appdirs import AppDirs
from pathlib import Path
import pkg_resources
import shutil
import configparser
import sys

logger = logging.getLogger("pproj")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler("pproj.log")
fh.setLevel(logging.WARNING)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

__author__ = """Nicolas Cordier"""
__email__ = "nicolas.cordier@numeric-gmbh"
__version__ = "0.3.0"

PREVIOUS_REVS_DIR = ".previous"
SETTINGS = ".settings.yaml"
REVISIONS = ".revisions.yaml"
DATEFMT = "%d %B %Y"

default_config = {
    "DEFAULT": {
        "pandoc_bin": shutil.which("pandoc"),
        "style": "default-style",
        "bootstrap_dir": "bootstrap",
        "mathjax_url": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
    },
}


def first_start():
    logging.warning(f"first start: creating configuration dir {CONFDIR}")
    CONFDIR.mkdir()
    src = Path(pkg_resources.resource_filename("pandocproj.data", "default-style"))
    target = CONFDIR / "default-style"
    shutil.copytree(src=src, dst=target)
    src = Path(pkg_resources.resource_filename("pandocproj.data", "bootstrap"))
    target = CONFDIR / "bootstrap"
    shutil.copytree(src=src, dst=target)
    src = Path(pkg_resources.resource_filename("pandocproj.data", "makefile"))
    target = CONFDIR / "makefile"
    shutil.copy(src=src, dst=target)
    # -------------------------------------------------------------------------
    # config file
    # also search for all pandoc-* stuff
    # this makes 'make pdf' compatible with pipx
    path = shutil.which("pandoc-fignos")
    if not path:
        # assume same rootdir as python bin path
        path = sys.executable
    if path:
        path = str(Path(path).parent)
    else:
        path = ""
    default_config["DEFAULT"]["pandoc_filters_path"] = str(path)
    config = configparser.ConfigParser()
    config["DEFAULT"] = default_config["DEFAULT"]
    with open(CONFDIR / "config.ini", "w") as fh:
        config.write(fh)


APPDIRS = AppDirs("pproj", "numeric")
CONFDIR = Path(APPDIRS.user_config_dir)
if not CONFDIR.exists():
    first_start()
