import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="blur",
    version="1.0",
    author="",
    author_email="",
    description="The most amazing blur suite you'll ever use!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.5",
)
