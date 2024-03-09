from setuptools import setup
import os

VERSION = "1.0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="skills_network_authoring_jupyterlab_extension",
    description="skills_network_authoring_jupyterlab_extension is now skillsnetwork-jupyter-extension",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["skillsnetwork-jupyter-extension"],
    classifiers=["Development Status :: 7 - Inactive"],
)
