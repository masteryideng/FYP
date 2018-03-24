#!/usr/bin/env python

import subprocess
import re
import pytest
import os
import sys
from shutil import copyfile, copytree
from BeautifulSoup import  BeautifulSoup

'''
if not os.environ.get('IN_CI'):
    devices = subprocess.check_output(['VBoxManage list vms'], shell=True)
    device_names = re.compile('"(.*)"').findall(devices)
    device_versions = re.compile('- (\d.\d.\d) -').findall(devices)
    vm_ids = re.compile('{(.*)}').findall(devices)

    print "Please give number of times running Monkey test: (number*1000)"
    os.environ['monkey_time'] = raw_input()
    print "Please give number of maximum_iteration_time in seconds:"
    os.environ['traversal_time'] = raw_input()

    """start emulator"""
    # pip install -r requirements.txt
    print "Please select the desired emulator for running the tests, the available emulators are:"
    for i in xrange(len(device_names)):
        print "%d: %s" % (i+1, device_names[i])
    os.environ['device_no'] = raw_input()
    os.environ['platformVersion'] = device_versions[int(os.environ['device_no']) - 1]
    os.environ['deviceName'] = '192.168.56.101:5555'
    os.environ['apk_dir'] = '/Users/MasterYideng/Desktop/apk_samples'
    subprocess.Popen('open -a /Applications/Genymotion.app/Contents/MacOS/player.app --args --vm-name %s' % vm_ids[int(os.environ['device_no'])-1], shell=True)
'''

"""start tests"""
os.environ['apk_dir'] = '/Users/MasterYideng/Desktop/apk_samples'
os.environ['root_dir'] = os.getcwd()
os.environ['app'] = os.path.join(os.environ['root_dir'], 'apk_samples', 'android-debug.apk')
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
