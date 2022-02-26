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
            return (True, message)
        else:
            message = "You're all good still"
            return (True, message)