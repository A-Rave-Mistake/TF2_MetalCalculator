from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

with open("requirements.txt") as f:
    lines = [line for line in f.readlines()]
    requirements = [x.strip() for x in lines]

setup(
    name="TF2_Metal_Calculator_ARaveMistake",
    version="1.0.0",
    description="Team Fortress 2 Metal Calculator - enter value and display total amounts of keys and metal you need.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/A-Rave-Mistake/TF2_MetalCalculator",
    author="A-Rave-Mistake",
    author_email="adrian.urbaniak1336@gmail.com",
    license=license,
    classifiers=[
                    "Topic :: Software Development",
                    "Programming Language :: Python :: 3.11",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: Microsoft :: Windows :: Windows 10",
],
    packages=find_packages(exclude=('tests', 'dist', '.git')),
    install_requires=requirements,
    include_package_data=True,
)