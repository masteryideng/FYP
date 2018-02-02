# coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os
import sys

rootdir = os.environ['apk_dir']


def check(apktype):
    global count
    count = 1
    apkdir = os.path.join(rootdir, apktype)
    for dirpath, dirnames, filenames in os.walk(apkdir):
        for filename in filenames:
            thefile = os.path.join(dirpath, filename)
            apkfile = os.path.split(thefile)[1]
            apkname = os.path.splitext(apkfile)[0]
            # print apkfile
            try:
                if os.path.splitext(thefile)[1] == ".apk":
                    get_permissions(thefile, apktype)
            except IOError, err:
                    print err
                    sys.exit()
    return count-1


def get_permissions(path, filename):
    app = apk.APK(path)
    permission = app.get_permissions()
    # print permission
    writeToTxt(permission, filename)
    return permission


def writeToTxt(permission, apktype):
    global count
    resultdir = os.path.join(os.environ['root_dir'], 'apk_samples', 'result', apktype)
    fm = open(resultdir + '%d' % count + '.txt', 'w')
    for i in permission:
        tmp = i.split('.')
        final = tmp[-1]
        fm.write(final)
        fm.write("\t")
    fm.close()
    count += 1


def get_permissions_main():
    good_num = check('good')
    bad_num = check('bad')
    check('test')
    return good_num, bad_num
