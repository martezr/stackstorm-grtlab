import requests

from st2common.runners.base_action import Action

class FetchJenkinsVersionAction(Action):
    def run(self, host):
        r = requests.get(host + "/api/json")
        version = r.headers['X-Jenkins']
        return (True, version)