import os
import versioneer
from setuptools import setup, find_packages


def read_file(filename):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath) as file:
        return file.read()


def get_data_files():
    data_files = [
        # ('etc/jupyter/jupyter_server_config.d', ['etc/jupyter/jupyter_server_config.d/voila.json']),
        # Like: jupyter serverextension enable --py jupyter_deps
        ('etc/jupyter/jupyter_notebook_config.d', ['etc/jupyter/jupyter_notebook_config.d/jupyter-deps.json']),
        # ('etc/jupyter/nbconfig/notebook.d', ['etc/jupyter/nbconfig/notebook.d/voila.json']),
        # ('share/jupyter/nbextensions/voila', ['voila/static/extension.js'])
    ]
    return data_files

print("JUPYTER-deps DATA FILES:\n", get_data_files())

setup(
    name="jupyter-deps",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Jupyter extension to manage Python dependencies",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Daniel Rodriguez",
    author_email="df.rodriguez143@gmail.com",
    url="https://github.com/danielfrg/jupyter-deps",
    license="Apache 2.0",
    python_requires=">=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    install_requires=read_file("requirements.txt").splitlines(),
    keywords=["jupyter", "ipython", "dependencies"],
    packages=find_packages(),
    include_package_data=True,
    data_files=get_data_files(),
    zip_safe=False,
)
