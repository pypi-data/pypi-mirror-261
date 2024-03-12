from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Run async functions in synchronous mode'
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="asyncoff2",
    version=VERSION,
    author="maryimana",
    author_email="tombutoyi@gmail.com",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # install_requires=[],
    keywords=['python', 'async', 'asyncoff', 'sync', 'async to sync'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)