
            #for node in nodes.items():



            for yarn_node in yarn_data:
                title = yarn_node['title'].replace(' ', '').replace("_","").capitalize()
                body = yarn_node['body']
                titles.append(title)

                speaker = self.get_speaker(body)

                if speaker not in players:
                    players.append(speaker)

                interactions[title] = {}
                interactions[title]['speaker'] = speaker
                interactions[title]['effects'] = []
                interactions[title]['opener'] = self.get_clean_body_text(body, speaker)
                interactions[title]['addressee'] = user_name

                user_response = self.get_user_response_text(body)

                for response in user_response:
                    response_and_next = response.split('|')

                    user_response_text = response_and_next[0]

                    if user_response_text == '':
                        #user doesn't do anything
                        interactions[title]['effects'].append(response_and_next[1])
                        incoming.append(response_and_next[1])
                    else:
                        user_response_text = self.process_response_text(user_response_text)
                        user_response_name = 'tmp_UserResponse' + str(i)
                        i = i + 1

                        response_text_map[user_response_text] = user_response_name
                        next_move = response_and_next[1]

                        if user_response_text == '':
                            user_response_text = '<Say Nothing>'

                        if next_move in list(groupings.keys()):
                            groupings[next_move].append(user_response_name)
                        else:
                            groupings[next_move] = [user_response_name]

                        interactions[title]['effects'].append(user_response_name)
                        #incoming.append(user_response_name)
                        interactions[user_response_name] = {}
                        interactions[user_response_name]['speaker'] = user_name
                        interactions[user_response_name]['effects'] = [next_move]
                        interactions[user_response_name]['opener'] = response_and_next[0]
                        interactions[user_response_name]['addressee'] = ''
                        incoming.append(next_move)

            mappings = {}

            i = 1

            for key, group in list(groupings.items()):
                for g in group:
                    mappings[g] = 'UserResponse' + str(i)

                i = i + 1

            for oldValue, newValue in list(mappings.items()):
                interactions[newValue] = interactions[oldValue]
                interactions.pop(oldValue, None)

            for name, interaction in list(interactions.items()):
                effects = interaction['effects']
                newEffects = []

                for effect in effects:
                    if effect in list(mappings.keys()):
                        newEffects.append(mappings[effect])
                    else:
                        newEffects.append(effect)

                interactions[name]['effects'] = newEffects

            initial = list(set(titles) - set(incoming))[0]
            initialInteraction = interactions[initial]
            initialSpeaker = initialInteraction['speaker']

            if initialInteraction['addressee'] != '':
                addressee = ', $' + initialInteraction['addressee'] + ', '
            else:
                addressee = ', '

            initialMove = 'move(add, next, ' + initial + addressee + initialSpeaker + ')'

            initialRule = '''rule{{id:StartingRule, scope:initial,
            \t\t{{
            \t\tassign({initialSpeaker}, speaker)
            \t\t& {initialMove}
            }}}} '''.format(initialSpeaker=initialSpeaker, initialMove=initialMove)

            theInteractions = []

            for name, interaction in list(interactions.items()):
                opener = interaction['opener'].replace('"', '').strip().encode('utf-8')
                effects = []

                if interaction['addressee'] != '':
                    addressee = ', $' + interaction['addressee'] + ', '
                else:
                    addressee = ', '

                effect_person = ''

                for effect in interaction['effects']:
                    if effect in list(interactions.keys()):
                        effect_person = interactions[effect]['speaker']
                        effects.append('move(add, next, ' + effect + ', ' + effect_person +')')

                if effects:
                    effects = "\n\t\t\t& ".join(effects)
                else:
                    effects = 'status(terminate, ' + protocolName.replace("_","") + ')'


                i = '''\tinteraction{{{name}{addressee}"{opener}",
                \t\t{{
                \t\t\t{effects}
                \t\t}}
                \t}}'''.encode('utf-8').format(name=name, addressee=addressee,opener=opener,effects=effects)

                theInteractions.append(i)

            theInteractions = "\n".join(theInteractions)

            playerSpec = []

            for player in players:
                playerSpec.append('player{id:' + player + ', max:1, min:1}')

            playerSpec = "\n\t".join(playerSpec)
            roles = 'roles{' + ",".join(players) + '}'

            minmax = 'players{min:' + str(len(players)) + ', max:' + str(len(players)) + '}'

            dgdl = '''System{{{protocolName}{{
\tturns{{magnitude:multiple, ordering:liberal}}
\t{roles}
\t{minmax}
\t{playerSpec}

\tbacktrack{{on}}

\t/* -- RULES -- */
\t{initialRule}

\t/* -- INTERACTIONS */
{theInteractions}
}}}}'''.encode('utf-8').replace("_","").format(protocolName=protocolName.replace("_",""),roles=roles,minmax=minmax,playerSpec=playerSpec,initialRule=initialRule,theInteractions=theInteractions)

            #print(dgdl)
            #print("XXXXXXXXX")
            #print("XXXXXXXXX")
            #print(dgdl[9593:])

            dgdl_file = open(self.dgdl_dir + '/' + protocolName + '.dgdl', 'w')
            dgdl_file.write(dgdl.encode('utf-8').strip())

            return protocolName
