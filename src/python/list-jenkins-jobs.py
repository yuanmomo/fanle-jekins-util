#!/usr/bin/python
# encoding: utf-8

import sys
import jenkins
import os
import json


from workflow import Workflow

def showResult(wf,source, params=[]):
    if len(params) > 0:
        for job in source:
            name = job['name']
            if name.find(params[0]) > -1:
                wf.add_item(job['name'], job['url'], valid=True, arg=job['name'])
    else:
        for job in source:
            wf.add_item(job['name'], job['url'], valid=True, arg=job['name'])

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


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`

    # Get args from Workflow, already in normalized Unicode
    args = wf.args

    config = json.loads(read('../config.json'))
    if config == None :
        sys.exit(2)

    job_list=[]
    job_json=None
    if os.path.exists(config["cache-file"]) :
        job_list = json.loads(read(config["cache-file"]))

    if job_list == None or len(job_list) == 0 :
        print "send jenkins request......"
        server = jenkins.Jenkins(config["jenkins-url"],username=config["username"], password=config["password"])
        job_list = server.get_jobs();
        job_json = json.dumps(job_list)

    showResult(wf, job_list, args)

    if job_json != None and len(job_json) > 0 :
        write(config["cache-file"], job_json)
    print job_list;


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))