#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect


def fancy_log(*args, **kw):
    """Returns an informative prefix for verbose debug output messages"""
    caller_module = inspect.currentframe().f_back.f_globals['__name__']
    method_name = inspect.stack()[1][3]
    print '%s :: %s() %s %s' % (caller_module, method_name, args or '',
                                kw or '')
