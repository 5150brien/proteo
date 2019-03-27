import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proteo",
    version="1.0.1",
    author="Devlin O'Brien",
    author_email="dobrien@my.ccsu.edu",
    license="MIT",
    keywords="uniprot protein bioinformatics proteomics",
    description="A simple client library for UniProt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/5150brien/proteo",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
