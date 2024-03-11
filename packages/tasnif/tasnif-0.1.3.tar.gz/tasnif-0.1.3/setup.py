from setuptools import setup, find_packages


# Function to read the requirements from the requirements.txt file
def read_requirements():
    with open("requirements.txt", "r") as req:
        return [line.strip() for line in req.readlines() if not line.startswith("#")]


setup(
    name="tasnif",
    version="0.1.3",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.6",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    description="A simple library for unsupervised image clustering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cobanov/tasnif",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
