

from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1.0",
    description="A Python-C++ hybrid project with PyTorch integration",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    install_requires=[
        "torch",
        "numpy",
        "pybind11"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS"
    ],
    python_requires=">=3.8",
)