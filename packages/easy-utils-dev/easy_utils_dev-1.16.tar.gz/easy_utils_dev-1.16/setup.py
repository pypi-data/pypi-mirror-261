from setuptools import setup, find_packages

VERSION = '1.16'

# Setting up
setup(
    name="easy_utils_dev",
    version=VERSION,
    packages=find_packages(),
    install_requires=['psutil' , 'ping3' , 'flask_socketio' , 'flask_cors' , 'engineio', 'paramiko'],
    keywords=['python3'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)