from pathlib import Path
import setuptools

_README = "README.md"
_REQUIREMENTS = "requirements.txt"

setuptools.setup(
    name = "pathdantic",
    version = "0.0.1",
    long_description = Path(_README).read_text(),
    long_description_content_type = "text/markdown",
    url = "https://alejoprietodavalos.github.io/",
    author = "Alejo Prieto Dávalos",
    author_email = "alejoprietodavalos@gmail.com",
    project_urls = {
        "Source": "https://github.com/AlejoPrietoDavalos/pathdantic/"
    },
    python_requires = ">=3.10,<3.12",
    install_requires = Path(_REQUIREMENTS).read_text().strip().split("\n"),
    packages = setuptools.find_packages(),
    include_package_data = True,
    #entry_points = {"console_scripts": ["carberra = "]}
)