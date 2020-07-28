#from dgdl.dgdl_file import dgdl_file
from .player import Player
from .participant import Participant
from .store import Store
from .rule import Rule
from .interaction import Interaction
import copy
import dill as pickle

class System:
    '''Class representing an overall dialogue system
        Manages the framework for the dialogue
        as well as the dialogue itself with participants etc'''

    def __init__(self, data=None, dialogue_manager=None, parent=None):
        self.dialogue_manager = dialogue_manager
        self.data = data
        self.name = ""
        self.turns = {}
        self.roles = []
        self.num_players = {}
        self.players = {}
        self.backtracking = "off"
        self.commitment_stores = {}
        self.ext_uri_map = {}
        self.rules = {}
        self.interactions = {}
        self.turns_magnitude = ""
        self.turntaking = ""

        self.last_error = ""

        self.parent = parent #if this is a sub-protocol then we have a parent...

        self.dialogue_history = []
        self.participants = {}

        self.participant_id_mapping = {}

        self.moves = {}

        self.speaker = ""

        self.runtime_vars = {}

        self.started = False

        self.name = ""

        self.terminated = False

    def start(self):
        ''' Method to start a dialogue, first checking if the constraints
            are all satisfied (e.g. max and min players)'''
        # first check that the requirements for max and min of types of players is met
        if len(self.participants) < int(self.num_players["min"]):
            self.last_error = "Error: not enough participants (current: " + str(len(self.participants)) + "; required: " + str(self.num_players["min"]) + ")"
            return False

        for type, player in self.players.items():
            if player.min > 0:
                if len(self.get_participants_in_role(type)) < player.min:
                    self.last_error = "Error: not enough participants in role " + type + " (current: " + str(len(self.get_participants_in_role(type))) + "; required: " + str(player.min) + ")"
                    return False

        for r in self.rules["initial"]:
            effects = r.process(self)
            for e in effects:
                e.perform(self)

        self.started = True
        return True

    def add_participant(self, playerID, name=None):
        '''Method to add a participant to a dialogue
            A participant is a real or virtual agent that
            actually takes part in the dialogue'''

        #If max is defined and we have max then don't add
        if len(list(self.participants.keys())) == int(self.num_players["max"]):
            #print("Error: already at the maximum number of players (" + str(self.num_players["max"]) + ")")
            return

        # partipcant number will be used to identify them throughout
        participant_number = len(list(self.participants.keys())) + 1

        # get the player template that this participant is to be based on
        if playerID in list(self.players.keys()):
            template = self.players[playerID]

            max = template.max

            if max != -1:
                if len(self.get_participants_in_role(playerID)) >= max:
                    return "Error: player type " + playerID + " is currently at its maximum (" + str(max) + ")"

            #create the new participant and add them to the dictionary
            participant = Participant(participant_number, template, name)
            self.participants[participant_number] = participant

        # Create a new entry in the moves dictionary for this participant
        self.moves[participant_number] = {"next":[], "future":[]}

        # If the participant has been given a name, map this to their number
        if name:
            self.participant_id_mapping[name] = participant_number

        # We return the participant number so it can be used
        return participant_number

    def get_participants_in_role(self, role_name):
        result = []
        for p in list(self.participants.values()):
            if p.in_role(role_name):
                result.append(p)

        return result

    def in_role(self, participant, role):

        if role == "speaker":
            if self.speaker == participant:
                return True
            else:
                return False

        if participant in list(self.participant_id_mapping.keys()):
            participant = self.participant_id_mapping[participant]

        for p in list(self.participants.values()):
            if p.participantID == participant and p.in_role(role):
                return True

        return False

    def add_move(self, role, move):

        time = move.time
        if role == "speaker":
            self.moves[self.speaker][time].append(move)
        elif role in list(self.participants.keys()):
            self.moves[role][time].append(move)
        elif role in list(self.participant_id_mapping.keys()):
            role = self.participant_id_mapping[role]
            self.moves[role][time].append(move)
        else:
            for p in self.get_participants_in_role(role):
                self.moves[p.participantID][time].append(move)

    def update_speaker(self, speaker):
        if speaker in list(self.participant_id_mapping.keys()):
            self.speaker = self.participant_id_mapping[speaker]
        elif speaker in list(self.participants.keys()):
            self.speaker = speaker

    def is_current_player(self, player):
        return False

    def get_dialogue_history(self):
        return self.dialogue_history

    def get_participant(self, participantID):
        if participantID in list(self.participants.keys()):
            return self.participants[participantID]
        else:
            return None

    def perform_interaction(self, interaction_id, interaction_data):

        subsystem = None

        if not self.started:
            #print("Error: cannot perform interaction because the dialogue has not started")
            return

        if interaction_id in list(self.interactions.keys()):

            # empty everyone's "next" moves
            for k in list(self.moves.keys()):
                self.moves[k]["next"] = []

            # Take a deep copy of the interaction; we don't want updates
            # to the effects to persist
            interaction = copy.deepcopy(self.interactions[interaction_id])
            effects = interaction.perform(self, interaction_data)
            interaction_data["moveID"] = interaction_id
            for e in effects:
                if e.type == "initiate":
                    subsystem = e.perform(self, interaction_data)
                else:
                    e.perform(self, interaction_data)

            tmp = interaction_data

            self.dialogue_history.append(tmp)

            if subsystem:
                return subsystem
            else:
                return self.get_available_moves() #Send back the available moves following this interaction
        else:
            print("Error: unknown interaction")


    def get_available_moves(self):
        '''Method to get the available moves at the current point in the dialogue
            Will return the available moves (if any) for the speaker (if there is one)
            under 'strict' turntaking; or for all participants under 'liberal' turntaking'''

        return_moves = {}
        tmp_moves = {}

        #If we're using strict ordering, only return moves for the current speaker - if there is one
        if self.turntaking == "strict":
            if self.speaker:
                tmp_moves[self.speaker] = self.moves[self.speaker]
        else:
            tmp_moves = self.moves

        for participant, moves in tmp_moves.items():
            p = self.get_participant(participant)
            move_set = []

            if moves["next"]:
                working_moves = moves["next"]
            elif moves["future"]:
                working_moves = moves["future"]
            else:
                continue

            for move in working_moves:
                if move.addressee:
                    for a in self.get_participants_in_role(move.addressee):
                        if p.participantID == a.participantID:
                            continue  #don't let a participant target a move at themselves

                        new_move = {}
                        new_move["reply"], new_move["opener"] = self.process_move_content_reply(move, self.interactions[move.id])
                        new_move["moveID"] = move.id

                        if a.name:
                            new_move["target"] = a.name
                        else:
                            new_move["target"] = a.participantID

                        move_set.append(new_move)
                else:
                        new_move = {}
                        new_move["reply"], new_move["opener"] = self.process_move_content_reply(move, self.interactions[move.id])

                        new_move["moveID"] = move.id
                        move_set.append(new_move)

                if p.name:
                    return_moves[p.name] = move_set
                else:
                    return_moves[p.participantID] = move_set

        return return_moves

    def get_uri(self, identifier):
        if identifier in self.ext_uri_map:
            return self.ext_uri_map[identifier]
        else:
            return None

    def get_runtime_var(self, var_name):
        if var_name in self.runtime_vars:
            return self.runtime_vars[var_name]
        else:
            return ""

    def process_move_content_reply(self, move, interaction):
        ''' Method to process move content based on the given interaction
            Replaces variables with concrete content where required'''
        reply = {}

        if move.opener is None:
            opener = interaction.opener
        else:
            opener = move.opener

        content = move.content

        multivar = False
        change_val = True

        val = ""

        for i in range(0,len(content)):
            c = content[i]

            #print("Content in process move: " + str(c))
            variable = None

            key = list(c.keys())[0]

            #somewhere here to handle unspecified numbers of parameters
            if multivar:
                variable = '...' + str(i)
            else:
                #print("i=" + str(i))
                #print("Interaction targets: " + str(interaction.target))
                variable = interaction.target[i]
                if variable == '...':
                    multivar = True
                    variable = '...' + str(i)

            if variable is not None:

                if key == "VAR":

                    #print("FOUND A VAR")
                    #print(c[key])
                    #print(self.runtime_vars)

                    if isinstance(self.runtime_vars[c[key]], list):
                        change_val = False
                        l = self.runtime_vars[c[key]]
                        #print("Variable " + c[key] + ": " + str(l))

                        s = ""

                        for i in range(0, len(l)):
                            v = '...' + str(i)
                            reply[v] = l[i]

                            if i < (len(l) - 1):
                                s = s + ", " + l[i]
                            else:
                                if "$OR" in opener:
                                    s = s + " or " + l[i]
                                    opener = opener.replace("$OR", s)
                                elif "$AND" in opener:
                                    s = s + " and " + l[i]
                                    opener = opener.replace("$AND", s)

                            val = ""

                    elif c[key][0] == "!":
                        val = "!" + self.runtime_vars[c[key][1:]]
                    else:
                        val = self.runtime_vars[c[key]]
                elif c[key][:1] == "$":
                    val = "$" + variable
                else:
                    val = c[key]

                if val[:1] == "!":
                    val = "not " + val[1:]

            if change_val:
                reply[variable] = val
                opener = opener.replace("$" + variable, val)

        return reply, opener

    def initiate_new(self, protocol):
        '''Method to initiate a new dialogue using the given protocol, assuming a dialogue manager is instantiated'''
        if not self.dialogue_manager is None:
            return self.dialogue_manager.new_dialogue(data={"protocol":protocol},system=self)

    def __getstate__(self):
        '''Overriden __getstate__ to remove the dialogue manager from the serialization
            Serializing dialogue_manager instance is overkill and causes issues'''
        odict = self.__dict__.copy()
        del odict['dialogue_manager']
        return odict
