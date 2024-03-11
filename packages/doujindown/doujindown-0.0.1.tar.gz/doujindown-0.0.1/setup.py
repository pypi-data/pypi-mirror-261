from setuptools import setup, find_packages

with open("./doujindown/conf/doujindown.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="doujindown",
    version="0.0.1",
    author="hashirkz",
    author_email="hashirxkhan1@gmail.com",
    description="command line app to download doujins + manga from many websites *manganelo.com hitomi.la",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/hashirkz/doujindown",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'doujindown = doujindown.app:app',
        ],
    },
    install_requires=[
        'numpy==1.24.3',
        'pandas==2.0.2',
        'requests==2.28.1',
        'bs4==0.0.1',
        'tabulate==0.9.0',
        'urllib3==1.26.12',
        'pillow==10.0.0',
        'matplotlib==3.7.2',
        'pyyaml==6.0.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
    ],
)