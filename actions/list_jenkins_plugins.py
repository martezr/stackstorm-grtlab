import jenkins

from st2common.runners.base_action import Action

class ListJenkinsPluginsAction(Action):
    def run(self, host, username, password):

        server = jenkins.Jenkins(host, username=username, password=password)
        plugins = server.get_plugins_info()
        return (True, plugins)