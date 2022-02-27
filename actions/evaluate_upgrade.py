import semver
import requests
import json
import sys

from st2common.runners.base_action import Action

class EvaluateUpgradeAction(Action):
    def run(self, active_version, current_version):
        if current_version.startswith('v'):
            current_version = current_version[1:]
        if active_version.startswith('v'):
            active_version = active_version[1:]

        currentversion = semver.VersionInfo.parse(current_version)
        activeversion = semver.VersionInfo.parse(active_version)
        #payload = {}
        #payload['currentversion'] = currentversion
        #payload['activeversion'] = activeversion
        #return (True, payload)
        if (currentversion.major != activeversion.major):
            outpayload = {}
            outpayload['upgrade_type'] = "major"
            print(outpayload)
            return (True, outpayload)

        if (currentversion.minor != activeversion.minor):
            outpayload = {}
            outpayload['upgrade_type'] = "minor"
            print(outpayload)
            return (True, outpayload)

        if (currentversion.patch != activeversion.patch):
            outpayload = {}
            outpayload['upgrade_type'] = "patch"
            print(outpayload)
            return (True, outpayload)

        payload = {}
        payload['upgrade_type'] = "logic skipped"
        return (True, payload)