from setuptools import setup, find_packages

setup(
    name="nicotool",
    version=1.1,
    packages=find_packages(),
    author="Nico",
    description="A handy litle tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)