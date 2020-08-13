import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arithmetic-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Mike Driscoll",
    author_email="driscoll@example.com",
    description="A simple arithmetic package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/driscollis/arithmetic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)