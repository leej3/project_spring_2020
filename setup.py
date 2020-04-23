import setuptools
from pathlib import Path


SCRIPTS = [str(f) for f in Path('scripts').glob('*program.py')]
long_description = "some text"

setuptools.setup(
    name="johns_package",
    version="0.0.1",
    author="Me",
    author_email="me@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/packaging_demo",
    packages=setuptools.find_packages(),
    scripts = SCRIPTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
