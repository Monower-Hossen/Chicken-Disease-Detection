import setuptools
import os

def get_requirements(file_path: str) -> list[str]:
    """
    Reads the requirements from the specified file.
    """
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, "r", encoding="utf-8") as f:
        # Read lines, strip whitespace, ignore empty lines and editable installs
        requirements = [
            req.strip() 
            for req in f.readlines() 
            if req.strip() and not req.startswith('-e')
        ]
    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Chicken-Disease-Detection"
AUTHOR_USER_NAME = "Monower-Hossen"
SRC_REPO = "chicken_classifier"
AUTHOR_EMAIL = "monower.cse@gmail.com" 

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for chicken disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ]
)