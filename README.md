# pash
![travis](https://travis-ci.org/Windsooon/pash.svg?branch=master)

Implement Bash ls command using Python

## Quickstart
    
    git@github.com:Windsooon/pash.git
    cd pash
    python3 ls.py -lS
    # Other Examples
    python3 ls.py -p path_location -l
    python3 ls.py -lSaR

## Usage

    usage: ls.py [-h] [-p PATH] [-l] [-a] [-S] [-R]

    optional arguments:
      -h, --help  show this help message and exit
      -p PATH     Spectify the path
      -l          use a long listing format
      -a          do not ignore entries starting with .
      -S          sort by file size
      -R          list subdirectories recursively

## API

    pip3 install pash

    >>> import pash_src
    >>> pash_src.ls()
    LICENSE                   README.md                 __pycache__               
    build                     dist                      htmlcov                   
    pash.egg-info             pash_src                  run_tests.py              
    setup.py                  src                       tests   
