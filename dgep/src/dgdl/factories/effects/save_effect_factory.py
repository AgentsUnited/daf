from .effect_factory import EffectFactory
from ....defcon.effects.save_effect import Save_Effect

class SaveEffectFactory(EffectFactory):

    def __init__(self, tree):

        children = tree.getChildren()

        content = ""
        var_name = ""

        for i in range(0, len(children)):
            label = children[i].text

            #print("Label value is " + str(label))

            if label == "CONTENT":
                content = children[i].getChildren()[0].text
            elif label == "VAR":
                #print("FOUND VAR IN FACTORY")
                var_name = children[i].getChildren()[1].text
                #print(var_name)
            else:
                # the "label" is a stringliteral which is the content
                content = label

        #print("Saving effect with content " + str(content) + " in var name: " + str(var_name))

        self.effect = Save_Effect(content, var_name)
