from defcon.effects.effect import Effect
from .plugin.plugin_loader import PluginLoader

class InvokeEffect(Effect):
    """ A DGDL/DGEP-specific effect for invoking a plugin
        Extends a defcon Effect in the usual way
    """

    def __init__(self, identifier):
        self.type = "invoke"

        self.identifier = identifier
        self.vars = {}

        self.content_sets = []

    def perform(self, system=None, update_data=None):

        if update_data:
            content = update_data["content"]

            for content_var, content_value in content.items():
                for key,value in self.vars.items():
                    if value == "$" + content_var:
                        self.vars[key] = content_value

            p = system.dialogue_manager.loaded_plugins[self.identifier]

            invoke_data = {"moveID": update_data["moveID"], "speaker":update_data["speaker"], "params": self.vars}

            p.invoke(invoke_data)


        '''if value.text == "CONTENT":
            values = []
            for v in value.getChildren():
                values.append(v.text)

            value = values
            self.content_sets.append(variable)

        elif value.text == "$":
            value = "$" + vars[i].getChildren()[2].text
        else:
            value = value.text

        if value[0] == '"':
            value = value[1:]

        if value[len(value)-1] == '"':
            value = value[:-1]

        self.vars[variable] = value'''
