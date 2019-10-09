import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="larousse-api-sunbro",
    version="0.0.2",
    author="Quentin Barbarat",
    author_email="q.barbarat@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quentin-dev/larousse_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
