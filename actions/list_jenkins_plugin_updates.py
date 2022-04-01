import jenkins

from st2common.runners.base_action import Action

class ListJenkinsPluginUpdatesAction(Action):
    def run(self, host, username, password):

        server = jenkins.Jenkins(host, username=username, password=password)
        plugins = server.get_plugins_info()
        updateablePlugins = []
        for plugin in plugins:
            if plugin['hasUpdate']:
                updateablePlugins.append(plugin['shortName'])

        return (True, updateablePlugins)