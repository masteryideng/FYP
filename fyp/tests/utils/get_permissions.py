# coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os
import sys

path = os.environ['root_dir']
rootdir = os.path.join(path, 'apk_samples')


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
    resultdir = os.path.join(rootdir, 'result', apktype)
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

"""
def get_apis(path, filename):
  app = apk.APK(path)
  app_dex = dvm.DalvikVMFormat(app.get_dex())
  app_x = analysis.newVMAnalysis(app_dex)
  methods = set()
  cs = [cc.get_name() for cc in app_dex.get_classes()]

  for method in app_dex.get_methods():
    g = app_x.get_method(method)
    if method.get_code() == None:
      continue

    for i in g.get_basic_blocks().get():
      for ins in i.get_instructions():
        output = ins.get_output()
        match = re.search(r'(L[^;]*;)->[^\(]*\([^\)]*\).*', output)
        if match and match.group(1) not in cs:
          methods.add(match.group())

  methods = list(methods)
  methods.sort()
  print "methods:"+"\n"
  print methods
  str = "Methods:"
  file = methods
  writeToTxt(str, file, filename)
  return methods


def get_providers(path, filename):
    app = apk.APK(path)
    providers = app.get_providers()
    print "providers:"+"\n"
    print providers
    str = "Providers:"
    file = providers
    writeToTxt(str, file, filename)
    return providers


def get_package(path, filename):
    app = apk.APK(path)
    packname = app.get_package()
    print "packageName:"+"\n"
    print packname
    str = "PackageName:"
    file = packname
    writeToTxt(str, file, filename)
    return packname


def get_activities(path, filename):
    app = apk.APK(path)
    activitys = app.get_activities()
    print "ActivityName:"+"\n"
    print activitys
    str = "Activitys:"
    file = activitys
    writeToTxt(str, file, filename)
    return activitys


def get_receivers(path, filename):
    app = apk.APK(path)
    receivers = app.get_receivers()
    print "Receivers:"+"\n"
    print receivers
    str = "Receivers:"
    file = receivers
    writeToTxt(str, file, filename)
    return receivers


def get_services(path, filename):
    app = apk.APK(path)
    services = app.get_services()
    print "Services:"+"\n"
    print services
    str = "Services:"
    file = services
    writeToTxt(str, file, filename)
    return services
"""
