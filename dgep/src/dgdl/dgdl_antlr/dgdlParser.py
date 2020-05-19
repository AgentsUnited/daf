# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 dgdl.g 2019-05-31 16:33:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
REQUIREMENTS=9
ELSEIF=54
VARS=13
VAR=14
UNDEFINED=113
MAGNITUDE=79
OWNER=92
TURNWISE=27
EXTURI=62
SMALLER=104
INROLE=73
ELSE=53
ID=66
IF=67
OPENER=10
IN=69
T__130=130
SIZE=103
LPAREN=38
CORRESPONDS=50
WARRANT=115
CONDITIONAL=5
FORCETARGET=7
PLAYER=95
MIN=82
TERMINATE=108
LINE_COMMENT=117
TOP=111
ROLES=99
INITIATE=72
PAST=94
NOTTOP=110
T__129=129
PUBLIC=24
DOLLAR=42
THEN=109
T__126=126
T__125=125
T__128=128
T__127=127
LBRACE=40
SET=21
EXTCONDITION=60
MAX=80
ASSIGN=46
UpperChar=31
OFF=88
COMMENT=116
DELETE=52
LISTENER=17
REMOVE=98
COMMA=36
BACKING=47
RELATION=97
GREATER=64
NOTIN=68
QUEUE=22
PRIVATE=25
LowerChar=32
NOTLAST=76
INACTIVE=70
BACKTRACK=48
STORE=106
TARGET=8
ADD=45
INSPECT=74
SINGLE=102
SCOPE=101
MOVEWISE=28
FUTURE=63
EVENT=59
MULTIPLE=84
STATUS=105
Identifier=33
LEGALMOVES=78
MAXTURNS=81
EFFECTS=4
STRICT=15
NOTON=89
HELLO=65
RPAREN=39
STRINGLITERAL=19
CURRENT=51
NOTEQUAL=57
TURNS=112
NOT=86
VISIBILITY=114
RBRACE=41
NOTEMPTY=55
LAST=77
AND=29
T__122=122
T__121=121
T__124=124
T__123=123
ACTIVE=44
T__120=120
INITIAL=26
SPEAKER=18
EXTEFFECT=61
INTERACTION=75
STACK=23
SHARED=20
COMPLETE=49
LIBERAL=16
Number=30
NEXT=85
T__119=119
RULE=100
CONTENT=6
WS=118
EOF=-1
EMPTY=56
ON=90
OR=43
EQUAL=58
STRUCTURE=107
INCOMPLETE=71
TIME=12
COLON=37
NUMTURNS=87
USER=11
ORDERING=91
PLAYERS=96
MOVE=83
LESSTHAN=34
NOTPAST=93
GREATERTHAN=35

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "EFFECTS", "CONDITIONAL", "CONTENT", "FORCETARGET", "TARGET", "REQUIREMENTS", 
    "OPENER", "USER", "TIME", "VARS", "VAR", "STRICT", "LIBERAL", "LISTENER", 
    "SPEAKER", "STRINGLITERAL", "SHARED", "SET", "QUEUE", "STACK", "PUBLIC", 
    "PRIVATE", "INITIAL", "TURNWISE", "MOVEWISE", "AND", "Number", "UpperChar", 
    "LowerChar", "Identifier", "LESSTHAN", "GREATERTHAN", "COMMA", "COLON", 
    "LPAREN", "RPAREN", "LBRACE", "RBRACE", "DOLLAR", "OR", "ACTIVE", "ADD", 
    "ASSIGN", "BACKING", "BACKTRACK", "COMPLETE", "CORRESPONDS", "CURRENT", 
    "DELETE", "ELSE", "ELSEIF", "NOTEMPTY", "EMPTY", "NOTEQUAL", "EQUAL", 
    "EVENT", "EXTCONDITION", "EXTEFFECT", "EXTURI", "FUTURE", "GREATER", 
    "HELLO", "ID", "IF", "NOTIN", "IN", "INACTIVE", "INCOMPLETE", "INITIATE", 
    "INROLE", "INSPECT", "INTERACTION", "NOTLAST", "LAST", "LEGALMOVES", 
    "MAGNITUDE", "MAX", "MAXTURNS", "MIN", "MOVE", "MULTIPLE", "NEXT", "NOT", 
    "NUMTURNS", "OFF", "NOTON", "ON", "ORDERING", "OWNER", "NOTPAST", "PAST", 
    "PLAYER", "PLAYERS", "RELATION", "REMOVE", "ROLES", "RULE", "SCOPE", 
    "SINGLE", "SIZE", "SMALLER", "STATUS", "STORE", "STRUCTURE", "TERMINATE", 
    "THEN", "NOTTOP", "TOP", "TURNS", "UNDEFINED", "VISIBILITY", "WARRANT", 
    "COMMENT", "LINE_COMMENT", "WS", "'uri'", "'plugin'", "'name'", "'$...'", 
    "'...'", "'value'", "'unassign'", "'send'", "'receive'", "'invoke'", 
    "'protocol'", "'save'"
]




class dgdlParser(Parser):
    grammarFileName = "dgdl.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(dgdlParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class system_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.system_return, self).__init__()

            self.tree = None




    # $ANTLR start "system"
    # dgdl.g:23:1: system : ( systemID '{' ( game )+ '}' ) EOF -> ^( systemID ( game )+ ) ;
    def system(self, ):

        retval = self.system_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal2 = None
        char_literal4 = None
        EOF5 = None
        systemID1 = None

        game3 = None


        char_literal2_tree = None
        char_literal4_tree = None
        EOF5_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_systemID = RewriteRuleSubtreeStream(self._adaptor, "rule systemID")
        stream_game = RewriteRuleSubtreeStream(self._adaptor, "rule game")
        try:
            try:
                # dgdl.g:23:11: ( ( systemID '{' ( game )+ '}' ) EOF -> ^( systemID ( game )+ ) )
                # dgdl.g:23:13: ( systemID '{' ( game )+ '}' ) EOF
                pass 
                # dgdl.g:23:13: ( systemID '{' ( game )+ '}' )
                # dgdl.g:23:15: systemID '{' ( game )+ '}'
                pass 
                self._state.following.append(self.FOLLOW_systemID_in_system121)
                systemID1 = self.systemID()

                self._state.following.pop()
                stream_systemID.add(systemID1.tree)
                char_literal2=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_system123) 
                stream_LBRACE.add(char_literal2)
                # dgdl.g:23:28: ( game )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == Identifier) :
                        alt1 = 1


                    if alt1 == 1:
                        # dgdl.g:23:29: game
                        pass 
                        self._state.following.append(self.FOLLOW_game_in_system126)
                        game3 = self.game()

                        self._state.following.pop()
                        stream_game.add(game3.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1
                char_literal4=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_system130) 
                stream_RBRACE.add(char_literal4)



                EOF5=self.match(self.input, EOF, self.FOLLOW_EOF_in_system133) 
                stream_EOF.add(EOF5)

                # AST Rewrite
                # elements: game, systemID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 24:13: -> ^( systemID ( game )+ )
                # dgdl.g:24:16: ^( systemID ( game )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_systemID.nextNode(), root_1)

                # dgdl.g:24:27: ( game )+
                if not (stream_game.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_game.hasNext():
                    self._adaptor.addChild(root_1, stream_game.nextTree())


                stream_game.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "system"

    class systemID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.systemID_return, self).__init__()

            self.tree = None




    # $ANTLR start "systemID"
    # dgdl.g:27:1: systemID : identifier ;
    def systemID(self, ):

        retval = self.systemID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier6 = None



        try:
            try:
                # dgdl.g:27:10: ( identifier )
                # dgdl.g:27:12: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_systemID183)
                identifier6 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier6.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "systemID"

    class game_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.game_return, self).__init__()

            self.tree = None




    # $ANTLR start "game"
    # dgdl.g:29:1: game : gameID '{' composition ( rule )* ( interaction )+ '}' -> ^( gameID composition ( rule )* ( interaction )+ ) ;
    def game(self, ):

        retval = self.game_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal8 = None
        char_literal12 = None
        gameID7 = None

        composition9 = None

        rule10 = None

        interaction11 = None


        char_literal8_tree = None
        char_literal12_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_gameID = RewriteRuleSubtreeStream(self._adaptor, "rule gameID")
        stream_composition = RewriteRuleSubtreeStream(self._adaptor, "rule composition")
        stream_interaction = RewriteRuleSubtreeStream(self._adaptor, "rule interaction")
        stream_rule = RewriteRuleSubtreeStream(self._adaptor, "rule rule")
        try:
            try:
                # dgdl.g:29:7: ( gameID '{' composition ( rule )* ( interaction )+ '}' -> ^( gameID composition ( rule )* ( interaction )+ ) )
                # dgdl.g:29:9: gameID '{' composition ( rule )* ( interaction )+ '}'
                pass 
                self._state.following.append(self.FOLLOW_gameID_in_game192)
                gameID7 = self.gameID()

                self._state.following.pop()
                stream_gameID.add(gameID7.tree)
                char_literal8=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_game194) 
                stream_LBRACE.add(char_literal8)
                self._state.following.append(self.FOLLOW_composition_in_game196)
                composition9 = self.composition()

                self._state.following.pop()
                stream_composition.add(composition9.tree)
                # dgdl.g:29:32: ( rule )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == RULE) :
                        alt2 = 1


                    if alt2 == 1:
                        # dgdl.g:29:33: rule
                        pass 
                        self._state.following.append(self.FOLLOW_rule_in_game199)
                        rule10 = self.rule()

                        self._state.following.pop()
                        stream_rule.add(rule10.tree)


                    else:
                        break #loop2
                # dgdl.g:29:40: ( interaction )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == INTERACTION) :
                        alt3 = 1


                    if alt3 == 1:
                        # dgdl.g:29:41: interaction
                        pass 
                        self._state.following.append(self.FOLLOW_interaction_in_game204)
                        interaction11 = self.interaction()

                        self._state.following.pop()
                        stream_interaction.add(interaction11.tree)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1
                char_literal12=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_game208) 
                stream_RBRACE.add(char_literal12)

                # AST Rewrite
                # elements: rule, gameID, interaction, composition
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 30:13: -> ^( gameID composition ( rule )* ( interaction )+ )
                # dgdl.g:30:16: ^( gameID composition ( rule )* ( interaction )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_gameID.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_composition.nextTree())
                # dgdl.g:30:37: ( rule )*
                while stream_rule.hasNext():
                    self._adaptor.addChild(root_1, stream_rule.nextTree())


                stream_rule.reset();
                # dgdl.g:30:43: ( interaction )+
                if not (stream_interaction.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_interaction.hasNext():
                    self._adaptor.addChild(root_1, stream_interaction.nextTree())


                stream_interaction.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "game"

    class gameID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.gameID_return, self).__init__()

            self.tree = None




    # $ANTLR start "gameID"
    # dgdl.g:31:1: gameID : identifier ;
    def gameID(self, ):

        retval = self.gameID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier13 = None



        try:
            try:
                # dgdl.g:31:9: ( identifier )
                # dgdl.g:31:11: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_gameID242)
                identifier13 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier13.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "gameID"

    class composition_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.composition_return, self).__init__()

            self.tree = None




    # $ANTLR start "composition"
    # dgdl.g:37:1: composition : turns ( roleList )? participants ( player )+ ( extURImap )* ( plugin )* ( store )* ( backtrack )? ;
    def composition(self, ):

        retval = self.composition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        turns14 = None

        roleList15 = None

        participants16 = None

        player17 = None

        extURImap18 = None

        plugin19 = None

        store20 = None

        backtrack21 = None



        try:
            try:
                # dgdl.g:37:13: ( turns ( roleList )? participants ( player )+ ( extURImap )* ( plugin )* ( store )* ( backtrack )? )
                # dgdl.g:37:15: turns ( roleList )? participants ( player )+ ( extURImap )* ( plugin )* ( store )* ( backtrack )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_turns_in_composition255)
                turns14 = self.turns()

                self._state.following.pop()
                self._adaptor.addChild(root_0, turns14.tree)
                # dgdl.g:37:21: ( roleList )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == ROLES) :
                    alt4 = 1
                if alt4 == 1:
                    # dgdl.g:37:22: roleList
                    pass 
                    self._state.following.append(self.FOLLOW_roleList_in_composition258)
                    roleList15 = self.roleList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleList15.tree)



                self._state.following.append(self.FOLLOW_participants_in_composition262)
                participants16 = self.participants()

                self._state.following.pop()
                self._adaptor.addChild(root_0, participants16.tree)
                # dgdl.g:37:46: ( player )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == PLAYER) :
                        alt5 = 1


                    if alt5 == 1:
                        # dgdl.g:37:47: player
                        pass 
                        self._state.following.append(self.FOLLOW_player_in_composition265)
                        player17 = self.player()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, player17.tree)


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1
                # dgdl.g:37:56: ( extURImap )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == EXTURI) :
                        alt6 = 1


                    if alt6 == 1:
                        # dgdl.g:37:57: extURImap
                        pass 
                        self._state.following.append(self.FOLLOW_extURImap_in_composition270)
                        extURImap18 = self.extURImap()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, extURImap18.tree)


                    else:
                        break #loop6
                # dgdl.g:37:69: ( plugin )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 120) :
                        alt7 = 1


                    if alt7 == 1:
                        # dgdl.g:37:70: plugin
                        pass 
                        self._state.following.append(self.FOLLOW_plugin_in_composition275)
                        plugin19 = self.plugin()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, plugin19.tree)


                    else:
                        break #loop7
                # dgdl.g:37:79: ( store )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == STORE) :
                        alt8 = 1


                    if alt8 == 1:
                        # dgdl.g:37:80: store
                        pass 
                        self._state.following.append(self.FOLLOW_store_in_composition280)
                        store20 = self.store()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, store20.tree)


                    else:
                        break #loop8
                # dgdl.g:37:88: ( backtrack )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == BACKTRACK) :
                    alt9 = 1
                if alt9 == 1:
                    # dgdl.g:37:89: backtrack
                    pass 
                    self._state.following.append(self.FOLLOW_backtrack_in_composition285)
                    backtrack21 = self.backtrack()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, backtrack21.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "composition"

    class turns_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.turns_return, self).__init__()

            self.tree = None




    # $ANTLR start "turns"
    # dgdl.g:39:1: turns : 'turns' '{' turnSize ',' ordering ( ',' maxTurns )? '}' -> ^( 'turns' turnSize ordering ( maxTurns )? ) ;
    def turns(self, ):

        retval = self.turns_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal22 = None
        char_literal23 = None
        char_literal25 = None
        char_literal27 = None
        char_literal29 = None
        turnSize24 = None

        ordering26 = None

        maxTurns28 = None


        string_literal22_tree = None
        char_literal23_tree = None
        char_literal25_tree = None
        char_literal27_tree = None
        char_literal29_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_TURNS = RewriteRuleTokenStream(self._adaptor, "token TURNS")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_turnSize = RewriteRuleSubtreeStream(self._adaptor, "rule turnSize")
        stream_ordering = RewriteRuleSubtreeStream(self._adaptor, "rule ordering")
        stream_maxTurns = RewriteRuleSubtreeStream(self._adaptor, "rule maxTurns")
        try:
            try:
                # dgdl.g:39:10: ( 'turns' '{' turnSize ',' ordering ( ',' maxTurns )? '}' -> ^( 'turns' turnSize ordering ( maxTurns )? ) )
                # dgdl.g:39:12: 'turns' '{' turnSize ',' ordering ( ',' maxTurns )? '}'
                pass 
                string_literal22=self.match(self.input, TURNS, self.FOLLOW_TURNS_in_turns298) 
                stream_TURNS.add(string_literal22)
                char_literal23=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_turns300) 
                stream_LBRACE.add(char_literal23)
                self._state.following.append(self.FOLLOW_turnSize_in_turns302)
                turnSize24 = self.turnSize()

                self._state.following.pop()
                stream_turnSize.add(turnSize24.tree)
                char_literal25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_turns304) 
                stream_COMMA.add(char_literal25)
                self._state.following.append(self.FOLLOW_ordering_in_turns306)
                ordering26 = self.ordering()

                self._state.following.pop()
                stream_ordering.add(ordering26.tree)
                # dgdl.g:39:46: ( ',' maxTurns )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == COMMA) :
                    alt10 = 1
                if alt10 == 1:
                    # dgdl.g:39:47: ',' maxTurns
                    pass 
                    char_literal27=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_turns309) 
                    stream_COMMA.add(char_literal27)
                    self._state.following.append(self.FOLLOW_maxTurns_in_turns311)
                    maxTurns28 = self.maxTurns()

                    self._state.following.pop()
                    stream_maxTurns.add(maxTurns28.tree)



                char_literal29=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_turns315) 
                stream_RBRACE.add(char_literal29)

                # AST Rewrite
                # elements: ordering, maxTurns, TURNS, turnSize
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 40:13: -> ^( 'turns' turnSize ordering ( maxTurns )? )
                # dgdl.g:40:16: ^( 'turns' turnSize ordering ( maxTurns )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_TURNS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_turnSize.nextTree())
                self._adaptor.addChild(root_1, stream_ordering.nextTree())
                # dgdl.g:40:44: ( maxTurns )?
                if stream_maxTurns.hasNext():
                    self._adaptor.addChild(root_1, stream_maxTurns.nextTree())


                stream_maxTurns.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "turns"

    class turnSize_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.turnSize_return, self).__init__()

            self.tree = None




    # $ANTLR start "turnSize"
    # dgdl.g:41:1: turnSize : 'magnitude' ':' ( number | 'single' | 'multiple' ) -> ^( 'magnitude' ( number )? ( 'single' )? ( 'multiple' )? ) ;
    def turnSize(self, ):

        retval = self.turnSize_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal30 = None
        char_literal31 = None
        string_literal33 = None
        string_literal34 = None
        number32 = None


        string_literal30_tree = None
        char_literal31_tree = None
        string_literal33_tree = None
        string_literal34_tree = None
        stream_MAGNITUDE = RewriteRuleTokenStream(self._adaptor, "token MAGNITUDE")
        stream_SINGLE = RewriteRuleTokenStream(self._adaptor, "token SINGLE")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_MULTIPLE = RewriteRuleTokenStream(self._adaptor, "token MULTIPLE")
        stream_number = RewriteRuleSubtreeStream(self._adaptor, "rule number")
        try:
            try:
                # dgdl.g:41:10: ( 'magnitude' ':' ( number | 'single' | 'multiple' ) -> ^( 'magnitude' ( number )? ( 'single' )? ( 'multiple' )? ) )
                # dgdl.g:41:12: 'magnitude' ':' ( number | 'single' | 'multiple' )
                pass 
                string_literal30=self.match(self.input, MAGNITUDE, self.FOLLOW_MAGNITUDE_in_turnSize347) 
                stream_MAGNITUDE.add(string_literal30)
                char_literal31=self.match(self.input, COLON, self.FOLLOW_COLON_in_turnSize349) 
                stream_COLON.add(char_literal31)
                # dgdl.g:41:28: ( number | 'single' | 'multiple' )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == Number:
                    alt11 = 1
                elif LA11 == SINGLE:
                    alt11 = 2
                elif LA11 == MULTIPLE:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # dgdl.g:41:29: number
                    pass 
                    self._state.following.append(self.FOLLOW_number_in_turnSize352)
                    number32 = self.number()

                    self._state.following.pop()
                    stream_number.add(number32.tree)


                elif alt11 == 2:
                    # dgdl.g:41:38: 'single'
                    pass 
                    string_literal33=self.match(self.input, SINGLE, self.FOLLOW_SINGLE_in_turnSize356) 
                    stream_SINGLE.add(string_literal33)


                elif alt11 == 3:
                    # dgdl.g:41:49: 'multiple'
                    pass 
                    string_literal34=self.match(self.input, MULTIPLE, self.FOLLOW_MULTIPLE_in_turnSize360) 
                    stream_MULTIPLE.add(string_literal34)




                # AST Rewrite
                # elements: MAGNITUDE, SINGLE, number, MULTIPLE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 42:13: -> ^( 'magnitude' ( number )? ( 'single' )? ( 'multiple' )? )
                # dgdl.g:42:16: ^( 'magnitude' ( number )? ( 'single' )? ( 'multiple' )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MAGNITUDE.nextNode(), root_1)

                # dgdl.g:42:30: ( number )?
                if stream_number.hasNext():
                    self._adaptor.addChild(root_1, stream_number.nextTree())


                stream_number.reset();
                # dgdl.g:42:38: ( 'single' )?
                if stream_SINGLE.hasNext():
                    self._adaptor.addChild(root_1, stream_SINGLE.nextNode())


                stream_SINGLE.reset();
                # dgdl.g:42:48: ( 'multiple' )?
                if stream_MULTIPLE.hasNext():
                    self._adaptor.addChild(root_1, stream_MULTIPLE.nextNode())


                stream_MULTIPLE.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "turnSize"

    class ordering_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.ordering_return, self).__init__()

            self.tree = None




    # $ANTLR start "ordering"
    # dgdl.g:43:1: ordering : 'ordering' ':' ( STRICT | LIBERAL ) -> ^( 'ordering' ( STRICT )? ( LIBERAL )? ) ;
    def ordering(self, ):

        retval = self.ordering_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal35 = None
        char_literal36 = None
        STRICT37 = None
        LIBERAL38 = None

        string_literal35_tree = None
        char_literal36_tree = None
        STRICT37_tree = None
        LIBERAL38_tree = None
        stream_STRICT = RewriteRuleTokenStream(self._adaptor, "token STRICT")
        stream_LIBERAL = RewriteRuleTokenStream(self._adaptor, "token LIBERAL")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_ORDERING = RewriteRuleTokenStream(self._adaptor, "token ORDERING")

        try:
            try:
                # dgdl.g:43:10: ( 'ordering' ':' ( STRICT | LIBERAL ) -> ^( 'ordering' ( STRICT )? ( LIBERAL )? ) )
                # dgdl.g:43:12: 'ordering' ':' ( STRICT | LIBERAL )
                pass 
                string_literal35=self.match(self.input, ORDERING, self.FOLLOW_ORDERING_in_ordering395) 
                stream_ORDERING.add(string_literal35)
                char_literal36=self.match(self.input, COLON, self.FOLLOW_COLON_in_ordering397) 
                stream_COLON.add(char_literal36)
                # dgdl.g:43:27: ( STRICT | LIBERAL )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == STRICT) :
                    alt12 = 1
                elif (LA12_0 == LIBERAL) :
                    alt12 = 2
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # dgdl.g:43:28: STRICT
                    pass 
                    STRICT37=self.match(self.input, STRICT, self.FOLLOW_STRICT_in_ordering400) 
                    stream_STRICT.add(STRICT37)


                elif alt12 == 2:
                    # dgdl.g:43:37: LIBERAL
                    pass 
                    LIBERAL38=self.match(self.input, LIBERAL, self.FOLLOW_LIBERAL_in_ordering404) 
                    stream_LIBERAL.add(LIBERAL38)




                # AST Rewrite
                # elements: STRICT, LIBERAL, ORDERING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 44:13: -> ^( 'ordering' ( STRICT )? ( LIBERAL )? )
                # dgdl.g:44:16: ^( 'ordering' ( STRICT )? ( LIBERAL )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ORDERING.nextNode(), root_1)

                # dgdl.g:44:29: ( STRICT )?
                if stream_STRICT.hasNext():
                    self._adaptor.addChild(root_1, stream_STRICT.nextNode())


                stream_STRICT.reset();
                # dgdl.g:44:37: ( LIBERAL )?
                if stream_LIBERAL.hasNext():
                    self._adaptor.addChild(root_1, stream_LIBERAL.nextNode())


                stream_LIBERAL.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ordering"

    class maxTurns_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.maxTurns_return, self).__init__()

            self.tree = None




    # $ANTLR start "maxTurns"
    # dgdl.g:45:1: maxTurns : 'maxturns' ':' ( number | runTimeVar | 'undefined' ) -> ^( 'maxturns' ( number )? ( runTimeVar )? ( 'undefined' )? ) ;
    def maxTurns(self, ):

        retval = self.maxTurns_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal39 = None
        char_literal40 = None
        string_literal43 = None
        number41 = None

        runTimeVar42 = None


        string_literal39_tree = None
        char_literal40_tree = None
        string_literal43_tree = None
        stream_MAXTURNS = RewriteRuleTokenStream(self._adaptor, "token MAXTURNS")
        stream_UNDEFINED = RewriteRuleTokenStream(self._adaptor, "token UNDEFINED")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_number = RewriteRuleSubtreeStream(self._adaptor, "rule number")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        try:
            try:
                # dgdl.g:45:10: ( 'maxturns' ':' ( number | runTimeVar | 'undefined' ) -> ^( 'maxturns' ( number )? ( runTimeVar )? ( 'undefined' )? ) )
                # dgdl.g:45:12: 'maxturns' ':' ( number | runTimeVar | 'undefined' )
                pass 
                string_literal39=self.match(self.input, MAXTURNS, self.FOLLOW_MAXTURNS_in_maxTurns436) 
                stream_MAXTURNS.add(string_literal39)
                char_literal40=self.match(self.input, COLON, self.FOLLOW_COLON_in_maxTurns438) 
                stream_COLON.add(char_literal40)
                # dgdl.g:45:27: ( number | runTimeVar | 'undefined' )
                alt13 = 3
                LA13 = self.input.LA(1)
                if LA13 == Number:
                    alt13 = 1
                elif LA13 == DOLLAR:
                    alt13 = 2
                elif LA13 == UNDEFINED:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # dgdl.g:45:28: number
                    pass 
                    self._state.following.append(self.FOLLOW_number_in_maxTurns441)
                    number41 = self.number()

                    self._state.following.pop()
                    stream_number.add(number41.tree)


                elif alt13 == 2:
                    # dgdl.g:45:37: runTimeVar
                    pass 
                    self._state.following.append(self.FOLLOW_runTimeVar_in_maxTurns445)
                    runTimeVar42 = self.runTimeVar()

                    self._state.following.pop()
                    stream_runTimeVar.add(runTimeVar42.tree)


                elif alt13 == 3:
                    # dgdl.g:45:50: 'undefined'
                    pass 
                    string_literal43=self.match(self.input, UNDEFINED, self.FOLLOW_UNDEFINED_in_maxTurns449) 
                    stream_UNDEFINED.add(string_literal43)




                # AST Rewrite
                # elements: MAXTURNS, UNDEFINED, number, runTimeVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 46:13: -> ^( 'maxturns' ( number )? ( runTimeVar )? ( 'undefined' )? )
                # dgdl.g:46:16: ^( 'maxturns' ( number )? ( runTimeVar )? ( 'undefined' )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MAXTURNS.nextNode(), root_1)

                # dgdl.g:46:29: ( number )?
                if stream_number.hasNext():
                    self._adaptor.addChild(root_1, stream_number.nextTree())


                stream_number.reset();
                # dgdl.g:46:37: ( runTimeVar )?
                if stream_runTimeVar.hasNext():
                    self._adaptor.addChild(root_1, stream_runTimeVar.nextTree())


                stream_runTimeVar.reset();
                # dgdl.g:46:49: ( 'undefined' )?
                if stream_UNDEFINED.hasNext():
                    self._adaptor.addChild(root_1, stream_UNDEFINED.nextNode())


                stream_UNDEFINED.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "maxTurns"

    class runTimeVar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.runTimeVar_return, self).__init__()

            self.tree = None




    # $ANTLR start "runTimeVar"
    # dgdl.g:47:1: runTimeVar : '$' identifier '$' ;
    def runTimeVar(self, ):

        retval = self.runTimeVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal44 = None
        char_literal46 = None
        identifier45 = None


        char_literal44_tree = None
        char_literal46_tree = None

        try:
            try:
                # dgdl.g:47:12: ( '$' identifier '$' )
                # dgdl.g:47:14: '$' identifier '$'
                pass 
                root_0 = self._adaptor.nil()

                char_literal44=self.match(self.input, DOLLAR, self.FOLLOW_DOLLAR_in_runTimeVar484)

                char_literal44_tree = self._adaptor.createWithPayload(char_literal44)
                self._adaptor.addChild(root_0, char_literal44_tree)

                self._state.following.append(self.FOLLOW_identifier_in_runTimeVar486)
                identifier45 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier45.tree)
                char_literal46=self.match(self.input, DOLLAR, self.FOLLOW_DOLLAR_in_runTimeVar488)

                char_literal46_tree = self._adaptor.createWithPayload(char_literal46)
                self._adaptor.addChild(root_0, char_literal46_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "runTimeVar"

    class roleList_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.roleList_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleList"
    # dgdl.g:49:1: roleList : 'roles' '{' role ( ',' role )* '}' -> ^( 'roles' ( role )+ ) ;
    def roleList(self, ):

        retval = self.roleList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal47 = None
        char_literal48 = None
        char_literal50 = None
        char_literal52 = None
        role49 = None

        role51 = None


        string_literal47_tree = None
        char_literal48_tree = None
        char_literal50_tree = None
        char_literal52_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_ROLES = RewriteRuleTokenStream(self._adaptor, "token ROLES")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_role = RewriteRuleSubtreeStream(self._adaptor, "rule role")
        try:
            try:
                # dgdl.g:49:13: ( 'roles' '{' role ( ',' role )* '}' -> ^( 'roles' ( role )+ ) )
                # dgdl.g:49:15: 'roles' '{' role ( ',' role )* '}'
                pass 
                string_literal47=self.match(self.input, ROLES, self.FOLLOW_ROLES_in_roleList499) 
                stream_ROLES.add(string_literal47)
                char_literal48=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_roleList501) 
                stream_LBRACE.add(char_literal48)
                self._state.following.append(self.FOLLOW_role_in_roleList503)
                role49 = self.role()

                self._state.following.pop()
                stream_role.add(role49.tree)
                # dgdl.g:49:32: ( ',' role )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COMMA) :
                        alt14 = 1


                    if alt14 == 1:
                        # dgdl.g:49:33: ',' role
                        pass 
                        char_literal50=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_roleList506) 
                        stream_COMMA.add(char_literal50)
                        self._state.following.append(self.FOLLOW_role_in_roleList508)
                        role51 = self.role()

                        self._state.following.pop()
                        stream_role.add(role51.tree)


                    else:
                        break #loop14
                char_literal52=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_roleList512) 
                stream_RBRACE.add(char_literal52)

                # AST Rewrite
                # elements: role, ROLES
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 50:13: -> ^( 'roles' ( role )+ )
                # dgdl.g:50:16: ^( 'roles' ( role )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ROLES.nextNode(), root_1)

                # dgdl.g:50:26: ( role )+
                if not (stream_role.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_role.hasNext():
                    self._adaptor.addChild(root_1, stream_role.nextTree())


                stream_role.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleList"

    class role_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.role_return, self).__init__()

            self.tree = None




    # $ANTLR start "role"
    # dgdl.g:51:1: role : ( LISTENER | SPEAKER | identifier ) ;
    def role(self, ):

        retval = self.role_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LISTENER53 = None
        SPEAKER54 = None
        identifier55 = None


        LISTENER53_tree = None
        SPEAKER54_tree = None

        try:
            try:
                # dgdl.g:51:13: ( ( LISTENER | SPEAKER | identifier ) )
                # dgdl.g:51:15: ( LISTENER | SPEAKER | identifier )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:51:15: ( LISTENER | SPEAKER | identifier )
                alt15 = 3
                LA15 = self.input.LA(1)
                if LA15 == LISTENER:
                    alt15 = 1
                elif LA15 == SPEAKER:
                    alt15 = 2
                elif LA15 == Identifier:
                    alt15 = 3
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # dgdl.g:51:16: LISTENER
                    pass 
                    LISTENER53=self.match(self.input, LISTENER, self.FOLLOW_LISTENER_in_role548)

                    LISTENER53_tree = self._adaptor.createWithPayload(LISTENER53)
                    self._adaptor.addChild(root_0, LISTENER53_tree)



                elif alt15 == 2:
                    # dgdl.g:51:27: SPEAKER
                    pass 
                    SPEAKER54=self.match(self.input, SPEAKER, self.FOLLOW_SPEAKER_in_role552)

                    SPEAKER54_tree = self._adaptor.createWithPayload(SPEAKER54)
                    self._adaptor.addChild(root_0, SPEAKER54_tree)



                elif alt15 == 3:
                    # dgdl.g:51:37: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_role556)
                    identifier55 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier55.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "role"

    class participants_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.participants_return, self).__init__()

            self.tree = None




    # $ANTLR start "participants"
    # dgdl.g:53:1: participants : 'players' '{' 'min' ':' minplayers ',' 'max' ':' maxplayers '}' -> ^( 'players' ^( 'min' minplayers ) ^( 'max' maxplayers ) ) ;
    def participants(self, ):

        retval = self.participants_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal56 = None
        char_literal57 = None
        string_literal58 = None
        char_literal59 = None
        char_literal61 = None
        string_literal62 = None
        char_literal63 = None
        char_literal65 = None
        minplayers60 = None

        maxplayers64 = None


        string_literal56_tree = None
        char_literal57_tree = None
        string_literal58_tree = None
        char_literal59_tree = None
        char_literal61_tree = None
        string_literal62_tree = None
        char_literal63_tree = None
        char_literal65_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_PLAYERS = RewriteRuleTokenStream(self._adaptor, "token PLAYERS")
        stream_MIN = RewriteRuleTokenStream(self._adaptor, "token MIN")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_MAX = RewriteRuleTokenStream(self._adaptor, "token MAX")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_maxplayers = RewriteRuleSubtreeStream(self._adaptor, "rule maxplayers")
        stream_minplayers = RewriteRuleSubtreeStream(self._adaptor, "rule minplayers")
        try:
            try:
                # dgdl.g:53:13: ( 'players' '{' 'min' ':' minplayers ',' 'max' ':' maxplayers '}' -> ^( 'players' ^( 'min' minplayers ) ^( 'max' maxplayers ) ) )
                # dgdl.g:53:15: 'players' '{' 'min' ':' minplayers ',' 'max' ':' maxplayers '}'
                pass 
                string_literal56=self.match(self.input, PLAYERS, self.FOLLOW_PLAYERS_in_participants564) 
                stream_PLAYERS.add(string_literal56)
                char_literal57=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_participants566) 
                stream_LBRACE.add(char_literal57)
                string_literal58=self.match(self.input, MIN, self.FOLLOW_MIN_in_participants568) 
                stream_MIN.add(string_literal58)
                char_literal59=self.match(self.input, COLON, self.FOLLOW_COLON_in_participants570) 
                stream_COLON.add(char_literal59)
                self._state.following.append(self.FOLLOW_minplayers_in_participants572)
                minplayers60 = self.minplayers()

                self._state.following.pop()
                stream_minplayers.add(minplayers60.tree)
                char_literal61=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_participants574) 
                stream_COMMA.add(char_literal61)
                string_literal62=self.match(self.input, MAX, self.FOLLOW_MAX_in_participants576) 
                stream_MAX.add(string_literal62)
                char_literal63=self.match(self.input, COLON, self.FOLLOW_COLON_in_participants578) 
                stream_COLON.add(char_literal63)
                self._state.following.append(self.FOLLOW_maxplayers_in_participants580)
                maxplayers64 = self.maxplayers()

                self._state.following.pop()
                stream_maxplayers.add(maxplayers64.tree)
                char_literal65=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_participants582) 
                stream_RBRACE.add(char_literal65)

                # AST Rewrite
                # elements: PLAYERS, minplayers, MIN, MAX, maxplayers
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 54:13: -> ^( 'players' ^( 'min' minplayers ) ^( 'max' maxplayers ) )
                # dgdl.g:54:16: ^( 'players' ^( 'min' minplayers ) ^( 'max' maxplayers ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PLAYERS.nextNode(), root_1)

                # dgdl.g:54:28: ^( 'min' minplayers )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_MIN.nextNode(), root_2)

                self._adaptor.addChild(root_2, stream_minplayers.nextTree())

                self._adaptor.addChild(root_1, root_2)
                # dgdl.g:54:48: ^( 'max' maxplayers )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(stream_MAX.nextNode(), root_2)

                self._adaptor.addChild(root_2, stream_maxplayers.nextTree())

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "participants"

    class minplayers_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.minplayers_return, self).__init__()

            self.tree = None




    # $ANTLR start "minplayers"
    # dgdl.g:55:1: minplayers : number ;
    def minplayers(self, ):

        retval = self.minplayers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        number66 = None



        try:
            try:
                # dgdl.g:55:13: ( number )
                # dgdl.g:55:15: number
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_number_in_minplayers620)
                number66 = self.number()

                self._state.following.pop()
                self._adaptor.addChild(root_0, number66.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "minplayers"

    class maxplayers_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.maxplayers_return, self).__init__()

            self.tree = None




    # $ANTLR start "maxplayers"
    # dgdl.g:56:1: maxplayers : ( number | 'undefined' ) ;
    def maxplayers(self, ):

        retval = self.maxplayers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal68 = None
        number67 = None


        string_literal68_tree = None

        try:
            try:
                # dgdl.g:56:13: ( ( number | 'undefined' ) )
                # dgdl.g:56:15: ( number | 'undefined' )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:56:15: ( number | 'undefined' )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == Number) :
                    alt16 = 1
                elif (LA16_0 == UNDEFINED) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # dgdl.g:56:16: number
                    pass 
                    self._state.following.append(self.FOLLOW_number_in_maxplayers629)
                    number67 = self.number()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, number67.tree)


                elif alt16 == 2:
                    # dgdl.g:56:25: 'undefined'
                    pass 
                    string_literal68=self.match(self.input, UNDEFINED, self.FOLLOW_UNDEFINED_in_maxplayers633)

                    string_literal68_tree = self._adaptor.createWithPayload(string_literal68)
                    self._adaptor.addChild(root_0, string_literal68_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "maxplayers"

    class player_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.player_return, self).__init__()

            self.tree = None




    # $ANTLR start "player"
    # dgdl.g:58:1: player : 'player' '{' 'id' ':' playerID ( ',' roleList )? ( ',' 'max' ':' maxplayers )? ( ',' 'min' ':' minplayers )? '}' -> ^( 'player' playerID ( roleList )? ( ^( 'max' maxplayers ) )? ( ^( 'min' minplayers ) )? ) ;
    def player(self, ):

        retval = self.player_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal69 = None
        char_literal70 = None
        string_literal71 = None
        char_literal72 = None
        char_literal74 = None
        char_literal76 = None
        string_literal77 = None
        char_literal78 = None
        char_literal80 = None
        string_literal81 = None
        char_literal82 = None
        char_literal84 = None
        playerID73 = None

        roleList75 = None

        maxplayers79 = None

        minplayers83 = None


        string_literal69_tree = None
        char_literal70_tree = None
        string_literal71_tree = None
        char_literal72_tree = None
        char_literal74_tree = None
        char_literal76_tree = None
        string_literal77_tree = None
        char_literal78_tree = None
        char_literal80_tree = None
        string_literal81_tree = None
        char_literal82_tree = None
        char_literal84_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_PLAYER = RewriteRuleTokenStream(self._adaptor, "token PLAYER")
        stream_MIN = RewriteRuleTokenStream(self._adaptor, "token MIN")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_MAX = RewriteRuleTokenStream(self._adaptor, "token MAX")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_maxplayers = RewriteRuleSubtreeStream(self._adaptor, "rule maxplayers")
        stream_roleList = RewriteRuleSubtreeStream(self._adaptor, "rule roleList")
        stream_minplayers = RewriteRuleSubtreeStream(self._adaptor, "rule minplayers")
        stream_playerID = RewriteRuleSubtreeStream(self._adaptor, "rule playerID")
        try:
            try:
                # dgdl.g:58:13: ( 'player' '{' 'id' ':' playerID ( ',' roleList )? ( ',' 'max' ':' maxplayers )? ( ',' 'min' ':' minplayers )? '}' -> ^( 'player' playerID ( roleList )? ( ^( 'max' maxplayers ) )? ( ^( 'min' minplayers ) )? ) )
                # dgdl.g:58:15: 'player' '{' 'id' ':' playerID ( ',' roleList )? ( ',' 'max' ':' maxplayers )? ( ',' 'min' ':' minplayers )? '}'
                pass 
                string_literal69=self.match(self.input, PLAYER, self.FOLLOW_PLAYER_in_player647) 
                stream_PLAYER.add(string_literal69)
                char_literal70=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_player649) 
                stream_LBRACE.add(char_literal70)
                string_literal71=self.match(self.input, ID, self.FOLLOW_ID_in_player651) 
                stream_ID.add(string_literal71)
                char_literal72=self.match(self.input, COLON, self.FOLLOW_COLON_in_player653) 
                stream_COLON.add(char_literal72)
                self._state.following.append(self.FOLLOW_playerID_in_player655)
                playerID73 = self.playerID()

                self._state.following.pop()
                stream_playerID.add(playerID73.tree)
                # dgdl.g:58:46: ( ',' roleList )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == COMMA) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == ROLES) :
                        alt17 = 1
                if alt17 == 1:
                    # dgdl.g:58:47: ',' roleList
                    pass 
                    char_literal74=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_player658) 
                    stream_COMMA.add(char_literal74)
                    self._state.following.append(self.FOLLOW_roleList_in_player660)
                    roleList75 = self.roleList()

                    self._state.following.pop()
                    stream_roleList.add(roleList75.tree)



                # dgdl.g:58:62: ( ',' 'max' ':' maxplayers )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == COMMA) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == MAX) :
                        alt18 = 1
                if alt18 == 1:
                    # dgdl.g:58:63: ',' 'max' ':' maxplayers
                    pass 
                    char_literal76=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_player665) 
                    stream_COMMA.add(char_literal76)
                    string_literal77=self.match(self.input, MAX, self.FOLLOW_MAX_in_player667) 
                    stream_MAX.add(string_literal77)
                    char_literal78=self.match(self.input, COLON, self.FOLLOW_COLON_in_player669) 
                    stream_COLON.add(char_literal78)
                    self._state.following.append(self.FOLLOW_maxplayers_in_player671)
                    maxplayers79 = self.maxplayers()

                    self._state.following.pop()
                    stream_maxplayers.add(maxplayers79.tree)



                # dgdl.g:58:90: ( ',' 'min' ':' minplayers )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == COMMA) :
                    alt19 = 1
                if alt19 == 1:
                    # dgdl.g:58:91: ',' 'min' ':' minplayers
                    pass 
                    char_literal80=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_player676) 
                    stream_COMMA.add(char_literal80)
                    string_literal81=self.match(self.input, MIN, self.FOLLOW_MIN_in_player678) 
                    stream_MIN.add(string_literal81)
                    char_literal82=self.match(self.input, COLON, self.FOLLOW_COLON_in_player680) 
                    stream_COLON.add(char_literal82)
                    self._state.following.append(self.FOLLOW_minplayers_in_player682)
                    minplayers83 = self.minplayers()

                    self._state.following.pop()
                    stream_minplayers.add(minplayers83.tree)



                char_literal84=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_player686) 
                stream_RBRACE.add(char_literal84)

                # AST Rewrite
                # elements: minplayers, roleList, MAX, PLAYER, maxplayers, MIN, playerID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 59:13: -> ^( 'player' playerID ( roleList )? ( ^( 'max' maxplayers ) )? ( ^( 'min' minplayers ) )? )
                # dgdl.g:59:16: ^( 'player' playerID ( roleList )? ( ^( 'max' maxplayers ) )? ( ^( 'min' minplayers ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PLAYER.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_playerID.nextTree())
                # dgdl.g:59:36: ( roleList )?
                if stream_roleList.hasNext():
                    self._adaptor.addChild(root_1, stream_roleList.nextTree())


                stream_roleList.reset();
                # dgdl.g:59:46: ( ^( 'max' maxplayers ) )?
                if stream_MAX.hasNext() or stream_maxplayers.hasNext():
                    # dgdl.g:59:46: ^( 'max' maxplayers )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_MAX.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_maxplayers.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_MAX.reset();
                stream_maxplayers.reset();
                # dgdl.g:59:67: ( ^( 'min' minplayers ) )?
                if stream_minplayers.hasNext() or stream_MIN.hasNext():
                    # dgdl.g:59:67: ^( 'min' minplayers )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_MIN.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_minplayers.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_minplayers.reset();
                stream_MIN.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "player"

    class playerID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.playerID_return, self).__init__()

            self.tree = None




    # $ANTLR start "playerID"
    # dgdl.g:60:1: playerID : ( identifier | runTimeVar ) ;
    def playerID(self, ):

        retval = self.playerID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier85 = None

        runTimeVar86 = None



        try:
            try:
                # dgdl.g:60:13: ( ( identifier | runTimeVar ) )
                # dgdl.g:60:15: ( identifier | runTimeVar )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:60:15: ( identifier | runTimeVar )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == Identifier) :
                    alt20 = 1
                elif (LA20_0 == DOLLAR) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # dgdl.g:60:16: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_playerID735)
                    identifier85 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier85.tree)


                elif alt20 == 2:
                    # dgdl.g:60:29: runTimeVar
                    pass 
                    self._state.following.append(self.FOLLOW_runTimeVar_in_playerID739)
                    runTimeVar86 = self.runTimeVar()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, runTimeVar86.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "playerID"

    class extURImap_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.extURImap_return, self).__init__()

            self.tree = None




    # $ANTLR start "extURImap"
    # dgdl.g:62:1: extURImap : 'extURI' '{' 'id' ':' extURIID ',' 'uri' ':' extURI '}' -> ^( 'extURI' extURIID extURI ) ;
    def extURImap(self, ):

        retval = self.extURImap_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal87 = None
        char_literal88 = None
        string_literal89 = None
        char_literal90 = None
        char_literal92 = None
        string_literal93 = None
        char_literal94 = None
        char_literal96 = None
        extURIID91 = None

        extURI95 = None


        string_literal87_tree = None
        char_literal88_tree = None
        string_literal89_tree = None
        char_literal90_tree = None
        char_literal92_tree = None
        string_literal93_tree = None
        char_literal94_tree = None
        char_literal96_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_EXTURI = RewriteRuleTokenStream(self._adaptor, "token EXTURI")
        stream_119 = RewriteRuleTokenStream(self._adaptor, "token 119")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_extURI = RewriteRuleSubtreeStream(self._adaptor, "rule extURI")
        stream_extURIID = RewriteRuleSubtreeStream(self._adaptor, "rule extURIID")
        try:
            try:
                # dgdl.g:62:13: ( 'extURI' '{' 'id' ':' extURIID ',' 'uri' ':' extURI '}' -> ^( 'extURI' extURIID extURI ) )
                # dgdl.g:62:15: 'extURI' '{' 'id' ':' extURIID ',' 'uri' ':' extURI '}'
                pass 
                string_literal87=self.match(self.input, EXTURI, self.FOLLOW_EXTURI_in_extURImap750) 
                stream_EXTURI.add(string_literal87)
                char_literal88=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_extURImap752) 
                stream_LBRACE.add(char_literal88)
                string_literal89=self.match(self.input, ID, self.FOLLOW_ID_in_extURImap754) 
                stream_ID.add(string_literal89)
                char_literal90=self.match(self.input, COLON, self.FOLLOW_COLON_in_extURImap756) 
                stream_COLON.add(char_literal90)
                self._state.following.append(self.FOLLOW_extURIID_in_extURImap758)
                extURIID91 = self.extURIID()

                self._state.following.pop()
                stream_extURIID.add(extURIID91.tree)
                char_literal92=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_extURImap760) 
                stream_COMMA.add(char_literal92)
                string_literal93=self.match(self.input, 119, self.FOLLOW_119_in_extURImap762) 
                stream_119.add(string_literal93)
                char_literal94=self.match(self.input, COLON, self.FOLLOW_COLON_in_extURImap764) 
                stream_COLON.add(char_literal94)
                self._state.following.append(self.FOLLOW_extURI_in_extURImap766)
                extURI95 = self.extURI()

                self._state.following.pop()
                stream_extURI.add(extURI95.tree)
                char_literal96=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_extURImap768) 
                stream_RBRACE.add(char_literal96)

                # AST Rewrite
                # elements: extURI, EXTURI, extURIID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 63:13: -> ^( 'extURI' extURIID extURI )
                # dgdl.g:63:16: ^( 'extURI' extURIID extURI )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EXTURI.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_extURIID.nextTree())
                self._adaptor.addChild(root_1, stream_extURI.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "extURImap"

    class extURIID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.extURIID_return, self).__init__()

            self.tree = None




    # $ANTLR start "extURIID"
    # dgdl.g:64:1: extURIID : identifier ;
    def extURIID(self, ):

        retval = self.extURIID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier97 = None



        try:
            try:
                # dgdl.g:64:13: ( identifier )
                # dgdl.g:64:15: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_extURIID800)
                identifier97 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier97.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "extURIID"

    class extURI_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.extURI_return, self).__init__()

            self.tree = None




    # $ANTLR start "extURI"
    # dgdl.g:65:1: extURI : STRINGLITERAL ;
    def extURI(self, ):

        retval = self.extURI_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRINGLITERAL98 = None

        STRINGLITERAL98_tree = None

        try:
            try:
                # dgdl.g:65:13: ( STRINGLITERAL )
                # dgdl.g:65:15: STRINGLITERAL
                pass 
                root_0 = self._adaptor.nil()

                STRINGLITERAL98=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_extURI812)

                STRINGLITERAL98_tree = self._adaptor.createWithPayload(STRINGLITERAL98)
                self._adaptor.addChild(root_0, STRINGLITERAL98_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "extURI"

    class store_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.store_return, self).__init__()

            self.tree = None




    # $ANTLR start "store"
    # dgdl.g:67:1: store : 'store' '{' 'id' ':' storeName ',' 'owner' ':' storeOwner ',' storeStructure ',' visibility ',' content '}' -> ^( 'store' storeName storeOwner storeStructure visibility content ) ;
    def store(self, ):

        retval = self.store_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal99 = None
        char_literal100 = None
        string_literal101 = None
        char_literal102 = None
        char_literal104 = None
        string_literal105 = None
        char_literal106 = None
        char_literal108 = None
        char_literal110 = None
        char_literal112 = None
        char_literal114 = None
        storeName103 = None

        storeOwner107 = None

        storeStructure109 = None

        visibility111 = None

        content113 = None


        string_literal99_tree = None
        char_literal100_tree = None
        string_literal101_tree = None
        char_literal102_tree = None
        char_literal104_tree = None
        string_literal105_tree = None
        char_literal106_tree = None
        char_literal108_tree = None
        char_literal110_tree = None
        char_literal112_tree = None
        char_literal114_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OWNER = RewriteRuleTokenStream(self._adaptor, "token OWNER")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_STORE = RewriteRuleTokenStream(self._adaptor, "token STORE")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_storeOwner = RewriteRuleSubtreeStream(self._adaptor, "rule storeOwner")
        stream_visibility = RewriteRuleSubtreeStream(self._adaptor, "rule visibility")
        stream_storeStructure = RewriteRuleSubtreeStream(self._adaptor, "rule storeStructure")
        stream_storeName = RewriteRuleSubtreeStream(self._adaptor, "rule storeName")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:67:13: ( 'store' '{' 'id' ':' storeName ',' 'owner' ':' storeOwner ',' storeStructure ',' visibility ',' content '}' -> ^( 'store' storeName storeOwner storeStructure visibility content ) )
                # dgdl.g:67:15: 'store' '{' 'id' ':' storeName ',' 'owner' ':' storeOwner ',' storeStructure ',' visibility ',' content '}'
                pass 
                string_literal99=self.match(self.input, STORE, self.FOLLOW_STORE_in_store826) 
                stream_STORE.add(string_literal99)
                char_literal100=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_store828) 
                stream_LBRACE.add(char_literal100)
                string_literal101=self.match(self.input, ID, self.FOLLOW_ID_in_store830) 
                stream_ID.add(string_literal101)
                char_literal102=self.match(self.input, COLON, self.FOLLOW_COLON_in_store832) 
                stream_COLON.add(char_literal102)
                self._state.following.append(self.FOLLOW_storeName_in_store834)
                storeName103 = self.storeName()

                self._state.following.pop()
                stream_storeName.add(storeName103.tree)
                char_literal104=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store836) 
                stream_COMMA.add(char_literal104)
                string_literal105=self.match(self.input, OWNER, self.FOLLOW_OWNER_in_store838) 
                stream_OWNER.add(string_literal105)
                char_literal106=self.match(self.input, COLON, self.FOLLOW_COLON_in_store840) 
                stream_COLON.add(char_literal106)
                self._state.following.append(self.FOLLOW_storeOwner_in_store842)
                storeOwner107 = self.storeOwner()

                self._state.following.pop()
                stream_storeOwner.add(storeOwner107.tree)
                char_literal108=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store844) 
                stream_COMMA.add(char_literal108)
                self._state.following.append(self.FOLLOW_storeStructure_in_store846)
                storeStructure109 = self.storeStructure()

                self._state.following.pop()
                stream_storeStructure.add(storeStructure109.tree)
                char_literal110=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store848) 
                stream_COMMA.add(char_literal110)
                self._state.following.append(self.FOLLOW_visibility_in_store850)
                visibility111 = self.visibility()

                self._state.following.pop()
                stream_visibility.add(visibility111.tree)
                char_literal112=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store852) 
                stream_COMMA.add(char_literal112)
                self._state.following.append(self.FOLLOW_content_in_store854)
                content113 = self.content()

                self._state.following.pop()
                stream_content.add(content113.tree)
                char_literal114=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_store856) 
                stream_RBRACE.add(char_literal114)

                # AST Rewrite
                # elements: storeOwner, content, STORE, storeStructure, storeName, visibility
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 68:13: -> ^( 'store' storeName storeOwner storeStructure visibility content )
                # dgdl.g:68:16: ^( 'store' storeName storeOwner storeStructure visibility content )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_STORE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_storeName.nextTree())
                self._adaptor.addChild(root_1, stream_storeOwner.nextTree())
                self._adaptor.addChild(root_1, stream_storeStructure.nextTree())
                self._adaptor.addChild(root_1, stream_visibility.nextTree())
                self._adaptor.addChild(root_1, stream_content.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "store"

    class storeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeName"
    # dgdl.g:69:1: storeName : identifier ;
    def storeName(self, ):

        retval = self.storeName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier115 = None



        try:
            try:
                # dgdl.g:69:13: ( identifier )
                # dgdl.g:69:15: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_storeName893)
                identifier115 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier115.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeName"

    class storeOwner_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeOwner_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeOwner"
    # dgdl.g:70:1: storeOwner : ( playerID | '{' playerID ( ',' playerID )+ '}' | SHARED );
    def storeOwner(self, ):

        retval = self.storeOwner_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal117 = None
        char_literal119 = None
        char_literal121 = None
        SHARED122 = None
        playerID116 = None

        playerID118 = None

        playerID120 = None


        char_literal117_tree = None
        char_literal119_tree = None
        char_literal121_tree = None
        SHARED122_tree = None

        try:
            try:
                # dgdl.g:70:13: ( playerID | '{' playerID ( ',' playerID )+ '}' | SHARED )
                alt22 = 3
                LA22 = self.input.LA(1)
                if LA22 == Identifier or LA22 == DOLLAR:
                    alt22 = 1
                elif LA22 == LBRACE:
                    alt22 = 2
                elif LA22 == SHARED:
                    alt22 = 3
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # dgdl.g:70:15: playerID
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_playerID_in_storeOwner901)
                    playerID116 = self.playerID()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, playerID116.tree)


                elif alt22 == 2:
                    # dgdl.g:70:26: '{' playerID ( ',' playerID )+ '}'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal117=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_storeOwner905)

                    char_literal117_tree = self._adaptor.createWithPayload(char_literal117)
                    self._adaptor.addChild(root_0, char_literal117_tree)

                    self._state.following.append(self.FOLLOW_playerID_in_storeOwner907)
                    playerID118 = self.playerID()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, playerID118.tree)
                    # dgdl.g:70:39: ( ',' playerID )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == COMMA) :
                            alt21 = 1


                        if alt21 == 1:
                            # dgdl.g:70:40: ',' playerID
                            pass 
                            char_literal119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeOwner910)

                            char_literal119_tree = self._adaptor.createWithPayload(char_literal119)
                            self._adaptor.addChild(root_0, char_literal119_tree)

                            self._state.following.append(self.FOLLOW_playerID_in_storeOwner912)
                            playerID120 = self.playerID()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, playerID120.tree)


                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1
                    char_literal121=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_storeOwner916)

                    char_literal121_tree = self._adaptor.createWithPayload(char_literal121)
                    self._adaptor.addChild(root_0, char_literal121_tree)



                elif alt22 == 3:
                    # dgdl.g:70:61: SHARED
                    pass 
                    root_0 = self._adaptor.nil()

                    SHARED122=self.match(self.input, SHARED, self.FOLLOW_SHARED_in_storeOwner920)

                    SHARED122_tree = self._adaptor.createWithPayload(SHARED122)
                    self._adaptor.addChild(root_0, SHARED122_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeOwner"

    class storeStructure_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeStructure_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeStructure"
    # dgdl.g:71:1: storeStructure : 'structure' ':' ( SET | QUEUE | STACK ) ;
    def storeStructure(self, ):

        retval = self.storeStructure_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal123 = None
        char_literal124 = None
        set125 = None

        string_literal123_tree = None
        char_literal124_tree = None
        set125_tree = None

        try:
            try:
                # dgdl.g:71:15: ( 'structure' ':' ( SET | QUEUE | STACK ) )
                # dgdl.g:71:17: 'structure' ':' ( SET | QUEUE | STACK )
                pass 
                root_0 = self._adaptor.nil()

                string_literal123=self.match(self.input, STRUCTURE, self.FOLLOW_STRUCTURE_in_storeStructure926)
                char_literal124=self.match(self.input, COLON, self.FOLLOW_COLON_in_storeStructure929)
                set125 = self.input.LT(1)
                if (SET <= self.input.LA(1) <= STACK):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set125))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeStructure"

    class visibility_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.visibility_return, self).__init__()

            self.tree = None




    # $ANTLR start "visibility"
    # dgdl.g:72:1: visibility : 'visibility' ':' ( PUBLIC | PRIVATE ) ;
    def visibility(self, ):

        retval = self.visibility_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal126 = None
        char_literal127 = None
        set128 = None

        string_literal126_tree = None
        char_literal127_tree = None
        set128_tree = None

        try:
            try:
                # dgdl.g:72:13: ( 'visibility' ':' ( PUBLIC | PRIVATE ) )
                # dgdl.g:72:15: 'visibility' ':' ( PUBLIC | PRIVATE )
                pass 
                root_0 = self._adaptor.nil()

                string_literal126=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_visibility950)
                char_literal127=self.match(self.input, COLON, self.FOLLOW_COLON_in_visibility953)
                set128 = self.input.LT(1)
                if (PUBLIC <= self.input.LA(1) <= PRIVATE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set128))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "visibility"

    class backtrack_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.backtrack_return, self).__init__()

            self.tree = None




    # $ANTLR start "backtrack"
    # dgdl.g:74:1: backtrack : 'backtrack' '{' ( 'on' | 'off' ) '}' -> ^( 'backtrack' ( 'on' )? ( 'off' )? ) ;
    def backtrack(self, ):

        retval = self.backtrack_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal129 = None
        char_literal130 = None
        string_literal131 = None
        string_literal132 = None
        char_literal133 = None

        string_literal129_tree = None
        char_literal130_tree = None
        string_literal131_tree = None
        string_literal132_tree = None
        char_literal133_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_BACKTRACK = RewriteRuleTokenStream(self._adaptor, "token BACKTRACK")
        stream_OFF = RewriteRuleTokenStream(self._adaptor, "token OFF")
        stream_ON = RewriteRuleTokenStream(self._adaptor, "token ON")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")

        try:
            try:
                # dgdl.g:74:13: ( 'backtrack' '{' ( 'on' | 'off' ) '}' -> ^( 'backtrack' ( 'on' )? ( 'off' )? ) )
                # dgdl.g:74:15: 'backtrack' '{' ( 'on' | 'off' ) '}'
                pass 
                string_literal129=self.match(self.input, BACKTRACK, self.FOLLOW_BACKTRACK_in_backtrack972) 
                stream_BACKTRACK.add(string_literal129)
                char_literal130=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_backtrack974) 
                stream_LBRACE.add(char_literal130)
                # dgdl.g:74:31: ( 'on' | 'off' )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == ON) :
                    alt23 = 1
                elif (LA23_0 == OFF) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # dgdl.g:74:32: 'on'
                    pass 
                    string_literal131=self.match(self.input, ON, self.FOLLOW_ON_in_backtrack977) 
                    stream_ON.add(string_literal131)


                elif alt23 == 2:
                    # dgdl.g:74:39: 'off'
                    pass 
                    string_literal132=self.match(self.input, OFF, self.FOLLOW_OFF_in_backtrack981) 
                    stream_OFF.add(string_literal132)



                char_literal133=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_backtrack984) 
                stream_RBRACE.add(char_literal133)

                # AST Rewrite
                # elements: BACKTRACK, OFF, ON
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 75:13: -> ^( 'backtrack' ( 'on' )? ( 'off' )? )
                # dgdl.g:75:16: ^( 'backtrack' ( 'on' )? ( 'off' )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_BACKTRACK.nextNode(), root_1)

                # dgdl.g:75:30: ( 'on' )?
                if stream_ON.hasNext():
                    self._adaptor.addChild(root_1, stream_ON.nextNode())


                stream_ON.reset();
                # dgdl.g:75:36: ( 'off' )?
                if stream_OFF.hasNext():
                    self._adaptor.addChild(root_1, stream_OFF.nextNode())


                stream_OFF.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "backtrack"

    class plugin_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.plugin_return, self).__init__()

            self.tree = None




    # $ANTLR start "plugin"
    # dgdl.g:77:1: plugin : 'plugin' '{' 'id' ':' identifier ',' 'name' ':' STRINGLITERAL '}' -> ^( 'plugin' identifier STRINGLITERAL ) ;
    def plugin(self, ):

        retval = self.plugin_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal134 = None
        char_literal135 = None
        string_literal136 = None
        char_literal137 = None
        char_literal139 = None
        string_literal140 = None
        char_literal141 = None
        STRINGLITERAL142 = None
        char_literal143 = None
        identifier138 = None


        string_literal134_tree = None
        char_literal135_tree = None
        string_literal136_tree = None
        char_literal137_tree = None
        char_literal139_tree = None
        string_literal140_tree = None
        char_literal141_tree = None
        STRINGLITERAL142_tree = None
        char_literal143_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_121 = RewriteRuleTokenStream(self._adaptor, "token 121")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_STRINGLITERAL = RewriteRuleTokenStream(self._adaptor, "token STRINGLITERAL")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_120 = RewriteRuleTokenStream(self._adaptor, "token 120")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # dgdl.g:77:13: ( 'plugin' '{' 'id' ':' identifier ',' 'name' ':' STRINGLITERAL '}' -> ^( 'plugin' identifier STRINGLITERAL ) )
                # dgdl.g:77:15: 'plugin' '{' 'id' ':' identifier ',' 'name' ':' STRINGLITERAL '}'
                pass 
                string_literal134=self.match(self.input, 120, self.FOLLOW_120_in_plugin1033) 
                stream_120.add(string_literal134)
                char_literal135=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_plugin1035) 
                stream_LBRACE.add(char_literal135)
                string_literal136=self.match(self.input, ID, self.FOLLOW_ID_in_plugin1037) 
                stream_ID.add(string_literal136)
                char_literal137=self.match(self.input, COLON, self.FOLLOW_COLON_in_plugin1039) 
                stream_COLON.add(char_literal137)
                self._state.following.append(self.FOLLOW_identifier_in_plugin1041)
                identifier138 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier138.tree)
                char_literal139=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_plugin1043) 
                stream_COMMA.add(char_literal139)
                string_literal140=self.match(self.input, 121, self.FOLLOW_121_in_plugin1045) 
                stream_121.add(string_literal140)
                char_literal141=self.match(self.input, COLON, self.FOLLOW_COLON_in_plugin1047) 
                stream_COLON.add(char_literal141)
                STRINGLITERAL142=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_plugin1049) 
                stream_STRINGLITERAL.add(STRINGLITERAL142)
                char_literal143=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_plugin1051) 
                stream_RBRACE.add(char_literal143)

                # AST Rewrite
                # elements: identifier, 120, STRINGLITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 78:13: -> ^( 'plugin' identifier STRINGLITERAL )
                # dgdl.g:78:16: ^( 'plugin' identifier STRINGLITERAL )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_120.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                self._adaptor.addChild(root_1, stream_STRINGLITERAL.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "plugin"

    class rule_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.rule_return, self).__init__()

            self.tree = None




    # $ANTLR start "rule"
    # dgdl.g:83:1: rule : 'rule' '{' 'id' ':' ruleID ',' 'scope' ':' scopeType ',' ruleBody '}' -> ^( 'rule' ruleID scopeType ruleBody ) ;
    def rule(self, ):

        retval = self.rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal144 = None
        char_literal145 = None
        string_literal146 = None
        char_literal147 = None
        char_literal149 = None
        string_literal150 = None
        char_literal151 = None
        char_literal153 = None
        char_literal155 = None
        ruleID148 = None

        scopeType152 = None

        ruleBody154 = None


        string_literal144_tree = None
        char_literal145_tree = None
        string_literal146_tree = None
        char_literal147_tree = None
        char_literal149_tree = None
        string_literal150_tree = None
        char_literal151_tree = None
        char_literal153_tree = None
        char_literal155_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RULE = RewriteRuleTokenStream(self._adaptor, "token RULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_scopeType = RewriteRuleSubtreeStream(self._adaptor, "rule scopeType")
        stream_ruleBody = RewriteRuleSubtreeStream(self._adaptor, "rule ruleBody")
        stream_ruleID = RewriteRuleSubtreeStream(self._adaptor, "rule ruleID")
        try:
            try:
                # dgdl.g:83:13: ( 'rule' '{' 'id' ':' ruleID ',' 'scope' ':' scopeType ',' ruleBody '}' -> ^( 'rule' ruleID scopeType ruleBody ) )
                # dgdl.g:83:15: 'rule' '{' 'id' ':' ruleID ',' 'scope' ':' scopeType ',' ruleBody '}'
                pass 
                string_literal144=self.match(self.input, RULE, self.FOLLOW_RULE_in_rule1092) 
                stream_RULE.add(string_literal144)
                char_literal145=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_rule1094) 
                stream_LBRACE.add(char_literal145)
                string_literal146=self.match(self.input, ID, self.FOLLOW_ID_in_rule1096) 
                stream_ID.add(string_literal146)
                char_literal147=self.match(self.input, COLON, self.FOLLOW_COLON_in_rule1098) 
                stream_COLON.add(char_literal147)
                self._state.following.append(self.FOLLOW_ruleID_in_rule1100)
                ruleID148 = self.ruleID()

                self._state.following.pop()
                stream_ruleID.add(ruleID148.tree)
                char_literal149=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule1102) 
                stream_COMMA.add(char_literal149)
                string_literal150=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_rule1104) 
                stream_SCOPE.add(string_literal150)
                char_literal151=self.match(self.input, COLON, self.FOLLOW_COLON_in_rule1106) 
                stream_COLON.add(char_literal151)
                self._state.following.append(self.FOLLOW_scopeType_in_rule1108)
                scopeType152 = self.scopeType()

                self._state.following.pop()
                stream_scopeType.add(scopeType152.tree)
                char_literal153=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rule1110) 
                stream_COMMA.add(char_literal153)
                self._state.following.append(self.FOLLOW_ruleBody_in_rule1112)
                ruleBody154 = self.ruleBody()

                self._state.following.pop()
                stream_ruleBody.add(ruleBody154.tree)
                char_literal155=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_rule1114) 
                stream_RBRACE.add(char_literal155)

                # AST Rewrite
                # elements: scopeType, ruleBody, ruleID, RULE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 84:13: -> ^( 'rule' ruleID scopeType ruleBody )
                # dgdl.g:84:16: ^( 'rule' ruleID scopeType ruleBody )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_RULE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ruleID.nextTree())
                self._adaptor.addChild(root_1, stream_scopeType.nextTree())
                self._adaptor.addChild(root_1, stream_ruleBody.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rule"

    class ruleID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.ruleID_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleID"
    # dgdl.g:85:1: ruleID : identifier ;
    def ruleID(self, ):

        retval = self.ruleID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier156 = None



        try:
            try:
                # dgdl.g:85:13: ( identifier )
                # dgdl.g:85:15: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_ruleID1150)
                identifier156 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier156.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ruleID"

    class scopeType_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.scopeType_return, self).__init__()

            self.tree = None




    # $ANTLR start "scopeType"
    # dgdl.g:86:1: scopeType : ( INITIAL | TURNWISE | MOVEWISE ) ;
    def scopeType(self, ):

        retval = self.scopeType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set157 = None

        set157_tree = None

        try:
            try:
                # dgdl.g:86:13: ( ( INITIAL | TURNWISE | MOVEWISE ) )
                # dgdl.g:86:15: ( INITIAL | TURNWISE | MOVEWISE )
                pass 
                root_0 = self._adaptor.nil()

                set157 = self.input.LT(1)
                if (INITIAL <= self.input.LA(1) <= MOVEWISE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set157))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "scopeType"

    class ruleBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.ruleBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleBody"
    # dgdl.g:88:1: ruleBody : ( effects -> ^( EFFECTS effects ) | conditional -> ^( CONDITIONAL conditional ) );
    def ruleBody(self, ):

        retval = self.ruleBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        effects158 = None

        conditional159 = None


        stream_effects = RewriteRuleSubtreeStream(self._adaptor, "rule effects")
        stream_conditional = RewriteRuleSubtreeStream(self._adaptor, "rule conditional")
        try:
            try:
                # dgdl.g:88:13: ( effects -> ^( EFFECTS effects ) | conditional -> ^( CONDITIONAL conditional ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == LBRACE) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == IF) :
                        alt24 = 2
                    elif (LA24_1 == ASSIGN or LA24_1 == EXTEFFECT or LA24_1 == INITIATE or LA24_1 == MOVE or (STATUS <= LA24_1 <= STORE) or (125 <= LA24_1 <= 128) or LA24_1 == 130) :
                        alt24 = 1
                    else:
                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # dgdl.g:88:15: effects
                    pass 
                    self._state.following.append(self.FOLLOW_effects_in_ruleBody1180)
                    effects158 = self.effects()

                    self._state.following.pop()
                    stream_effects.add(effects158.tree)

                    # AST Rewrite
                    # elements: effects
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 88:24: -> ^( EFFECTS effects )
                    # dgdl.g:88:27: ^( EFFECTS effects )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EFFECTS, "EFFECTS"), root_1)

                    self._adaptor.addChild(root_1, stream_effects.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt24 == 2:
                    # dgdl.g:89:15: conditional
                    pass 
                    self._state.following.append(self.FOLLOW_conditional_in_ruleBody1205)
                    conditional159 = self.conditional()

                    self._state.following.pop()
                    stream_conditional.add(conditional159.tree)

                    # AST Rewrite
                    # elements: conditional
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 89:27: -> ^( CONDITIONAL conditional )
                    # dgdl.g:89:30: ^( CONDITIONAL conditional )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONDITIONAL, "CONDITIONAL"), root_1)

                    self._adaptor.addChild(root_1, stream_conditional.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ruleBody"

    class effects_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.effects_return, self).__init__()

            self.tree = None




    # $ANTLR start "effects"
    # dgdl.g:91:1: effects : '{' effect ( '&' effect )* '}' ;
    def effects(self, ):

        retval = self.effects_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal160 = None
        char_literal162 = None
        char_literal164 = None
        effect161 = None

        effect163 = None


        char_literal160_tree = None
        char_literal162_tree = None
        char_literal164_tree = None

        try:
            try:
                # dgdl.g:91:13: ( '{' effect ( '&' effect )* '}' )
                # dgdl.g:91:15: '{' effect ( '&' effect )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal160=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_effects1225)
                self._state.following.append(self.FOLLOW_effect_in_effects1228)
                effect161 = self.effect()

                self._state.following.pop()
                self._adaptor.addChild(root_0, effect161.tree)
                # dgdl.g:91:27: ( '&' effect )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == AND) :
                        alt25 = 1


                    if alt25 == 1:
                        # dgdl.g:91:28: '&' effect
                        pass 
                        char_literal162=self.match(self.input, AND, self.FOLLOW_AND_in_effects1231)
                        self._state.following.append(self.FOLLOW_effect_in_effects1234)
                        effect163 = self.effect()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, effect163.tree)


                    else:
                        break #loop25
                char_literal164=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_effects1238)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "effects"

    class effect_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.effect_return, self).__init__()

            self.tree = None




    # $ANTLR start "effect"
    # dgdl.g:92:1: effect : ( move | storeOp | statusUpdate | roleAssignment | externalEffect | send | receive | invoke | initiate | save ) ;
    def effect(self, ):

        retval = self.effect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        move165 = None

        storeOp166 = None

        statusUpdate167 = None

        roleAssignment168 = None

        externalEffect169 = None

        send170 = None

        receive171 = None

        invoke172 = None

        initiate173 = None

        save174 = None



        try:
            try:
                # dgdl.g:92:13: ( ( move | storeOp | statusUpdate | roleAssignment | externalEffect | send | receive | invoke | initiate | save ) )
                # dgdl.g:92:15: ( move | storeOp | statusUpdate | roleAssignment | externalEffect | send | receive | invoke | initiate | save )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:92:15: ( move | storeOp | statusUpdate | roleAssignment | externalEffect | send | receive | invoke | initiate | save )
                alt26 = 10
                LA26 = self.input.LA(1)
                if LA26 == MOVE:
                    alt26 = 1
                elif LA26 == STORE:
                    alt26 = 2
                elif LA26 == STATUS:
                    alt26 = 3
                elif LA26 == ASSIGN or LA26 == 125:
                    alt26 = 4
                elif LA26 == EXTEFFECT:
                    alt26 = 5
                elif LA26 == 126:
                    alt26 = 6
                elif LA26 == 127:
                    alt26 = 7
                elif LA26 == 128:
                    alt26 = 8
                elif LA26 == INITIATE:
                    alt26 = 9
                elif LA26 == 130:
                    alt26 = 10
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # dgdl.g:92:16: move
                    pass 
                    self._state.following.append(self.FOLLOW_move_in_effect1252)
                    move165 = self.move()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, move165.tree)


                elif alt26 == 2:
                    # dgdl.g:92:23: storeOp
                    pass 
                    self._state.following.append(self.FOLLOW_storeOp_in_effect1256)
                    storeOp166 = self.storeOp()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, storeOp166.tree)


                elif alt26 == 3:
                    # dgdl.g:92:33: statusUpdate
                    pass 
                    self._state.following.append(self.FOLLOW_statusUpdate_in_effect1260)
                    statusUpdate167 = self.statusUpdate()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statusUpdate167.tree)


                elif alt26 == 4:
                    # dgdl.g:92:48: roleAssignment
                    pass 
                    self._state.following.append(self.FOLLOW_roleAssignment_in_effect1264)
                    roleAssignment168 = self.roleAssignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleAssignment168.tree)


                elif alt26 == 5:
                    # dgdl.g:92:65: externalEffect
                    pass 
                    self._state.following.append(self.FOLLOW_externalEffect_in_effect1268)
                    externalEffect169 = self.externalEffect()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, externalEffect169.tree)


                elif alt26 == 6:
                    # dgdl.g:92:82: send
                    pass 
                    self._state.following.append(self.FOLLOW_send_in_effect1272)
                    send170 = self.send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, send170.tree)


                elif alt26 == 7:
                    # dgdl.g:92:89: receive
                    pass 
                    self._state.following.append(self.FOLLOW_receive_in_effect1276)
                    receive171 = self.receive()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, receive171.tree)


                elif alt26 == 8:
                    # dgdl.g:92:99: invoke
                    pass 
                    self._state.following.append(self.FOLLOW_invoke_in_effect1280)
                    invoke172 = self.invoke()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, invoke172.tree)


                elif alt26 == 9:
                    # dgdl.g:92:108: initiate
                    pass 
                    self._state.following.append(self.FOLLOW_initiate_in_effect1284)
                    initiate173 = self.initiate()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, initiate173.tree)


                elif alt26 == 10:
                    # dgdl.g:92:119: save
                    pass 
                    self._state.following.append(self.FOLLOW_save_in_effect1288)
                    save174 = self.save()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, save174.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "effect"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # dgdl.g:94:1: parameter : ( identifier | contentSet | contentVar | 'hello' );
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal178 = None
        identifier175 = None

        contentSet176 = None

        contentVar177 = None


        string_literal178_tree = None

        try:
            try:
                # dgdl.g:94:11: ( identifier | contentSet | contentVar | 'hello' )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 == Identifier:
                    alt27 = 1
                elif LA27 == UpperChar:
                    alt27 = 2
                elif LA27 == LowerChar or LA27 == NOT:
                    alt27 = 3
                elif LA27 == HELLO:
                    alt27 = 4
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # dgdl.g:94:13: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_parameter1297)
                    identifier175 = self.identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, identifier175.tree)


                elif alt27 == 2:
                    # dgdl.g:94:26: contentSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_contentSet_in_parameter1301)
                    contentSet176 = self.contentSet()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, contentSet176.tree)


                elif alt27 == 3:
                    # dgdl.g:94:39: contentVar
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_contentVar_in_parameter1305)
                    contentVar177 = self.contentVar()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, contentVar177.tree)


                elif alt27 == 4:
                    # dgdl.g:94:52: 'hello'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal178=self.match(self.input, HELLO, self.FOLLOW_HELLO_in_parameter1309)

                    string_literal178_tree = self._adaptor.createWithPayload(string_literal178)
                    self._adaptor.addChild(root_0, string_literal178_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameter"

    class content_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.content_return, self).__init__()

            self.tree = None




    # $ANTLR start "content"
    # dgdl.g:95:1: content : '{' ( contentItem ( ',' contentItem )* | '$...' | '...' ) '}' -> ^( CONTENT ( contentItem )* ( '$...' )? ( '...' )? ) ;
    def content(self, ):

        retval = self.content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal179 = None
        char_literal181 = None
        string_literal183 = None
        string_literal184 = None
        char_literal185 = None
        contentItem180 = None

        contentItem182 = None


        char_literal179_tree = None
        char_literal181_tree = None
        string_literal183_tree = None
        string_literal184_tree = None
        char_literal185_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_122 = RewriteRuleTokenStream(self._adaptor, "token 122")
        stream_123 = RewriteRuleTokenStream(self._adaptor, "token 123")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_contentItem = RewriteRuleSubtreeStream(self._adaptor, "rule contentItem")
        try:
            try:
                # dgdl.g:95:13: ( '{' ( contentItem ( ',' contentItem )* | '$...' | '...' ) '}' -> ^( CONTENT ( contentItem )* ( '$...' )? ( '...' )? ) )
                # dgdl.g:95:15: '{' ( contentItem ( ',' contentItem )* | '$...' | '...' ) '}'
                pass 
                char_literal179=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_content1320) 
                stream_LBRACE.add(char_literal179)
                # dgdl.g:95:19: ( contentItem ( ',' contentItem )* | '$...' | '...' )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 == STRINGLITERAL or LA29 == UpperChar or LA29 == LowerChar or LA29 == DOLLAR or LA29 == NOT:
                    alt29 = 1
                elif LA29 == 122:
                    alt29 = 2
                elif LA29 == 123:
                    alt29 = 3
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # dgdl.g:95:21: contentItem ( ',' contentItem )*
                    pass 
                    self._state.following.append(self.FOLLOW_contentItem_in_content1324)
                    contentItem180 = self.contentItem()

                    self._state.following.pop()
                    stream_contentItem.add(contentItem180.tree)
                    # dgdl.g:95:33: ( ',' contentItem )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == COMMA) :
                            alt28 = 1


                        if alt28 == 1:
                            # dgdl.g:95:34: ',' contentItem
                            pass 
                            char_literal181=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_content1327) 
                            stream_COMMA.add(char_literal181)
                            self._state.following.append(self.FOLLOW_contentItem_in_content1329)
                            contentItem182 = self.contentItem()

                            self._state.following.pop()
                            stream_contentItem.add(contentItem182.tree)


                        else:
                            break #loop28


                elif alt29 == 2:
                    # dgdl.g:95:54: '$...'
                    pass 
                    string_literal183=self.match(self.input, 122, self.FOLLOW_122_in_content1335) 
                    stream_122.add(string_literal183)


                elif alt29 == 3:
                    # dgdl.g:95:63: '...'
                    pass 
                    string_literal184=self.match(self.input, 123, self.FOLLOW_123_in_content1339) 
                    stream_123.add(string_literal184)



                char_literal185=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_content1343) 
                stream_RBRACE.add(char_literal185)

                # AST Rewrite
                # elements: 122, contentItem, 123
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 96:13: -> ^( CONTENT ( contentItem )* ( '$...' )? ( '...' )? )
                # dgdl.g:96:16: ^( CONTENT ( contentItem )* ( '$...' )? ( '...' )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONTENT, "CONTENT"), root_1)

                # dgdl.g:96:26: ( contentItem )*
                while stream_contentItem.hasNext():
                    self._adaptor.addChild(root_1, stream_contentItem.nextTree())


                stream_contentItem.reset();
                # dgdl.g:96:39: ( '$...' )?
                if stream_122.hasNext():
                    self._adaptor.addChild(root_1, stream_122.nextNode())


                stream_122.reset();
                # dgdl.g:96:47: ( '...' )?
                if stream_123.hasNext():
                    self._adaptor.addChild(root_1, stream_123.nextNode())


                stream_123.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "content"

    class contentItem_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.contentItem_return, self).__init__()

            self.tree = None




    # $ANTLR start "contentItem"
    # dgdl.g:97:1: contentItem : ( contentSet | contentVar | contentStr | rtv ) ;
    def contentItem(self, ):

        retval = self.contentItem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        contentSet186 = None

        contentVar187 = None

        contentStr188 = None

        rtv189 = None



        try:
            try:
                # dgdl.g:97:13: ( ( contentSet | contentVar | contentStr | rtv ) )
                # dgdl.g:97:15: ( contentSet | contentVar | contentStr | rtv )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:97:15: ( contentSet | contentVar | contentStr | rtv )
                alt30 = 4
                LA30 = self.input.LA(1)
                if LA30 == UpperChar:
                    alt30 = 1
                elif LA30 == NOT:
                    LA30_2 = self.input.LA(2)

                    if (LA30_2 == LowerChar) :
                        alt30 = 2
                    elif (LA30_2 == DOLLAR) :
                        alt30 = 4
                    else:
                        nvae = NoViableAltException("", 30, 2, self.input)

                        raise nvae

                elif LA30 == LowerChar:
                    alt30 = 2
                elif LA30 == STRINGLITERAL:
                    alt30 = 3
                elif LA30 == DOLLAR:
                    alt30 = 4
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # dgdl.g:97:16: contentSet
                    pass 
                    self._state.following.append(self.FOLLOW_contentSet_in_contentItem1378)
                    contentSet186 = self.contentSet()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, contentSet186.tree)


                elif alt30 == 2:
                    # dgdl.g:97:29: contentVar
                    pass 
                    self._state.following.append(self.FOLLOW_contentVar_in_contentItem1382)
                    contentVar187 = self.contentVar()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, contentVar187.tree)


                elif alt30 == 3:
                    # dgdl.g:97:42: contentStr
                    pass 
                    self._state.following.append(self.FOLLOW_contentStr_in_contentItem1386)
                    contentStr188 = self.contentStr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, contentStr188.tree)


                elif alt30 == 4:
                    # dgdl.g:97:55: rtv
                    pass 
                    self._state.following.append(self.FOLLOW_rtv_in_contentItem1390)
                    rtv189 = self.rtv()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rtv189.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "contentItem"

    class contentSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.contentSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "contentSet"
    # dgdl.g:98:1: contentSet : upperChar ;
    def contentSet(self, ):

        retval = self.contentSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        upperChar190 = None



        try:
            try:
                # dgdl.g:98:13: ( upperChar )
                # dgdl.g:98:15: upperChar
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_upperChar_in_contentSet1399)
                upperChar190 = self.upperChar()

                self._state.following.pop()
                self._adaptor.addChild(root_0, upperChar190.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "contentSet"

    class contentVar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.contentVar_return, self).__init__()

            self.tree = None




    # $ANTLR start "contentVar"
    # dgdl.g:99:1: contentVar : ( '!' )? lowerChar ;
    def contentVar(self, ):

        retval = self.contentVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal191 = None
        lowerChar192 = None


        char_literal191_tree = None

        try:
            try:
                # dgdl.g:99:13: ( ( '!' )? lowerChar )
                # dgdl.g:99:15: ( '!' )? lowerChar
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:99:15: ( '!' )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == NOT) :
                    alt31 = 1
                if alt31 == 1:
                    # dgdl.g:99:15: '!'
                    pass 
                    char_literal191=self.match(self.input, NOT, self.FOLLOW_NOT_in_contentVar1407)

                    char_literal191_tree = self._adaptor.createWithPayload(char_literal191)
                    self._adaptor.addChild(root_0, char_literal191_tree)




                self._state.following.append(self.FOLLOW_lowerChar_in_contentVar1409)
                lowerChar192 = self.lowerChar()

                self._state.following.pop()
                self._adaptor.addChild(root_0, lowerChar192.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "contentVar"

    class contentStr_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.contentStr_return, self).__init__()

            self.tree = None




    # $ANTLR start "contentStr"
    # dgdl.g:100:1: contentStr : STRINGLITERAL ;
    def contentStr(self, ):

        retval = self.contentStr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRINGLITERAL193 = None

        STRINGLITERAL193_tree = None

        try:
            try:
                # dgdl.g:100:13: ( STRINGLITERAL )
                # dgdl.g:100:15: STRINGLITERAL
                pass 
                root_0 = self._adaptor.nil()

                STRINGLITERAL193=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_contentStr1417)

                STRINGLITERAL193_tree = self._adaptor.createWithPayload(STRINGLITERAL193)
                self._adaptor.addChild(root_0, STRINGLITERAL193_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "contentStr"

    class rtv_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.rtv_return, self).__init__()

            self.tree = None




    # $ANTLR start "rtv"
    # dgdl.g:101:1: rtv : ( '!' )? runTimeVar -> ^( VAR ( '!' )? runTimeVar ) ;
    def rtv(self, ):

        retval = self.rtv_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal194 = None
        runTimeVar195 = None


        char_literal194_tree = None
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        try:
            try:
                # dgdl.g:101:13: ( ( '!' )? runTimeVar -> ^( VAR ( '!' )? runTimeVar ) )
                # dgdl.g:101:15: ( '!' )? runTimeVar
                pass 
                # dgdl.g:101:15: ( '!' )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == NOT) :
                    alt32 = 1
                if alt32 == 1:
                    # dgdl.g:101:15: '!'
                    pass 
                    char_literal194=self.match(self.input, NOT, self.FOLLOW_NOT_in_rtv1432) 
                    stream_NOT.add(char_literal194)



                self._state.following.append(self.FOLLOW_runTimeVar_in_rtv1434)
                runTimeVar195 = self.runTimeVar()

                self._state.following.pop()
                stream_runTimeVar.add(runTimeVar195.tree)

                # AST Rewrite
                # elements: NOT, runTimeVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 102:13: -> ^( VAR ( '!' )? runTimeVar )
                # dgdl.g:102:16: ^( VAR ( '!' )? runTimeVar )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                # dgdl.g:102:22: ( '!' )?
                if stream_NOT.hasNext():
                    self._adaptor.addChild(root_1, stream_NOT.nextNode())


                stream_NOT.reset();
                self._adaptor.addChild(root_1, stream_runTimeVar.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rtv"

    class conditional_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.conditional_return, self).__init__()

            self.tree = None




    # $ANTLR start "conditional"
    # dgdl.g:104:1: conditional : '{' 'if' requirements 'then' effects ( condelseif )? ( condelse )? '}' -> requirements 'then' ^( EFFECTS effects ) ( condelseif )* ( condelse )? ;
    def conditional(self, ):

        retval = self.conditional_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal196 = None
        string_literal197 = None
        string_literal199 = None
        char_literal203 = None
        requirements198 = None

        effects200 = None

        condelseif201 = None

        condelse202 = None


        char_literal196_tree = None
        string_literal197_tree = None
        string_literal199_tree = None
        char_literal203_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_requirements = RewriteRuleSubtreeStream(self._adaptor, "rule requirements")
        stream_effects = RewriteRuleSubtreeStream(self._adaptor, "rule effects")
        stream_condelse = RewriteRuleSubtreeStream(self._adaptor, "rule condelse")
        stream_condelseif = RewriteRuleSubtreeStream(self._adaptor, "rule condelseif")
        try:
            try:
                # dgdl.g:104:13: ( '{' 'if' requirements 'then' effects ( condelseif )? ( condelse )? '}' -> requirements 'then' ^( EFFECTS effects ) ( condelseif )* ( condelse )? )
                # dgdl.g:104:15: '{' 'if' requirements 'then' effects ( condelseif )? ( condelse )? '}'
                pass 
                char_literal196=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_conditional1465) 
                stream_LBRACE.add(char_literal196)
                string_literal197=self.match(self.input, IF, self.FOLLOW_IF_in_conditional1467) 
                stream_IF.add(string_literal197)
                self._state.following.append(self.FOLLOW_requirements_in_conditional1469)
                requirements198 = self.requirements()

                self._state.following.pop()
                stream_requirements.add(requirements198.tree)
                string_literal199=self.match(self.input, THEN, self.FOLLOW_THEN_in_conditional1471) 
                stream_THEN.add(string_literal199)
                self._state.following.append(self.FOLLOW_effects_in_conditional1473)
                effects200 = self.effects()

                self._state.following.pop()
                stream_effects.add(effects200.tree)
                # dgdl.g:104:52: ( condelseif )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == ELSEIF) :
                    alt33 = 1
                if alt33 == 1:
                    # dgdl.g:104:52: condelseif
                    pass 
                    self._state.following.append(self.FOLLOW_condelseif_in_conditional1475)
                    condelseif201 = self.condelseif()

                    self._state.following.pop()
                    stream_condelseif.add(condelseif201.tree)



                # dgdl.g:104:64: ( condelse )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == ELSE) :
                    alt34 = 1
                if alt34 == 1:
                    # dgdl.g:104:64: condelse
                    pass 
                    self._state.following.append(self.FOLLOW_condelse_in_conditional1478)
                    condelse202 = self.condelse()

                    self._state.following.pop()
                    stream_condelse.add(condelse202.tree)



                char_literal203=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_conditional1481) 
                stream_RBRACE.add(char_literal203)

                # AST Rewrite
                # elements: requirements, condelseif, THEN, effects, condelse
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 105:13: -> requirements 'then' ^( EFFECTS effects ) ( condelseif )* ( condelse )?
                self._adaptor.addChild(root_0, stream_requirements.nextTree())
                self._adaptor.addChild(root_0, stream_THEN.nextNode())
                # dgdl.g:105:36: ^( EFFECTS effects )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EFFECTS, "EFFECTS"), root_1)

                self._adaptor.addChild(root_1, stream_effects.nextTree())

                self._adaptor.addChild(root_0, root_1)
                # dgdl.g:105:55: ( condelseif )*
                while stream_condelseif.hasNext():
                    self._adaptor.addChild(root_0, stream_condelseif.nextTree())


                stream_condelseif.reset();
                # dgdl.g:105:67: ( condelse )?
                if stream_condelse.hasNext():
                    self._adaptor.addChild(root_0, stream_condelse.nextTree())


                stream_condelse.reset();



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "conditional"

    class condelseif_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.condelseif_return, self).__init__()

            self.tree = None




    # $ANTLR start "condelseif"
    # dgdl.g:106:1: condelseif : 'elseif' requirements 'then' effects ( condelseif )? -> 'elseif' ^( CONDITIONAL requirements 'then' ^( EFFECTS effects ) ( condelseif )? ) ;
    def condelseif(self, ):

        retval = self.condelseif_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal204 = None
        string_literal206 = None
        requirements205 = None

        effects207 = None

        condelseif208 = None


        string_literal204_tree = None
        string_literal206_tree = None
        stream_ELSEIF = RewriteRuleTokenStream(self._adaptor, "token ELSEIF")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_requirements = RewriteRuleSubtreeStream(self._adaptor, "rule requirements")
        stream_effects = RewriteRuleSubtreeStream(self._adaptor, "rule effects")
        stream_condelseif = RewriteRuleSubtreeStream(self._adaptor, "rule condelseif")
        try:
            try:
                # dgdl.g:106:13: ( 'elseif' requirements 'then' effects ( condelseif )? -> 'elseif' ^( CONDITIONAL requirements 'then' ^( EFFECTS effects ) ( condelseif )? ) )
                # dgdl.g:106:15: 'elseif' requirements 'then' effects ( condelseif )?
                pass 
                string_literal204=self.match(self.input, ELSEIF, self.FOLLOW_ELSEIF_in_condelseif1519) 
                stream_ELSEIF.add(string_literal204)
                self._state.following.append(self.FOLLOW_requirements_in_condelseif1521)
                requirements205 = self.requirements()

                self._state.following.pop()
                stream_requirements.add(requirements205.tree)
                string_literal206=self.match(self.input, THEN, self.FOLLOW_THEN_in_condelseif1523) 
                stream_THEN.add(string_literal206)
                self._state.following.append(self.FOLLOW_effects_in_condelseif1525)
                effects207 = self.effects()

                self._state.following.pop()
                stream_effects.add(effects207.tree)
                # dgdl.g:106:52: ( condelseif )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == ELSEIF) :
                    alt35 = 1
                if alt35 == 1:
                    # dgdl.g:106:52: condelseif
                    pass 
                    self._state.following.append(self.FOLLOW_condelseif_in_condelseif1527)
                    condelseif208 = self.condelseif()

                    self._state.following.pop()
                    stream_condelseif.add(condelseif208.tree)




                # AST Rewrite
                # elements: requirements, THEN, condelseif, ELSEIF, effects
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 106:64: -> 'elseif' ^( CONDITIONAL requirements 'then' ^( EFFECTS effects ) ( condelseif )? )
                self._adaptor.addChild(root_0, stream_ELSEIF.nextNode())
                # dgdl.g:106:76: ^( CONDITIONAL requirements 'then' ^( EFFECTS effects ) ( condelseif )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONDITIONAL, "CONDITIONAL"), root_1)

                self._adaptor.addChild(root_1, stream_requirements.nextTree())
                self._adaptor.addChild(root_1, stream_THEN.nextNode())
                # dgdl.g:106:110: ^( EFFECTS effects )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(EFFECTS, "EFFECTS"), root_2)

                self._adaptor.addChild(root_2, stream_effects.nextTree())

                self._adaptor.addChild(root_1, root_2)
                # dgdl.g:106:129: ( condelseif )?
                if stream_condelseif.hasNext():
                    self._adaptor.addChild(root_1, stream_condelseif.nextTree())


                stream_condelseif.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "condelseif"

    class condelse_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.condelse_return, self).__init__()

            self.tree = None




    # $ANTLR start "condelse"
    # dgdl.g:107:1: condelse : 'else' effects -> 'else' ^( EFFECTS effects ) ;
    def condelse(self, ):

        retval = self.condelse_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal209 = None
        effects210 = None


        string_literal209_tree = None
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_effects = RewriteRuleSubtreeStream(self._adaptor, "rule effects")
        try:
            try:
                # dgdl.g:107:13: ( 'else' effects -> 'else' ^( EFFECTS effects ) )
                # dgdl.g:107:15: 'else' effects
                pass 
                string_literal209=self.match(self.input, ELSE, self.FOLLOW_ELSE_in_condelse1559) 
                stream_ELSE.add(string_literal209)
                self._state.following.append(self.FOLLOW_effects_in_condelse1561)
                effects210 = self.effects()

                self._state.following.pop()
                stream_effects.add(effects210.tree)

                # AST Rewrite
                # elements: ELSE, effects
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 107:30: -> 'else' ^( EFFECTS effects )
                self._adaptor.addChild(root_0, stream_ELSE.nextNode())
                # dgdl.g:107:40: ^( EFFECTS effects )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EFFECTS, "EFFECTS"), root_1)

                self._adaptor.addChild(root_1, stream_effects.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "condelse"

    class requirements_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.requirements_return, self).__init__()

            self.tree = None




    # $ANTLR start "requirements"
    # dgdl.g:109:1: requirements : '{' condition ( AND condition )* '}' -> ^( REQUIREMENTS condition ( AND condition )* ) ;
    def requirements(self, ):

        retval = self.requirements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal211 = None
        AND213 = None
        char_literal215 = None
        condition212 = None

        condition214 = None


        char_literal211_tree = None
        AND213_tree = None
        char_literal215_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_AND = RewriteRuleTokenStream(self._adaptor, "token AND")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # dgdl.g:109:13: ( '{' condition ( AND condition )* '}' -> ^( REQUIREMENTS condition ( AND condition )* ) )
                # dgdl.g:109:15: '{' condition ( AND condition )* '}'
                pass 
                char_literal211=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_requirements1578) 
                stream_LBRACE.add(char_literal211)
                self._state.following.append(self.FOLLOW_condition_in_requirements1580)
                condition212 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition212.tree)
                # dgdl.g:109:29: ( AND condition )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == AND) :
                        alt36 = 1


                    if alt36 == 1:
                        # dgdl.g:109:30: AND condition
                        pass 
                        AND213=self.match(self.input, AND, self.FOLLOW_AND_in_requirements1583) 
                        stream_AND.add(AND213)
                        self._state.following.append(self.FOLLOW_condition_in_requirements1585)
                        condition214 = self.condition()

                        self._state.following.pop()
                        stream_condition.add(condition214.tree)


                    else:
                        break #loop36
                char_literal215=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_requirements1589) 
                stream_RBRACE.add(char_literal215)

                # AST Rewrite
                # elements: condition, condition, AND
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 109:50: -> ^( REQUIREMENTS condition ( AND condition )* )
                # dgdl.g:109:53: ^( REQUIREMENTS condition ( AND condition )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REQUIREMENTS, "REQUIREMENTS"), root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())
                # dgdl.g:109:78: ( AND condition )*
                while stream_condition.hasNext() or stream_AND.hasNext():
                    self._adaptor.addChild(root_1, stream_AND.nextNode())
                    self._adaptor.addChild(root_1, stream_condition.nextTree())


                stream_condition.reset();
                stream_AND.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "requirements"

    class condition_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.condition_return, self).__init__()

            self.tree = None




    # $ANTLR start "condition"
    # dgdl.g:112:1: condition : ( event | storeInspection | roleInspection | magnitude | storeComparison | dialogueSize | correspondence | relation | currentPlayer | externalCondition | value ) ;
    def condition(self, ):

        retval = self.condition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        event216 = None

        storeInspection217 = None

        roleInspection218 = None

        magnitude219 = None

        storeComparison220 = None

        dialogueSize221 = None

        correspondence222 = None

        relation223 = None

        currentPlayer224 = None

        externalCondition225 = None

        value226 = None



        try:
            try:
                # dgdl.g:112:13: ( ( event | storeInspection | roleInspection | magnitude | storeComparison | dialogueSize | correspondence | relation | currentPlayer | externalCondition | value ) )
                # dgdl.g:112:15: ( event | storeInspection | roleInspection | magnitude | storeComparison | dialogueSize | correspondence | relation | currentPlayer | externalCondition | value )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:112:15: ( event | storeInspection | roleInspection | magnitude | storeComparison | dialogueSize | correspondence | relation | currentPlayer | externalCondition | value )
                alt37 = 11
                LA37 = self.input.LA(1)
                if LA37 == EVENT:
                    alt37 = 1
                elif LA37 == INSPECT:
                    alt37 = 2
                elif LA37 == INROLE:
                    alt37 = 3
                elif LA37 == SIZE:
                    alt37 = 4
                elif LA37 == MAGNITUDE:
                    alt37 = 5
                elif LA37 == NUMTURNS:
                    alt37 = 6
                elif LA37 == CORRESPONDS:
                    alt37 = 7
                elif LA37 == RELATION:
                    alt37 = 8
                elif LA37 == PLAYER:
                    alt37 = 9
                elif LA37 == EXTCONDITION:
                    alt37 = 10
                elif LA37 == 124:
                    alt37 = 11
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae

                if alt37 == 1:
                    # dgdl.g:112:16: event
                    pass 
                    self._state.following.append(self.FOLLOW_event_in_condition1618)
                    event216 = self.event()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, event216.tree)


                elif alt37 == 2:
                    # dgdl.g:112:24: storeInspection
                    pass 
                    self._state.following.append(self.FOLLOW_storeInspection_in_condition1622)
                    storeInspection217 = self.storeInspection()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, storeInspection217.tree)


                elif alt37 == 3:
                    # dgdl.g:112:42: roleInspection
                    pass 
                    self._state.following.append(self.FOLLOW_roleInspection_in_condition1626)
                    roleInspection218 = self.roleInspection()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleInspection218.tree)


                elif alt37 == 4:
                    # dgdl.g:112:59: magnitude
                    pass 
                    self._state.following.append(self.FOLLOW_magnitude_in_condition1630)
                    magnitude219 = self.magnitude()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, magnitude219.tree)


                elif alt37 == 5:
                    # dgdl.g:112:71: storeComparison
                    pass 
                    self._state.following.append(self.FOLLOW_storeComparison_in_condition1634)
                    storeComparison220 = self.storeComparison()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, storeComparison220.tree)


                elif alt37 == 6:
                    # dgdl.g:112:89: dialogueSize
                    pass 
                    self._state.following.append(self.FOLLOW_dialogueSize_in_condition1638)
                    dialogueSize221 = self.dialogueSize()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dialogueSize221.tree)


                elif alt37 == 7:
                    # dgdl.g:112:104: correspondence
                    pass 
                    self._state.following.append(self.FOLLOW_correspondence_in_condition1642)
                    correspondence222 = self.correspondence()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, correspondence222.tree)


                elif alt37 == 8:
                    # dgdl.g:112:121: relation
                    pass 
                    self._state.following.append(self.FOLLOW_relation_in_condition1646)
                    relation223 = self.relation()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, relation223.tree)


                elif alt37 == 9:
                    # dgdl.g:112:132: currentPlayer
                    pass 
                    self._state.following.append(self.FOLLOW_currentPlayer_in_condition1650)
                    currentPlayer224 = self.currentPlayer()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, currentPlayer224.tree)


                elif alt37 == 10:
                    # dgdl.g:112:148: externalCondition
                    pass 
                    self._state.following.append(self.FOLLOW_externalCondition_in_condition1654)
                    externalCondition225 = self.externalCondition()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, externalCondition225.tree)


                elif alt37 == 11:
                    # dgdl.g:112:168: value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_condition1658)
                    value226 = self.value()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, value226.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "condition"

    class interaction_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.interaction_return, self).__init__()

            self.tree = None




    # $ANTLR start "interaction"
    # dgdl.g:117:1: interaction : 'interaction' '{' moveID ( ',' addressee )? ( ',' target )? ( ',' forcetarget )* ( ',' opener )? ',' ruleBody '}' -> ^( 'interaction' moveID ( addressee )? ( target )? ( forcetarget )* ( opener )? ruleBody ) ;
    def interaction(self, ):

        retval = self.interaction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal227 = None
        char_literal228 = None
        char_literal230 = None
        char_literal232 = None
        char_literal234 = None
        char_literal236 = None
        char_literal238 = None
        char_literal240 = None
        moveID229 = None

        addressee231 = None

        target233 = None

        forcetarget235 = None

        opener237 = None

        ruleBody239 = None


        string_literal227_tree = None
        char_literal228_tree = None
        char_literal230_tree = None
        char_literal232_tree = None
        char_literal234_tree = None
        char_literal236_tree = None
        char_literal238_tree = None
        char_literal240_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_INTERACTION = RewriteRuleTokenStream(self._adaptor, "token INTERACTION")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_addressee = RewriteRuleSubtreeStream(self._adaptor, "rule addressee")
        stream_forcetarget = RewriteRuleSubtreeStream(self._adaptor, "rule forcetarget")
        stream_opener = RewriteRuleSubtreeStream(self._adaptor, "rule opener")
        stream_ruleBody = RewriteRuleSubtreeStream(self._adaptor, "rule ruleBody")
        stream_moveID = RewriteRuleSubtreeStream(self._adaptor, "rule moveID")
        stream_target = RewriteRuleSubtreeStream(self._adaptor, "rule target")
        try:
            try:
                # dgdl.g:117:13: ( 'interaction' '{' moveID ( ',' addressee )? ( ',' target )? ( ',' forcetarget )* ( ',' opener )? ',' ruleBody '}' -> ^( 'interaction' moveID ( addressee )? ( target )? ( forcetarget )* ( opener )? ruleBody ) )
                # dgdl.g:117:15: 'interaction' '{' moveID ( ',' addressee )? ( ',' target )? ( ',' forcetarget )* ( ',' opener )? ',' ruleBody '}'
                pass 
                string_literal227=self.match(self.input, INTERACTION, self.FOLLOW_INTERACTION_in_interaction1671) 
                stream_INTERACTION.add(string_literal227)
                char_literal228=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_interaction1673) 
                stream_LBRACE.add(char_literal228)
                self._state.following.append(self.FOLLOW_moveID_in_interaction1675)
                moveID229 = self.moveID()

                self._state.following.pop()
                stream_moveID.add(moveID229.tree)
                # dgdl.g:117:40: ( ',' addressee )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == COMMA) :
                    LA38_1 = self.input.LA(2)

                    if (LA38_1 == DOLLAR) :
                        alt38 = 1
                if alt38 == 1:
                    # dgdl.g:117:41: ',' addressee
                    pass 
                    char_literal230=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interaction1678) 
                    stream_COMMA.add(char_literal230)
                    self._state.following.append(self.FOLLOW_addressee_in_interaction1680)
                    addressee231 = self.addressee()

                    self._state.following.pop()
                    stream_addressee.add(addressee231.tree)



                # dgdl.g:117:57: ( ',' target )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == COMMA) :
                    LA39_1 = self.input.LA(2)

                    if (LA39_1 == LBRACE) :
                        LA39_2 = self.input.LA(3)

                        if (LA39_2 == STRINGLITERAL or (UpperChar <= LA39_2 <= LowerChar) or LA39_2 == LESSTHAN or LA39_2 == DOLLAR or LA39_2 == NOT or (122 <= LA39_2 <= 123)) :
                            alt39 = 1
                if alt39 == 1:
                    # dgdl.g:117:58: ',' target
                    pass 
                    char_literal232=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interaction1685) 
                    stream_COMMA.add(char_literal232)
                    self._state.following.append(self.FOLLOW_target_in_interaction1687)
                    target233 = self.target()

                    self._state.following.pop()
                    stream_target.add(target233.tree)



                # dgdl.g:117:71: ( ',' forcetarget )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == COMMA) :
                        LA40_1 = self.input.LA(2)

                        if (LA40_1 == Identifier) :
                            alt40 = 1




                    if alt40 == 1:
                        # dgdl.g:117:72: ',' forcetarget
                        pass 
                        char_literal234=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interaction1692) 
                        stream_COMMA.add(char_literal234)
                        self._state.following.append(self.FOLLOW_forcetarget_in_interaction1694)
                        forcetarget235 = self.forcetarget()

                        self._state.following.pop()
                        stream_forcetarget.add(forcetarget235.tree)


                    else:
                        break #loop40
                # dgdl.g:117:90: ( ',' opener )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == COMMA) :
                    LA41_1 = self.input.LA(2)

                    if (LA41_1 == STRINGLITERAL) :
                        alt41 = 1
                if alt41 == 1:
                    # dgdl.g:117:91: ',' opener
                    pass 
                    char_literal236=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interaction1699) 
                    stream_COMMA.add(char_literal236)
                    self._state.following.append(self.FOLLOW_opener_in_interaction1701)
                    opener237 = self.opener()

                    self._state.following.pop()
                    stream_opener.add(opener237.tree)



                char_literal238=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interaction1705) 
                stream_COMMA.add(char_literal238)
                self._state.following.append(self.FOLLOW_ruleBody_in_interaction1707)
                ruleBody239 = self.ruleBody()

                self._state.following.pop()
                stream_ruleBody.add(ruleBody239.tree)
                char_literal240=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_interaction1709) 
                stream_RBRACE.add(char_literal240)

                # AST Rewrite
                # elements: forcetarget, target, opener, INTERACTION, addressee, ruleBody, moveID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 118:13: -> ^( 'interaction' moveID ( addressee )? ( target )? ( forcetarget )* ( opener )? ruleBody )
                # dgdl.g:118:16: ^( 'interaction' moveID ( addressee )? ( target )? ( forcetarget )* ( opener )? ruleBody )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_INTERACTION.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_moveID.nextTree())
                # dgdl.g:118:39: ( addressee )?
                if stream_addressee.hasNext():
                    self._adaptor.addChild(root_1, stream_addressee.nextTree())


                stream_addressee.reset();
                # dgdl.g:118:50: ( target )?
                if stream_target.hasNext():
                    self._adaptor.addChild(root_1, stream_target.nextTree())


                stream_target.reset();
                # dgdl.g:118:58: ( forcetarget )*
                while stream_forcetarget.hasNext():
                    self._adaptor.addChild(root_1, stream_forcetarget.nextTree())


                stream_forcetarget.reset();
                # dgdl.g:118:71: ( opener )?
                if stream_opener.hasNext():
                    self._adaptor.addChild(root_1, stream_opener.nextTree())


                stream_opener.reset();
                self._adaptor.addChild(root_1, stream_ruleBody.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "interaction"

    class addressee_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.addressee_return, self).__init__()

            self.tree = None




    # $ANTLR start "addressee"
    # dgdl.g:119:1: addressee : '$' identifier -> ^( '$' identifier ) ;
    def addressee(self, ):

        retval = self.addressee_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal241 = None
        identifier242 = None


        char_literal241_tree = None
        stream_DOLLAR = RewriteRuleTokenStream(self._adaptor, "token DOLLAR")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # dgdl.g:119:13: ( '$' identifier -> ^( '$' identifier ) )
                # dgdl.g:119:15: '$' identifier
                pass 
                char_literal241=self.match(self.input, DOLLAR, self.FOLLOW_DOLLAR_in_addressee1752) 
                stream_DOLLAR.add(char_literal241)
                self._state.following.append(self.FOLLOW_identifier_in_addressee1754)
                identifier242 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier242.tree)

                # AST Rewrite
                # elements: identifier, DOLLAR
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 120:13: -> ^( '$' identifier )
                # dgdl.g:120:16: ^( '$' identifier )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_DOLLAR.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "addressee"

    class target_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.target_return, self).__init__()

            self.tree = None




    # $ANTLR start "target"
    # dgdl.g:121:1: target : ( content -> ^( TARGET content ) | '{' schemeApp ',' schemeID '}' -> ^( TARGET schemeApp schemeID ) );
    def target(self, ):

        retval = self.target_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal244 = None
        char_literal246 = None
        char_literal248 = None
        content243 = None

        schemeApp245 = None

        schemeID247 = None


        char_literal244_tree = None
        char_literal246_tree = None
        char_literal248_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_schemeID = RewriteRuleSubtreeStream(self._adaptor, "rule schemeID")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        stream_schemeApp = RewriteRuleSubtreeStream(self._adaptor, "rule schemeApp")
        try:
            try:
                # dgdl.g:121:13: ( content -> ^( TARGET content ) | '{' schemeApp ',' schemeID '}' -> ^( TARGET schemeApp schemeID ) )
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == LBRACE) :
                    LA42_1 = self.input.LA(2)

                    if (LA42_1 == STRINGLITERAL or (UpperChar <= LA42_1 <= LowerChar) or LA42_1 == DOLLAR or LA42_1 == NOT or (122 <= LA42_1 <= 123)) :
                        alt42 = 1
                    elif (LA42_1 == LESSTHAN) :
                        alt42 = 2
                    else:
                        nvae = NoViableAltException("", 42, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # dgdl.g:121:15: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_target1786)
                    content243 = self.content()

                    self._state.following.pop()
                    stream_content.add(content243.tree)

                    # AST Rewrite
                    # elements: content
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 121:23: -> ^( TARGET content )
                    # dgdl.g:121:26: ^( TARGET content )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TARGET, "TARGET"), root_1)

                    self._adaptor.addChild(root_1, stream_content.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 2:
                    # dgdl.g:122:15: '{' schemeApp ',' schemeID '}'
                    pass 
                    char_literal244=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_target1810) 
                    stream_LBRACE.add(char_literal244)
                    self._state.following.append(self.FOLLOW_schemeApp_in_target1812)
                    schemeApp245 = self.schemeApp()

                    self._state.following.pop()
                    stream_schemeApp.add(schemeApp245.tree)
                    char_literal246=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_target1814) 
                    stream_COMMA.add(char_literal246)
                    self._state.following.append(self.FOLLOW_schemeID_in_target1816)
                    schemeID247 = self.schemeID()

                    self._state.following.pop()
                    stream_schemeID.add(schemeID247.tree)
                    char_literal248=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_target1818) 
                    stream_RBRACE.add(char_literal248)

                    # AST Rewrite
                    # elements: schemeID, schemeApp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 122:46: -> ^( TARGET schemeApp schemeID )
                    # dgdl.g:122:49: ^( TARGET schemeApp schemeID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TARGET, "TARGET"), root_1)

                    self._adaptor.addChild(root_1, stream_schemeApp.nextTree())
                    self._adaptor.addChild(root_1, stream_schemeID.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "target"

    class schemeApp_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.schemeApp_return, self).__init__()

            self.tree = None




    # $ANTLR start "schemeApp"
    # dgdl.g:123:1: schemeApp : '<' content ',' content '>' ;
    def schemeApp(self, ):

        retval = self.schemeApp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal249 = None
        char_literal251 = None
        char_literal253 = None
        content250 = None

        content252 = None


        char_literal249_tree = None
        char_literal251_tree = None
        char_literal253_tree = None

        try:
            try:
                # dgdl.g:123:13: ( '<' content ',' content '>' )
                # dgdl.g:123:15: '<' content ',' content '>'
                pass 
                root_0 = self._adaptor.nil()

                char_literal249=self.match(self.input, LESSTHAN, self.FOLLOW_LESSTHAN_in_schemeApp1837)

                char_literal249_tree = self._adaptor.createWithPayload(char_literal249)
                self._adaptor.addChild(root_0, char_literal249_tree)

                self._state.following.append(self.FOLLOW_content_in_schemeApp1839)
                content250 = self.content()

                self._state.following.pop()
                self._adaptor.addChild(root_0, content250.tree)
                char_literal251=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_schemeApp1841)

                char_literal251_tree = self._adaptor.createWithPayload(char_literal251)
                self._adaptor.addChild(root_0, char_literal251_tree)

                self._state.following.append(self.FOLLOW_content_in_schemeApp1843)
                content252 = self.content()

                self._state.following.pop()
                self._adaptor.addChild(root_0, content252.tree)
                char_literal253=self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_schemeApp1845)

                char_literal253_tree = self._adaptor.createWithPayload(char_literal253)
                self._adaptor.addChild(root_0, char_literal253_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "schemeApp"

    class forcetarget_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.forcetarget_return, self).__init__()

            self.tree = None




    # $ANTLR start "forcetarget"
    # dgdl.g:124:1: forcetarget : forceID ',' target -> ^( FORCETARGET forceID target ) ;
    def forcetarget(self, ):

        retval = self.forcetarget_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal255 = None
        forceID254 = None

        target256 = None


        char_literal255_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_forceID = RewriteRuleSubtreeStream(self._adaptor, "rule forceID")
        stream_target = RewriteRuleSubtreeStream(self._adaptor, "rule target")
        try:
            try:
                # dgdl.g:124:13: ( forceID ',' target -> ^( FORCETARGET forceID target ) )
                # dgdl.g:124:15: forceID ',' target
                pass 
                self._state.following.append(self.FOLLOW_forceID_in_forcetarget1852)
                forceID254 = self.forceID()

                self._state.following.pop()
                stream_forceID.add(forceID254.tree)
                char_literal255=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_forcetarget1854) 
                stream_COMMA.add(char_literal255)
                self._state.following.append(self.FOLLOW_target_in_forcetarget1856)
                target256 = self.target()

                self._state.following.pop()
                stream_target.add(target256.tree)

                # AST Rewrite
                # elements: forceID, target
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 125:13: -> ^( FORCETARGET forceID target )
                # dgdl.g:125:16: ^( FORCETARGET forceID target )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FORCETARGET, "FORCETARGET"), root_1)

                self._adaptor.addChild(root_1, stream_forceID.nextTree())
                self._adaptor.addChild(root_1, stream_target.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "forcetarget"

    class forceID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.forceID_return, self).__init__()

            self.tree = None




    # $ANTLR start "forceID"
    # dgdl.g:126:1: forceID : identifier ;
    def forceID(self, ):

        retval = self.forceID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier257 = None



        try:
            try:
                # dgdl.g:126:13: ( identifier )
                # dgdl.g:126:15: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_forceID1889)
                identifier257 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier257.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "forceID"

    class opener_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.opener_return, self).__init__()

            self.tree = None




    # $ANTLR start "opener"
    # dgdl.g:128:1: opener : STRINGLITERAL -> ^( OPENER STRINGLITERAL ) ;
    def opener(self, ):

        retval = self.opener_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRINGLITERAL258 = None

        STRINGLITERAL258_tree = None
        stream_STRINGLITERAL = RewriteRuleTokenStream(self._adaptor, "token STRINGLITERAL")

        try:
            try:
                # dgdl.g:128:13: ( STRINGLITERAL -> ^( OPENER STRINGLITERAL ) )
                # dgdl.g:128:15: STRINGLITERAL
                pass 
                STRINGLITERAL258=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_opener1902) 
                stream_STRINGLITERAL.add(STRINGLITERAL258)

                # AST Rewrite
                # elements: STRINGLITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 129:13: -> ^( OPENER STRINGLITERAL )
                # dgdl.g:129:16: ^( OPENER STRINGLITERAL )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPENER, "OPENER"), root_1)

                self._adaptor.addChild(root_1, stream_STRINGLITERAL.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "opener"

    class event_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.event_return, self).__init__()

            self.tree = None




    # $ANTLR start "event"
    # dgdl.g:133:1: event : 'event' '(' eventpos ',' moveID ( ',' content )? ( ',' user )? ( ',' requirements )? ')' -> ^( 'event' eventpos moveID ( content )? ( user )? ( requirements )? ) ;
    def event(self, ):

        retval = self.event_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal259 = None
        char_literal260 = None
        char_literal262 = None
        char_literal264 = None
        char_literal266 = None
        char_literal268 = None
        char_literal270 = None
        eventpos261 = None

        moveID263 = None

        content265 = None

        user267 = None

        requirements269 = None


        string_literal259_tree = None
        char_literal260_tree = None
        char_literal262_tree = None
        char_literal264_tree = None
        char_literal266_tree = None
        char_literal268_tree = None
        char_literal270_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_EVENT = RewriteRuleTokenStream(self._adaptor, "token EVENT")
        stream_requirements = RewriteRuleSubtreeStream(self._adaptor, "rule requirements")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        stream_eventpos = RewriteRuleSubtreeStream(self._adaptor, "rule eventpos")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        stream_moveID = RewriteRuleSubtreeStream(self._adaptor, "rule moveID")
        try:
            try:
                # dgdl.g:133:19: ( 'event' '(' eventpos ',' moveID ( ',' content )? ( ',' user )? ( ',' requirements )? ')' -> ^( 'event' eventpos moveID ( content )? ( user )? ( requirements )? ) )
                # dgdl.g:133:21: 'event' '(' eventpos ',' moveID ( ',' content )? ( ',' user )? ( ',' requirements )? ')'
                pass 
                string_literal259=self.match(self.input, EVENT, self.FOLLOW_EVENT_in_event1945) 
                stream_EVENT.add(string_literal259)
                char_literal260=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_event1947) 
                stream_LPAREN.add(char_literal260)
                self._state.following.append(self.FOLLOW_eventpos_in_event1949)
                eventpos261 = self.eventpos()

                self._state.following.pop()
                stream_eventpos.add(eventpos261.tree)
                char_literal262=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_event1951) 
                stream_COMMA.add(char_literal262)
                self._state.following.append(self.FOLLOW_moveID_in_event1953)
                moveID263 = self.moveID()

                self._state.following.pop()
                stream_moveID.add(moveID263.tree)
                # dgdl.g:133:53: ( ',' content )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == COMMA) :
                    LA43_1 = self.input.LA(2)

                    if (LA43_1 == LBRACE) :
                        LA43_3 = self.input.LA(3)

                        if (LA43_3 == STRINGLITERAL or (UpperChar <= LA43_3 <= LowerChar) or LA43_3 == DOLLAR or LA43_3 == NOT or (122 <= LA43_3 <= 123)) :
                            alt43 = 1
                if alt43 == 1:
                    # dgdl.g:133:54: ',' content
                    pass 
                    char_literal264=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_event1956) 
                    stream_COMMA.add(char_literal264)
                    self._state.following.append(self.FOLLOW_content_in_event1958)
                    content265 = self.content()

                    self._state.following.pop()
                    stream_content.add(content265.tree)



                # dgdl.g:133:69: ( ',' user )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == COMMA) :
                    LA44_1 = self.input.LA(2)

                    if ((LISTENER <= LA44_1 <= SPEAKER) or LA44_1 == Identifier) :
                        alt44 = 1
                if alt44 == 1:
                    # dgdl.g:133:70: ',' user
                    pass 
                    char_literal266=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_event1964) 
                    stream_COMMA.add(char_literal266)
                    self._state.following.append(self.FOLLOW_user_in_event1966)
                    user267 = self.user()

                    self._state.following.pop()
                    stream_user.add(user267.tree)



                # dgdl.g:133:81: ( ',' requirements )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == COMMA) :
                    alt45 = 1
                if alt45 == 1:
                    # dgdl.g:133:82: ',' requirements
                    pass 
                    char_literal268=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_event1971) 
                    stream_COMMA.add(char_literal268)
                    self._state.following.append(self.FOLLOW_requirements_in_event1973)
                    requirements269 = self.requirements()

                    self._state.following.pop()
                    stream_requirements.add(requirements269.tree)



                char_literal270=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_event1977) 
                stream_RPAREN.add(char_literal270)

                # AST Rewrite
                # elements: eventpos, user, requirements, EVENT, content, moveID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 134:19: -> ^( 'event' eventpos moveID ( content )? ( user )? ( requirements )? )
                # dgdl.g:134:22: ^( 'event' eventpos moveID ( content )? ( user )? ( requirements )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EVENT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_eventpos.nextTree())
                self._adaptor.addChild(root_1, stream_moveID.nextTree())
                # dgdl.g:134:48: ( content )?
                if stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset();
                # dgdl.g:134:57: ( user )?
                if stream_user.hasNext():
                    self._adaptor.addChild(root_1, stream_user.nextTree())


                stream_user.reset();
                # dgdl.g:134:63: ( requirements )?
                if stream_requirements.hasNext():
                    self._adaptor.addChild(root_1, stream_requirements.nextTree())


                stream_requirements.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "event"

    class eventpos_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.eventpos_return, self).__init__()

            self.tree = None




    # $ANTLR start "eventpos"
    # dgdl.g:135:1: eventpos : ( 'last' | '!last' | 'past' | '!past' ) ;
    def eventpos(self, ):

        retval = self.eventpos_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set271 = None

        set271_tree = None

        try:
            try:
                # dgdl.g:135:19: ( ( 'last' | '!last' | 'past' | '!past' ) )
                # dgdl.g:135:21: ( 'last' | '!last' | 'past' | '!past' )
                pass 
                root_0 = self._adaptor.nil()

                set271 = self.input.LT(1)
                if (NOTLAST <= self.input.LA(1) <= LAST) or (NOTPAST <= self.input.LA(1) <= PAST):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set271))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "eventpos"

    class storeInspection_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeInspection_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeInspection"
    # dgdl.g:137:1: storeInspection : 'inspect' '(' storepos ',' commitment ',' storeName ( ',' user )? ( ',' ( 'initial' | 'past' | 'current' ) )? ')' -> ^( 'inspect' storepos commitment storeName ( ^( USER user ) )? ( ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? ) )? ) ;
    def storeInspection(self, ):

        retval = self.storeInspection_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal272 = None
        char_literal273 = None
        char_literal275 = None
        char_literal277 = None
        char_literal279 = None
        char_literal281 = None
        string_literal282 = None
        string_literal283 = None
        string_literal284 = None
        char_literal285 = None
        storepos274 = None

        commitment276 = None

        storeName278 = None

        user280 = None


        string_literal272_tree = None
        char_literal273_tree = None
        char_literal275_tree = None
        char_literal277_tree = None
        char_literal279_tree = None
        char_literal281_tree = None
        string_literal282_tree = None
        string_literal283_tree = None
        string_literal284_tree = None
        char_literal285_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_INSPECT = RewriteRuleTokenStream(self._adaptor, "token INSPECT")
        stream_PAST = RewriteRuleTokenStream(self._adaptor, "token PAST")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_INITIAL = RewriteRuleTokenStream(self._adaptor, "token INITIAL")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_CURRENT = RewriteRuleTokenStream(self._adaptor, "token CURRENT")
        stream_storepos = RewriteRuleSubtreeStream(self._adaptor, "rule storepos")
        stream_commitment = RewriteRuleSubtreeStream(self._adaptor, "rule commitment")
        stream_storeName = RewriteRuleSubtreeStream(self._adaptor, "rule storeName")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        try:
            try:
                # dgdl.g:137:19: ( 'inspect' '(' storepos ',' commitment ',' storeName ( ',' user )? ( ',' ( 'initial' | 'past' | 'current' ) )? ')' -> ^( 'inspect' storepos commitment storeName ( ^( USER user ) )? ( ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? ) )? ) )
                # dgdl.g:137:21: 'inspect' '(' storepos ',' commitment ',' storeName ( ',' user )? ( ',' ( 'initial' | 'past' | 'current' ) )? ')'
                pass 
                string_literal272=self.match(self.input, INSPECT, self.FOLLOW_INSPECT_in_storeInspection2054) 
                stream_INSPECT.add(string_literal272)
                char_literal273=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_storeInspection2056) 
                stream_LPAREN.add(char_literal273)
                self._state.following.append(self.FOLLOW_storepos_in_storeInspection2058)
                storepos274 = self.storepos()

                self._state.following.pop()
                stream_storepos.add(storepos274.tree)
                char_literal275=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeInspection2060) 
                stream_COMMA.add(char_literal275)
                self._state.following.append(self.FOLLOW_commitment_in_storeInspection2062)
                commitment276 = self.commitment()

                self._state.following.pop()
                stream_commitment.add(commitment276.tree)
                char_literal277=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeInspection2064) 
                stream_COMMA.add(char_literal277)
                self._state.following.append(self.FOLLOW_storeName_in_storeInspection2066)
                storeName278 = self.storeName()

                self._state.following.pop()
                stream_storeName.add(storeName278.tree)
                # dgdl.g:137:73: ( ',' user )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == COMMA) :
                    LA46_1 = self.input.LA(2)

                    if ((LISTENER <= LA46_1 <= SPEAKER) or LA46_1 == Identifier) :
                        alt46 = 1
                if alt46 == 1:
                    # dgdl.g:137:74: ',' user
                    pass 
                    char_literal279=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeInspection2069) 
                    stream_COMMA.add(char_literal279)
                    self._state.following.append(self.FOLLOW_user_in_storeInspection2071)
                    user280 = self.user()

                    self._state.following.pop()
                    stream_user.add(user280.tree)



                # dgdl.g:137:85: ( ',' ( 'initial' | 'past' | 'current' ) )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == COMMA) :
                    alt48 = 1
                if alt48 == 1:
                    # dgdl.g:137:86: ',' ( 'initial' | 'past' | 'current' )
                    pass 
                    char_literal281=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeInspection2076) 
                    stream_COMMA.add(char_literal281)
                    # dgdl.g:137:90: ( 'initial' | 'past' | 'current' )
                    alt47 = 3
                    LA47 = self.input.LA(1)
                    if LA47 == INITIAL:
                        alt47 = 1
                    elif LA47 == PAST:
                        alt47 = 2
                    elif LA47 == CURRENT:
                        alt47 = 3
                    else:
                        nvae = NoViableAltException("", 47, 0, self.input)

                        raise nvae

                    if alt47 == 1:
                        # dgdl.g:137:91: 'initial'
                        pass 
                        string_literal282=self.match(self.input, INITIAL, self.FOLLOW_INITIAL_in_storeInspection2079) 
                        stream_INITIAL.add(string_literal282)


                    elif alt47 == 2:
                        # dgdl.g:137:103: 'past'
                        pass 
                        string_literal283=self.match(self.input, PAST, self.FOLLOW_PAST_in_storeInspection2083) 
                        stream_PAST.add(string_literal283)


                    elif alt47 == 3:
                        # dgdl.g:137:112: 'current'
                        pass 
                        string_literal284=self.match(self.input, CURRENT, self.FOLLOW_CURRENT_in_storeInspection2087) 
                        stream_CURRENT.add(string_literal284)






                char_literal285=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_storeInspection2092) 
                stream_RPAREN.add(char_literal285)

                # AST Rewrite
                # elements: PAST, storepos, storeName, commitment, user, CURRENT, INITIAL, INSPECT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 138:19: -> ^( 'inspect' storepos commitment storeName ( ^( USER user ) )? ( ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? ) )? )
                # dgdl.g:138:22: ^( 'inspect' storepos commitment storeName ( ^( USER user ) )? ( ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? ) )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_INSPECT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_storepos.nextTree())
                self._adaptor.addChild(root_1, stream_commitment.nextTree())
                self._adaptor.addChild(root_1, stream_storeName.nextTree())
                # dgdl.g:138:64: ( ^( USER user ) )?
                if stream_user.hasNext():
                    # dgdl.g:138:64: ^( USER user )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(USER, "USER"), root_2)

                    self._adaptor.addChild(root_2, stream_user.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_user.reset();
                # dgdl.g:138:78: ( ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? ) )?
                if stream_PAST.hasNext() or stream_CURRENT.hasNext() or stream_INITIAL.hasNext():
                    # dgdl.g:138:78: ^( TIME ( 'initial' )? ( 'past' )? ( 'current' )? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(TIME, "TIME"), root_2)

                    # dgdl.g:138:85: ( 'initial' )?
                    if stream_INITIAL.hasNext():
                        self._adaptor.addChild(root_2, stream_INITIAL.nextNode())


                    stream_INITIAL.reset();
                    # dgdl.g:138:96: ( 'past' )?
                    if stream_PAST.hasNext():
                        self._adaptor.addChild(root_2, stream_PAST.nextNode())


                    stream_PAST.reset();
                    # dgdl.g:138:104: ( 'current' )?
                    if stream_CURRENT.hasNext():
                        self._adaptor.addChild(root_2, stream_CURRENT.nextNode())


                    stream_CURRENT.reset();

                    self._adaptor.addChild(root_1, root_2)


                stream_PAST.reset();
                stream_CURRENT.reset();
                stream_INITIAL.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeInspection"

    class storepos_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storepos_return, self).__init__()

            self.tree = None




    # $ANTLR start "storepos"
    # dgdl.g:139:1: storepos : ( 'in' | '!in' | 'on' | '!on' | 'top' | '!top' ) ;
    def storepos(self, ):

        retval = self.storepos_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set286 = None

        set286_tree = None

        try:
            try:
                # dgdl.g:139:19: ( ( 'in' | '!in' | 'on' | '!on' | 'top' | '!top' ) )
                # dgdl.g:139:21: ( 'in' | '!in' | 'on' | '!on' | 'top' | '!top' )
                pass 
                root_0 = self._adaptor.nil()

                set286 = self.input.LT(1)
                if (NOTIN <= self.input.LA(1) <= IN) or (NOTON <= self.input.LA(1) <= ON) or (NOTTOP <= self.input.LA(1) <= TOP):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set286))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storepos"

    class roleInspection_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.roleInspection_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleInspection"
    # dgdl.g:141:1: roleInspection : 'inrole' '(' playerID ',' role ')' -> ^( 'inrole' playerID role ) ;
    def roleInspection(self, ):

        retval = self.roleInspection_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal287 = None
        char_literal288 = None
        char_literal290 = None
        char_literal292 = None
        playerID289 = None

        role291 = None


        string_literal287_tree = None
        char_literal288_tree = None
        char_literal290_tree = None
        char_literal292_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_INROLE = RewriteRuleTokenStream(self._adaptor, "token INROLE")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_role = RewriteRuleSubtreeStream(self._adaptor, "rule role")
        stream_playerID = RewriteRuleSubtreeStream(self._adaptor, "rule playerID")
        try:
            try:
                # dgdl.g:141:19: ( 'inrole' '(' playerID ',' role ')' -> ^( 'inrole' playerID role ) )
                # dgdl.g:141:21: 'inrole' '(' playerID ',' role ')'
                pass 
                string_literal287=self.match(self.input, INROLE, self.FOLLOW_INROLE_in_roleInspection2192) 
                stream_INROLE.add(string_literal287)
                char_literal288=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_roleInspection2194) 
                stream_LPAREN.add(char_literal288)
                self._state.following.append(self.FOLLOW_playerID_in_roleInspection2196)
                playerID289 = self.playerID()

                self._state.following.pop()
                stream_playerID.add(playerID289.tree)
                char_literal290=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_roleInspection2198) 
                stream_COMMA.add(char_literal290)
                self._state.following.append(self.FOLLOW_role_in_roleInspection2200)
                role291 = self.role()

                self._state.following.pop()
                stream_role.add(role291.tree)
                char_literal292=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_roleInspection2202) 
                stream_RPAREN.add(char_literal292)

                # AST Rewrite
                # elements: role, INROLE, playerID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 142:19: -> ^( 'inrole' playerID role )
                # dgdl.g:142:22: ^( 'inrole' playerID role )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_INROLE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_playerID.nextTree())
                self._adaptor.addChild(root_1, stream_role.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleInspection"

    class magnitude_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.magnitude_return, self).__init__()

            self.tree = None




    # $ANTLR start "magnitude"
    # dgdl.g:144:1: magnitude : 'size' '(' container ',' playerID ',' containersize ')' -> ^( 'size' container playerID containersize ) ;
    def magnitude(self, ):

        retval = self.magnitude_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal293 = None
        char_literal294 = None
        char_literal296 = None
        char_literal298 = None
        char_literal300 = None
        container295 = None

        playerID297 = None

        containersize299 = None


        string_literal293_tree = None
        char_literal294_tree = None
        char_literal296_tree = None
        char_literal298_tree = None
        char_literal300_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_SIZE = RewriteRuleTokenStream(self._adaptor, "token SIZE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_container = RewriteRuleSubtreeStream(self._adaptor, "rule container")
        stream_containersize = RewriteRuleSubtreeStream(self._adaptor, "rule containersize")
        stream_playerID = RewriteRuleSubtreeStream(self._adaptor, "rule playerID")
        try:
            try:
                # dgdl.g:144:19: ( 'size' '(' container ',' playerID ',' containersize ')' -> ^( 'size' container playerID containersize ) )
                # dgdl.g:144:21: 'size' '(' container ',' playerID ',' containersize ')'
                pass 
                string_literal293=self.match(self.input, SIZE, self.FOLLOW_SIZE_in_magnitude2246) 
                stream_SIZE.add(string_literal293)
                char_literal294=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_magnitude2248) 
                stream_LPAREN.add(char_literal294)
                self._state.following.append(self.FOLLOW_container_in_magnitude2250)
                container295 = self.container()

                self._state.following.pop()
                stream_container.add(container295.tree)
                char_literal296=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_magnitude2252) 
                stream_COMMA.add(char_literal296)
                self._state.following.append(self.FOLLOW_playerID_in_magnitude2254)
                playerID297 = self.playerID()

                self._state.following.pop()
                stream_playerID.add(playerID297.tree)
                char_literal298=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_magnitude2256) 
                stream_COMMA.add(char_literal298)
                self._state.following.append(self.FOLLOW_containersize_in_magnitude2258)
                containersize299 = self.containersize()

                self._state.following.pop()
                stream_containersize.add(containersize299.tree)
                char_literal300=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_magnitude2260) 
                stream_RPAREN.add(char_literal300)

                # AST Rewrite
                # elements: container, playerID, SIZE, containersize
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 145:19: -> ^( 'size' container playerID containersize )
                # dgdl.g:145:22: ^( 'size' container playerID containersize )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_SIZE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_container.nextTree())
                self._adaptor.addChild(root_1, stream_playerID.nextTree())
                self._adaptor.addChild(root_1, stream_containersize.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "magnitude"

    class container_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.container_return, self).__init__()

            self.tree = None




    # $ANTLR start "container"
    # dgdl.g:146:1: container : ( storeName | 'legalmoves' ) ;
    def container(self, ):

        retval = self.container_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal302 = None
        storeName301 = None


        string_literal302_tree = None

        try:
            try:
                # dgdl.g:146:19: ( ( storeName | 'legalmoves' ) )
                # dgdl.g:146:21: ( storeName | 'legalmoves' )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:146:21: ( storeName | 'legalmoves' )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == Identifier) :
                    alt49 = 1
                elif (LA49_0 == LEGALMOVES) :
                    alt49 = 2
                else:
                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # dgdl.g:146:22: storeName
                    pass 
                    self._state.following.append(self.FOLLOW_storeName_in_container2306)
                    storeName301 = self.storeName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, storeName301.tree)


                elif alt49 == 2:
                    # dgdl.g:146:34: 'legalmoves'
                    pass 
                    string_literal302=self.match(self.input, LEGALMOVES, self.FOLLOW_LEGALMOVES_in_container2310)

                    string_literal302_tree = self._adaptor.createWithPayload(string_literal302)
                    self._adaptor.addChild(root_0, string_literal302_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "container"

    class containersize_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.containersize_return, self).__init__()

            self.tree = None




    # $ANTLR start "containersize"
    # dgdl.g:147:1: containersize : ( 'empty' | '!empty' | Number ) ;
    def containersize(self, ):

        retval = self.containersize_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set303 = None

        set303_tree = None

        try:
            try:
                # dgdl.g:147:19: ( ( 'empty' | '!empty' | Number ) )
                # dgdl.g:147:21: ( 'empty' | '!empty' | Number )
                pass 
                root_0 = self._adaptor.nil()

                set303 = self.input.LT(1)
                if self.input.LA(1) == Number or (NOTEMPTY <= self.input.LA(1) <= EMPTY):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set303))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "containersize"

    class storeComparison_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeComparison_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeComparison"
    # dgdl.g:149:1: storeComparison : 'magnitude' '(' store1 ',' user1 ',' comparison ',' store2 ',' user2 ')' -> ^( 'magnitude' store1 user1 comparison store2 user2 ) ;
    def storeComparison(self, ):

        retval = self.storeComparison_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal304 = None
        char_literal305 = None
        char_literal307 = None
        char_literal309 = None
        char_literal311 = None
        char_literal313 = None
        char_literal315 = None
        store1306 = None

        user1308 = None

        comparison310 = None

        store2312 = None

        user2314 = None


        string_literal304_tree = None
        char_literal305_tree = None
        char_literal307_tree = None
        char_literal309_tree = None
        char_literal311_tree = None
        char_literal313_tree = None
        char_literal315_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_MAGNITUDE = RewriteRuleTokenStream(self._adaptor, "token MAGNITUDE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_user1 = RewriteRuleSubtreeStream(self._adaptor, "rule user1")
        stream_user2 = RewriteRuleSubtreeStream(self._adaptor, "rule user2")
        stream_comparison = RewriteRuleSubtreeStream(self._adaptor, "rule comparison")
        stream_store1 = RewriteRuleSubtreeStream(self._adaptor, "rule store1")
        stream_store2 = RewriteRuleSubtreeStream(self._adaptor, "rule store2")
        try:
            try:
                # dgdl.g:149:19: ( 'magnitude' '(' store1 ',' user1 ',' comparison ',' store2 ',' user2 ')' -> ^( 'magnitude' store1 user1 comparison store2 user2 ) )
                # dgdl.g:149:21: 'magnitude' '(' store1 ',' user1 ',' comparison ',' store2 ',' user2 ')'
                pass 
                string_literal304=self.match(self.input, MAGNITUDE, self.FOLLOW_MAGNITUDE_in_storeComparison2342) 
                stream_MAGNITUDE.add(string_literal304)
                char_literal305=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_storeComparison2344) 
                stream_LPAREN.add(char_literal305)
                self._state.following.append(self.FOLLOW_store1_in_storeComparison2346)
                store1306 = self.store1()

                self._state.following.pop()
                stream_store1.add(store1306.tree)
                char_literal307=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeComparison2348) 
                stream_COMMA.add(char_literal307)
                self._state.following.append(self.FOLLOW_user1_in_storeComparison2350)
                user1308 = self.user1()

                self._state.following.pop()
                stream_user1.add(user1308.tree)
                char_literal309=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeComparison2352) 
                stream_COMMA.add(char_literal309)
                self._state.following.append(self.FOLLOW_comparison_in_storeComparison2354)
                comparison310 = self.comparison()

                self._state.following.pop()
                stream_comparison.add(comparison310.tree)
                char_literal311=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeComparison2356) 
                stream_COMMA.add(char_literal311)
                self._state.following.append(self.FOLLOW_store2_in_storeComparison2358)
                store2312 = self.store2()

                self._state.following.pop()
                stream_store2.add(store2312.tree)
                char_literal313=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeComparison2360) 
                stream_COMMA.add(char_literal313)
                self._state.following.append(self.FOLLOW_user2_in_storeComparison2362)
                user2314 = self.user2()

                self._state.following.pop()
                stream_user2.add(user2314.tree)
                char_literal315=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_storeComparison2364) 
                stream_RPAREN.add(char_literal315)

                # AST Rewrite
                # elements: comparison, store2, MAGNITUDE, user2, user1, store1
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 150:19: -> ^( 'magnitude' store1 user1 comparison store2 user2 )
                # dgdl.g:150:22: ^( 'magnitude' store1 user1 comparison store2 user2 )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MAGNITUDE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_store1.nextTree())
                self._adaptor.addChild(root_1, stream_user1.nextTree())
                self._adaptor.addChild(root_1, stream_comparison.nextTree())
                self._adaptor.addChild(root_1, stream_store2.nextTree())
                self._adaptor.addChild(root_1, stream_user2.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeComparison"

    class comparison_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.comparison_return, self).__init__()

            self.tree = None




    # $ANTLR start "comparison"
    # dgdl.g:151:1: comparison : ( 'greater' | 'smaller' | 'equal' | '!equal' ) ;
    def comparison(self, ):

        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set316 = None

        set316_tree = None

        try:
            try:
                # dgdl.g:151:19: ( ( 'greater' | 'smaller' | 'equal' | '!equal' ) )
                # dgdl.g:151:21: ( 'greater' | 'smaller' | 'equal' | '!equal' )
                pass 
                root_0 = self._adaptor.nil()

                set316 = self.input.LT(1)
                if (NOTEQUAL <= self.input.LA(1) <= EQUAL) or self.input.LA(1) == GREATER or self.input.LA(1) == SMALLER:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set316))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "comparison"

    class store1_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.store1_return, self).__init__()

            self.tree = None




    # $ANTLR start "store1"
    # dgdl.g:152:1: store1 : storeName ;
    def store1(self, ):

        retval = self.store1_return()
        retval.start = self.input.LT(1)

        root_0 = None

        storeName317 = None



        try:
            try:
                # dgdl.g:152:19: ( storeName )
                # dgdl.g:152:21: storeName
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_storeName_in_store12444)
                storeName317 = self.storeName()

                self._state.following.pop()
                self._adaptor.addChild(root_0, storeName317.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "store1"

    class user1_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.user1_return, self).__init__()

            self.tree = None




    # $ANTLR start "user1"
    # dgdl.g:153:1: user1 : ( user | SHARED );
    def user1(self, ):

        retval = self.user1_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SHARED319 = None
        user318 = None


        SHARED319_tree = None

        try:
            try:
                # dgdl.g:153:19: ( user | SHARED )
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if ((LISTENER <= LA50_0 <= SPEAKER) or LA50_0 == Identifier) :
                    alt50 = 1
                elif (LA50_0 == SHARED) :
                    alt50 = 2
                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # dgdl.g:153:21: user
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_user_in_user12463)
                    user318 = self.user()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, user318.tree)


                elif alt50 == 2:
                    # dgdl.g:153:28: SHARED
                    pass 
                    root_0 = self._adaptor.nil()

                    SHARED319=self.match(self.input, SHARED, self.FOLLOW_SHARED_in_user12467)

                    SHARED319_tree = self._adaptor.createWithPayload(SHARED319)
                    self._adaptor.addChild(root_0, SHARED319_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "user1"

    class store2_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.store2_return, self).__init__()

            self.tree = None




    # $ANTLR start "store2"
    # dgdl.g:154:1: store2 : storeName ;
    def store2(self, ):

        retval = self.store2_return()
        retval.start = self.input.LT(1)

        root_0 = None

        storeName320 = None



        try:
            try:
                # dgdl.g:154:19: ( storeName )
                # dgdl.g:154:21: storeName
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_storeName_in_store22485)
                storeName320 = self.storeName()

                self._state.following.pop()
                self._adaptor.addChild(root_0, storeName320.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "store2"

    class user2_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.user2_return, self).__init__()

            self.tree = None




    # $ANTLR start "user2"
    # dgdl.g:155:1: user2 : ( user | SHARED );
    def user2(self, ):

        retval = self.user2_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SHARED322 = None
        user321 = None


        SHARED322_tree = None

        try:
            try:
                # dgdl.g:155:19: ( user | SHARED )
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if ((LISTENER <= LA51_0 <= SPEAKER) or LA51_0 == Identifier) :
                    alt51 = 1
                elif (LA51_0 == SHARED) :
                    alt51 = 2
                else:
                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # dgdl.g:155:21: user
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_user_in_user22504)
                    user321 = self.user()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, user321.tree)


                elif alt51 == 2:
                    # dgdl.g:155:28: SHARED
                    pass 
                    root_0 = self._adaptor.nil()

                    SHARED322=self.match(self.input, SHARED, self.FOLLOW_SHARED_in_user22508)

                    SHARED322_tree = self._adaptor.createWithPayload(SHARED322)
                    self._adaptor.addChild(root_0, SHARED322_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "user2"

    class dialogueSize_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.dialogueSize_return, self).__init__()

            self.tree = None




    # $ANTLR start "dialogueSize"
    # dgdl.g:157:1: dialogueSize : 'numturns' '(' systemID ',' ( number | runTimeVar ) ')' -> ^( 'numturns' systemID ( number )? ( runTimeVar )? ) ;
    def dialogueSize(self, ):

        retval = self.dialogueSize_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal323 = None
        char_literal324 = None
        char_literal326 = None
        char_literal329 = None
        systemID325 = None

        number327 = None

        runTimeVar328 = None


        string_literal323_tree = None
        char_literal324_tree = None
        char_literal326_tree = None
        char_literal329_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_NUMTURNS = RewriteRuleTokenStream(self._adaptor, "token NUMTURNS")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_number = RewriteRuleSubtreeStream(self._adaptor, "rule number")
        stream_systemID = RewriteRuleSubtreeStream(self._adaptor, "rule systemID")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        try:
            try:
                # dgdl.g:157:19: ( 'numturns' '(' systemID ',' ( number | runTimeVar ) ')' -> ^( 'numturns' systemID ( number )? ( runTimeVar )? ) )
                # dgdl.g:157:21: 'numturns' '(' systemID ',' ( number | runTimeVar ) ')'
                pass 
                string_literal323=self.match(self.input, NUMTURNS, self.FOLLOW_NUMTURNS_in_dialogueSize2521) 
                stream_NUMTURNS.add(string_literal323)
                char_literal324=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_dialogueSize2523) 
                stream_LPAREN.add(char_literal324)
                self._state.following.append(self.FOLLOW_systemID_in_dialogueSize2525)
                systemID325 = self.systemID()

                self._state.following.pop()
                stream_systemID.add(systemID325.tree)
                char_literal326=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dialogueSize2527) 
                stream_COMMA.add(char_literal326)
                # dgdl.g:157:49: ( number | runTimeVar )
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == Number) :
                    alt52 = 1
                elif (LA52_0 == DOLLAR) :
                    alt52 = 2
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # dgdl.g:157:50: number
                    pass 
                    self._state.following.append(self.FOLLOW_number_in_dialogueSize2530)
                    number327 = self.number()

                    self._state.following.pop()
                    stream_number.add(number327.tree)


                elif alt52 == 2:
                    # dgdl.g:157:59: runTimeVar
                    pass 
                    self._state.following.append(self.FOLLOW_runTimeVar_in_dialogueSize2534)
                    runTimeVar328 = self.runTimeVar()

                    self._state.following.pop()
                    stream_runTimeVar.add(runTimeVar328.tree)



                char_literal329=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_dialogueSize2537) 
                stream_RPAREN.add(char_literal329)

                # AST Rewrite
                # elements: number, NUMTURNS, systemID, runTimeVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 158:19: -> ^( 'numturns' systemID ( number )? ( runTimeVar )? )
                # dgdl.g:158:22: ^( 'numturns' systemID ( number )? ( runTimeVar )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_NUMTURNS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_systemID.nextTree())
                # dgdl.g:158:44: ( number )?
                if stream_number.hasNext():
                    self._adaptor.addChild(root_1, stream_number.nextTree())


                stream_number.reset();
                # dgdl.g:158:52: ( runTimeVar )?
                if stream_runTimeVar.hasNext():
                    self._adaptor.addChild(root_1, stream_runTimeVar.nextTree())


                stream_runTimeVar.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "dialogueSize"

    class correspondence_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.correspondence_return, self).__init__()

            self.tree = None




    # $ANTLR start "correspondence"
    # dgdl.g:160:1: correspondence : 'corresponds' '(' argument ',' schemeID ')' -> ^( 'corresponds' argument schemeID ) ;
    def correspondence(self, ):

        retval = self.correspondence_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal330 = None
        char_literal331 = None
        char_literal333 = None
        char_literal335 = None
        argument332 = None

        schemeID334 = None


        string_literal330_tree = None
        char_literal331_tree = None
        char_literal333_tree = None
        char_literal335_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_CORRESPONDS = RewriteRuleTokenStream(self._adaptor, "token CORRESPONDS")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_argument = RewriteRuleSubtreeStream(self._adaptor, "rule argument")
        stream_schemeID = RewriteRuleSubtreeStream(self._adaptor, "rule schemeID")
        try:
            try:
                # dgdl.g:160:19: ( 'corresponds' '(' argument ',' schemeID ')' -> ^( 'corresponds' argument schemeID ) )
                # dgdl.g:160:21: 'corresponds' '(' argument ',' schemeID ')'
                pass 
                string_literal330=self.match(self.input, CORRESPONDS, self.FOLLOW_CORRESPONDS_in_correspondence2580) 
                stream_CORRESPONDS.add(string_literal330)
                char_literal331=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_correspondence2582) 
                stream_LPAREN.add(char_literal331)
                self._state.following.append(self.FOLLOW_argument_in_correspondence2584)
                argument332 = self.argument()

                self._state.following.pop()
                stream_argument.add(argument332.tree)
                char_literal333=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_correspondence2586) 
                stream_COMMA.add(char_literal333)
                self._state.following.append(self.FOLLOW_schemeID_in_correspondence2588)
                schemeID334 = self.schemeID()

                self._state.following.pop()
                stream_schemeID.add(schemeID334.tree)
                char_literal335=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_correspondence2590) 
                stream_RPAREN.add(char_literal335)

                # AST Rewrite
                # elements: schemeID, argument, CORRESPONDS
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 161:19: -> ^( 'corresponds' argument schemeID )
                # dgdl.g:161:22: ^( 'corresponds' argument schemeID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_CORRESPONDS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_argument.nextTree())
                self._adaptor.addChild(root_1, stream_schemeID.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "correspondence"

    class relation_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.relation_return, self).__init__()

            self.tree = None




    # $ANTLR start "relation"
    # dgdl.g:163:1: relation : 'relation' '(' ( content | argument ) ',' ( 'backing' | 'warrant' ) ',' ( content | argument ) ')' -> ^( 'relation' ( 'backing' )? ( 'warrant' )? ) ;
    def relation(self, ):

        retval = self.relation_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal336 = None
        char_literal337 = None
        char_literal340 = None
        string_literal341 = None
        string_literal342 = None
        char_literal343 = None
        char_literal346 = None
        content338 = None

        argument339 = None

        content344 = None

        argument345 = None


        string_literal336_tree = None
        char_literal337_tree = None
        char_literal340_tree = None
        string_literal341_tree = None
        string_literal342_tree = None
        char_literal343_tree = None
        char_literal346_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_BACKING = RewriteRuleTokenStream(self._adaptor, "token BACKING")
        stream_RELATION = RewriteRuleTokenStream(self._adaptor, "token RELATION")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_WARRANT = RewriteRuleTokenStream(self._adaptor, "token WARRANT")
        stream_argument = RewriteRuleSubtreeStream(self._adaptor, "rule argument")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:163:19: ( 'relation' '(' ( content | argument ) ',' ( 'backing' | 'warrant' ) ',' ( content | argument ) ')' -> ^( 'relation' ( 'backing' )? ( 'warrant' )? ) )
                # dgdl.g:163:21: 'relation' '(' ( content | argument ) ',' ( 'backing' | 'warrant' ) ',' ( content | argument ) ')'
                pass 
                string_literal336=self.match(self.input, RELATION, self.FOLLOW_RELATION_in_relation2635) 
                stream_RELATION.add(string_literal336)
                char_literal337=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_relation2637) 
                stream_LPAREN.add(char_literal337)
                # dgdl.g:163:36: ( content | argument )
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == LBRACE) :
                    alt53 = 1
                elif (LA53_0 == LESSTHAN) :
                    alt53 = 2
                else:
                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # dgdl.g:163:37: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_relation2640)
                    content338 = self.content()

                    self._state.following.pop()
                    stream_content.add(content338.tree)


                elif alt53 == 2:
                    # dgdl.g:163:47: argument
                    pass 
                    self._state.following.append(self.FOLLOW_argument_in_relation2644)
                    argument339 = self.argument()

                    self._state.following.pop()
                    stream_argument.add(argument339.tree)



                char_literal340=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_relation2647) 
                stream_COMMA.add(char_literal340)
                # dgdl.g:163:61: ( 'backing' | 'warrant' )
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == BACKING) :
                    alt54 = 1
                elif (LA54_0 == WARRANT) :
                    alt54 = 2
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # dgdl.g:163:62: 'backing'
                    pass 
                    string_literal341=self.match(self.input, BACKING, self.FOLLOW_BACKING_in_relation2650) 
                    stream_BACKING.add(string_literal341)


                elif alt54 == 2:
                    # dgdl.g:163:74: 'warrant'
                    pass 
                    string_literal342=self.match(self.input, WARRANT, self.FOLLOW_WARRANT_in_relation2654) 
                    stream_WARRANT.add(string_literal342)



                char_literal343=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_relation2657) 
                stream_COMMA.add(char_literal343)
                # dgdl.g:163:89: ( content | argument )
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == LBRACE) :
                    alt55 = 1
                elif (LA55_0 == LESSTHAN) :
                    alt55 = 2
                else:
                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # dgdl.g:163:90: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_relation2660)
                    content344 = self.content()

                    self._state.following.pop()
                    stream_content.add(content344.tree)


                elif alt55 == 2:
                    # dgdl.g:163:100: argument
                    pass 
                    self._state.following.append(self.FOLLOW_argument_in_relation2664)
                    argument345 = self.argument()

                    self._state.following.pop()
                    stream_argument.add(argument345.tree)



                char_literal346=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_relation2667) 
                stream_RPAREN.add(char_literal346)

                # AST Rewrite
                # elements: BACKING, RELATION, WARRANT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 164:19: -> ^( 'relation' ( 'backing' )? ( 'warrant' )? )
                # dgdl.g:164:22: ^( 'relation' ( 'backing' )? ( 'warrant' )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_RELATION.nextNode(), root_1)

                # dgdl.g:164:35: ( 'backing' )?
                if stream_BACKING.hasNext():
                    self._adaptor.addChild(root_1, stream_BACKING.nextNode())


                stream_BACKING.reset();
                # dgdl.g:164:46: ( 'warrant' )?
                if stream_WARRANT.hasNext():
                    self._adaptor.addChild(root_1, stream_WARRANT.nextNode())


                stream_WARRANT.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "relation"

    class currentPlayer_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.currentPlayer_return, self).__init__()

            self.tree = None




    # $ANTLR start "currentPlayer"
    # dgdl.g:166:1: currentPlayer : 'player' '(' user ')' -> ^( 'player' user ) ;
    def currentPlayer(self, ):

        retval = self.currentPlayer_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal347 = None
        char_literal348 = None
        char_literal350 = None
        user349 = None


        string_literal347_tree = None
        char_literal348_tree = None
        char_literal350_tree = None
        stream_PLAYER = RewriteRuleTokenStream(self._adaptor, "token PLAYER")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        try:
            try:
                # dgdl.g:166:19: ( 'player' '(' user ')' -> ^( 'player' user ) )
                # dgdl.g:166:21: 'player' '(' user ')'
                pass 
                string_literal347=self.match(self.input, PLAYER, self.FOLLOW_PLAYER_in_currentPlayer2709) 
                stream_PLAYER.add(string_literal347)
                char_literal348=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_currentPlayer2711) 
                stream_LPAREN.add(char_literal348)
                self._state.following.append(self.FOLLOW_user_in_currentPlayer2713)
                user349 = self.user()

                self._state.following.pop()
                stream_user.add(user349.tree)
                char_literal350=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_currentPlayer2715) 
                stream_RPAREN.add(char_literal350)

                # AST Rewrite
                # elements: user, PLAYER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 167:19: -> ^( 'player' user )
                # dgdl.g:167:22: ^( 'player' user )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PLAYER.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_user.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "currentPlayer"

    class externalCondition_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.externalCondition_return, self).__init__()

            self.tree = None




    # $ANTLR start "externalCondition"
    # dgdl.g:172:1: externalCondition : 'extCondition' '(' identifier ( ',' content )+ ')' -> ^( 'extCondition' identifier ( content )+ ) ;
    def externalCondition(self, ):

        retval = self.externalCondition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal351 = None
        char_literal352 = None
        char_literal354 = None
        char_literal356 = None
        identifier353 = None

        content355 = None


        string_literal351_tree = None
        char_literal352_tree = None
        char_literal354_tree = None
        char_literal356_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_EXTCONDITION = RewriteRuleTokenStream(self._adaptor, "token EXTCONDITION")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:172:19: ( 'extCondition' '(' identifier ( ',' content )+ ')' -> ^( 'extCondition' identifier ( content )+ ) )
                # dgdl.g:172:21: 'extCondition' '(' identifier ( ',' content )+ ')'
                pass 
                string_literal351=self.match(self.input, EXTCONDITION, self.FOLLOW_EXTCONDITION_in_externalCondition2770) 
                stream_EXTCONDITION.add(string_literal351)
                char_literal352=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_externalCondition2772) 
                stream_LPAREN.add(char_literal352)
                self._state.following.append(self.FOLLOW_identifier_in_externalCondition2774)
                identifier353 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier353.tree)
                # dgdl.g:172:51: ( ',' content )+
                cnt56 = 0
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == COMMA) :
                        alt56 = 1


                    if alt56 == 1:
                        # dgdl.g:172:52: ',' content
                        pass 
                        char_literal354=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_externalCondition2777) 
                        stream_COMMA.add(char_literal354)
                        self._state.following.append(self.FOLLOW_content_in_externalCondition2779)
                        content355 = self.content()

                        self._state.following.pop()
                        stream_content.add(content355.tree)


                    else:
                        if cnt56 >= 1:
                            break #loop56

                        eee = EarlyExitException(56, self.input)
                        raise eee

                    cnt56 += 1
                char_literal356=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_externalCondition2783) 
                stream_RPAREN.add(char_literal356)

                # AST Rewrite
                # elements: identifier, content, EXTCONDITION
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 173:18: -> ^( 'extCondition' identifier ( content )+ )
                # dgdl.g:173:21: ^( 'extCondition' identifier ( content )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EXTCONDITION.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                # dgdl.g:173:49: ( content )+
                if not (stream_content.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "externalCondition"

    class value_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.value_return, self).__init__()

            self.tree = None




    # $ANTLR start "value"
    # dgdl.g:176:1: value : 'value' '(' value1 ( ',' ( '!' )? value2 )? ')' -> ^( 'value' value1 ( value2 )? ) ;
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal357 = None
        char_literal358 = None
        char_literal360 = None
        char_literal361 = None
        char_literal363 = None
        value1359 = None

        value2362 = None


        string_literal357_tree = None
        char_literal358_tree = None
        char_literal360_tree = None
        char_literal361_tree = None
        char_literal363_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_124 = RewriteRuleTokenStream(self._adaptor, "token 124")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_value2 = RewriteRuleSubtreeStream(self._adaptor, "rule value2")
        stream_value1 = RewriteRuleSubtreeStream(self._adaptor, "rule value1")
        try:
            try:
                # dgdl.g:176:19: ( 'value' '(' value1 ( ',' ( '!' )? value2 )? ')' -> ^( 'value' value1 ( value2 )? ) )
                # dgdl.g:176:21: 'value' '(' value1 ( ',' ( '!' )? value2 )? ')'
                pass 
                string_literal357=self.match(self.input, 124, self.FOLLOW_124_in_value2834) 
                stream_124.add(string_literal357)
                char_literal358=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_value2836) 
                stream_LPAREN.add(char_literal358)
                self._state.following.append(self.FOLLOW_value1_in_value2838)
                value1359 = self.value1()

                self._state.following.pop()
                stream_value1.add(value1359.tree)
                # dgdl.g:176:40: ( ',' ( '!' )? value2 )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == COMMA) :
                    alt58 = 1
                if alt58 == 1:
                    # dgdl.g:176:41: ',' ( '!' )? value2
                    pass 
                    char_literal360=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_value2841) 
                    stream_COMMA.add(char_literal360)
                    # dgdl.g:176:45: ( '!' )?
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == NOT) :
                        alt57 = 1
                    if alt57 == 1:
                        # dgdl.g:176:45: '!'
                        pass 
                        char_literal361=self.match(self.input, NOT, self.FOLLOW_NOT_in_value2843) 
                        stream_NOT.add(char_literal361)



                    self._state.following.append(self.FOLLOW_value2_in_value2846)
                    value2362 = self.value2()

                    self._state.following.pop()
                    stream_value2.add(value2362.tree)



                char_literal363=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_value2849) 
                stream_RPAREN.add(char_literal363)

                # AST Rewrite
                # elements: value1, 124, value2
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 177:17: -> ^( 'value' value1 ( value2 )? )
                # dgdl.g:177:20: ^( 'value' value1 ( value2 )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_124.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_value1.nextTree())
                # dgdl.g:177:37: ( value2 )?
                if stream_value2.hasNext():
                    self._adaptor.addChild(root_1, stream_value2.nextTree())


                stream_value2.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value"

    class value1_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.value1_return, self).__init__()

            self.tree = None




    # $ANTLR start "value1"
    # dgdl.g:179:1: value1 : ( content | STRINGLITERAL ) ;
    def value1(self, ):

        retval = self.value1_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRINGLITERAL365 = None
        content364 = None


        STRINGLITERAL365_tree = None

        try:
            try:
                # dgdl.g:179:19: ( ( content | STRINGLITERAL ) )
                # dgdl.g:179:21: ( content | STRINGLITERAL )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:179:21: ( content | STRINGLITERAL )
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == LBRACE) :
                    alt59 = 1
                elif (LA59_0 == STRINGLITERAL) :
                    alt59 = 2
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # dgdl.g:179:22: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_value12897)
                    content364 = self.content()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, content364.tree)


                elif alt59 == 2:
                    # dgdl.g:179:32: STRINGLITERAL
                    pass 
                    STRINGLITERAL365=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_value12901)

                    STRINGLITERAL365_tree = self._adaptor.createWithPayload(STRINGLITERAL365)
                    self._adaptor.addChild(root_0, STRINGLITERAL365_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value1"

    class value2_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.value2_return, self).__init__()

            self.tree = None




    # $ANTLR start "value2"
    # dgdl.g:180:1: value2 : ( valueVar | STRINGLITERAL ) ;
    def value2(self, ):

        retval = self.value2_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRINGLITERAL367 = None
        valueVar366 = None


        STRINGLITERAL367_tree = None

        try:
            try:
                # dgdl.g:180:19: ( ( valueVar | STRINGLITERAL ) )
                # dgdl.g:180:21: ( valueVar | STRINGLITERAL )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:180:21: ( valueVar | STRINGLITERAL )
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == DOLLAR) :
                    alt60 = 1
                elif (LA60_0 == STRINGLITERAL) :
                    alt60 = 2
                else:
                    nvae = NoViableAltException("", 60, 0, self.input)

                    raise nvae

                if alt60 == 1:
                    # dgdl.g:180:22: valueVar
                    pass 
                    self._state.following.append(self.FOLLOW_valueVar_in_value22921)
                    valueVar366 = self.valueVar()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, valueVar366.tree)


                elif alt60 == 2:
                    # dgdl.g:180:33: STRINGLITERAL
                    pass 
                    STRINGLITERAL367=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_value22925)

                    STRINGLITERAL367_tree = self._adaptor.createWithPayload(STRINGLITERAL367)
                    self._adaptor.addChild(root_0, STRINGLITERAL367_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value2"

    class valueVar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.valueVar_return, self).__init__()

            self.tree = None




    # $ANTLR start "valueVar"
    # dgdl.g:182:1: valueVar : runTimeVar -> ^( VAR runTimeVar ) ;
    def valueVar(self, ):

        retval = self.valueVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        runTimeVar368 = None


        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        try:
            try:
                # dgdl.g:182:19: ( runTimeVar -> ^( VAR runTimeVar ) )
                # dgdl.g:182:21: runTimeVar
                pass 
                self._state.following.append(self.FOLLOW_runTimeVar_in_valueVar2944)
                runTimeVar368 = self.runTimeVar()

                self._state.following.pop()
                stream_runTimeVar.add(runTimeVar368.tree)

                # AST Rewrite
                # elements: runTimeVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 183:17: -> ^( VAR runTimeVar )
                # dgdl.g:183:20: ^( VAR runTimeVar )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                self._adaptor.addChild(root_1, stream_runTimeVar.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "valueVar"

    class user_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.user_return, self).__init__()

            self.tree = None




    # $ANTLR start "user"
    # dgdl.g:192:1: user : role ;
    def user(self, ):

        retval = self.user_return()
        retval.start = self.input.LT(1)

        root_0 = None

        role369 = None



        try:
            try:
                # dgdl.g:192:19: ( role )
                # dgdl.g:192:21: role
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_role_in_user3037)
                role369 = self.role()

                self._state.following.pop()
                self._adaptor.addChild(root_0, role369.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "user"

    class schemeID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.schemeID_return, self).__init__()

            self.tree = None




    # $ANTLR start "schemeID"
    # dgdl.g:194:1: schemeID : identifier ;
    def schemeID(self, ):

        retval = self.schemeID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier370 = None



        try:
            try:
                # dgdl.g:194:19: ( identifier )
                # dgdl.g:194:21: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_schemeID3055)
                identifier370 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier370.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "schemeID"

    class commitment_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.commitment_return, self).__init__()

            self.tree = None




    # $ANTLR start "commitment"
    # dgdl.g:195:1: commitment : ( content | locution | argument ) ;
    def commitment(self, ):

        retval = self.commitment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        content371 = None

        locution372 = None

        argument373 = None



        try:
            try:
                # dgdl.g:195:19: ( ( content | locution | argument ) )
                # dgdl.g:195:21: ( content | locution | argument )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:195:21: ( content | locution | argument )
                alt61 = 3
                LA61_0 = self.input.LA(1)

                if (LA61_0 == LBRACE) :
                    alt61 = 1
                elif (LA61_0 == LESSTHAN) :
                    LA61_2 = self.input.LA(2)

                    if (LA61_2 == Identifier) :
                        alt61 = 2
                    elif (LA61_2 == LowerChar or LA61_2 == NOT) :
                        alt61 = 3
                    else:
                        nvae = NoViableAltException("", 61, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae

                if alt61 == 1:
                    # dgdl.g:195:22: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_commitment3070)
                    content371 = self.content()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, content371.tree)


                elif alt61 == 2:
                    # dgdl.g:195:32: locution
                    pass 
                    self._state.following.append(self.FOLLOW_locution_in_commitment3074)
                    locution372 = self.locution()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, locution372.tree)


                elif alt61 == 3:
                    # dgdl.g:195:43: argument
                    pass 
                    self._state.following.append(self.FOLLOW_argument_in_commitment3078)
                    argument373 = self.argument()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, argument373.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "commitment"

    class locution_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.locution_return, self).__init__()

            self.tree = None




    # $ANTLR start "locution"
    # dgdl.g:197:1: locution : '<' moveID ',' content '>' ;
    def locution(self, ):

        retval = self.locution_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal374 = None
        char_literal376 = None
        char_literal378 = None
        moveID375 = None

        content377 = None


        char_literal374_tree = None
        char_literal376_tree = None
        char_literal378_tree = None

        try:
            try:
                # dgdl.g:197:19: ( '<' moveID ',' content '>' )
                # dgdl.g:197:21: '<' moveID ',' content '>'
                pass 
                root_0 = self._adaptor.nil()

                char_literal374=self.match(self.input, LESSTHAN, self.FOLLOW_LESSTHAN_in_locution3096)

                char_literal374_tree = self._adaptor.createWithPayload(char_literal374)
                self._adaptor.addChild(root_0, char_literal374_tree)

                self._state.following.append(self.FOLLOW_moveID_in_locution3098)
                moveID375 = self.moveID()

                self._state.following.pop()
                self._adaptor.addChild(root_0, moveID375.tree)
                char_literal376=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_locution3100)

                char_literal376_tree = self._adaptor.createWithPayload(char_literal376)
                self._adaptor.addChild(root_0, char_literal376_tree)

                self._state.following.append(self.FOLLOW_content_in_locution3102)
                content377 = self.content()

                self._state.following.pop()
                self._adaptor.addChild(root_0, content377.tree)
                char_literal378=self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_locution3104)

                char_literal378_tree = self._adaptor.createWithPayload(char_literal378)
                self._adaptor.addChild(root_0, char_literal378_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "locution"

    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.argument_return, self).__init__()

            self.tree = None




    # $ANTLR start "argument"
    # dgdl.g:199:1: argument : '<' conclusion ',' premises '>' ;
    def argument(self, ):

        retval = self.argument_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal379 = None
        char_literal381 = None
        char_literal383 = None
        conclusion380 = None

        premises382 = None


        char_literal379_tree = None
        char_literal381_tree = None
        char_literal383_tree = None

        try:
            try:
                # dgdl.g:199:19: ( '<' conclusion ',' premises '>' )
                # dgdl.g:199:21: '<' conclusion ',' premises '>'
                pass 
                root_0 = self._adaptor.nil()

                char_literal379=self.match(self.input, LESSTHAN, self.FOLLOW_LESSTHAN_in_argument3121)

                char_literal379_tree = self._adaptor.createWithPayload(char_literal379)
                self._adaptor.addChild(root_0, char_literal379_tree)

                self._state.following.append(self.FOLLOW_conclusion_in_argument3123)
                conclusion380 = self.conclusion()

                self._state.following.pop()
                self._adaptor.addChild(root_0, conclusion380.tree)
                char_literal381=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argument3125)

                char_literal381_tree = self._adaptor.createWithPayload(char_literal381)
                self._adaptor.addChild(root_0, char_literal381_tree)

                self._state.following.append(self.FOLLOW_premises_in_argument3127)
                premises382 = self.premises()

                self._state.following.pop()
                self._adaptor.addChild(root_0, premises382.tree)
                char_literal383=self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_argument3129)

                char_literal383_tree = self._adaptor.createWithPayload(char_literal383)
                self._adaptor.addChild(root_0, char_literal383_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "argument"

    class premises_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.premises_return, self).__init__()

            self.tree = None




    # $ANTLR start "premises"
    # dgdl.g:200:1: premises : '{' contentVar ( ',' contentVar )* '}' ;
    def premises(self, ):

        retval = self.premises_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal384 = None
        char_literal386 = None
        char_literal388 = None
        contentVar385 = None

        contentVar387 = None


        char_literal384_tree = None
        char_literal386_tree = None
        char_literal388_tree = None

        try:
            try:
                # dgdl.g:200:19: ( '{' contentVar ( ',' contentVar )* '}' )
                # dgdl.g:200:21: '{' contentVar ( ',' contentVar )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal384=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_premises3145)

                char_literal384_tree = self._adaptor.createWithPayload(char_literal384)
                self._adaptor.addChild(root_0, char_literal384_tree)

                self._state.following.append(self.FOLLOW_contentVar_in_premises3147)
                contentVar385 = self.contentVar()

                self._state.following.pop()
                self._adaptor.addChild(root_0, contentVar385.tree)
                # dgdl.g:200:36: ( ',' contentVar )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == COMMA) :
                        alt62 = 1


                    if alt62 == 1:
                        # dgdl.g:200:37: ',' contentVar
                        pass 
                        char_literal386=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_premises3150)

                        char_literal386_tree = self._adaptor.createWithPayload(char_literal386)
                        self._adaptor.addChild(root_0, char_literal386_tree)

                        self._state.following.append(self.FOLLOW_contentVar_in_premises3152)
                        contentVar387 = self.contentVar()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, contentVar387.tree)


                    else:
                        break #loop62
                char_literal388=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_premises3156)

                char_literal388_tree = self._adaptor.createWithPayload(char_literal388)
                self._adaptor.addChild(root_0, char_literal388_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "premises"

    class conclusion_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.conclusion_return, self).__init__()

            self.tree = None




    # $ANTLR start "conclusion"
    # dgdl.g:201:1: conclusion : contentVar ;
    def conclusion(self, ):

        retval = self.conclusion_return()
        retval.start = self.input.LT(1)

        root_0 = None

        contentVar389 = None



        try:
            try:
                # dgdl.g:201:19: ( contentVar )
                # dgdl.g:201:21: contentVar
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_contentVar_in_conclusion3170)
                contentVar389 = self.contentVar()

                self._state.following.pop()
                self._adaptor.addChild(root_0, contentVar389.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "conclusion"

    class move_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.move_return, self).__init__()

            self.tree = None




    # $ANTLR start "move"
    # dgdl.g:205:1: move : 'move' '(' moveaction ',' movetime ',' moveID ( ',' addressee )? ( ',' content )? ( ',' user )? ( ',' requirements )? ( ',' opener )? ')' -> ^( 'move' moveaction movetime moveID ( addressee )? ( content )? ( user )? ( requirements )? ( opener )? ) ;
    def move(self, ):

        retval = self.move_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal390 = None
        char_literal391 = None
        char_literal393 = None
        char_literal395 = None
        char_literal397 = None
        char_literal399 = None
        char_literal401 = None
        char_literal403 = None
        char_literal405 = None
        char_literal407 = None
        moveaction392 = None

        movetime394 = None

        moveID396 = None

        addressee398 = None

        content400 = None

        user402 = None

        requirements404 = None

        opener406 = None


        string_literal390_tree = None
        char_literal391_tree = None
        char_literal393_tree = None
        char_literal395_tree = None
        char_literal397_tree = None
        char_literal399_tree = None
        char_literal401_tree = None
        char_literal403_tree = None
        char_literal405_tree = None
        char_literal407_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_MOVE = RewriteRuleTokenStream(self._adaptor, "token MOVE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_requirements = RewriteRuleSubtreeStream(self._adaptor, "rule requirements")
        stream_addressee = RewriteRuleSubtreeStream(self._adaptor, "rule addressee")
        stream_opener = RewriteRuleSubtreeStream(self._adaptor, "rule opener")
        stream_moveaction = RewriteRuleSubtreeStream(self._adaptor, "rule moveaction")
        stream_movetime = RewriteRuleSubtreeStream(self._adaptor, "rule movetime")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        stream_moveID = RewriteRuleSubtreeStream(self._adaptor, "rule moveID")
        try:
            try:
                # dgdl.g:205:15: ( 'move' '(' moveaction ',' movetime ',' moveID ( ',' addressee )? ( ',' content )? ( ',' user )? ( ',' requirements )? ( ',' opener )? ')' -> ^( 'move' moveaction movetime moveID ( addressee )? ( content )? ( user )? ( requirements )? ( opener )? ) )
                # dgdl.g:205:17: 'move' '(' moveaction ',' movetime ',' moveID ( ',' addressee )? ( ',' content )? ( ',' user )? ( ',' requirements )? ( ',' opener )? ')'
                pass 
                string_literal390=self.match(self.input, MOVE, self.FOLLOW_MOVE_in_move3190) 
                stream_MOVE.add(string_literal390)
                char_literal391=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_move3192) 
                stream_LPAREN.add(char_literal391)
                self._state.following.append(self.FOLLOW_moveaction_in_move3194)
                moveaction392 = self.moveaction()

                self._state.following.pop()
                stream_moveaction.add(moveaction392.tree)
                char_literal393=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3196) 
                stream_COMMA.add(char_literal393)
                self._state.following.append(self.FOLLOW_movetime_in_move3198)
                movetime394 = self.movetime()

                self._state.following.pop()
                stream_movetime.add(movetime394.tree)
                char_literal395=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3200) 
                stream_COMMA.add(char_literal395)
                self._state.following.append(self.FOLLOW_moveID_in_move3202)
                moveID396 = self.moveID()

                self._state.following.pop()
                stream_moveID.add(moveID396.tree)
                # dgdl.g:205:63: ( ',' addressee )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == COMMA) :
                    LA63_1 = self.input.LA(2)

                    if (LA63_1 == DOLLAR) :
                        alt63 = 1
                if alt63 == 1:
                    # dgdl.g:205:64: ',' addressee
                    pass 
                    char_literal397=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3205) 
                    stream_COMMA.add(char_literal397)
                    self._state.following.append(self.FOLLOW_addressee_in_move3207)
                    addressee398 = self.addressee()

                    self._state.following.pop()
                    stream_addressee.add(addressee398.tree)



                # dgdl.g:205:80: ( ',' content )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == COMMA) :
                    LA64_1 = self.input.LA(2)

                    if (LA64_1 == LBRACE) :
                        LA64_3 = self.input.LA(3)

                        if (LA64_3 == STRINGLITERAL or (UpperChar <= LA64_3 <= LowerChar) or LA64_3 == DOLLAR or LA64_3 == NOT or (122 <= LA64_3 <= 123)) :
                            alt64 = 1
                if alt64 == 1:
                    # dgdl.g:205:81: ',' content
                    pass 
                    char_literal399=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3212) 
                    stream_COMMA.add(char_literal399)
                    self._state.following.append(self.FOLLOW_content_in_move3214)
                    content400 = self.content()

                    self._state.following.pop()
                    stream_content.add(content400.tree)



                # dgdl.g:205:95: ( ',' user )?
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == COMMA) :
                    LA65_1 = self.input.LA(2)

                    if ((LISTENER <= LA65_1 <= SPEAKER) or LA65_1 == Identifier) :
                        alt65 = 1
                if alt65 == 1:
                    # dgdl.g:205:96: ',' user
                    pass 
                    char_literal401=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3219) 
                    stream_COMMA.add(char_literal401)
                    self._state.following.append(self.FOLLOW_user_in_move3221)
                    user402 = self.user()

                    self._state.following.pop()
                    stream_user.add(user402.tree)



                # dgdl.g:205:107: ( ',' requirements )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == COMMA) :
                    LA66_1 = self.input.LA(2)

                    if (LA66_1 == LBRACE) :
                        alt66 = 1
                if alt66 == 1:
                    # dgdl.g:205:108: ',' requirements
                    pass 
                    char_literal403=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3226) 
                    stream_COMMA.add(char_literal403)
                    self._state.following.append(self.FOLLOW_requirements_in_move3228)
                    requirements404 = self.requirements()

                    self._state.following.pop()
                    stream_requirements.add(requirements404.tree)



                # dgdl.g:205:127: ( ',' opener )?
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == COMMA) :
                    alt67 = 1
                if alt67 == 1:
                    # dgdl.g:205:128: ',' opener
                    pass 
                    char_literal405=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_move3233) 
                    stream_COMMA.add(char_literal405)
                    self._state.following.append(self.FOLLOW_opener_in_move3235)
                    opener406 = self.opener()

                    self._state.following.pop()
                    stream_opener.add(opener406.tree)



                char_literal407=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_move3239) 
                stream_RPAREN.add(char_literal407)

                # AST Rewrite
                # elements: movetime, moveID, requirements, MOVE, opener, addressee, moveaction, content, user
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 206:15: -> ^( 'move' moveaction movetime moveID ( addressee )? ( content )? ( user )? ( requirements )? ( opener )? )
                # dgdl.g:206:18: ^( 'move' moveaction movetime moveID ( addressee )? ( content )? ( user )? ( requirements )? ( opener )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MOVE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_moveaction.nextTree())
                self._adaptor.addChild(root_1, stream_movetime.nextTree())
                self._adaptor.addChild(root_1, stream_moveID.nextTree())
                # dgdl.g:206:54: ( addressee )?
                if stream_addressee.hasNext():
                    self._adaptor.addChild(root_1, stream_addressee.nextTree())


                stream_addressee.reset();
                # dgdl.g:206:65: ( content )?
                if stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset();
                # dgdl.g:206:74: ( user )?
                if stream_user.hasNext():
                    self._adaptor.addChild(root_1, stream_user.nextTree())


                stream_user.reset();
                # dgdl.g:206:80: ( requirements )?
                if stream_requirements.hasNext():
                    self._adaptor.addChild(root_1, stream_requirements.nextTree())


                stream_requirements.reset();
                # dgdl.g:206:94: ( opener )?
                if stream_opener.hasNext():
                    self._adaptor.addChild(root_1, stream_opener.nextTree())


                stream_opener.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "move"

    class moveaction_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.moveaction_return, self).__init__()

            self.tree = None




    # $ANTLR start "moveaction"
    # dgdl.g:207:1: moveaction : ( 'add' | 'delete' ) ;
    def moveaction(self, ):

        retval = self.moveaction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set408 = None

        set408_tree = None

        try:
            try:
                # dgdl.g:207:15: ( ( 'add' | 'delete' ) )
                # dgdl.g:207:17: ( 'add' | 'delete' )
                pass 
                root_0 = self._adaptor.nil()

                set408 = self.input.LT(1)
                if self.input.LA(1) == ADD or self.input.LA(1) == DELETE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set408))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "moveaction"

    class movetime_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.movetime_return, self).__init__()

            self.tree = None




    # $ANTLR start "movetime"
    # dgdl.g:208:1: movetime : ( 'next' | 'future' ) ;
    def movetime(self, ):

        retval = self.movetime_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set409 = None

        set409_tree = None

        try:
            try:
                # dgdl.g:208:15: ( ( 'next' | 'future' ) )
                # dgdl.g:208:17: ( 'next' | 'future' )
                pass 
                root_0 = self._adaptor.nil()

                set409 = self.input.LT(1)
                if self.input.LA(1) == FUTURE or self.input.LA(1) == NEXT:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set409))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "movetime"

    class storeOp_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeOp_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeOp"
    # dgdl.g:210:1: storeOp : 'store' '(' storeaction ',' content ',' storeName ',' user ')' -> ^( 'store' storeaction content storeName user ) ;
    def storeOp(self, ):

        retval = self.storeOp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal410 = None
        char_literal411 = None
        char_literal413 = None
        char_literal415 = None
        char_literal417 = None
        char_literal419 = None
        storeaction412 = None

        content414 = None

        storeName416 = None

        user418 = None


        string_literal410_tree = None
        char_literal411_tree = None
        char_literal413_tree = None
        char_literal415_tree = None
        char_literal417_tree = None
        char_literal419_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_STORE = RewriteRuleTokenStream(self._adaptor, "token STORE")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_storeName = RewriteRuleSubtreeStream(self._adaptor, "rule storeName")
        stream_storeaction = RewriteRuleSubtreeStream(self._adaptor, "rule storeaction")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:210:15: ( 'store' '(' storeaction ',' content ',' storeName ',' user ')' -> ^( 'store' storeaction content storeName user ) )
                # dgdl.g:210:17: 'store' '(' storeaction ',' content ',' storeName ',' user ')'
                pass 
                string_literal410=self.match(self.input, STORE, self.FOLLOW_STORE_in_storeOp3328) 
                stream_STORE.add(string_literal410)
                char_literal411=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_storeOp3330) 
                stream_LPAREN.add(char_literal411)
                self._state.following.append(self.FOLLOW_storeaction_in_storeOp3332)
                storeaction412 = self.storeaction()

                self._state.following.pop()
                stream_storeaction.add(storeaction412.tree)
                char_literal413=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeOp3334) 
                stream_COMMA.add(char_literal413)
                self._state.following.append(self.FOLLOW_content_in_storeOp3336)
                content414 = self.content()

                self._state.following.pop()
                stream_content.add(content414.tree)
                char_literal415=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeOp3338) 
                stream_COMMA.add(char_literal415)
                self._state.following.append(self.FOLLOW_storeName_in_storeOp3340)
                storeName416 = self.storeName()

                self._state.following.pop()
                stream_storeName.add(storeName416.tree)
                char_literal417=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_storeOp3342) 
                stream_COMMA.add(char_literal417)
                self._state.following.append(self.FOLLOW_user_in_storeOp3344)
                user418 = self.user()

                self._state.following.pop()
                stream_user.add(user418.tree)
                char_literal419=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_storeOp3346) 
                stream_RPAREN.add(char_literal419)

                # AST Rewrite
                # elements: content, storeaction, storeName, user, STORE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 211:15: -> ^( 'store' storeaction content storeName user )
                # dgdl.g:211:18: ^( 'store' storeaction content storeName user )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_STORE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_storeaction.nextTree())
                self._adaptor.addChild(root_1, stream_content.nextTree())
                self._adaptor.addChild(root_1, stream_storeName.nextTree())
                self._adaptor.addChild(root_1, stream_user.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeOp"

    class storeaction_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.storeaction_return, self).__init__()

            self.tree = None




    # $ANTLR start "storeaction"
    # dgdl.g:212:1: storeaction : ( 'add' | 'remove' | 'empty' ) ;
    def storeaction(self, ):

        retval = self.storeaction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set420 = None

        set420_tree = None

        try:
            try:
                # dgdl.g:212:15: ( ( 'add' | 'remove' | 'empty' ) )
                # dgdl.g:212:17: ( 'add' | 'remove' | 'empty' )
                pass 
                root_0 = self._adaptor.nil()

                set420 = self.input.LT(1)
                if self.input.LA(1) == ADD or self.input.LA(1) == EMPTY or self.input.LA(1) == REMOVE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set420))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "storeaction"

    class statusUpdate_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.statusUpdate_return, self).__init__()

            self.tree = None




    # $ANTLR start "statusUpdate"
    # dgdl.g:214:1: statusUpdate : 'status' '(' status ',' sysgame ')' -> ^( 'status' status sysgame ) ;
    def statusUpdate(self, ):

        retval = self.statusUpdate_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal421 = None
        char_literal422 = None
        char_literal424 = None
        char_literal426 = None
        status423 = None

        sysgame425 = None


        string_literal421_tree = None
        char_literal422_tree = None
        char_literal424_tree = None
        char_literal426_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_STATUS = RewriteRuleTokenStream(self._adaptor, "token STATUS")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_sysgame = RewriteRuleSubtreeStream(self._adaptor, "rule sysgame")
        stream_status = RewriteRuleSubtreeStream(self._adaptor, "rule status")
        try:
            try:
                # dgdl.g:214:15: ( 'status' '(' status ',' sysgame ')' -> ^( 'status' status sysgame ) )
                # dgdl.g:214:17: 'status' '(' status ',' sysgame ')'
                pass 
                string_literal421=self.match(self.input, STATUS, self.FOLLOW_STATUS_in_statusUpdate3402) 
                stream_STATUS.add(string_literal421)
                char_literal422=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_statusUpdate3404) 
                stream_LPAREN.add(char_literal422)
                self._state.following.append(self.FOLLOW_status_in_statusUpdate3406)
                status423 = self.status()

                self._state.following.pop()
                stream_status.add(status423.tree)
                char_literal424=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_statusUpdate3408) 
                stream_COMMA.add(char_literal424)
                self._state.following.append(self.FOLLOW_sysgame_in_statusUpdate3410)
                sysgame425 = self.sysgame()

                self._state.following.pop()
                stream_sysgame.add(sysgame425.tree)
                char_literal426=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_statusUpdate3412) 
                stream_RPAREN.add(char_literal426)

                # AST Rewrite
                # elements: STATUS, status, sysgame
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 215:15: -> ^( 'status' status sysgame )
                # dgdl.g:215:18: ^( 'status' status sysgame )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_STATUS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_status.nextTree())
                self._adaptor.addChild(root_1, stream_sysgame.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "statusUpdate"

    class status_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.status_return, self).__init__()

            self.tree = None




    # $ANTLR start "status"
    # dgdl.g:216:1: status : ( 'active' | 'inactive' | 'complete' | 'incomplete' | 'initiate' | 'terminate' ) ;
    def status(self, ):

        retval = self.status_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set427 = None

        set427_tree = None

        try:
            try:
                # dgdl.g:216:15: ( ( 'active' | 'inactive' | 'complete' | 'incomplete' | 'initiate' | 'terminate' ) )
                # dgdl.g:216:17: ( 'active' | 'inactive' | 'complete' | 'incomplete' | 'initiate' | 'terminate' )
                pass 
                root_0 = self._adaptor.nil()

                set427 = self.input.LT(1)
                if self.input.LA(1) == ACTIVE or self.input.LA(1) == COMPLETE or (INACTIVE <= self.input.LA(1) <= INITIATE) or self.input.LA(1) == TERMINATE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set427))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "status"

    class roleAssignment_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.roleAssignment_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleAssignment"
    # dgdl.g:218:1: roleAssignment : ( assignment | unassignment ) ;
    def roleAssignment(self, ):

        retval = self.roleAssignment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        assignment428 = None

        unassignment429 = None



        try:
            try:
                # dgdl.g:218:15: ( ( assignment | unassignment ) )
                # dgdl.g:218:17: ( assignment | unassignment )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:218:17: ( assignment | unassignment )
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == ASSIGN) :
                    alt68 = 1
                elif (LA68_0 == 125) :
                    alt68 = 2
                else:
                    nvae = NoViableAltException("", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # dgdl.g:218:18: assignment
                    pass 
                    self._state.following.append(self.FOLLOW_assignment_in_roleAssignment3480)
                    assignment428 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment428.tree)


                elif alt68 == 2:
                    # dgdl.g:218:31: unassignment
                    pass 
                    self._state.following.append(self.FOLLOW_unassignment_in_roleAssignment3484)
                    unassignment429 = self.unassignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unassignment429.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleAssignment"

    class assignment_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.assignment_return, self).__init__()

            self.tree = None




    # $ANTLR start "assignment"
    # dgdl.g:220:1: assignment : 'assign' '(' user ',' role ')' -> ^( 'assign' user role ) ;
    def assignment(self, ):

        retval = self.assignment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal430 = None
        char_literal431 = None
        char_literal433 = None
        char_literal435 = None
        user432 = None

        role434 = None


        string_literal430_tree = None
        char_literal431_tree = None
        char_literal433_tree = None
        char_literal435_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_role = RewriteRuleSubtreeStream(self._adaptor, "rule role")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        try:
            try:
                # dgdl.g:220:11: ( 'assign' '(' user ',' role ')' -> ^( 'assign' user role ) )
                # dgdl.g:220:13: 'assign' '(' user ',' role ')'
                pass 
                string_literal430=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignment3492) 
                stream_ASSIGN.add(string_literal430)
                char_literal431=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_assignment3494) 
                stream_LPAREN.add(char_literal431)
                self._state.following.append(self.FOLLOW_user_in_assignment3496)
                user432 = self.user()

                self._state.following.pop()
                stream_user.add(user432.tree)
                char_literal433=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_assignment3498) 
                stream_COMMA.add(char_literal433)
                self._state.following.append(self.FOLLOW_role_in_assignment3500)
                role434 = self.role()

                self._state.following.pop()
                stream_role.add(role434.tree)
                char_literal435=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_assignment3502) 
                stream_RPAREN.add(char_literal435)

                # AST Rewrite
                # elements: ASSIGN, user, role
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 221:15: -> ^( 'assign' user role )
                # dgdl.g:221:18: ^( 'assign' user role )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ASSIGN.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_user.nextTree())
                self._adaptor.addChild(root_1, stream_role.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assignment"

    class unassignment_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.unassignment_return, self).__init__()

            self.tree = None




    # $ANTLR start "unassignment"
    # dgdl.g:223:1: unassignment : 'unassign' '(' user ',' role ')' -> ^( 'unassign' user role ) ;
    def unassignment(self, ):

        retval = self.unassignment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal436 = None
        char_literal437 = None
        char_literal439 = None
        char_literal441 = None
        user438 = None

        role440 = None


        string_literal436_tree = None
        char_literal437_tree = None
        char_literal439_tree = None
        char_literal441_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_125 = RewriteRuleTokenStream(self._adaptor, "token 125")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_role = RewriteRuleSubtreeStream(self._adaptor, "rule role")
        stream_user = RewriteRuleSubtreeStream(self._adaptor, "rule user")
        try:
            try:
                # dgdl.g:223:13: ( 'unassign' '(' user ',' role ')' -> ^( 'unassign' user role ) )
                # dgdl.g:223:15: 'unassign' '(' user ',' role ')'
                pass 
                string_literal436=self.match(self.input, 125, self.FOLLOW_125_in_unassignment3547) 
                stream_125.add(string_literal436)
                char_literal437=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_unassignment3549) 
                stream_LPAREN.add(char_literal437)
                self._state.following.append(self.FOLLOW_user_in_unassignment3551)
                user438 = self.user()

                self._state.following.pop()
                stream_user.add(user438.tree)
                char_literal439=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_unassignment3553) 
                stream_COMMA.add(char_literal439)
                self._state.following.append(self.FOLLOW_role_in_unassignment3555)
                role440 = self.role()

                self._state.following.pop()
                stream_role.add(role440.tree)
                char_literal441=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_unassignment3557) 
                stream_RPAREN.add(char_literal441)

                # AST Rewrite
                # elements: user, role, 125
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 224:15: -> ^( 'unassign' user role )
                # dgdl.g:224:18: ^( 'unassign' user role )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_125.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_user.nextTree())
                self._adaptor.addChild(root_1, stream_role.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unassignment"

    class externalEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.externalEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "externalEffect"
    # dgdl.g:229:1: externalEffect : 'extEffect' '(' identifier ( ',' content )? ')' -> ^( 'extEffect' identifier ( content )? ) ;
    def externalEffect(self, ):

        retval = self.externalEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal442 = None
        char_literal443 = None
        char_literal445 = None
        char_literal447 = None
        identifier444 = None

        content446 = None


        string_literal442_tree = None
        char_literal443_tree = None
        char_literal445_tree = None
        char_literal447_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_EXTEFFECT = RewriteRuleTokenStream(self._adaptor, "token EXTEFFECT")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:229:15: ( 'extEffect' '(' identifier ( ',' content )? ')' -> ^( 'extEffect' identifier ( content )? ) )
                # dgdl.g:229:17: 'extEffect' '(' identifier ( ',' content )? ')'
                pass 
                string_literal442=self.match(self.input, EXTEFFECT, self.FOLLOW_EXTEFFECT_in_externalEffect3605) 
                stream_EXTEFFECT.add(string_literal442)
                char_literal443=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_externalEffect3607) 
                stream_LPAREN.add(char_literal443)
                self._state.following.append(self.FOLLOW_identifier_in_externalEffect3609)
                identifier444 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier444.tree)
                # dgdl.g:229:44: ( ',' content )?
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if (LA69_0 == COMMA) :
                    alt69 = 1
                if alt69 == 1:
                    # dgdl.g:229:45: ',' content
                    pass 
                    char_literal445=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_externalEffect3612) 
                    stream_COMMA.add(char_literal445)
                    self._state.following.append(self.FOLLOW_content_in_externalEffect3614)
                    content446 = self.content()

                    self._state.following.pop()
                    stream_content.add(content446.tree)



                char_literal447=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_externalEffect3618) 
                stream_RPAREN.add(char_literal447)

                # AST Rewrite
                # elements: EXTEFFECT, identifier, content
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 230:15: -> ^( 'extEffect' identifier ( content )? )
                # dgdl.g:230:18: ^( 'extEffect' identifier ( content )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EXTEFFECT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                # dgdl.g:230:43: ( content )?
                if stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "externalEffect"

    class send_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.send_return, self).__init__()

            self.tree = None




    # $ANTLR start "send"
    # dgdl.g:233:1: send : 'send' '(' identifier ( ',' postVars )* ')' -> ^( 'send' identifier ( postVars )* ) ;
    def send(self, ):

        retval = self.send_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal448 = None
        char_literal449 = None
        char_literal451 = None
        char_literal453 = None
        identifier450 = None

        postVars452 = None


        string_literal448_tree = None
        char_literal449_tree = None
        char_literal451_tree = None
        char_literal453_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_126 = RewriteRuleTokenStream(self._adaptor, "token 126")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_postVars = RewriteRuleSubtreeStream(self._adaptor, "rule postVars")
        try:
            try:
                # dgdl.g:233:6: ( 'send' '(' identifier ( ',' postVars )* ')' -> ^( 'send' identifier ( postVars )* ) )
                # dgdl.g:233:8: 'send' '(' identifier ( ',' postVars )* ')'
                pass 
                string_literal448=self.match(self.input, 126, self.FOLLOW_126_in_send3667) 
                stream_126.add(string_literal448)
                char_literal449=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_send3669) 
                stream_LPAREN.add(char_literal449)
                self._state.following.append(self.FOLLOW_identifier_in_send3671)
                identifier450 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier450.tree)
                # dgdl.g:233:30: ( ',' postVars )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == COMMA) :
                        alt70 = 1


                    if alt70 == 1:
                        # dgdl.g:233:31: ',' postVars
                        pass 
                        char_literal451=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_send3674) 
                        stream_COMMA.add(char_literal451)
                        self._state.following.append(self.FOLLOW_postVars_in_send3676)
                        postVars452 = self.postVars()

                        self._state.following.pop()
                        stream_postVars.add(postVars452.tree)


                    else:
                        break #loop70
                char_literal453=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_send3680) 
                stream_RPAREN.add(char_literal453)

                # AST Rewrite
                # elements: 126, postVars, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 234:9: -> ^( 'send' identifier ( postVars )* )
                # dgdl.g:234:12: ^( 'send' identifier ( postVars )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_126.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                # dgdl.g:234:32: ( postVars )*
                while stream_postVars.hasNext():
                    self._adaptor.addChild(root_1, stream_postVars.nextTree())


                stream_postVars.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "send"

    class postVars_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.postVars_return, self).__init__()

            self.tree = None




    # $ANTLR start "postVars"
    # dgdl.g:236:1: postVars : '{' postVar ( ',' postVar )* '}' -> ^( VARS ( postVar )+ ) ;
    def postVars(self, ):

        retval = self.postVars_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal454 = None
        char_literal456 = None
        char_literal458 = None
        postVar455 = None

        postVar457 = None


        char_literal454_tree = None
        char_literal456_tree = None
        char_literal458_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_postVar = RewriteRuleSubtreeStream(self._adaptor, "rule postVar")
        try:
            try:
                # dgdl.g:236:9: ( '{' postVar ( ',' postVar )* '}' -> ^( VARS ( postVar )+ ) )
                # dgdl.g:236:11: '{' postVar ( ',' postVar )* '}'
                pass 
                char_literal454=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_postVars3714) 
                stream_LBRACE.add(char_literal454)
                self._state.following.append(self.FOLLOW_postVar_in_postVars3716)
                postVar455 = self.postVar()

                self._state.following.pop()
                stream_postVar.add(postVar455.tree)
                # dgdl.g:236:23: ( ',' postVar )*
                while True: #loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == COMMA) :
                        alt71 = 1


                    if alt71 == 1:
                        # dgdl.g:236:24: ',' postVar
                        pass 
                        char_literal456=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_postVars3719) 
                        stream_COMMA.add(char_literal456)
                        self._state.following.append(self.FOLLOW_postVar_in_postVars3721)
                        postVar457 = self.postVar()

                        self._state.following.pop()
                        stream_postVar.add(postVar457.tree)


                    else:
                        break #loop71
                char_literal458=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_postVars3725) 
                stream_RBRACE.add(char_literal458)

                # AST Rewrite
                # elements: postVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 237:8: -> ^( VARS ( postVar )+ )
                # dgdl.g:237:11: ^( VARS ( postVar )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARS, "VARS"), root_1)

                # dgdl.g:237:18: ( postVar )+
                if not (stream_postVar.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_postVar.hasNext():
                    self._adaptor.addChild(root_1, stream_postVar.nextTree())


                stream_postVar.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "postVars"

    class postVar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.postVar_return, self).__init__()

            self.tree = None




    # $ANTLR start "postVar"
    # dgdl.g:239:1: postVar : varLabel ':' ( contentVar | STRINGLITERAL | runTimeVar | content ) -> ^( VAR varLabel ( contentVar )? ( STRINGLITERAL )? ( runTimeVar )? ( content )? ) ;
    def postVar(self, ):

        retval = self.postVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal460 = None
        STRINGLITERAL462 = None
        varLabel459 = None

        contentVar461 = None

        runTimeVar463 = None

        content464 = None


        char_literal460_tree = None
        STRINGLITERAL462_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_STRINGLITERAL = RewriteRuleTokenStream(self._adaptor, "token STRINGLITERAL")
        stream_varLabel = RewriteRuleSubtreeStream(self._adaptor, "rule varLabel")
        stream_contentVar = RewriteRuleSubtreeStream(self._adaptor, "rule contentVar")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:239:8: ( varLabel ':' ( contentVar | STRINGLITERAL | runTimeVar | content ) -> ^( VAR varLabel ( contentVar )? ( STRINGLITERAL )? ( runTimeVar )? ( content )? ) )
                # dgdl.g:239:10: varLabel ':' ( contentVar | STRINGLITERAL | runTimeVar | content )
                pass 
                self._state.following.append(self.FOLLOW_varLabel_in_postVar3756)
                varLabel459 = self.varLabel()

                self._state.following.pop()
                stream_varLabel.add(varLabel459.tree)
                char_literal460=self.match(self.input, COLON, self.FOLLOW_COLON_in_postVar3758) 
                stream_COLON.add(char_literal460)
                # dgdl.g:239:23: ( contentVar | STRINGLITERAL | runTimeVar | content )
                alt72 = 4
                LA72 = self.input.LA(1)
                if LA72 == LowerChar or LA72 == NOT:
                    alt72 = 1
                elif LA72 == STRINGLITERAL:
                    alt72 = 2
                elif LA72 == DOLLAR:
                    alt72 = 3
                elif LA72 == LBRACE:
                    alt72 = 4
                else:
                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # dgdl.g:239:24: contentVar
                    pass 
                    self._state.following.append(self.FOLLOW_contentVar_in_postVar3761)
                    contentVar461 = self.contentVar()

                    self._state.following.pop()
                    stream_contentVar.add(contentVar461.tree)


                elif alt72 == 2:
                    # dgdl.g:239:37: STRINGLITERAL
                    pass 
                    STRINGLITERAL462=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_postVar3765) 
                    stream_STRINGLITERAL.add(STRINGLITERAL462)


                elif alt72 == 3:
                    # dgdl.g:239:53: runTimeVar
                    pass 
                    self._state.following.append(self.FOLLOW_runTimeVar_in_postVar3769)
                    runTimeVar463 = self.runTimeVar()

                    self._state.following.pop()
                    stream_runTimeVar.add(runTimeVar463.tree)


                elif alt72 == 4:
                    # dgdl.g:239:66: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_postVar3773)
                    content464 = self.content()

                    self._state.following.pop()
                    stream_content.add(content464.tree)




                # AST Rewrite
                # elements: varLabel, content, runTimeVar, contentVar, STRINGLITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 240:8: -> ^( VAR varLabel ( contentVar )? ( STRINGLITERAL )? ( runTimeVar )? ( content )? )
                # dgdl.g:240:11: ^( VAR varLabel ( contentVar )? ( STRINGLITERAL )? ( runTimeVar )? ( content )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                self._adaptor.addChild(root_1, stream_varLabel.nextTree())
                # dgdl.g:240:26: ( contentVar )?
                if stream_contentVar.hasNext():
                    self._adaptor.addChild(root_1, stream_contentVar.nextTree())


                stream_contentVar.reset();
                # dgdl.g:240:38: ( STRINGLITERAL )?
                if stream_STRINGLITERAL.hasNext():
                    self._adaptor.addChild(root_1, stream_STRINGLITERAL.nextNode())


                stream_STRINGLITERAL.reset();
                # dgdl.g:240:53: ( runTimeVar )?
                if stream_runTimeVar.hasNext():
                    self._adaptor.addChild(root_1, stream_runTimeVar.nextTree())


                stream_runTimeVar.reset();
                # dgdl.g:240:65: ( content )?
                if stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "postVar"

    class receive_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.receive_return, self).__init__()

            self.tree = None




    # $ANTLR start "receive"
    # dgdl.g:243:1: receive : 'receive' '(' identifier ( ',' runTimeVar )? ')' -> ^( 'receive' identifier ^( VAR ( runTimeVar )* ) ) ;
    def receive(self, ):

        retval = self.receive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal465 = None
        char_literal466 = None
        char_literal468 = None
        char_literal470 = None
        identifier467 = None

        runTimeVar469 = None


        string_literal465_tree = None
        char_literal466_tree = None
        char_literal468_tree = None
        char_literal470_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_127 = RewriteRuleTokenStream(self._adaptor, "token 127")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        try:
            try:
                # dgdl.g:243:8: ( 'receive' '(' identifier ( ',' runTimeVar )? ')' -> ^( 'receive' identifier ^( VAR ( runTimeVar )* ) ) )
                # dgdl.g:243:10: 'receive' '(' identifier ( ',' runTimeVar )? ')'
                pass 
                string_literal465=self.match(self.input, 127, self.FOLLOW_127_in_receive3823) 
                stream_127.add(string_literal465)
                char_literal466=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_receive3825) 
                stream_LPAREN.add(char_literal466)
                self._state.following.append(self.FOLLOW_identifier_in_receive3827)
                identifier467 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier467.tree)
                # dgdl.g:243:35: ( ',' runTimeVar )?
                alt73 = 2
                LA73_0 = self.input.LA(1)

                if (LA73_0 == COMMA) :
                    alt73 = 1
                if alt73 == 1:
                    # dgdl.g:243:36: ',' runTimeVar
                    pass 
                    char_literal468=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_receive3830) 
                    stream_COMMA.add(char_literal468)
                    self._state.following.append(self.FOLLOW_runTimeVar_in_receive3832)
                    runTimeVar469 = self.runTimeVar()

                    self._state.following.pop()
                    stream_runTimeVar.add(runTimeVar469.tree)



                char_literal470=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_receive3835) 
                stream_RPAREN.add(char_literal470)

                # AST Rewrite
                # elements: 127, identifier, runTimeVar
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 244:9: -> ^( 'receive' identifier ^( VAR ( runTimeVar )* ) )
                # dgdl.g:244:12: ^( 'receive' identifier ^( VAR ( runTimeVar )* ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_127.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                # dgdl.g:244:35: ^( VAR ( runTimeVar )* )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_2)

                # dgdl.g:244:41: ( runTimeVar )*
                while stream_runTimeVar.hasNext():
                    self._adaptor.addChild(root_2, stream_runTimeVar.nextTree())


                stream_runTimeVar.reset();

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "receive"

    class invoke_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.invoke_return, self).__init__()

            self.tree = None




    # $ANTLR start "invoke"
    # dgdl.g:246:1: invoke : 'invoke' '(' identifier ( ',' postVars )* ')' -> ^( 'invoke' identifier ( postVars )* ) ;
    def invoke(self, ):

        retval = self.invoke_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal471 = None
        char_literal472 = None
        char_literal474 = None
        char_literal476 = None
        identifier473 = None

        postVars475 = None


        string_literal471_tree = None
        char_literal472_tree = None
        char_literal474_tree = None
        char_literal476_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_128 = RewriteRuleTokenStream(self._adaptor, "token 128")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_postVars = RewriteRuleSubtreeStream(self._adaptor, "rule postVars")
        try:
            try:
                # dgdl.g:246:8: ( 'invoke' '(' identifier ( ',' postVars )* ')' -> ^( 'invoke' identifier ( postVars )* ) )
                # dgdl.g:246:10: 'invoke' '(' identifier ( ',' postVars )* ')'
                pass 
                string_literal471=self.match(self.input, 128, self.FOLLOW_128_in_invoke3878) 
                stream_128.add(string_literal471)
                char_literal472=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_invoke3880) 
                stream_LPAREN.add(char_literal472)
                self._state.following.append(self.FOLLOW_identifier_in_invoke3882)
                identifier473 = self.identifier()

                self._state.following.pop()
                stream_identifier.add(identifier473.tree)
                # dgdl.g:246:34: ( ',' postVars )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == COMMA) :
                        alt74 = 1


                    if alt74 == 1:
                        # dgdl.g:246:35: ',' postVars
                        pass 
                        char_literal474=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_invoke3885) 
                        stream_COMMA.add(char_literal474)
                        self._state.following.append(self.FOLLOW_postVars_in_invoke3887)
                        postVars475 = self.postVars()

                        self._state.following.pop()
                        stream_postVars.add(postVars475.tree)


                    else:
                        break #loop74
                char_literal476=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_invoke3890) 
                stream_RPAREN.add(char_literal476)

                # AST Rewrite
                # elements: 128, postVars, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 247:5: -> ^( 'invoke' identifier ( postVars )* )
                # dgdl.g:247:8: ^( 'invoke' identifier ( postVars )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_128.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_identifier.nextTree())
                # dgdl.g:247:30: ( postVars )*
                while stream_postVars.hasNext():
                    self._adaptor.addChild(root_1, stream_postVars.nextTree())


                stream_postVars.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "invoke"

    class initiate_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.initiate_return, self).__init__()

            self.tree = None




    # $ANTLR start "initiate"
    # dgdl.g:249:1: initiate : 'initiate' '(' 'protocol' ':' STRINGLITERAL ')' -> ^( 'initiate' STRINGLITERAL ) ;
    def initiate(self, ):

        retval = self.initiate_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal477 = None
        char_literal478 = None
        string_literal479 = None
        char_literal480 = None
        STRINGLITERAL481 = None
        char_literal482 = None

        string_literal477_tree = None
        char_literal478_tree = None
        string_literal479_tree = None
        char_literal480_tree = None
        STRINGLITERAL481_tree = None
        char_literal482_tree = None
        stream_INITIATE = RewriteRuleTokenStream(self._adaptor, "token INITIATE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_129 = RewriteRuleTokenStream(self._adaptor, "token 129")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_STRINGLITERAL = RewriteRuleTokenStream(self._adaptor, "token STRINGLITERAL")

        try:
            try:
                # dgdl.g:249:10: ( 'initiate' '(' 'protocol' ':' STRINGLITERAL ')' -> ^( 'initiate' STRINGLITERAL ) )
                # dgdl.g:249:12: 'initiate' '(' 'protocol' ':' STRINGLITERAL ')'
                pass 
                string_literal477=self.match(self.input, INITIATE, self.FOLLOW_INITIATE_in_initiate3917) 
                stream_INITIATE.add(string_literal477)
                char_literal478=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_initiate3919) 
                stream_LPAREN.add(char_literal478)
                string_literal479=self.match(self.input, 129, self.FOLLOW_129_in_initiate3921) 
                stream_129.add(string_literal479)
                char_literal480=self.match(self.input, COLON, self.FOLLOW_COLON_in_initiate3923) 
                stream_COLON.add(char_literal480)
                STRINGLITERAL481=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_initiate3925) 
                stream_STRINGLITERAL.add(STRINGLITERAL481)
                char_literal482=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_initiate3927) 
                stream_RPAREN.add(char_literal482)

                # AST Rewrite
                # elements: INITIATE, STRINGLITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 250:9: -> ^( 'initiate' STRINGLITERAL )
                # dgdl.g:250:12: ^( 'initiate' STRINGLITERAL )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_INITIATE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_STRINGLITERAL.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "initiate"

    class save_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.save_return, self).__init__()

            self.tree = None




    # $ANTLR start "save"
    # dgdl.g:252:1: save : 'save' '(' ( content | STRINGLITERAL ) ',' runTimeVar ')' -> ^( 'save' ( content )? ( STRINGLITERAL )? ^( VAR runTimeVar ) ) ;
    def save(self, ):

        retval = self.save_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal483 = None
        char_literal484 = None
        STRINGLITERAL486 = None
        char_literal487 = None
        char_literal489 = None
        content485 = None

        runTimeVar488 = None


        string_literal483_tree = None
        char_literal484_tree = None
        STRINGLITERAL486_tree = None
        char_literal487_tree = None
        char_literal489_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_130 = RewriteRuleTokenStream(self._adaptor, "token 130")
        stream_STRINGLITERAL = RewriteRuleTokenStream(self._adaptor, "token STRINGLITERAL")
        stream_runTimeVar = RewriteRuleSubtreeStream(self._adaptor, "rule runTimeVar")
        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # dgdl.g:252:6: ( 'save' '(' ( content | STRINGLITERAL ) ',' runTimeVar ')' -> ^( 'save' ( content )? ( STRINGLITERAL )? ^( VAR runTimeVar ) ) )
                # dgdl.g:252:8: 'save' '(' ( content | STRINGLITERAL ) ',' runTimeVar ')'
                pass 
                string_literal483=self.match(self.input, 130, self.FOLLOW_130_in_save3959) 
                stream_130.add(string_literal483)
                char_literal484=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_save3961) 
                stream_LPAREN.add(char_literal484)
                # dgdl.g:252:19: ( content | STRINGLITERAL )
                alt75 = 2
                LA75_0 = self.input.LA(1)

                if (LA75_0 == LBRACE) :
                    alt75 = 1
                elif (LA75_0 == STRINGLITERAL) :
                    alt75 = 2
                else:
                    nvae = NoViableAltException("", 75, 0, self.input)

                    raise nvae

                if alt75 == 1:
                    # dgdl.g:252:20: content
                    pass 
                    self._state.following.append(self.FOLLOW_content_in_save3964)
                    content485 = self.content()

                    self._state.following.pop()
                    stream_content.add(content485.tree)


                elif alt75 == 2:
                    # dgdl.g:252:28: STRINGLITERAL
                    pass 
                    STRINGLITERAL486=self.match(self.input, STRINGLITERAL, self.FOLLOW_STRINGLITERAL_in_save3966) 
                    stream_STRINGLITERAL.add(STRINGLITERAL486)



                char_literal487=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_save3969) 
                stream_COMMA.add(char_literal487)
                self._state.following.append(self.FOLLOW_runTimeVar_in_save3971)
                runTimeVar488 = self.runTimeVar()

                self._state.following.pop()
                stream_runTimeVar.add(runTimeVar488.tree)
                char_literal489=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_save3972) 
                stream_RPAREN.add(char_literal489)

                # AST Rewrite
                # elements: content, runTimeVar, STRINGLITERAL, 130
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 253:9: -> ^( 'save' ( content )? ( STRINGLITERAL )? ^( VAR runTimeVar ) )
                # dgdl.g:253:12: ^( 'save' ( content )? ( STRINGLITERAL )? ^( VAR runTimeVar ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_130.nextNode(), root_1)

                # dgdl.g:253:21: ( content )?
                if stream_content.hasNext():
                    self._adaptor.addChild(root_1, stream_content.nextTree())


                stream_content.reset();
                # dgdl.g:253:30: ( STRINGLITERAL )?
                if stream_STRINGLITERAL.hasNext():
                    self._adaptor.addChild(root_1, stream_STRINGLITERAL.nextNode())


                stream_STRINGLITERAL.reset();
                # dgdl.g:253:45: ^( VAR runTimeVar )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_2)

                self._adaptor.addChild(root_2, stream_runTimeVar.nextTree())

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "save"

    class moveID_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.moveID_return, self).__init__()

            self.tree = None




    # $ANTLR start "moveID"
    # dgdl.g:255:1: moveID : identifier ;
    def moveID(self, ):

        retval = self.moveID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier490 = None



        try:
            try:
                # dgdl.g:255:15: ( identifier )
                # dgdl.g:255:17: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_moveID4013)
                identifier490 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier490.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "moveID"

    class sysgame_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.sysgame_return, self).__init__()

            self.tree = None




    # $ANTLR start "sysgame"
    # dgdl.g:256:1: sysgame : identifier ;
    def sysgame(self, ):

        retval = self.sysgame_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier491 = None



        try:
            try:
                # dgdl.g:256:15: ( identifier )
                # dgdl.g:256:17: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_sysgame4026)
                identifier491 = self.identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, identifier491.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sysgame"

    class upperChar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.upperChar_return, self).__init__()

            self.tree = None




    # $ANTLR start "upperChar"
    # dgdl.g:259:1: upperChar : UpperChar ;
    def upperChar(self, ):

        retval = self.upperChar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UpperChar492 = None

        UpperChar492_tree = None

        try:
            try:
                # dgdl.g:259:13: ( UpperChar )
                # dgdl.g:259:15: UpperChar
                pass 
                root_0 = self._adaptor.nil()

                UpperChar492=self.match(self.input, UpperChar, self.FOLLOW_UpperChar_in_upperChar4038)

                UpperChar492_tree = self._adaptor.createWithPayload(UpperChar492)
                self._adaptor.addChild(root_0, UpperChar492_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "upperChar"

    class lowerChar_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.lowerChar_return, self).__init__()

            self.tree = None




    # $ANTLR start "lowerChar"
    # dgdl.g:260:1: lowerChar : LowerChar ;
    def lowerChar(self, ):

        retval = self.lowerChar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LowerChar493 = None

        LowerChar493_tree = None

        try:
            try:
                # dgdl.g:260:13: ( LowerChar )
                # dgdl.g:260:15: LowerChar
                pass 
                root_0 = self._adaptor.nil()

                LowerChar493=self.match(self.input, LowerChar, self.FOLLOW_LowerChar_in_lowerChar4047)

                LowerChar493_tree = self._adaptor.createWithPayload(LowerChar493)
                self._adaptor.addChild(root_0, LowerChar493_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "lowerChar"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.identifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "identifier"
    # dgdl.g:261:1: identifier : Identifier ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Identifier494 = None

        Identifier494_tree = None

        try:
            try:
                # dgdl.g:261:14: ( Identifier )
                # dgdl.g:261:16: Identifier
                pass 
                root_0 = self._adaptor.nil()

                Identifier494=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_identifier4056)

                Identifier494_tree = self._adaptor.createWithPayload(Identifier494)
                self._adaptor.addChild(root_0, Identifier494_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "identifier"

    class number_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.number_return, self).__init__()

            self.tree = None




    # $ANTLR start "number"
    # dgdl.g:262:1: number : Number ;
    def number(self, ):

        retval = self.number_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Number495 = None

        Number495_tree = None

        try:
            try:
                # dgdl.g:262:11: ( Number )
                # dgdl.g:262:13: Number
                pass 
                root_0 = self._adaptor.nil()

                Number495=self.match(self.input, Number, self.FOLLOW_Number_in_number4066)

                Number495_tree = self._adaptor.createWithPayload(Number495)
                self._adaptor.addChild(root_0, Number495_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "number"

    class varLabel_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.varLabel_return, self).__init__()

            self.tree = None




    # $ANTLR start "varLabel"
    # dgdl.g:264:1: varLabel : ( Identifier | ( LowerChar )+ ) ;
    def varLabel(self, ):

        retval = self.varLabel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Identifier496 = None
        LowerChar497 = None

        Identifier496_tree = None
        LowerChar497_tree = None

        try:
            try:
                # dgdl.g:264:15: ( ( Identifier | ( LowerChar )+ ) )
                # dgdl.g:264:17: ( Identifier | ( LowerChar )+ )
                pass 
                root_0 = self._adaptor.nil()

                # dgdl.g:264:17: ( Identifier | ( LowerChar )+ )
                alt77 = 2
                LA77_0 = self.input.LA(1)

                if (LA77_0 == Identifier) :
                    alt77 = 1
                elif (LA77_0 == LowerChar) :
                    alt77 = 2
                else:
                    nvae = NoViableAltException("", 77, 0, self.input)

                    raise nvae

                if alt77 == 1:
                    # dgdl.g:264:18: Identifier
                    pass 
                    Identifier496=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_varLabel4080)

                    Identifier496_tree = self._adaptor.createWithPayload(Identifier496)
                    self._adaptor.addChild(root_0, Identifier496_tree)



                elif alt77 == 2:
                    # dgdl.g:264:31: ( LowerChar )+
                    pass 
                    # dgdl.g:264:31: ( LowerChar )+
                    cnt76 = 0
                    while True: #loop76
                        alt76 = 2
                        LA76_0 = self.input.LA(1)

                        if (LA76_0 == LowerChar) :
                            alt76 = 1


                        if alt76 == 1:
                            # dgdl.g:264:31: LowerChar
                            pass 
                            LowerChar497=self.match(self.input, LowerChar, self.FOLLOW_LowerChar_in_varLabel4084)

                            LowerChar497_tree = self._adaptor.createWithPayload(LowerChar497)
                            self._adaptor.addChild(root_0, LowerChar497_tree)



                        else:
                            if cnt76 >= 1:
                                break #loop76

                            eee = EarlyExitException(76, self.input)
                            raise eee

                        cnt76 += 1






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "varLabel"


    # Delegated rules


 

    FOLLOW_systemID_in_system121 = frozenset([40])
    FOLLOW_LBRACE_in_system123 = frozenset([33])
    FOLLOW_game_in_system126 = frozenset([33, 41])
    FOLLOW_RBRACE_in_system130 = frozenset([])
    FOLLOW_EOF_in_system133 = frozenset([1])
    FOLLOW_identifier_in_systemID183 = frozenset([1])
    FOLLOW_gameID_in_game192 = frozenset([40])
    FOLLOW_LBRACE_in_game194 = frozenset([112])
    FOLLOW_composition_in_game196 = frozenset([75, 100])
    FOLLOW_rule_in_game199 = frozenset([75, 100])
    FOLLOW_interaction_in_game204 = frozenset([41, 75, 100])
    FOLLOW_RBRACE_in_game208 = frozenset([1])
    FOLLOW_identifier_in_gameID242 = frozenset([1])
    FOLLOW_turns_in_composition255 = frozenset([96, 99])
    FOLLOW_roleList_in_composition258 = frozenset([96, 99])
    FOLLOW_participants_in_composition262 = frozenset([95])
    FOLLOW_player_in_composition265 = frozenset([1, 48, 62, 95, 106, 120])
    FOLLOW_extURImap_in_composition270 = frozenset([1, 48, 62, 106, 120])
    FOLLOW_plugin_in_composition275 = frozenset([1, 48, 106, 120])
    FOLLOW_store_in_composition280 = frozenset([1, 48, 106])
    FOLLOW_backtrack_in_composition285 = frozenset([1])
    FOLLOW_TURNS_in_turns298 = frozenset([40])
    FOLLOW_LBRACE_in_turns300 = frozenset([79])
    FOLLOW_turnSize_in_turns302 = frozenset([36])
    FOLLOW_COMMA_in_turns304 = frozenset([91])
    FOLLOW_ordering_in_turns306 = frozenset([36, 41])
    FOLLOW_COMMA_in_turns309 = frozenset([81])
    FOLLOW_maxTurns_in_turns311 = frozenset([41])
    FOLLOW_RBRACE_in_turns315 = frozenset([1])
    FOLLOW_MAGNITUDE_in_turnSize347 = frozenset([37])
    FOLLOW_COLON_in_turnSize349 = frozenset([30, 84, 102])
    FOLLOW_number_in_turnSize352 = frozenset([1])
    FOLLOW_SINGLE_in_turnSize356 = frozenset([1])
    FOLLOW_MULTIPLE_in_turnSize360 = frozenset([1])
    FOLLOW_ORDERING_in_ordering395 = frozenset([37])
    FOLLOW_COLON_in_ordering397 = frozenset([15, 16])
    FOLLOW_STRICT_in_ordering400 = frozenset([1])
    FOLLOW_LIBERAL_in_ordering404 = frozenset([1])
    FOLLOW_MAXTURNS_in_maxTurns436 = frozenset([37])
    FOLLOW_COLON_in_maxTurns438 = frozenset([30, 42, 113])
    FOLLOW_number_in_maxTurns441 = frozenset([1])
    FOLLOW_runTimeVar_in_maxTurns445 = frozenset([1])
    FOLLOW_UNDEFINED_in_maxTurns449 = frozenset([1])
    FOLLOW_DOLLAR_in_runTimeVar484 = frozenset([33])
    FOLLOW_identifier_in_runTimeVar486 = frozenset([42])
    FOLLOW_DOLLAR_in_runTimeVar488 = frozenset([1])
    FOLLOW_ROLES_in_roleList499 = frozenset([40])
    FOLLOW_LBRACE_in_roleList501 = frozenset([17, 18, 33])
    FOLLOW_role_in_roleList503 = frozenset([36, 41])
    FOLLOW_COMMA_in_roleList506 = frozenset([17, 18, 33])
    FOLLOW_role_in_roleList508 = frozenset([36, 41])
    FOLLOW_RBRACE_in_roleList512 = frozenset([1])
    FOLLOW_LISTENER_in_role548 = frozenset([1])
    FOLLOW_SPEAKER_in_role552 = frozenset([1])
    FOLLOW_identifier_in_role556 = frozenset([1])
    FOLLOW_PLAYERS_in_participants564 = frozenset([40])
    FOLLOW_LBRACE_in_participants566 = frozenset([82])
    FOLLOW_MIN_in_participants568 = frozenset([37])
    FOLLOW_COLON_in_participants570 = frozenset([30])
    FOLLOW_minplayers_in_participants572 = frozenset([36])
    FOLLOW_COMMA_in_participants574 = frozenset([80])
    FOLLOW_MAX_in_participants576 = frozenset([37])
    FOLLOW_COLON_in_participants578 = frozenset([30, 113])
    FOLLOW_maxplayers_in_participants580 = frozenset([41])
    FOLLOW_RBRACE_in_participants582 = frozenset([1])
    FOLLOW_number_in_minplayers620 = frozenset([1])
    FOLLOW_number_in_maxplayers629 = frozenset([1])
    FOLLOW_UNDEFINED_in_maxplayers633 = frozenset([1])
    FOLLOW_PLAYER_in_player647 = frozenset([40])
    FOLLOW_LBRACE_in_player649 = frozenset([66])
    FOLLOW_ID_in_player651 = frozenset([37])
    FOLLOW_COLON_in_player653 = frozenset([33, 42])
    FOLLOW_playerID_in_player655 = frozenset([36, 41])
    FOLLOW_COMMA_in_player658 = frozenset([99])
    FOLLOW_roleList_in_player660 = frozenset([36, 41])
    FOLLOW_COMMA_in_player665 = frozenset([80])
    FOLLOW_MAX_in_player667 = frozenset([37])
    FOLLOW_COLON_in_player669 = frozenset([30, 113])
    FOLLOW_maxplayers_in_player671 = frozenset([36, 41])
    FOLLOW_COMMA_in_player676 = frozenset([82])
    FOLLOW_MIN_in_player678 = frozenset([37])
    FOLLOW_COLON_in_player680 = frozenset([30])
    FOLLOW_minplayers_in_player682 = frozenset([41])
    FOLLOW_RBRACE_in_player686 = frozenset([1])
    FOLLOW_identifier_in_playerID735 = frozenset([1])
    FOLLOW_runTimeVar_in_playerID739 = frozenset([1])
    FOLLOW_EXTURI_in_extURImap750 = frozenset([40])
    FOLLOW_LBRACE_in_extURImap752 = frozenset([66])
    FOLLOW_ID_in_extURImap754 = frozenset([37])
    FOLLOW_COLON_in_extURImap756 = frozenset([33])
    FOLLOW_extURIID_in_extURImap758 = frozenset([36])
    FOLLOW_COMMA_in_extURImap760 = frozenset([119])
    FOLLOW_119_in_extURImap762 = frozenset([37])
    FOLLOW_COLON_in_extURImap764 = frozenset([19])
    FOLLOW_extURI_in_extURImap766 = frozenset([41])
    FOLLOW_RBRACE_in_extURImap768 = frozenset([1])
    FOLLOW_identifier_in_extURIID800 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_extURI812 = frozenset([1])
    FOLLOW_STORE_in_store826 = frozenset([40])
    FOLLOW_LBRACE_in_store828 = frozenset([66])
    FOLLOW_ID_in_store830 = frozenset([37])
    FOLLOW_COLON_in_store832 = frozenset([33])
    FOLLOW_storeName_in_store834 = frozenset([36])
    FOLLOW_COMMA_in_store836 = frozenset([92])
    FOLLOW_OWNER_in_store838 = frozenset([37])
    FOLLOW_COLON_in_store840 = frozenset([20, 33, 40, 42])
    FOLLOW_storeOwner_in_store842 = frozenset([36])
    FOLLOW_COMMA_in_store844 = frozenset([107])
    FOLLOW_storeStructure_in_store846 = frozenset([36])
    FOLLOW_COMMA_in_store848 = frozenset([114])
    FOLLOW_visibility_in_store850 = frozenset([36])
    FOLLOW_COMMA_in_store852 = frozenset([40])
    FOLLOW_content_in_store854 = frozenset([41])
    FOLLOW_RBRACE_in_store856 = frozenset([1])
    FOLLOW_identifier_in_storeName893 = frozenset([1])
    FOLLOW_playerID_in_storeOwner901 = frozenset([1])
    FOLLOW_LBRACE_in_storeOwner905 = frozenset([33, 42])
    FOLLOW_playerID_in_storeOwner907 = frozenset([36])
    FOLLOW_COMMA_in_storeOwner910 = frozenset([33, 42])
    FOLLOW_playerID_in_storeOwner912 = frozenset([36, 41])
    FOLLOW_RBRACE_in_storeOwner916 = frozenset([1])
    FOLLOW_SHARED_in_storeOwner920 = frozenset([1])
    FOLLOW_STRUCTURE_in_storeStructure926 = frozenset([37])
    FOLLOW_COLON_in_storeStructure929 = frozenset([21, 22, 23])
    FOLLOW_set_in_storeStructure932 = frozenset([1])
    FOLLOW_VISIBILITY_in_visibility950 = frozenset([37])
    FOLLOW_COLON_in_visibility953 = frozenset([24, 25])
    FOLLOW_set_in_visibility956 = frozenset([1])
    FOLLOW_BACKTRACK_in_backtrack972 = frozenset([40])
    FOLLOW_LBRACE_in_backtrack974 = frozenset([88, 90])
    FOLLOW_ON_in_backtrack977 = frozenset([41])
    FOLLOW_OFF_in_backtrack981 = frozenset([41])
    FOLLOW_RBRACE_in_backtrack984 = frozenset([1])
    FOLLOW_120_in_plugin1033 = frozenset([40])
    FOLLOW_LBRACE_in_plugin1035 = frozenset([66])
    FOLLOW_ID_in_plugin1037 = frozenset([37])
    FOLLOW_COLON_in_plugin1039 = frozenset([33])
    FOLLOW_identifier_in_plugin1041 = frozenset([36])
    FOLLOW_COMMA_in_plugin1043 = frozenset([121])
    FOLLOW_121_in_plugin1045 = frozenset([37])
    FOLLOW_COLON_in_plugin1047 = frozenset([19])
    FOLLOW_STRINGLITERAL_in_plugin1049 = frozenset([41])
    FOLLOW_RBRACE_in_plugin1051 = frozenset([1])
    FOLLOW_RULE_in_rule1092 = frozenset([40])
    FOLLOW_LBRACE_in_rule1094 = frozenset([66])
    FOLLOW_ID_in_rule1096 = frozenset([37])
    FOLLOW_COLON_in_rule1098 = frozenset([33])
    FOLLOW_ruleID_in_rule1100 = frozenset([36])
    FOLLOW_COMMA_in_rule1102 = frozenset([101])
    FOLLOW_SCOPE_in_rule1104 = frozenset([37])
    FOLLOW_COLON_in_rule1106 = frozenset([26, 27, 28])
    FOLLOW_scopeType_in_rule1108 = frozenset([36])
    FOLLOW_COMMA_in_rule1110 = frozenset([40])
    FOLLOW_ruleBody_in_rule1112 = frozenset([41])
    FOLLOW_RBRACE_in_rule1114 = frozenset([1])
    FOLLOW_identifier_in_ruleID1150 = frozenset([1])
    FOLLOW_set_in_scopeType1159 = frozenset([1])
    FOLLOW_effects_in_ruleBody1180 = frozenset([1])
    FOLLOW_conditional_in_ruleBody1205 = frozenset([1])
    FOLLOW_LBRACE_in_effects1225 = frozenset([46, 61, 72, 83, 105, 106, 125, 126, 127, 128, 130])
    FOLLOW_effect_in_effects1228 = frozenset([29, 41])
    FOLLOW_AND_in_effects1231 = frozenset([46, 61, 72, 83, 105, 106, 125, 126, 127, 128, 130])
    FOLLOW_effect_in_effects1234 = frozenset([29, 41])
    FOLLOW_RBRACE_in_effects1238 = frozenset([1])
    FOLLOW_move_in_effect1252 = frozenset([1])
    FOLLOW_storeOp_in_effect1256 = frozenset([1])
    FOLLOW_statusUpdate_in_effect1260 = frozenset([1])
    FOLLOW_roleAssignment_in_effect1264 = frozenset([1])
    FOLLOW_externalEffect_in_effect1268 = frozenset([1])
    FOLLOW_send_in_effect1272 = frozenset([1])
    FOLLOW_receive_in_effect1276 = frozenset([1])
    FOLLOW_invoke_in_effect1280 = frozenset([1])
    FOLLOW_initiate_in_effect1284 = frozenset([1])
    FOLLOW_save_in_effect1288 = frozenset([1])
    FOLLOW_identifier_in_parameter1297 = frozenset([1])
    FOLLOW_contentSet_in_parameter1301 = frozenset([1])
    FOLLOW_contentVar_in_parameter1305 = frozenset([1])
    FOLLOW_HELLO_in_parameter1309 = frozenset([1])
    FOLLOW_LBRACE_in_content1320 = frozenset([19, 31, 32, 42, 86, 122, 123])
    FOLLOW_contentItem_in_content1324 = frozenset([36, 41])
    FOLLOW_COMMA_in_content1327 = frozenset([19, 31, 32, 42, 86])
    FOLLOW_contentItem_in_content1329 = frozenset([36, 41])
    FOLLOW_122_in_content1335 = frozenset([41])
    FOLLOW_123_in_content1339 = frozenset([41])
    FOLLOW_RBRACE_in_content1343 = frozenset([1])
    FOLLOW_contentSet_in_contentItem1378 = frozenset([1])
    FOLLOW_contentVar_in_contentItem1382 = frozenset([1])
    FOLLOW_contentStr_in_contentItem1386 = frozenset([1])
    FOLLOW_rtv_in_contentItem1390 = frozenset([1])
    FOLLOW_upperChar_in_contentSet1399 = frozenset([1])
    FOLLOW_NOT_in_contentVar1407 = frozenset([32, 86])
    FOLLOW_lowerChar_in_contentVar1409 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_contentStr1417 = frozenset([1])
    FOLLOW_NOT_in_rtv1432 = frozenset([42])
    FOLLOW_runTimeVar_in_rtv1434 = frozenset([1])
    FOLLOW_LBRACE_in_conditional1465 = frozenset([67])
    FOLLOW_IF_in_conditional1467 = frozenset([40])
    FOLLOW_requirements_in_conditional1469 = frozenset([109])
    FOLLOW_THEN_in_conditional1471 = frozenset([40])
    FOLLOW_effects_in_conditional1473 = frozenset([41, 53, 54])
    FOLLOW_condelseif_in_conditional1475 = frozenset([41, 53])
    FOLLOW_condelse_in_conditional1478 = frozenset([41])
    FOLLOW_RBRACE_in_conditional1481 = frozenset([1])
    FOLLOW_ELSEIF_in_condelseif1519 = frozenset([40])
    FOLLOW_requirements_in_condelseif1521 = frozenset([109])
    FOLLOW_THEN_in_condelseif1523 = frozenset([40])
    FOLLOW_effects_in_condelseif1525 = frozenset([1, 54])
    FOLLOW_condelseif_in_condelseif1527 = frozenset([1])
    FOLLOW_ELSE_in_condelse1559 = frozenset([40])
    FOLLOW_effects_in_condelse1561 = frozenset([1])
    FOLLOW_LBRACE_in_requirements1578 = frozenset([50, 59, 60, 73, 74, 79, 87, 95, 97, 103, 124])
    FOLLOW_condition_in_requirements1580 = frozenset([29, 41])
    FOLLOW_AND_in_requirements1583 = frozenset([50, 59, 60, 73, 74, 79, 87, 95, 97, 103, 124])
    FOLLOW_condition_in_requirements1585 = frozenset([29, 41])
    FOLLOW_RBRACE_in_requirements1589 = frozenset([1])
    FOLLOW_event_in_condition1618 = frozenset([1])
    FOLLOW_storeInspection_in_condition1622 = frozenset([1])
    FOLLOW_roleInspection_in_condition1626 = frozenset([1])
    FOLLOW_magnitude_in_condition1630 = frozenset([1])
    FOLLOW_storeComparison_in_condition1634 = frozenset([1])
    FOLLOW_dialogueSize_in_condition1638 = frozenset([1])
    FOLLOW_correspondence_in_condition1642 = frozenset([1])
    FOLLOW_relation_in_condition1646 = frozenset([1])
    FOLLOW_currentPlayer_in_condition1650 = frozenset([1])
    FOLLOW_externalCondition_in_condition1654 = frozenset([1])
    FOLLOW_value_in_condition1658 = frozenset([1])
    FOLLOW_INTERACTION_in_interaction1671 = frozenset([40])
    FOLLOW_LBRACE_in_interaction1673 = frozenset([33])
    FOLLOW_moveID_in_interaction1675 = frozenset([36])
    FOLLOW_COMMA_in_interaction1678 = frozenset([42])
    FOLLOW_addressee_in_interaction1680 = frozenset([36])
    FOLLOW_COMMA_in_interaction1685 = frozenset([40])
    FOLLOW_target_in_interaction1687 = frozenset([36])
    FOLLOW_COMMA_in_interaction1692 = frozenset([33])
    FOLLOW_forcetarget_in_interaction1694 = frozenset([36])
    FOLLOW_COMMA_in_interaction1699 = frozenset([19])
    FOLLOW_opener_in_interaction1701 = frozenset([36])
    FOLLOW_COMMA_in_interaction1705 = frozenset([40])
    FOLLOW_ruleBody_in_interaction1707 = frozenset([41])
    FOLLOW_RBRACE_in_interaction1709 = frozenset([1])
    FOLLOW_DOLLAR_in_addressee1752 = frozenset([33])
    FOLLOW_identifier_in_addressee1754 = frozenset([1])
    FOLLOW_content_in_target1786 = frozenset([1])
    FOLLOW_LBRACE_in_target1810 = frozenset([34])
    FOLLOW_schemeApp_in_target1812 = frozenset([36])
    FOLLOW_COMMA_in_target1814 = frozenset([33])
    FOLLOW_schemeID_in_target1816 = frozenset([41])
    FOLLOW_RBRACE_in_target1818 = frozenset([1])
    FOLLOW_LESSTHAN_in_schemeApp1837 = frozenset([40])
    FOLLOW_content_in_schemeApp1839 = frozenset([36])
    FOLLOW_COMMA_in_schemeApp1841 = frozenset([40])
    FOLLOW_content_in_schemeApp1843 = frozenset([35])
    FOLLOW_GREATERTHAN_in_schemeApp1845 = frozenset([1])
    FOLLOW_forceID_in_forcetarget1852 = frozenset([36])
    FOLLOW_COMMA_in_forcetarget1854 = frozenset([40])
    FOLLOW_target_in_forcetarget1856 = frozenset([1])
    FOLLOW_identifier_in_forceID1889 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_opener1902 = frozenset([1])
    FOLLOW_EVENT_in_event1945 = frozenset([38])
    FOLLOW_LPAREN_in_event1947 = frozenset([76, 77, 93, 94])
    FOLLOW_eventpos_in_event1949 = frozenset([36])
    FOLLOW_COMMA_in_event1951 = frozenset([33])
    FOLLOW_moveID_in_event1953 = frozenset([36, 39])
    FOLLOW_COMMA_in_event1956 = frozenset([40])
    FOLLOW_content_in_event1958 = frozenset([36, 39])
    FOLLOW_COMMA_in_event1964 = frozenset([17, 18, 33])
    FOLLOW_user_in_event1966 = frozenset([36, 39])
    FOLLOW_COMMA_in_event1971 = frozenset([40])
    FOLLOW_requirements_in_event1973 = frozenset([39])
    FOLLOW_RPAREN_in_event1977 = frozenset([1])
    FOLLOW_set_in_eventpos2030 = frozenset([1])
    FOLLOW_INSPECT_in_storeInspection2054 = frozenset([38])
    FOLLOW_LPAREN_in_storeInspection2056 = frozenset([68, 69, 89, 90, 110, 111])
    FOLLOW_storepos_in_storeInspection2058 = frozenset([36])
    FOLLOW_COMMA_in_storeInspection2060 = frozenset([34, 40])
    FOLLOW_commitment_in_storeInspection2062 = frozenset([36])
    FOLLOW_COMMA_in_storeInspection2064 = frozenset([33])
    FOLLOW_storeName_in_storeInspection2066 = frozenset([36, 39])
    FOLLOW_COMMA_in_storeInspection2069 = frozenset([17, 18, 33])
    FOLLOW_user_in_storeInspection2071 = frozenset([36, 39])
    FOLLOW_COMMA_in_storeInspection2076 = frozenset([26, 51, 94])
    FOLLOW_INITIAL_in_storeInspection2079 = frozenset([39])
    FOLLOW_PAST_in_storeInspection2083 = frozenset([39])
    FOLLOW_CURRENT_in_storeInspection2087 = frozenset([39])
    FOLLOW_RPAREN_in_storeInspection2092 = frozenset([1])
    FOLLOW_set_in_storepos2159 = frozenset([1])
    FOLLOW_INROLE_in_roleInspection2192 = frozenset([38])
    FOLLOW_LPAREN_in_roleInspection2194 = frozenset([33, 42])
    FOLLOW_playerID_in_roleInspection2196 = frozenset([36])
    FOLLOW_COMMA_in_roleInspection2198 = frozenset([17, 18, 33])
    FOLLOW_role_in_roleInspection2200 = frozenset([39])
    FOLLOW_RPAREN_in_roleInspection2202 = frozenset([1])
    FOLLOW_SIZE_in_magnitude2246 = frozenset([38])
    FOLLOW_LPAREN_in_magnitude2248 = frozenset([33, 78])
    FOLLOW_container_in_magnitude2250 = frozenset([36])
    FOLLOW_COMMA_in_magnitude2252 = frozenset([33, 42])
    FOLLOW_playerID_in_magnitude2254 = frozenset([36])
    FOLLOW_COMMA_in_magnitude2256 = frozenset([30, 55, 56])
    FOLLOW_containersize_in_magnitude2258 = frozenset([39])
    FOLLOW_RPAREN_in_magnitude2260 = frozenset([1])
    FOLLOW_storeName_in_container2306 = frozenset([1])
    FOLLOW_LEGALMOVES_in_container2310 = frozenset([1])
    FOLLOW_set_in_containersize2322 = frozenset([1])
    FOLLOW_MAGNITUDE_in_storeComparison2342 = frozenset([38])
    FOLLOW_LPAREN_in_storeComparison2344 = frozenset([33])
    FOLLOW_store1_in_storeComparison2346 = frozenset([36])
    FOLLOW_COMMA_in_storeComparison2348 = frozenset([17, 18, 20, 33])
    FOLLOW_user1_in_storeComparison2350 = frozenset([36])
    FOLLOW_COMMA_in_storeComparison2352 = frozenset([57, 58, 64, 104])
    FOLLOW_comparison_in_storeComparison2354 = frozenset([36])
    FOLLOW_COMMA_in_storeComparison2356 = frozenset([33])
    FOLLOW_store2_in_storeComparison2358 = frozenset([36])
    FOLLOW_COMMA_in_storeComparison2360 = frozenset([17, 18, 20, 33])
    FOLLOW_user2_in_storeComparison2362 = frozenset([39])
    FOLLOW_RPAREN_in_storeComparison2364 = frozenset([1])
    FOLLOW_set_in_comparison2412 = frozenset([1])
    FOLLOW_storeName_in_store12444 = frozenset([1])
    FOLLOW_user_in_user12463 = frozenset([1])
    FOLLOW_SHARED_in_user12467 = frozenset([1])
    FOLLOW_storeName_in_store22485 = frozenset([1])
    FOLLOW_user_in_user22504 = frozenset([1])
    FOLLOW_SHARED_in_user22508 = frozenset([1])
    FOLLOW_NUMTURNS_in_dialogueSize2521 = frozenset([38])
    FOLLOW_LPAREN_in_dialogueSize2523 = frozenset([33])
    FOLLOW_systemID_in_dialogueSize2525 = frozenset([36])
    FOLLOW_COMMA_in_dialogueSize2527 = frozenset([30, 42])
    FOLLOW_number_in_dialogueSize2530 = frozenset([39])
    FOLLOW_runTimeVar_in_dialogueSize2534 = frozenset([39])
    FOLLOW_RPAREN_in_dialogueSize2537 = frozenset([1])
    FOLLOW_CORRESPONDS_in_correspondence2580 = frozenset([38])
    FOLLOW_LPAREN_in_correspondence2582 = frozenset([34, 40])
    FOLLOW_argument_in_correspondence2584 = frozenset([36])
    FOLLOW_COMMA_in_correspondence2586 = frozenset([33])
    FOLLOW_schemeID_in_correspondence2588 = frozenset([39])
    FOLLOW_RPAREN_in_correspondence2590 = frozenset([1])
    FOLLOW_RELATION_in_relation2635 = frozenset([38])
    FOLLOW_LPAREN_in_relation2637 = frozenset([34, 40])
    FOLLOW_content_in_relation2640 = frozenset([36])
    FOLLOW_argument_in_relation2644 = frozenset([36])
    FOLLOW_COMMA_in_relation2647 = frozenset([47, 115])
    FOLLOW_BACKING_in_relation2650 = frozenset([36])
    FOLLOW_WARRANT_in_relation2654 = frozenset([36])
    FOLLOW_COMMA_in_relation2657 = frozenset([34, 40])
    FOLLOW_content_in_relation2660 = frozenset([39])
    FOLLOW_argument_in_relation2664 = frozenset([39])
    FOLLOW_RPAREN_in_relation2667 = frozenset([1])
    FOLLOW_PLAYER_in_currentPlayer2709 = frozenset([38])
    FOLLOW_LPAREN_in_currentPlayer2711 = frozenset([17, 18, 33])
    FOLLOW_user_in_currentPlayer2713 = frozenset([39])
    FOLLOW_RPAREN_in_currentPlayer2715 = frozenset([1])
    FOLLOW_EXTCONDITION_in_externalCondition2770 = frozenset([38])
    FOLLOW_LPAREN_in_externalCondition2772 = frozenset([33])
    FOLLOW_identifier_in_externalCondition2774 = frozenset([36])
    FOLLOW_COMMA_in_externalCondition2777 = frozenset([40])
    FOLLOW_content_in_externalCondition2779 = frozenset([36, 39])
    FOLLOW_RPAREN_in_externalCondition2783 = frozenset([1])
    FOLLOW_124_in_value2834 = frozenset([38])
    FOLLOW_LPAREN_in_value2836 = frozenset([19, 40])
    FOLLOW_value1_in_value2838 = frozenset([36, 39])
    FOLLOW_COMMA_in_value2841 = frozenset([19, 42, 86])
    FOLLOW_NOT_in_value2843 = frozenset([19, 42, 86])
    FOLLOW_value2_in_value2846 = frozenset([39])
    FOLLOW_RPAREN_in_value2849 = frozenset([1])
    FOLLOW_content_in_value12897 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_value12901 = frozenset([1])
    FOLLOW_valueVar_in_value22921 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_value22925 = frozenset([1])
    FOLLOW_runTimeVar_in_valueVar2944 = frozenset([1])
    FOLLOW_role_in_user3037 = frozenset([1])
    FOLLOW_identifier_in_schemeID3055 = frozenset([1])
    FOLLOW_content_in_commitment3070 = frozenset([1])
    FOLLOW_locution_in_commitment3074 = frozenset([1])
    FOLLOW_argument_in_commitment3078 = frozenset([1])
    FOLLOW_LESSTHAN_in_locution3096 = frozenset([33])
    FOLLOW_moveID_in_locution3098 = frozenset([36])
    FOLLOW_COMMA_in_locution3100 = frozenset([40])
    FOLLOW_content_in_locution3102 = frozenset([35])
    FOLLOW_GREATERTHAN_in_locution3104 = frozenset([1])
    FOLLOW_LESSTHAN_in_argument3121 = frozenset([32, 86])
    FOLLOW_conclusion_in_argument3123 = frozenset([36])
    FOLLOW_COMMA_in_argument3125 = frozenset([40])
    FOLLOW_premises_in_argument3127 = frozenset([35])
    FOLLOW_GREATERTHAN_in_argument3129 = frozenset([1])
    FOLLOW_LBRACE_in_premises3145 = frozenset([32, 86])
    FOLLOW_contentVar_in_premises3147 = frozenset([36, 41])
    FOLLOW_COMMA_in_premises3150 = frozenset([32, 86])
    FOLLOW_contentVar_in_premises3152 = frozenset([36, 41])
    FOLLOW_RBRACE_in_premises3156 = frozenset([1])
    FOLLOW_contentVar_in_conclusion3170 = frozenset([1])
    FOLLOW_MOVE_in_move3190 = frozenset([38])
    FOLLOW_LPAREN_in_move3192 = frozenset([45, 52])
    FOLLOW_moveaction_in_move3194 = frozenset([36])
    FOLLOW_COMMA_in_move3196 = frozenset([63, 85])
    FOLLOW_movetime_in_move3198 = frozenset([36])
    FOLLOW_COMMA_in_move3200 = frozenset([33])
    FOLLOW_moveID_in_move3202 = frozenset([36, 39])
    FOLLOW_COMMA_in_move3205 = frozenset([42])
    FOLLOW_addressee_in_move3207 = frozenset([36, 39])
    FOLLOW_COMMA_in_move3212 = frozenset([40])
    FOLLOW_content_in_move3214 = frozenset([36, 39])
    FOLLOW_COMMA_in_move3219 = frozenset([17, 18, 33])
    FOLLOW_user_in_move3221 = frozenset([36, 39])
    FOLLOW_COMMA_in_move3226 = frozenset([40])
    FOLLOW_requirements_in_move3228 = frozenset([36, 39])
    FOLLOW_COMMA_in_move3233 = frozenset([19])
    FOLLOW_opener_in_move3235 = frozenset([39])
    FOLLOW_RPAREN_in_move3239 = frozenset([1])
    FOLLOW_set_in_moveaction3290 = frozenset([1])
    FOLLOW_set_in_movetime3308 = frozenset([1])
    FOLLOW_STORE_in_storeOp3328 = frozenset([38])
    FOLLOW_LPAREN_in_storeOp3330 = frozenset([45, 56, 98])
    FOLLOW_storeaction_in_storeOp3332 = frozenset([36])
    FOLLOW_COMMA_in_storeOp3334 = frozenset([40])
    FOLLOW_content_in_storeOp3336 = frozenset([36])
    FOLLOW_COMMA_in_storeOp3338 = frozenset([33])
    FOLLOW_storeName_in_storeOp3340 = frozenset([36])
    FOLLOW_COMMA_in_storeOp3342 = frozenset([17, 18, 33])
    FOLLOW_user_in_storeOp3344 = frozenset([39])
    FOLLOW_RPAREN_in_storeOp3346 = frozenset([1])
    FOLLOW_set_in_storeaction3383 = frozenset([1])
    FOLLOW_STATUS_in_statusUpdate3402 = frozenset([38])
    FOLLOW_LPAREN_in_statusUpdate3404 = frozenset([44, 49, 70, 71, 72, 108])
    FOLLOW_status_in_statusUpdate3406 = frozenset([36])
    FOLLOW_COMMA_in_statusUpdate3408 = frozenset([33])
    FOLLOW_sysgame_in_statusUpdate3410 = frozenset([39])
    FOLLOW_RPAREN_in_statusUpdate3412 = frozenset([1])
    FOLLOW_set_in_status3450 = frozenset([1])
    FOLLOW_assignment_in_roleAssignment3480 = frozenset([1])
    FOLLOW_unassignment_in_roleAssignment3484 = frozenset([1])
    FOLLOW_ASSIGN_in_assignment3492 = frozenset([38])
    FOLLOW_LPAREN_in_assignment3494 = frozenset([17, 18, 33])
    FOLLOW_user_in_assignment3496 = frozenset([36])
    FOLLOW_COMMA_in_assignment3498 = frozenset([17, 18, 33])
    FOLLOW_role_in_assignment3500 = frozenset([39])
    FOLLOW_RPAREN_in_assignment3502 = frozenset([1])
    FOLLOW_125_in_unassignment3547 = frozenset([38])
    FOLLOW_LPAREN_in_unassignment3549 = frozenset([17, 18, 33])
    FOLLOW_user_in_unassignment3551 = frozenset([36])
    FOLLOW_COMMA_in_unassignment3553 = frozenset([17, 18, 33])
    FOLLOW_role_in_unassignment3555 = frozenset([39])
    FOLLOW_RPAREN_in_unassignment3557 = frozenset([1])
    FOLLOW_EXTEFFECT_in_externalEffect3605 = frozenset([38])
    FOLLOW_LPAREN_in_externalEffect3607 = frozenset([33])
    FOLLOW_identifier_in_externalEffect3609 = frozenset([36, 39])
    FOLLOW_COMMA_in_externalEffect3612 = frozenset([40])
    FOLLOW_content_in_externalEffect3614 = frozenset([39])
    FOLLOW_RPAREN_in_externalEffect3618 = frozenset([1])
    FOLLOW_126_in_send3667 = frozenset([38])
    FOLLOW_LPAREN_in_send3669 = frozenset([33])
    FOLLOW_identifier_in_send3671 = frozenset([36, 39])
    FOLLOW_COMMA_in_send3674 = frozenset([40])
    FOLLOW_postVars_in_send3676 = frozenset([36, 39])
    FOLLOW_RPAREN_in_send3680 = frozenset([1])
    FOLLOW_LBRACE_in_postVars3714 = frozenset([32, 33])
    FOLLOW_postVar_in_postVars3716 = frozenset([36, 41])
    FOLLOW_COMMA_in_postVars3719 = frozenset([32, 33])
    FOLLOW_postVar_in_postVars3721 = frozenset([36, 41])
    FOLLOW_RBRACE_in_postVars3725 = frozenset([1])
    FOLLOW_varLabel_in_postVar3756 = frozenset([37])
    FOLLOW_COLON_in_postVar3758 = frozenset([19, 32, 40, 42, 86])
    FOLLOW_contentVar_in_postVar3761 = frozenset([1])
    FOLLOW_STRINGLITERAL_in_postVar3765 = frozenset([1])
    FOLLOW_runTimeVar_in_postVar3769 = frozenset([1])
    FOLLOW_content_in_postVar3773 = frozenset([1])
    FOLLOW_127_in_receive3823 = frozenset([38])
    FOLLOW_LPAREN_in_receive3825 = frozenset([33])
    FOLLOW_identifier_in_receive3827 = frozenset([36, 39])
    FOLLOW_COMMA_in_receive3830 = frozenset([42])
    FOLLOW_runTimeVar_in_receive3832 = frozenset([39])
    FOLLOW_RPAREN_in_receive3835 = frozenset([1])
    FOLLOW_128_in_invoke3878 = frozenset([38])
    FOLLOW_LPAREN_in_invoke3880 = frozenset([33])
    FOLLOW_identifier_in_invoke3882 = frozenset([36, 39])
    FOLLOW_COMMA_in_invoke3885 = frozenset([40])
    FOLLOW_postVars_in_invoke3887 = frozenset([36, 39])
    FOLLOW_RPAREN_in_invoke3890 = frozenset([1])
    FOLLOW_INITIATE_in_initiate3917 = frozenset([38])
    FOLLOW_LPAREN_in_initiate3919 = frozenset([129])
    FOLLOW_129_in_initiate3921 = frozenset([37])
    FOLLOW_COLON_in_initiate3923 = frozenset([19])
    FOLLOW_STRINGLITERAL_in_initiate3925 = frozenset([39])
    FOLLOW_RPAREN_in_initiate3927 = frozenset([1])
    FOLLOW_130_in_save3959 = frozenset([38])
    FOLLOW_LPAREN_in_save3961 = frozenset([19, 40])
    FOLLOW_content_in_save3964 = frozenset([36])
    FOLLOW_STRINGLITERAL_in_save3966 = frozenset([36])
    FOLLOW_COMMA_in_save3969 = frozenset([42])
    FOLLOW_runTimeVar_in_save3971 = frozenset([39])
    FOLLOW_RPAREN_in_save3972 = frozenset([1])
    FOLLOW_identifier_in_moveID4013 = frozenset([1])
    FOLLOW_identifier_in_sysgame4026 = frozenset([1])
    FOLLOW_UpperChar_in_upperChar4038 = frozenset([1])
    FOLLOW_LowerChar_in_lowerChar4047 = frozenset([1])
    FOLLOW_Identifier_in_identifier4056 = frozenset([1])
    FOLLOW_Number_in_number4066 = frozenset([1])
    FOLLOW_Identifier_in_varLabel4080 = frozenset([1])
    FOLLOW_LowerChar_in_varLabel4084 = frozenset([1, 32])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("dgdlLexer", dgdlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
