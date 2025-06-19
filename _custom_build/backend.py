import os
import subprocess
from setuptools import build_meta as _orig
from setuptools.build_meta import *


def _run_npm_build():
    """Run npm install and build if static files don't exist"""
    if not os.path.exists("omero_forms/static/forms/js"):
        subprocess.check_call(["npm", "install", "--legacy-peer-deps"])
        subprocess.check_call(["npm", "run", "build"])


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _run_npm_build()
    return _orig.build_wheel(wheel_directory, config_settings, metadata_directory)


def build_sdist(sdist_directory, config_settings=None):
    _run_npm_build()
    return _orig.build_sdist(sdist_directory, config_settings)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _run_npm_build()
    return _orig.build_editable(wheel_directory, config_settings, metadata_directory)
