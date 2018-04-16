# coding=utf-8
from androguard.core.bytecodes import apk
import os
import sys


def check(apktype):
    global count
    count = 1
    apkdir = os.path.join(sample_dir, apktype)
    for dirpath, dirnames, filenames in os.walk(apkdir):
        for filename in filenames:
            thefile = os.path.join(dirpath, filename)
            apkfile = os.path.split(thefile)[1]
            apkname = os.path.splitext(apkfile)[0]
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
    writeToTxt(permission, filename)
    return permission


def writeToTxt(permission, apktype):
    global count
    resultdir = os.path.join(target_dir, 'permissions', apktype)
    fm = open(resultdir + '/%d' % count + '.txt', 'w')
    print resultdir + '%d' % count + '.txt'
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
    return good_num, bad_num


def get_test_permission(test_file):
    app = apk.APK(test_file)
    permission = app.get_permissions()
    resultdir = os.path.join(os.environ['root_dir'], 'permissions', 'test')
    fm = open(resultdir + '/1' + '.txt', 'w')
    for i in permission:
        tmp = i.split('.')
        final = tmp[-1]
        fm.write(final)
        fm.write("\t")
    fm.close()

if __name__ == "__main__":
    sample_dir = '/Users/MasterYideng/Desktop/apk_samples'
    target_dir = '/Users/MasterYideng/fyp/FYP/fyp'
    get_permissions_main()
