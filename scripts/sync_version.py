from setuptools_scm import get_version
import json
import os


def sync_package_json_version():
    """Sync version from git tags to package.json"""
    version = get_version(root='..', relative_to=__file__)

    pkg_json_path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'package.json')
    with open(pkg_json_path, 'r') as f:
        data = json.load(f)

    data['version'] = version

    with open(pkg_json_path, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    sync_package_json_version()
