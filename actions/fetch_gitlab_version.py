import requests
import json

from st2common.runners.base_action import Action

class FetchGitlabVersionAction(Action):
    def run(self, host, token):
        headers = {}
        headers['PRIVATE-TOKEN'] = token
        r = requests.get(host + "/api/v4/version", headers=headers, verify=False)
        apiVersionPayload = json.loads(r.text)
        version = apiVersionPayload['version']
        return (True, version)