import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nickgenfast",
    version="0.0.3",
    author="Dhruv Khara",
    author_email="dhruvkhara167@gmail.com",
    description="A random nickname generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BeLazy167/nickgenfast",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'nickgenfast': ['nouns.txt', 'adjectives.txt', 'verbs.txt']},
    python_requires='>=3.6',
    
)