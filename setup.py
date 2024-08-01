# setup.py
from setuptools import setup, find_packages

setup(
    name="cronpulse",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple monitor and wrap function for cron jobs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cronpulse",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
    ],
)
