import requests
import json
import sys

from st2common.runners.base_action import Action

class CheckJenkinsVersionAction(Action):
    def run(self, active_version):
        r = requests.get('https://api.github.com/repos/jenkinsci/jenkins/releases')
        payload = json.loads(r.text)
        for jenkins_tag in payload:
            payloadVersion = jenkins_tag
            if "stable" in payloadVersion['body']:
                continue
            if "rc" in payloadVersion['tag_name']:
                continue
            stripVersion = payloadVersion['tag_name'].split('-')
            current_version = (stripVersion[1])
            break

        if active_version != current_version:
            outpayload = {}
            outpayload['current_version'] = current_version
            outpayload['active_version'] = active_version
            outpayload['status'] = "upgrade"
            return (True, outpayload)
        else:
            outpayload = {}
            outpayload['current_version'] = ""
            outpayload['active_version'] = ""
            outpayload['status'] = "current"
            return (True, outpayload)