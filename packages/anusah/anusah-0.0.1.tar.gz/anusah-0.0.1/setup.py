from setuptools import setup, find_packages


setup(
    name = 'anusah',
    version = '0.0.1',
    author = 'Anurag Goenka, Ashutosh Sah',
    author_email = 'anurag.goenka25@gmail.com',
    license = 'MIT',
    description = 'Generic CLI tool anusah',
    long_description_content_type = "text/markdown",
    url = '',
    py_modules = ['anusah', 'app'],
    packages = find_packages(),
    install_requires = [
        "click>=8.0.1",
        "pyperclip>=1.8.2"
    ],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        anusah=anusah:cli
    '''
)
