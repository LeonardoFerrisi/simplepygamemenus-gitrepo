import setuptools
from setuptools import find_packages
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="simplepygamemenus",
    version="0.0.9.1",
    author="Leonardo Ferrisi",
    author_email="ferrisil@union.edu",
    package_dir={'simplepygamemenus': 'simplepygamemenus'},
    packages=find_packages(),
    package_data={'simplepygamemenus': ['assets/rect.png', 'assets/font.ttf', 'menu.py']},
    data_files=[('simplepygamemenus/assets', ['rect.png', 'font.ttf'])],
    include_package_data=True,
    description="A package for making simple menus for your python games!",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeonardoFerrisi/simplepygamemenus-gitrepo",
    license='MIT',
    python_requires='>=3.8',
    install_requires=["pygame"]
)