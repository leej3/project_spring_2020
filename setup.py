import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_name", 
    version="0.0.1",
    author="put_your_name_here",
    author_email="insert_email",
    description="insert package description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aob93/project_spring_2020",
    scripts = ['annotation_plot.py'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
