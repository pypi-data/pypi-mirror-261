from setuptools import setup, find_packages
import os

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="check-swear",
    version="0.1.1",
    description="A profanity filter for Russian comments.",
    long_description=read('README.md'),  # Here we read the contents of README.md
    long_description_content_type="text/markdown",  
    author="Daniil Kremnev",
    author_email="legend.super567@gmail.com",
    packages=find_packages(exclude=["check_swear.tests", "check_swear.tests*", "check_swear.parsing", "check_swear.parsing*"]),  # Exclude patterns adjusted
    include_package_data=True,
    package_data={
        'check_swear.data': ['*.joblib'],
        'check_swear.model_prep': ['*.json'],
    },
    install_requires=[
        "scikit-learn>=0.24.2",
        "joblib>=1.3.2",
        "nltk>=3.8.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)