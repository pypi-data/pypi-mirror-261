from setuptools import setup, find_packages


setup(
    name="tasnif",
    version="0.1.6",
    install_requires=[
        "numpy",
        "scikit-learn",
        "matplotlib",
        "Pillow",
        "scipy",
        "tqdm",
        "torch",
        "torchvision",
        "img2vec_pytorch",
    ],
    python_requires=">=3.9",
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
