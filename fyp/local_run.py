#!/usr/bin/env python

import pytest
import os

"""start tests"""
os.environ['root_dir'] = os.getcwd()
os.environ['app'] = '/Users/MasterYideng/Desktop/android-debug.apk'
os.environ['platformVersion']= '6.0.1'
os.environ['deviceName'] = '00b53032759badf1'
os.environ['traversal_time'] = '300'
test_script_path = os.path.join(os.environ['root_dir'], 'tests', 'tests', 'security_test.py')
pytest.main(['-s', test_script_path, '--html=bvt_report.html'])
