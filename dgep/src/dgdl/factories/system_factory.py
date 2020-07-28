from ..dgdl_file import dgdl_file
#from ...participant import Participant
#from ...plugin.plugin_loader import Plugin_loader
#from ..yarn.yarn import Yarn
import copy
import dill as pickle
from ...defcon.system import System
from .interaction_factory import InteractionFactory
from .rule_factory import RuleFactory
from .player_factory import PlayerFactory
from .store_factory import StoreFactory
from ...plugin.plugin_loader import PluginLoader

class SystemFactory:
    '''Class to build a DEFCON dialogue system from a DGDL specification'''

    def __init__(self, dgep):

        # Dictionary of methods to construct the system based on the DGDL composition
        self.composition_methods = {
            "turns": self.set_turns,
            "roles": self.set_roles,
            "players": self.set_num_players,
            "player": self.add_player,
            "backtrack": self.set_backtrack,
            "store": self.add_store,
            "extURI": self.add_ext_uri,
            "plugin": self.load_plugin,
            "rule": self.add_rule,
            "interaction": self.add_interaction
        }

        self.dgep = dgep

        #Create a new empty system
        self.system = System(dialogue_manager=dgep)

    def get_system(self, protocol):
        '''Method to get a system for the given protocol
            Loads a DGDL file for that protocol and builds the system from it'''

        #print("LOADING PROTOCOL: " + str(protocol))

        if protocol[:5] == "yarn.":
            y = Yarn()
            protocol = y.convert_to_dgdl(protocol[5:], 'User')

        tree = dgdl_file().load(protocol)

        #Main tree is the first (and only) child of the loaded tree
        tree = tree.getChildren()[0]

        #Name is the text here
        self.system.name = tree.text

        #These children are the main body of the game; the text tells us what to do
        for child in tree.getChildren():
            label = child.text
            if label in list(self.composition_methods.keys()):
                m = self.composition_methods[label]
                m(child)

        return self.system

    ################################################################################
    # The methods below are called from the composition_methods dictionary         #
    # Most simply hand off the (sub)tree to the relevant class to build the object #
    ################################################################################

    def set_turns(self, tree):
        '''Method to set the turns in a system'''
        for child in tree.getChildren():
            if child.text == "magnitude":
                self.system.turns_magnitude = child.getChildren()[0].text
            elif child.text == "ordering":
                self.system.turntaking = child.getChildren()[0].text

    def set_roles(self, tree):
        '''Method to set the roles in a system'''
        for child in tree.getChildren():
            self.system.roles.append(child.text)

    def set_num_players(self, tree):
        '''Method to set the number of players in a system'''
        for child in tree.getChildren():
            self.system.num_players[child.text] = child.getChildren()[0].text

    def add_player(self, tree):
        '''Method to add a player to the system'''
        p = PlayerFactory(tree).get_player()
        self.system.roles.append(p.playerID)
        self.system.players[p.playerID] = p

    def set_backtrack(self, tree):
        '''Method to set backtracking on/off in the system'''
        self.system.backtracking = tree.getChildren()[0].text

    def add_store(self, tree):
        '''Method to add a store to the system'''
        store_id = tree.getChildren()[0].text

        s = StoreFactory(tree).get_store()
        self.system.commitment_stores[store_id] = s

    def add_ext_uri(self, tree):
        '''Method to add an external URI to the system'''
        id = tree.getChildren()[0].text
        uri = tree.getChildren()[1].text

        self.system.ext_uri_map[id] = uri[1:][:-1]

    def load_plugin(self, tree):
        '''Method to load a plugin (needs work...)'''
        children = tree.getChildren()

        plugin_id = children[0].text
        plugin_name = children[1].text.replace('"','')

        p = PluginLoader()
        self.dgep.loaded_plugins[plugin_id] = p.load(plugin_name)

    def add_rule(self, tree):
        '''Method to add a rule to the system'''
        scope = tree.getChildren()[1].text

        r = RuleFactory(tree).get_rule()
        if scope in list(self.system.rules.keys()):
            self.system.rules[scope].append(r)
        else:
            self.system.rules[scope] = [r]

    def add_interaction(self, tree):
        '''Method to add an interaction to the system'''
        i = InteractionFactory(tree).get_interaction()
        self.system.interactions[i.id] = i
