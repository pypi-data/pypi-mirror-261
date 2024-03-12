from setuptools import setup, find_packages

setup(
    name="TineFlutterAppium",
    version="1.1.0",
    author="Pornpawit Suttha",
    author_email="pornpawit14suttha@gmail.com",
    description="This Library is support to appiumlibrary and appiumflutterlibrary",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pornpawit08/TineFlutterAppium.git",
    packages=find_packages(),
    install_requires=[
        'robotframework>=3.0', 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)