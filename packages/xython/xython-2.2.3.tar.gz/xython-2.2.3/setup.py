# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

#from sphinx.setup_command import BuildDoc
#commands["build_sphinx"] = BuildDoc


with open("README.md", "rt", encoding='UTF8') as fh:
    long_description = fh.read()
setup(
    name='xython',
    version='2.2.3',
    url='https://github.com/sjpark/xython',
    download_url='https://github.com/sjpark/xython/archive/v2.2.3.tar.gz',
    author='sjpark',
    author_email='sjpkorea@yahoo.com',
    description='Functional Programming for Excel, Word, Outlook, Color, Etc with Python',
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "xython": ["*.*"],
        },
    long_description_content_type="text/markdown",
    long_description=open('README.md', "r", encoding='UTF8').read(),
    install_requires=[''],
    python_requires='>=3.8',
    zip_safe=False,
    classifiers=['License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
    project_urls = {
      'Documentation': 'https://sjpkorea.github.io/xython.github.io/',
      'Link 1': 'https://www.xython.co.kr',
    }
    )

