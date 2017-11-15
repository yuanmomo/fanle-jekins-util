#!/usr/bin/env python
# encoding: utf-8


"This is a module of "

"""
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
import util

debug = True


config_file="../config.json";

def loadJsonConfig() :
    config = json.loads(read(config_file))
    if config == None :
        sys.exit(2)
    return config;

def showJobListResult(wf, source, params=[]):
    if len(params) > 0:
        for job in source:
            name = job['name']
            if name.find(params[0]) > -1:
                wf.add_item(title=job['name'],subtitle= job['url'], copytext=job['url'], valid=True, arg=job['name'])
    else:
        for job in source:
            wf.add_item(title=job['name'], subtitle= job['url'], copytext=job['url'],valid=True, arg=job['name'])

def read(fileName):
    if not os.path.exists(fileName):
        print "ERROR: file %s not exists." % (fileName)
        return
    file = open(fileName, "r")
    fileContent = file.read()
    file.close()
    return fileContent


def write(fileName, content):
    # check file exists
    if not os.path.exists(fileName):
        file = open(fileName, "w")
        file.write(content)
        file.close()



if __name__ == '__main__':
    pass