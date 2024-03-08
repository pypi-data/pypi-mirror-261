from setuptools import setup, find_packages

setup(
    name="datamug",
    version="0.0.20",
    author="Erfan Varedi",
    author_email="erfanvaredi@gmail.com",
    description="Python package to generate training data with LLMs for LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt").read().splitlines(),
    url="https://github.com/erfanvaredi/datamug",
    project_urls={
        "Bug Tracker": "https://github.com/erfanvaredi/datamug/-/issues",
        "Repository": "https://github.com/erfanvaredi/datamug",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
