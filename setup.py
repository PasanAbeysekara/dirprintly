from setuptools import setup, find_packages

setup(
    name='dirprintly',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dirprintly=dirprintly.file_printer:print_file_contents',
        ],
    },
)
