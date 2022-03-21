import requests

from st2common.runners.base_action import Action

class FetchJenkinsVersionAction(Action):
    def run(self, host):
        r = requests.get(host + "/api/json")
        version = r.headers['X-Jenkins']
        if len(version.split('.')) > 2:
            active_version = version
        else:
            active_version = version + ".0"
        return (True, active_version)