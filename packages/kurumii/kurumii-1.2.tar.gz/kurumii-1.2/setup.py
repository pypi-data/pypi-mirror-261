from setuptools import setup, find_packages

setup(
    name="kurumii",
    version=1.2,
    packages=find_packages(),
    author="Nico",
    description="A handy litle tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)