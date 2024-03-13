from setuptools import setup, find_packages

from metadata import metadata
from version import get_version


setup(
    name=f"{metadata['plugin_name']}",
    version=f"{get_version()}",
    author=", ".join([author['name'] for author in metadata['authors']]),
    author_email=", ".join([author['email'] for author in metadata['authors']]),
    description=f"{metadata['description']}",
    url=f"{metadata['github_url']}",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 4 - Beta',
    ],
    python_requires=f"{metadata['python_requires']}",
    install_requires=[
        'capstone>=5.0.1',
        'flare-capa>=7.0.1',
    ],
    test_suite='yaraforge.tests',
)


