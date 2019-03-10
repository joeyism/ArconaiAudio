from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('arconai/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'ArconaiAudio',
        packages = ['ArconaiAudio'], # this must be the same as the name above
        version = version,
        description = 'Downloads and unzips chromedriver to curent directory',
        long_description=long_description,
        entry_points = {
            "console_scripts": ['ArconaiAudio = arconai.cli:main']
        },
        author = 'joeyism',
        author_email = 'joeyism101@gmail.com',
        url = 'https://github.com/joeyism/ArconaiAudio', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/ArconaiAudio' + version + '.tar.gz',
        keywords = [], 
        classifiers = [],
        install_requires=['selenium', 'jsbeautifier', 'python-mpv', 'PyInquirer', 'prompt_toolkit', 'tqdm' 'autochromedriver'],
        )
