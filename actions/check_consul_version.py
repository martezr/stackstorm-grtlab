import requests
import json
import sys

from st2common.runners.base_action import Action

class CheckConsulVersionAction(Action):
    def run(self, active_version):
        r = requests.get('https://api.github.com/repos/hashicorp/consul/tags')
        payload = json.loads(r.text)
        for vault_tag in payload:
            payloadVersion = vault_tag['name']
            # exclude release candidates
            if "rc" in payloadVersion:
                continue
            # exclude alpha releases
            if "alpha" in payloadVersion:
                continue
            # exclude beta releases
            if "beta" in payloadVersion:
                continue     
            # use the first valid version
            if payloadVersion.startswith('v'):
               current_version = payloadVersion[1:]
               break
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
