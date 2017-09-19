#!/usr/bin/env python
# -*- coding:utf8 -*-


import os
import pytest

path = os.getcwd()
test_script_path = os.path.join(path, 'tests', 'tests', 'demo_test.py')
pytest.main(['-x', test_script_path, '--html=report.html'])
