from setuptools import setup

VERSION = '1.0.1'
DESCRIPTION = 'Package to write data from database to excel files'

# Setting up
setup(
    name="EaseExcel",
    version=VERSION,
    author="Vishal Sharma",
    author_email="vashisth671@gmail.com",
    description=DESCRIPTION,
    url='https://github.com/Vishal-Vashisht/EaseExcel',
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=open('readme.md').read(),
    packages=['EaseExcel/src/Excel'],
    install_requires=['sqlalchemy', 'XlsxWriter'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6'
)
