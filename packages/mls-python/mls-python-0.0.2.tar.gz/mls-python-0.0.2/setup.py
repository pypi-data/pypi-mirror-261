from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A modular login system'

# Setting up
setup(
    name="mls-python",
    version=VERSION,
    author="Loftea",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['ntplib', 'datetime', 'uuid', 'ast', 'importlib.util', 'hashlib'],
    keywords=['python', 'login', 'GUI', 'simple', 'modular', 'user', 'fast', 'beginner'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)