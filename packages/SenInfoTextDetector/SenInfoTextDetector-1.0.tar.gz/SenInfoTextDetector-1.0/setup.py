from setuptools import setup

setup(
    name="SenInfoTextDetector",
    version="1.0",
    description="A useful module for detect sensitive information/secrets",
    author="sanket bahir",
    author_email="bahirsanket22271@gmail.com",
    install_requires=["black", "pytest", "pylint"],
    python_requires=">=3.6",
)
