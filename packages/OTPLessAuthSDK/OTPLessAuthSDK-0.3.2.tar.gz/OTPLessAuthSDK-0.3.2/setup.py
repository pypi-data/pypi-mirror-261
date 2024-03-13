from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="OTPLessAuthSDK",  # This is the name of the package
    version="0.3.2",  # The initial release version
    author="OTPless",  # Full name of the author
    description="otpless-auth-sdk",
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3',  # Minimum version requirement of the package
    py_modules=["OTPLessAuthSDK"],  # Name of the python package
    package_dir={'': 'OTPLessAuthSDK/'},  # Directory of the source code of the package
    install_requires=[
        'requests',
        'PyJWT',
        'rsa',
        'cryptography',
    ],
)
