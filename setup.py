from setuptools import find_packages, setup

setup(
    name="cytocherrypick",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "seaborn",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "cytocherrypick = cytocherrypick.main:main",
        ],
    },
    author="Your Name",
    author_email="michael.lippincott@cucanschutz.edu",
    description="A tool for visualizing a miscropscopy image's feature space.",
    url="https://github.com/MikeLippincott/CytoCherryPick",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
