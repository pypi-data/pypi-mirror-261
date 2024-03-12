from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="crypto-ai-agent",
    version="0.0.9",
    author="Voltfin Crypto",
    author_email="zinnober.haus@gmail.com",
    description="Import your own Crypto AI Agent to help fetch, analyze, learn, understand and streamline your crypto work",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    long_description=description,
    long_description_content_type="text/markdown",
)
