#!/usr/bin/env sh

# Create a virtual env in current directory
python3 -m venv .

# Activate the virtual env
. ./bin/activate

# Install dependencies
pip3 install -r requirements.txt
