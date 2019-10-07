from setuptools import setup, find_packages
setup(
    name='BusinessCardParser',
    version='1.0.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
	install_requires=[
        "names_dataset",
        "spacy"]
)

import subprocess
subprocess.run(["python", "-m","spacy","download","en_core_web_sm"])
