from setuptools import setup, find_packages

VERSION = '1.0.1' 
DESCRIPTION = 'Generate analog clock images'
LONG_DESCRIPTION = 'A helper that lets you generate analog clock images.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="analog-clock", 
        version=VERSION,
        author="Core447",
        author_email="core447@proton.me",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pillow"],
        keywords=['python', 'clock', "analog", "analog-clock", "pillow"],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3 :: Only",
            "Operating System :: Unix",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English"
        ],
        url="https://github.com/Core447/analog-clock",
)