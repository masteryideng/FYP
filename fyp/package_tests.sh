#!/bin/bash

find . -name '__pycache__' -type d -exec rm -r {} +
find . -name '.cache' -type d -exec rm -r {} +
find . -name '.idea' -type d -exec rm -r {} +
find . -name '.DS_Store' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name 'report.html' -exec rm -f {} +
find . -name 'assets' -type d -exec rm -r {} +

pipreqs --force ./
