#!/usr/bin/python
# encoding: utf-8

import sys
import pprint
import jenkins
import time
import os

#pprint.pprint(sys.path)
from workflow import Workflow


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # Get args from Workflow, already in normalized Unicode
    args = wf.args 
    # print("=======================")
    # print '======================='
  
    # wf.add_item('test', args[0])
    # wf.args = ['build finished']
    # sys.stdout.write('build failed')

    server = jenkins.Jenkins('http://192.168.1.232:8080/jenkins',username='test', password='test')
    jobInfo = server.get_job_info(args[0])
    lastVersionNum = jobInfo['lastSuccessfulBuild']['number']
    server.build_job(args[0])
    result = True
    while result:
        time.sleep(10)
        runningJobs = server.get_running_builds()
        if len(runningJobs) > 0:
            pass
        else:
            jobInfo = server.get_job_info(args[0])
            curVersionNum = jobInfo['lastSuccessfulBuild']['number']
            if curVersionNum == lastVersionNum + 1:
                # wf.args = ['build finished']
                sys.stdout.write('build finished')
            else:
                sys.stdout.write('build failed')
            result = False



    # for job in allJobs:
    #     wf.add_item(job['name'], job['url'], valid=True, arg=job['name'])        

    # Do stuff here ...

    # Add an item to Alfred feedback
    # wf.add_item(u'Item title', u'Item subtitle')

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))