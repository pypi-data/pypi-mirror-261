from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyxbst",
    version="0.0.2",
    author="Abdelouahed Ben Mhamed",
    author_email="a.benmhamed@intelligentica.net",
    description="A Python library for extended branching search trees.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benmhamed-a/pyxbst",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add any dependencies your library may have
    ]
)
