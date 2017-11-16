#!/usr/bin/env python
# encoding: utf-8


"""
List jenkins jobs of Jenkins-Python-Alfred.

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
import jenkins
import os
import json
import util

from workflow import Workflow3


def main(wf):
    args = wf.args

    # load configurations
    config = util.load_json_config();

    job_list = []
    job_json = None
    if os.path.exists(config["cache-file"]):
        job_list = json.loads(util.read(config["cache-file"]))

    if job_list or len(job_list) == 0:
        server = jenkins.Jenkins(config["jenkins-url"], username=config["username"], password=config["password"])
        job_list = server.get_jobs();
        job_json = json.dumps(job_list)

    util.add_job_list_to_dlfred(wf, job_list, args)

    if job_json and len(job_json) > 0:
        util.write(config["cache-file"], job_json)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
