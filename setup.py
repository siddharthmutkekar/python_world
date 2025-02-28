import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_world",
    version="0.0.1",
    author="Siddharth Mutkekar",
    author_email="siddharthmutkekar@in.ibm.com",
    description="A function that returns 'world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SiddharthMutkekar/python_world",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)