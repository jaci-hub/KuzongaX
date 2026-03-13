from setuptools import setup, find_packages

setup(
    name="kuzongax",
    version="0.1.0",
    author="Jacinto Jeje Matamba Quimua",
    description="KuzongaX Phase 1: Action-State benchmark environment for faithful strategic reasoning.",
    packages=find_packages(),
    install_requires=[
        "gymnasium>=0.29",
        "numpy>=1.23",
        "kuzongaenv>=0.3.2",
    ],
    python_requires=">=3.10",
)
