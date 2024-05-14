
# Bingo

Simple program to generate bingo boards.  Wrote this to support an offsite event at work.

## Getting started

1. Install necessary prerequisites
   ```
   sudo apt install -y python3
   python3 -m pip install --user --upgrade pip
   python3 -m pip install --user virtualenv
   ```
1. Create a new virtual environment within the same directory as the git checkout.
   ```
   python3 -m virtualenv --python=python3 env
   ```
1. Activate the new virtual environment
   ```
   source env/bin/activate
   ```
1. Install, into the new virtual environment, the required python modules for this specific environment.  This will be installed within the virtual env which was activated earlier.
   ```
   python3 -m pip install -r requirements.txt
   ```

## Running

A simple

```
python build.py --help
```

shows usage.
