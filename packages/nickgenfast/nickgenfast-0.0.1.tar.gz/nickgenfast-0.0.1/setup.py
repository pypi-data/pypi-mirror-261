import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nickgenfast",
    version="0.0.1",
    author="Your Name",
    author_email="dhruvkhara167@gmail.com",
    description="A random nickname generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'random'
    ],
)