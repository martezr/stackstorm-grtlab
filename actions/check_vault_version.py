import requests
import json
import sys

from st2common.runners.base_action import Action

class CheckVaultVersionAction(Action):
    def run(self, active_version):
        r = requests.get('https://api.github.com/repos/hashicorp/vault/tags')
        payload = json.loads(r.text)
        if active_version != payload[0]['name']:
            message = "Time for an upgrade"
            outpayload = {}
            outpayload['current_version'] = payload[0]['name']
            outpayload['active_version'] = active_version
            return (True, json.dumps(outpayload))
        else:
            message = "You're all good still"
            return (True, message)