from setuptools import find_packages, setup

PACKAGE_NAME = "oeahr_package"

setup(
    name=PACKAGE_NAME,
    version="0.0.8",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["test_dyna = oeahr_package.utils:list_package_tools"],
    },
    install_requires=[
        "promptflow",
        "promptflow-tools"
    ]
)
