#!/usr/bin/env python
# encoding: utf-8


"""
Request build job of Jenkins-Python-Alfred.

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
from jenkinsapi import jenkins as japi
from jenkins import Jenkins as jks
import time
import util
import string

from workflow import Workflow3


def main(wf):
    args = wf.args

    # load configurations
    config = util.load_json_config();

    api_server = japi.Jenkins(config["jenkins-url"], username=config["username"], password=config["password"])
    server = jks(config["jenkins-url"], username=config["username"], password=config["password"])

    retry_count = 0

    while True:
        # refresh job status
        job_info = server.get_job_info(args[0])
        if job_info:
            sys.exit(3);

        if retry_count >= config["retry-count"]:
            print "Build job is not available!!!!"
            sys.exit(4)
        if not job_info.get("buildable"):
            time.sleep(10)
            retry_count += 1
        else:
            break

    # get next build id
    job = api_server.get_job(args[0])
    next_build_number = job.get_next_build_number();

    # start to build
    server.build_job(args[0])

    # waite server to put job in queue
    time.sleep(config["start_job_delay_seconds"])

    while True:
        time.sleep(config["refresh_period"])
        status = job.get_build(next_build_number).get_status();
        if status:
            continue
        if status == u"SUCCESS":
            print "%s%s.zip" % (config["zip-download-url"], string.split(args[0], ".")[0])
            break
        else:
            print('Build [%s] failed!!' % next_build_number);


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
