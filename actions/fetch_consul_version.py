import requests
import json
import sys

from st2common.runners.base_action import Action

class FetchConsulVersionAction(Action):
    def run(self, host):
        r = requests.get(host + "/v1/agent/self")
        payload = json.loads(r.text)
        version = payload['Config']['Version']
        return (True, version)