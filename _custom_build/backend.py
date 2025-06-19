import os
import subprocess
import json
from setuptools import build_meta as _orig
from setuptools.build_meta import *
from setuptools_scm import get_version


def _sync_package_json_version():
    """Sync version from git tags to package.json"""
    version = get_version()

    with open("package.json", "r") as f:
        data = json.load(f)

    data["version"] = version

    with open("package.json", "w") as f:
        json.dump(data, f, indent=2)


def _run_npm_build():
    """Run npm install and build"""
    # Create directory if it doesn't exist
    os.makedirs("omero_forms/static/forms/js", exist_ok=True)
    # Sync version before npm install
    _sync_package_json_version()
    subprocess.check_call(["npm", "install", "--legacy-peer-deps"])
    subprocess.check_call(["npm", "run", "build"])


def get_requires_for_build_sdist(config_settings=None):
    """Run npm build before sdist requirements check"""
    _run_npm_build()
    return _orig.get_requires_for_build_sdist(config_settings)


def get_requires_for_build_wheel(config_settings=None):
    """Run npm build before wheel requirements check"""
    _run_npm_build()
    return _orig.get_requires_for_build_wheel(config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    return _orig.build_wheel(wheel_directory, config_settings, metadata_directory)


def build_sdist(sdist_directory, config_settings=None):
    return _orig.build_sdist(sdist_directory, config_settings)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    return _orig.build_editable(wheel_directory, config_settings, metadata_directory)
