from setuptools import setup, find_packages

setup(
    name="dna-mass-sonifier-pg",
    version="1.0.8",
    author="Patrick Grate",
    author_email="grate.pat@gmail.com",
    description="An algorithmic framework mapping DNA molecular mass directly to absolute musical frequencies.",
    long_description="An algorithmic framework mapping DNA molecular mass directly to absolute musical frequencies to eliminate subjective scaling bias.",
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com",
        "Preprint / Paper": "https://zenodo.org",
        "Bug Tracker": "https://github.com/issues",
    },
    python_requires=">=3.7",
)
