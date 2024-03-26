from setuptools import setup, find_packages

setup(
    name='dirprintly',
    version='1.0',  # Ensure this version number is incremented if re-uploading.
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dirprintly=dirprintly.file_printer:explore_directory_cli',
        ],
    },
)
