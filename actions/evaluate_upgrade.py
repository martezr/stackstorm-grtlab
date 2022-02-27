import semver
import requests
import json
import sys

from st2common.runners.base_action import Action

class EvaluateUpgradeAction(Action):
    def run(self, active_version, current_version):
        def evaluateversion(activeversion, currentversion):
            if (currentversion.major != activeversion.major):
                outpayload = {}
                outpayload['upgrade_type'] = "major"
                return outpayload

            if (currentversion.minor != activeversion.minor):
                outpayload = {}
                outpayload['upgrade_type'] = "minor"
                return outpayload

            if (currentversion.patch != activeversion.patch):
                outpayload = {}
                outpayload['upgrade_type'] = "patch"
                return outpayload

        if current_version.startswith('v'):
            current_version = current_version[1:]
        if active_version.startswith('v'):
            active_version = active_version[1:]

        currentversion = semver.VersionInfo.parse(current_version)
        activeversion = semver.VersionInfo.parse(active_version)
        payload = evaluateversion(activeversion, currentversion)
        return (True, payload)