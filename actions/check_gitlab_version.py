from ensurepip import version
import requests
import json
import sys

from st2common.runners.base_action import Action

class CheckGitlabVersionAction(Action):
    def run(self, active_version):
        r = requests.get('https://gitlab.com/api/v4/projects/278964/repository/tags?per_page=100')
        payload = json.loads(r.text)
        versions = []
        for gitlab_tag in payload:
            payloadVersion = gitlab_tag['name']
            if "rc" in payloadVersion:
                continue
            stripVersion = payloadVersion.split('-')[0]
            outVersion = stripVersion[1:]
            versions.append(outVersion)
        versions.sort(key=lambda s: list(map(int, s.split('.'))))
        versions.reverse()
        current_version = versions[0]


        if active_version != current_version:
            outpayload = {}
            outpayload['current_version'] = current_version
            outpayload['active_version'] = active_version
            outpayload['status'] = "upgrade"
            return (True, outpayload)
        else:
            outpayload = {}
            outpayload['current_version'] = current_version
            outpayload['active_version'] = active_version
            outpayload['status'] = "current"
            return (True, outpayload)