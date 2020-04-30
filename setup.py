
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EEG/GSR Wellness Tracker", 
    version="0.0.1",
    author="Bar Lehmann",
    author_email="bar.lehmann@gmail.com",
    description="A package to help explore connections between EEG/GSR with self reported measures of Mood and Focus using the MNE API",
    long_description= "A package to facilitate easy introductory use of MNE Python and simple statistical analyses of EEG biometrics with self reported mood and focus ratings. Short records of about (10 seconds) can be used as entries, and GSR data can be added if possible/desired. Basic means of analyses of such connections between EEG/GSR with self reported measures of Mood and Focus are provided in the package. This package uses the MNE API",
    long_description_content_type="text/markdown",
    url="https://github.com/barlehmann/EEG_GSR_Wellness_Tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)



