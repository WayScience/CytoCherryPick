from setuptools import find_packages, setup

# pull requirements for install_requires
with open("requirements.txt") as f:
    REQUIRED_PKGS = f.read().splitlines()

setup(
    name="cytocherrypick",
    version="0.1",
    packages=find_packages(),
    install_requires=REQUIRED_PKGS,
    entry_points={
        "console_scripts": [
            "cytocherrypick = cytocherrypick.main:main",
        ],
    },
    author="Your Name",
    author_email="michael.lippincott@cucanschutz.edu",
    description="A tool for visualizing a miscropscopy image's feature space.",
    url="https://github.com/WayScience/CytoCherryPick",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
)
