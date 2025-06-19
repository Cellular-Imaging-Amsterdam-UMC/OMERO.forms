from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("omero-forms")
except PackageNotFoundError:
    # Handle dev installs
    from ._version import version
    __version__ = version

default_app_config = "omero_forms.apps.FormsAppConfig"