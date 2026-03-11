"""Setup configuration for google-adk demo projects."""

from setuptools import setup, find_packages

setup(
    name="google-adk-demos",
    version="1.0.0",
    description="Demonstration projects for Google Agent Development Kit (ADK)",
    author="ADK Course Team",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "google-adk>=0.1.0",
        "pydantic>=2.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
    ],
)
