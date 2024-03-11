import os
import re
import setuptools


def readme(file_name):
    text = open(os.path.join(os.path.dirname(__file__), file_name), encoding="utf8").read()
    return text


setuptools.setup(
    name="UnrealAPI",
    packages=setuptools.find_packages(),
    version="0.1",
    license="MIT",
    description="Python Wrapper For UnrealAPI",
    long_description=readme("README.md"),
    long_description_content_type="text/markdown",
    author="imuniq",
    author_email="im.uniq.dev@gmail.com",
    url="https://github.com/imuniq/UnrealAPI",
    keywords=["Unreal-API", "Decoder", "Unrealapi"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
)