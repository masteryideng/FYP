import subprocess
import re
import pytest
import os

devices = subprocess.check_output(['VBoxManage list vms'], shell=True)
device_names = re.compile('"(.*)"').findall(devices)
device_versions = re.compile('- (\d.\d.\d) -').findall(devices)
vm_ids = re.compile('{(.*)}').findall(devices)

if not os.environ.get('IN_CI'):
    print "Please give the apk file directory being tested:"
    os.environ['app'] = raw_input()
    print "Please give number of times running Monkey test: (number*1000)"
    os.environ['monkey_time'] = raw_input()
    print "Please give number of maximum_iteration_times:"
    os.environ['traversal_time'] = raw_input()

    """start emulator"""
    # pip install -r requirements.txt
    print "Please select the desired emulator for running the tests, the available emulators are:"
    for i in xrange(len(device_names)):
        print "%d: %s" % (i+1, device_names[i])
    os.environ['device_no'] = raw_input()


subprocess.Popen('open -a /Applications/Genymotion.app/Contents/MacOS/player.app --args --vm-name %s' % vm_ids[int(os.environ['device_no'])-1], shell=True)

"""start tests"""
os.environ['root_dir'] = os.getcwd()
test_script_path = os.path.join(os.environ['root_dir'], 'tests', 'tests')
os.environ['platformVersion'] = device_versions[int(os.environ['device_no'])-1]
pytest.main(['-vv', '-s', '-x', test_script_path, '--html=bvt_report.html'])
