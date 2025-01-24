#!/bin/bash

# clean up folders
rm -rf public/
rm -rf resources/

# run python scripts
python3 -m scripts.reads

# build site for production
hugo