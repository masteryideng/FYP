#!/usr/bin/env python
# -*- coding:utf8 -*-

import subprocess
from datetime import datetime
from time import sleep
import os
from html import HTML
from androguard.core.bytecodes import apk


MONKEY_CMD = 'adb shell monkey -p %s -v %s'
run_times = os.environ['monkey_time']


def run_monkey(package):

    curr_time = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    log_file = 'run_monkey_%s.log' % curr_time
    with open(log_file, 'w') as f:
        for t in xrange(1, run_times):
            monkey_cmd = MONKEY_CMD % (package, '500')
            p = subprocess.Popen(monkey_cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            f.write('*' * 10 + '\n')
            f.write('-->DATETIME::%s' % str(datetime.now().strftime('%Y-%m-%d_%H_%M_%S')) + '\n')
            f.write('-->START::%s::time(s)' % str(t) + '\n')
            f.writelines(out)
            if err:
                f.write('-->END::err::%s' % str(err))
                assert False
            else:
                f.write('-->END')
                assert True
            sleep(5)
    return log_file


def gen_report(log_file, apk_file):
    crash_dict = {}
    simple_log = []

    with open(log_file) as f:
        crash_log_flag = False
        for l in f.readlines():

            if l.startswith('// CRASH:'):
                crash_log_flag = True

            if '// Long Msg: ' in l:
                crash_long_msg = l.split('// Long Msg: ')[1]
                if crash_dict.has_key(crash_long_msg):
                    crash_dict[crash_long_msg] +=1
                else:
                    crash_dict[crash_long_msg] = 1

            if l.startswith('** Monkey aborted due to error.'):
                crash_log_flag = False

            if crash_log_flag:
                simple_log.append(l)

    gen_html_report(crash_dict, apk_file, simple_log)
    #print crash_dict


def gen_html_report(crash_dict, apk_file, simple_log):
    h = HTML()

    h.h2('Monkey Test Report')
    h.li(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    h.li(apk_file)

    h.br

    t = h.table(border='1')
    r = t.tr
    r.th('Crash Long Msg')
    r.th('Crash Times')

    for k, v in crash_dict.iteritems():
        r = t.tr
        r.td(k)
        r.td(str(v))

    h.h6('Logs')
    h.pre()
    for l in simple_log:
        h.code(str(l))
    h.pre()

    with open('monkey_test_report.html', 'w') as r:
        r.write(str(h))


def test_monkey():
    package = get_package(os.environ['app'])
    log_file = run_monkey(package)
    gen_report(log_file, package)


def get_package(path):
    app = apk.APK(path)
    packname = app.get_package()
    return packname
