from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Colorized text console'
LONG_DESCRIPTION = 'Python library that allows users to colorized their \
    text for any console'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="colorizedtextconsole", 
        version=VERSION,
        author="CeREF Technique",
        author_email="licence.tech@ceref.be",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        
        keywords=['python', 'Colorized text console'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)