import requests
import json
import sys

from st2common.runners.base_action import Action

class CheckVaultVersionAction(Action):
    def run(self, active_version):
        r = requests.get('https://api.github.com/repos/hashicorp/vault/tags')
        payload = json.loads(r.text)
        payloadVersion = payload[0]['name']
        if payloadVersion.startswith('v'):
            current_version = payloadVersion[1:]
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