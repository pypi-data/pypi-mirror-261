from setuptools import setup, find_packages


setup(
    name="TineAppiumFlutterLibrary",
    version="1.0.0",
    author="Pornpawit Suttha",
    author_email="pornpawit14suttha@gmail.com",
    description="This Library is support to appiumlibrary and appiumflutterlibrary",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pornpawit08/TineAppiumFlutterLibrary.git",
    packages=find_packages(),
    install_requires=[
        'robotframework>=3.0', 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)