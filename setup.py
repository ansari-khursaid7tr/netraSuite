from setuptools import setup, find_packages
from netrasuite.__version__ import __version__

setup(
    name='netrasuite',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'rich',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'netrasuite=netrasuite.main:main',
        ],
    },
    author='Your Name',
    description='LLM-Powered Network Security Assistant',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires='>=3.8',
)
