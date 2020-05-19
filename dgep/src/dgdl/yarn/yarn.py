import json
import re
import os
from ...tools.regex import Regex
from yarn_node import YarnNode

class Yarn:
    """Class to translate Yarn scripts into DGDL specifications"""

    def __init__(self):
        self.yarnfile_dir = os.getcwd() + "/src/assets/protocols/yarnfiles"
        self.dgdl_dir = os.getcwd() + "/src/assets/protocols/"

    def convert_to_dgdl(self, yarnfile, user_name="User"):
        """Converts the given yarnfile into a DGDL file"""

        protocolName = 'Yarn' + yarnfile
        system_name = protocolName.replace(' ', '').replace("_","")

        with open(self.yarnfile_dir + '/' + yarnfile + '.json', 'rb') as yarn_file:
            yarn_data_str = yarn_file.read(); yarn_data = json.loads(yarn_data_str)

            players = [user_name]
            titles = []
            nodes = {}
            user_nodes = 0
            nodes_with_incoming_edges = []

            for yarn_node in yarn_data:
                title = yarn_node['title'].replace(' ','').replace('_','').capitalize()
                body = yarn_node['body']

                n = YarnNode(title)

                speaker = self.get_speaker(body)
                n.set_speaker(speaker)
                n.set_opener(self.get_clean_body_text(body,speaker))

                if speaker not in players:
                    players.append(speaker)

                matches = Regex().get_matches(body,r"\[\[([^\[\]\|]*)\|([^\[\]\|]+)\]\]")

                for match_num, match in matches.items():
                    #match[0] is user response text (if exists);
                    #match[1] is the name of the agent move that follows either the current move, or the user move
                    next = match[1].replace(' ','').replace('_','').capitalize()
                    if next not in nodes_with_incoming_edges:
                        nodes_with_incoming_edges.append(next)

                    #if there's no match[0] (i.e. user response text) we move straight to the next agent move
                    if match[0] == "":
                        n.add_next(next)
                    else:
                        #otherwise, create a node for the user move
                        user_nodes = user_nodes + 1; user_node_title = "UserReply" + str(user_nodes)
                        user_node = YarnNode(user_node_title)
                        user_node.set_speaker(user_name)
                        user_node.set_opener(match[0])
                        user_node.add_next(next)
                        n.add_next(user_node_title)
                        nodes[user_node_title] = user_node
                        nodes_with_incoming_edges.append(user_node_title)

                nodes[title] = n

            # the initial moves are any nodes without incoming edges
            initial_moves = []
            for m in (set(nodes.keys()) ^ set(nodes_with_incoming_edges)):
                node = nodes[m]
                move = 'move(add, next, {name}, {speaker})'.format(name=node.title,speaker=node.speaker)
                initial_moves.append(move)

            initial_rule = 'rule{{id:StartingRule, scope:initial, {{\n\t\t{rule_body}\n\t\t}}\n\t}}'.format(rule_body="\n\t& ".join(initial_moves))

            interactions = []

            for title, node in nodes.items():
                next_nodes = []

                #if a node doesn't have a next node, its effect should be to terminate the dialogue
                if not node.next:
                    next_nodes.append('status(terminate, {system_name})'.format(system_name=system_name))
                else:
                    for next in node.next:
                        next_node = nodes[next]
                        s = next_node.speaker
                        n = 'move(add, next, {next}, {speaker})'.format(next=next, speaker=s)
                        next_nodes.append(n)

                signature = 'interaction{{{name}, "{opener}", {{\n\t\t{rule_body}\n\t\t}}\n\t}}'.format(name=title,opener=node.opener,rule_body="\n\t\t& ".join(next_nodes))
                interactions.append(signature)

            interactions = "\n\n\t".join(interactions)

            turns = 'turns{magnitude:multiple, ordering:liberal}'
            player_nums = 'players{{min:{num_players}, max:{num_players}}}'.format(num_players=str(len(players)))

            player_spec = []

            for p in players:
                player_spec.append('player{{id:{name}, max:1, min:1}}'.format(name=p))

            player_spec = "\n\t".join(player_spec)

            composition = '{turns}\n\n\t{players}\n\n\t{player_spec}\n\n\tbacktrack{{on}}\n'.format(turns=turns,players=player_nums,player_spec=player_spec)

            dgdl = 'System{{{system_name}{{\n\t{composition}\n\t{initial_rule}\n\t{interactions}\n}}}}'.format(system_name=system_name, composition=composition, initial_rule=initial_rule, interactions=interactions)

            dgdl_file = open(self.dgdl_dir + '/' + protocolName + '.dgdl', 'w')
            dgdl_file.write(dgdl.encode('utf-8').strip())

            return protocolName

    def get_speaker(self, body_text):
        regex = r"[>]*([A-Z][^ >.]+):"
        return Regex().get_matches(body_text, regex)[1][0]

    def get_clean_body_text(self, body_text, name):
        regex = r"" + name + ":([^\[\]]+)"
        return Regex().get_matches(body_text, regex)[1][0].replace("\n"," ").strip()

    def process_response_text(self, text):
        symbols = [","," ",";",".","!",".","'","?"]
        for s in symbols:
            text = text.replace(s, '')

        return text
