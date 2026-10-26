from setuptools import setup, find_packages

setup(
    name="dna-mass-sonifier",
    version="1.0.0",
    author="Patrick Grate",
    author_email="grate.pat@gmail.com",
    description="An algorithmic framework mapping DNA molecular mass directly to absolute musical frequencies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],
    python_requires=">=3.6",
)
