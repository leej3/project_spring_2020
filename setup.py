import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SNP Annotation Matrix Plot", 
    version="0.0.1",
    author="Aidan O'Brien",
    author_email="aidanobrien93@hotmail.com",
    description="Generate a binary matrix to identify putative functional SNPs co-localiseing to epigenetically enriched regions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aob93/project_spring_2020",
    scripts = ['project_code/annotation_plot.py'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
