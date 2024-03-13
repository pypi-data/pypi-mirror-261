import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataPrepKitz",
    version="0.1.0",
    author="zuhairalorfahly",
    author_email="zuhairalorfahly@gmail.com",
    description="A package for data preprocessing tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zuhair31002/DataPrepKitz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
    ],
)