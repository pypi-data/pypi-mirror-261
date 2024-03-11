from setuptools import setup, find_packages

setup(
    name="flysearch",
    version="0.1.3",
    author="adiorz",
    author_email="adiorz90@gmail.com",
    description="Flight Search API Wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/Adiorz/flysearch",
        "Tracker": "https://github.com/Adiorz/flysearch/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
