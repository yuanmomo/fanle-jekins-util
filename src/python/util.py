#!/usr/bin/env python
# encoding: utf-8


"""
Util of Jenkins-Python-Alfred.

@version    :   1.0
@author     :   MoMo
@license    :   Apache Licence 
@contact    :   yuanhongbin9090@gmail.com
@site       :   http://yuanmomo.net
@software   :   PyCharm
@file       :   util.py
@time       :   15/11/2017 17:39
"""

import sys
import os
import json

debug = True

config_file = "../config.json"


def load_json_config():
    """
    load configurations from config file.
    :return:
    """
    config = json.loads(read(config_file))
    if not config:
        sys.exit(2)
    return config


def add_job_list_to_dlfred(wf, source, params=[]):
    """
    add job list to Alfred item list.
    :param wf:
    :param source:
    :param params:
    :return:
    """
    if len(params) > 0:
        for job in source:
            name = job['name']
            if name.find(params[0]) > -1:
                wf.add_item(title=job['name'], subtitle=job['url'], copytext=job['url'], valid=True, arg=job['name'])
    else:
        for job in source:
            wf.add_item(title=job['name'], subtitle=job['url'], copytext=job['url'], valid=True, arg=job['name'])


def read(file_name):
    """
        read file content to String.
    :param file_name:
    :return:
    """
    if not os.path.exists(file_name):
        print "ERROR: file %s not exists." % (file_name)
        return
    f = open(file_name, "r")
    file_content = f.read()
    f.close()
    return file_content


def write(file_name, content):
    """
    write to file.
    :param file_name:
    :param content:
    :return:
    """
    if not os.path.exists(file_name):
        f = open(file_name, "w")
        f.write(content)
        f.close()


if __name__ == '__main__':
    pass
