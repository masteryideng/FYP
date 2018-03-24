#!/usr/bin/env python

import subprocess
import re
import pytest
import os
import sys
from shutil import copyfile, copytree
from BeautifulSoup import BeautifulSoup

"""start tests"""
os.environ['root_dir'] = os.getcwd()
copyfile(os.environ['apk'], os.environ['root_dir'])
os.environ['app'] = os.path.join(os.environ['root_dir'], 'android-debug.apk')
test_script_path = os.path.join(os.environ['root_dir'], 'tests', 'tests')
pytest.main(['-s', test_script_path, '--html=bvt_report.html'])

with open('bvt_report.html', 'r') as r:
    source_code = r.read()
soup = BeautifulSoup(source_code)
result = soup.findAll('tbody', {'class': 'passed results-table-row'})
passed = ''
for each in result:
    passed += each.tr.contents[3].text + '\n'
with open("result.txt", "w") as f:
    f.write(passed)

copyfile('bvt_report.html', '/Applications/XAMPP/htdocs/temp/bvt_report.html')
copyfile('security_test_report.html', '/Applications/XAMPP/htdocs/temp/security_test_report.html')
copyfile('monkey_test_report.html', '/Applications/XAMPP/htdocs/temp/monkey_test_report.html')
copyfile('result.txt', '/Applications/XAMPP/htdocs/temp/result.txt')
copytree('screenshots', '/Applications/XAMPP/htdocs/temp/screenshots')
