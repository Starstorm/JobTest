from setuptools import setup, find_packages
setup(
    name='BusinessCardParser',
    version='1.0.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
)

import subprocess
subprocess.run(["python", "-m","spacy","download","en_core_web_sm"])
