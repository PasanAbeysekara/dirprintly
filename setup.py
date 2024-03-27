from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name='dirprintly',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dirprintly=dirprintly.file_printer:explore_directory_cli',
        ],
    },
    url='https://github.com/PasanAbeysekara/dirprintly',  # GitHub Repo URL
    project_urls={
        'Bug Tracker': 'https://github.com/PasanAbeysekara/dirprintly/issues',
    },
    author='Pasan Abeysekara',
    author_email='pasankavindaabey@gmail.com',

    long_description=description,
    long_description_content_type="text/markdown"
)
