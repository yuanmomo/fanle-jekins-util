#!/usr/bin/python
# encoding: utf-8

import sys
import jenkins
import os
import json
import util


from workflow import Workflow3



def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`

    # Get args from Workflow, already in normalized Unicode
    args = wf.args

    config = util.loadJsonConfig();

    job_list=[]
    job_json=None
    if os.path.exists(config["cache-file"]) :
        job_list = json.loads(util.read(config["cache-file"]))

    if job_list == None or len(job_list) == 0 :
        server = jenkins.Jenkins(config["jenkins-url"],username=config["username"], password=config["password"])
        job_list = server.get_jobs();
        job_json = json.dumps(job_list)

    util.showJobListResult(wf, job_list, args)

    if job_json != None and len(job_json) > 0 :
        util.write(config["cache-file"], job_json)

    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow3()

    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))