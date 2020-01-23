from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def _jupyter_server_extension_paths():
    return [{
        "module": "jupyter_deps.server_extension"
    }]
