from setuptools import setup, find_packages

setup(
    name="datalib",
    version="0.1.0",
    description="A simple data manipulation and analysis library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Asma Guiza",
    author_email="asma.guiza@ieee.org",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
    ],
    extras_require={
        "dev": ["pytest", "sphinx", "tox"],
    },
    test_suite='tests',
    python_requires='>=3.7',  
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
)
