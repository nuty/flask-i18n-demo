# -*- coding: utf-8 -*-
import os


class Configuration(object):
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    DEBUG = False
    SECRET_KEY = '&r4c*ig+hzp*e!_f)3&nh)zee^(=o)rp_+a-9ab5v*9n1*gr^n'
    LANGUAGES = {
        'en_US': u'English',
        'zh_CN': u'中文'
    }
    BABEL_DIRNAME = os.path.join(APP_ROOT, 'translations')
