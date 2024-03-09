from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="donutdb",
    version="0.1.0",
    author="Srinivas T B",
    author_email="tbsrinivas.x@gmail.com",
    description="(distributed) vector database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/notahuman-1-0/donut",
    packages=(
        find_packages(
            exclude=["demo"]
        ) +
        ["donutdb.db.index", "donutdb.db.sqlite", "donutdb.db.postgres"]
    ),
    include_package_data=True,
    install_requires=[
        "numpy",
        "hnswlib",
        "openai",
        "psycopg[c]",
        "psycopg[pool]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
