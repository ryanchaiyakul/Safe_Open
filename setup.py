import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Safe_Open",
    version="0.0.1",
    author="Ryan Chaiyakul",
    description="safe writing and reading of a file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanchaiyakul/Safe_Open",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
