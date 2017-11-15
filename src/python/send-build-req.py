#!/usr/bin/python
# encoding: utf-8

import sys
from jenkinsapi import jenkins as japi
from jenkins import Jenkins as jks
import time
import util

from workflow import Workflow3


def main(wf):
    args = wf.args

    config = util.loadJsonConfig();

    apiServer = japi.Jenkins(config["jenkins-url"],username=config["username"], password=config["password"])
    server = jks(config["jenkins-url"],username=config["username"], password=config["password"])

    retry_count = 0
    jobInfo = None

    while True:
        # refresh job status
        jobInfo = server.get_job_info(args[0])
        if jobInfo == None :
            sys.exit(3);

        if retry_count >= config["retry-count"] :
            print "Build job is not available!!!!"
            sys.exit(4)
        if not jobInfo.get("buildable") :
            time.sleep(10)
            retry_count += 1
        else :
            break

    # get next build id
    job = apiServer.get_job(args[0])
    next_build_number = job.get_next_build_number();

    # start to build
    server.build_job(args[0])

    # waite server to put job in queue
    time.sleep(10)

    while True:
        time.sleep(5)
        status = job.get_build(next_build_number).get_status();
        if status == None :
            continue
        if status == u"SUCCESS" :
            print "SUCCESS"
            break
        else:
            print('Build [%s] failed!!' % next_build_number);

    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow3()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))