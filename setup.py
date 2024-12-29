from setuptools import setup
from ChillBot import __version__

def parse_requirements_file(path):
    with open(path) as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]

setup(
    name="ChillBot.py",
    version=__version__,
    description="An API wrapper for ChillBot's API",
    long_description="Temp",
    author="RainzDev",
    author_email="jessrblx16@gmail.com",
    install_requires=parse_requirements_file("requirements.txt"),
    python_requires=">=3.10",
    project_urls={
        "Homepage": "https://github.com/RainzDev/ChillBot.py",
    }
)