  
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fptavsss",
    version="0.0.1",
    author="Sanjay Seetharaman",
    author_email="sanjayms0111@gmail.com",
    description="FPTAS for Vector Subset Search Problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chiefsan/FPTAvssS",
    license="MIT",
    tests_require=["pytest"],
    py_modules="fptavsss",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)