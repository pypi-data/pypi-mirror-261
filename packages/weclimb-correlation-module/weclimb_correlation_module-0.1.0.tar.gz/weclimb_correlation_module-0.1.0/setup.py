from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="weclimb_correlation_module",
    version="0.1.0",
    author="Shiv Shankar Singh",
    author_email="shivshankarsingh.py@gmail.com",
    description="A module for climate data correlation analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shiv3679/weclimb_modules",
    project_urls={
        "Bug Tracker": "https://github.com/shiv3679/weclimb_modules/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),  # This automatically finds packages in the current directory
    python_requires=">=3.6",
    install_requires=[
        "xarray>=0.16.2",
        "pandas>=1.1.5",
        "matplotlib>=3.3.4",
        "seaborn>=0.11.1",
        "numpy>=1.19.5"
    ],
    license="GPL-3.0",
)
