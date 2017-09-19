#!/bin/bash

pip install -r requirements.txt
pytest tests/demo_test.py --html=report.html
