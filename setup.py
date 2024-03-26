from setuptools import setup, find_packages

setup(
    name='dirprintly',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dirprintly=dirprintly.file_printer:print_file_contents',
        ],
    },
)
