# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 dgdl.g 2019-05-31 16:33:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class dgdlLexer(Lexer):

    grammarFileName = "dgdl.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(dgdlLexer, self).__init__(input, state)


        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "T__119"
    def mT__119(self, ):

        try:
            _type = T__119
            _channel = DEFAULT_CHANNEL

            # dgdl.g:7:8: ( 'uri' )
            # dgdl.g:7:10: 'uri'
            pass 
            self.match("uri")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__119"



    # $ANTLR start "T__120"
    def mT__120(self, ):

        try:
            _type = T__120
            _channel = DEFAULT_CHANNEL

            # dgdl.g:8:8: ( 'plugin' )
            # dgdl.g:8:10: 'plugin'
            pass 
            self.match("plugin")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__120"



    # $ANTLR start "T__121"
    def mT__121(self, ):

        try:
            _type = T__121
            _channel = DEFAULT_CHANNEL

            # dgdl.g:9:8: ( 'name' )
            # dgdl.g:9:10: 'name'
            pass 
            self.match("name")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__121"



    # $ANTLR start "T__122"
    def mT__122(self, ):

        try:
            _type = T__122
            _channel = DEFAULT_CHANNEL

            # dgdl.g:10:8: ( '$...' )
            # dgdl.g:10:10: '$...'
            pass 
            self.match("$...")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__122"



    # $ANTLR start "T__123"
    def mT__123(self, ):

        try:
            _type = T__123
            _channel = DEFAULT_CHANNEL

            # dgdl.g:11:8: ( '...' )
            # dgdl.g:11:10: '...'
            pass 
            self.match("...")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__123"



    # $ANTLR start "T__124"
    def mT__124(self, ):

        try:
            _type = T__124
            _channel = DEFAULT_CHANNEL

            # dgdl.g:12:8: ( 'value' )
            # dgdl.g:12:10: 'value'
            pass 
            self.match("value")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__124"



    # $ANTLR start "T__125"
    def mT__125(self, ):

        try:
            _type = T__125
            _channel = DEFAULT_CHANNEL

            # dgdl.g:13:8: ( 'unassign' )
            # dgdl.g:13:10: 'unassign'
            pass 
            self.match("unassign")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__125"



    # $ANTLR start "T__126"
    def mT__126(self, ):

        try:
            _type = T__126
            _channel = DEFAULT_CHANNEL

            # dgdl.g:14:8: ( 'send' )
            # dgdl.g:14:10: 'send'
            pass 
            self.match("send")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__126"



    # $ANTLR start "T__127"
    def mT__127(self, ):

        try:
            _type = T__127
            _channel = DEFAULT_CHANNEL

            # dgdl.g:15:8: ( 'receive' )
            # dgdl.g:15:10: 'receive'
            pass 
            self.match("receive")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__127"



    # $ANTLR start "T__128"
    def mT__128(self, ):

        try:
            _type = T__128
            _channel = DEFAULT_CHANNEL

            # dgdl.g:16:8: ( 'invoke' )
            # dgdl.g:16:10: 'invoke'
            pass 
            self.match("invoke")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__128"



    # $ANTLR start "T__129"
    def mT__129(self, ):

        try:
            _type = T__129
            _channel = DEFAULT_CHANNEL

            # dgdl.g:17:8: ( 'protocol' )
            # dgdl.g:17:10: 'protocol'
            pass 
            self.match("protocol")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__129"



    # $ANTLR start "T__130"
    def mT__130(self, ):

        try:
            _type = T__130
            _channel = DEFAULT_CHANNEL

            # dgdl.g:18:8: ( 'save' )
            # dgdl.g:18:10: 'save'
            pass 
            self.match("save")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__130"



    # $ANTLR start "Identifier"
    def mIdentifier(self, ):

        try:
            _type = Identifier
            _channel = DEFAULT_CHANNEL

            # dgdl.g:266:14: ( UpperChar ( UpperChar | LowerChar | Number )+ )
            # dgdl.g:266:16: UpperChar ( UpperChar | LowerChar | Number )+
            pass 
            self.mUpperChar()
            # dgdl.g:266:26: ( UpperChar | LowerChar | Number )+
            cnt1 = 0
            while True: #loop1
                alt1 = 4
                LA1 = self.input.LA(1)
                if LA1 == 65 or LA1 == 66 or LA1 == 67 or LA1 == 68 or LA1 == 69 or LA1 == 70 or LA1 == 71 or LA1 == 72 or LA1 == 73 or LA1 == 74 or LA1 == 75 or LA1 == 76 or LA1 == 77 or LA1 == 78 or LA1 == 79 or LA1 == 80 or LA1 == 81 or LA1 == 82 or LA1 == 83 or LA1 == 84 or LA1 == 85 or LA1 == 86 or LA1 == 87 or LA1 == 88 or LA1 == 89 or LA1 == 90:
                    alt1 = 1
                elif LA1 == 97 or LA1 == 98 or LA1 == 99 or LA1 == 100 or LA1 == 101 or LA1 == 102 or LA1 == 103 or LA1 == 104 or LA1 == 105 or LA1 == 106 or LA1 == 107 or LA1 == 108 or LA1 == 109 or LA1 == 110 or LA1 == 111 or LA1 == 112 or LA1 == 113 or LA1 == 114 or LA1 == 115 or LA1 == 116 or LA1 == 117 or LA1 == 118 or LA1 == 119 or LA1 == 120 or LA1 == 121 or LA1 == 122:
                    alt1 = 2
                elif LA1 == 48 or LA1 == 49 or LA1 == 50 or LA1 == 51 or LA1 == 52 or LA1 == 53 or LA1 == 54 or LA1 == 55 or LA1 == 56 or LA1 == 57:
                    alt1 = 3

                if alt1 == 1:
                    # dgdl.g:266:27: UpperChar
                    pass 
                    self.mUpperChar()


                elif alt1 == 2:
                    # dgdl.g:266:39: LowerChar
                    pass 
                    self.mLowerChar()


                elif alt1 == 3:
                    # dgdl.g:266:51: Number
                    pass 
                    self.mNumber()


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Identifier"



    # $ANTLR start "LowerChar"
    def mLowerChar(self, ):

        try:
            _type = LowerChar
            _channel = DEFAULT_CHANNEL

            # dgdl.g:267:13: ( 'a' .. 'z' )
            # dgdl.g:267:15: 'a' .. 'z'
            pass 
            self.matchRange(97, 122)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LowerChar"



    # $ANTLR start "Number"
    def mNumber(self, ):

        try:
            _type = Number
            _channel = DEFAULT_CHANNEL

            # dgdl.g:268:11: ( '0' .. '9' ( '0' .. '9' )* )
            # dgdl.g:268:13: '0' .. '9' ( '0' .. '9' )*
            pass 
            self.matchRange(48, 57)
            # dgdl.g:268:22: ( '0' .. '9' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # dgdl.g:268:22: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop2



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Number"



    # $ANTLR start "UpperChar"
    def mUpperChar(self, ):

        try:
            _type = UpperChar
            _channel = DEFAULT_CHANNEL

            # dgdl.g:269:13: ( 'A' .. 'Z' )
            # dgdl.g:269:15: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UpperChar"



    # $ANTLR start "LESSTHAN"
    def mLESSTHAN(self, ):

        try:
            _type = LESSTHAN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:278:17: ( '<' )
            # dgdl.g:278:19: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESSTHAN"



    # $ANTLR start "GREATERTHAN"
    def mGREATERTHAN(self, ):

        try:
            _type = GREATERTHAN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:279:17: ( '>' )
            # dgdl.g:279:19: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATERTHAN"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # dgdl.g:280:17: ( ',' )
            # dgdl.g:280:19: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # dgdl.g:281:17: ( ':' )
            # dgdl.g:281:19: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:282:17: ( '(' )
            # dgdl.g:282:19: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:283:17: ( ')' )
            # dgdl.g:283:19: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACE"
    def mLBRACE(self, ):

        try:
            _type = LBRACE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:284:17: ( '{' )
            # dgdl.g:284:19: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACE"



    # $ANTLR start "RBRACE"
    def mRBRACE(self, ):

        try:
            _type = RBRACE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:285:17: ( '}' )
            # dgdl.g:285:19: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACE"



    # $ANTLR start "DOLLAR"
    def mDOLLAR(self, ):

        try:
            _type = DOLLAR
            _channel = DEFAULT_CHANNEL

            # dgdl.g:286:17: ( '$' )
            # dgdl.g:286:19: '$'
            pass 
            self.match(36)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOLLAR"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # dgdl.g:287:17: ( '&' )
            # dgdl.g:287:19: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # dgdl.g:288:17: ( '||' )
            # dgdl.g:288:19: '||'
            pass 
            self.match("||")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "ACTIVE"
    def mACTIVE(self, ):

        try:
            _type = ACTIVE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:289:17: ( 'active' )
            # dgdl.g:289:19: 'active'
            pass 
            self.match("active")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ACTIVE"



    # $ANTLR start "ADD"
    def mADD(self, ):

        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # dgdl.g:290:17: ( 'add' )
            # dgdl.g:290:19: 'add'
            pass 
            self.match("add")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ADD"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:291:17: ( 'assign' )
            # dgdl.g:291:19: 'assign'
            pass 
            self.match("assign")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "BACKING"
    def mBACKING(self, ):

        try:
            _type = BACKING
            _channel = DEFAULT_CHANNEL

            # dgdl.g:292:17: ( 'backing' )
            # dgdl.g:292:19: 'backing'
            pass 
            self.match("backing")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BACKING"



    # $ANTLR start "BACKTRACK"
    def mBACKTRACK(self, ):

        try:
            _type = BACKTRACK
            _channel = DEFAULT_CHANNEL

            # dgdl.g:293:17: ( 'backtrack' )
            # dgdl.g:293:19: 'backtrack'
            pass 
            self.match("backtrack")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BACKTRACK"



    # $ANTLR start "COMPLETE"
    def mCOMPLETE(self, ):

        try:
            _type = COMPLETE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:294:17: ( 'complete' )
            # dgdl.g:294:19: 'complete'
            pass 
            self.match("complete")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMPLETE"



    # $ANTLR start "CORRESPONDS"
    def mCORRESPONDS(self, ):

        try:
            _type = CORRESPONDS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:295:17: ( 'corresponds' )
            # dgdl.g:295:19: 'corresponds'
            pass 
            self.match("corresponds")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CORRESPONDS"



    # $ANTLR start "CURRENT"
    def mCURRENT(self, ):

        try:
            _type = CURRENT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:296:17: ( 'current' )
            # dgdl.g:296:19: 'current'
            pass 
            self.match("current")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CURRENT"



    # $ANTLR start "DELETE"
    def mDELETE(self, ):

        try:
            _type = DELETE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:297:17: ( 'delete' )
            # dgdl.g:297:19: 'delete'
            pass 
            self.match("delete")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DELETE"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:298:17: ( 'else' )
            # dgdl.g:298:19: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "ELSEIF"
    def mELSEIF(self, ):

        try:
            _type = ELSEIF
            _channel = DEFAULT_CHANNEL

            # dgdl.g:299:17: ( 'elseif' )
            # dgdl.g:299:19: 'elseif'
            pass 
            self.match("elseif")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSEIF"



    # $ANTLR start "NOTEMPTY"
    def mNOTEMPTY(self, ):

        try:
            _type = NOTEMPTY
            _channel = DEFAULT_CHANNEL

            # dgdl.g:300:17: ( '!empty' )
            # dgdl.g:300:19: '!empty'
            pass 
            self.match("!empty")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTEMPTY"



    # $ANTLR start "EMPTY"
    def mEMPTY(self, ):

        try:
            _type = EMPTY
            _channel = DEFAULT_CHANNEL

            # dgdl.g:301:17: ( 'empty' )
            # dgdl.g:301:19: 'empty'
            pass 
            self.match("empty")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY"



    # $ANTLR start "NOTEQUAL"
    def mNOTEQUAL(self, ):

        try:
            _type = NOTEQUAL
            _channel = DEFAULT_CHANNEL

            # dgdl.g:302:17: ( '!equal' )
            # dgdl.g:302:19: '!equal'
            pass 
            self.match("!equal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTEQUAL"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # dgdl.g:303:17: ( 'equal' )
            # dgdl.g:303:19: 'equal'
            pass 
            self.match("equal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "EVENT"
    def mEVENT(self, ):

        try:
            _type = EVENT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:304:17: ( 'event' )
            # dgdl.g:304:19: 'event'
            pass 
            self.match("event")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EVENT"



    # $ANTLR start "EXTCONDITION"
    def mEXTCONDITION(self, ):

        try:
            _type = EXTCONDITION
            _channel = DEFAULT_CHANNEL

            # dgdl.g:305:17: ( 'extCondition' )
            # dgdl.g:305:19: 'extCondition'
            pass 
            self.match("extCondition")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTCONDITION"



    # $ANTLR start "EXTEFFECT"
    def mEXTEFFECT(self, ):

        try:
            _type = EXTEFFECT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:306:17: ( 'extEffect' )
            # dgdl.g:306:19: 'extEffect'
            pass 
            self.match("extEffect")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTEFFECT"



    # $ANTLR start "EXTURI"
    def mEXTURI(self, ):

        try:
            _type = EXTURI
            _channel = DEFAULT_CHANNEL

            # dgdl.g:307:17: ( 'extURI' )
            # dgdl.g:307:19: 'extURI'
            pass 
            self.match("extURI")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTURI"



    # $ANTLR start "FUTURE"
    def mFUTURE(self, ):

        try:
            _type = FUTURE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:308:17: ( 'future' )
            # dgdl.g:308:19: 'future'
            pass 
            self.match("future")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FUTURE"



    # $ANTLR start "GREATER"
    def mGREATER(self, ):

        try:
            _type = GREATER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:309:17: ( 'greater' )
            # dgdl.g:309:19: 'greater'
            pass 
            self.match("greater")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER"



    # $ANTLR start "HELLO"
    def mHELLO(self, ):

        try:
            _type = HELLO
            _channel = DEFAULT_CHANNEL

            # dgdl.g:310:17: ( 'hello' )
            # dgdl.g:310:19: 'hello'
            pass 
            self.match("hello")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HELLO"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # dgdl.g:311:17: ( 'id' )
            # dgdl.g:311:19: 'id'
            pass 
            self.match("id")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # dgdl.g:312:17: ( 'if' )
            # dgdl.g:312:19: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "NOTIN"
    def mNOTIN(self, ):

        try:
            _type = NOTIN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:313:17: ( '!in' )
            # dgdl.g:313:19: '!in'
            pass 
            self.match("!in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTIN"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:314:17: ( 'in' )
            # dgdl.g:314:19: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "INACTIVE"
    def mINACTIVE(self, ):

        try:
            _type = INACTIVE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:315:17: ( 'inactive' )
            # dgdl.g:315:19: 'inactive'
            pass 
            self.match("inactive")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INACTIVE"



    # $ANTLR start "INCOMPLETE"
    def mINCOMPLETE(self, ):

        try:
            _type = INCOMPLETE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:316:17: ( 'incomplete' )
            # dgdl.g:316:19: 'incomplete'
            pass 
            self.match("incomplete")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INCOMPLETE"



    # $ANTLR start "INITIAL"
    def mINITIAL(self, ):

        try:
            _type = INITIAL
            _channel = DEFAULT_CHANNEL

            # dgdl.g:317:17: ( 'initial' )
            # dgdl.g:317:19: 'initial'
            pass 
            self.match("initial")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INITIAL"



    # $ANTLR start "INITIATE"
    def mINITIATE(self, ):

        try:
            _type = INITIATE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:318:17: ( 'initiate' )
            # dgdl.g:318:19: 'initiate'
            pass 
            self.match("initiate")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INITIATE"



    # $ANTLR start "INROLE"
    def mINROLE(self, ):

        try:
            _type = INROLE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:319:17: ( 'inrole' )
            # dgdl.g:319:19: 'inrole'
            pass 
            self.match("inrole")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INROLE"



    # $ANTLR start "INSPECT"
    def mINSPECT(self, ):

        try:
            _type = INSPECT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:320:17: ( 'inspect' )
            # dgdl.g:320:19: 'inspect'
            pass 
            self.match("inspect")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSPECT"



    # $ANTLR start "INTERACTION"
    def mINTERACTION(self, ):

        try:
            _type = INTERACTION
            _channel = DEFAULT_CHANNEL

            # dgdl.g:321:17: ( 'interaction' )
            # dgdl.g:321:19: 'interaction'
            pass 
            self.match("interaction")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTERACTION"



    # $ANTLR start "NOTLAST"
    def mNOTLAST(self, ):

        try:
            _type = NOTLAST
            _channel = DEFAULT_CHANNEL

            # dgdl.g:322:17: ( '!last' )
            # dgdl.g:322:19: '!last'
            pass 
            self.match("!last")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTLAST"



    # $ANTLR start "LAST"
    def mLAST(self, ):

        try:
            _type = LAST
            _channel = DEFAULT_CHANNEL

            # dgdl.g:323:17: ( 'last' )
            # dgdl.g:323:19: 'last'
            pass 
            self.match("last")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LAST"



    # $ANTLR start "LEGALMOVES"
    def mLEGALMOVES(self, ):

        try:
            _type = LEGALMOVES
            _channel = DEFAULT_CHANNEL

            # dgdl.g:324:17: ( 'legalmoves' )
            # dgdl.g:324:19: 'legalmoves'
            pass 
            self.match("legalmoves")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEGALMOVES"



    # $ANTLR start "LIBERAL"
    def mLIBERAL(self, ):

        try:
            _type = LIBERAL
            _channel = DEFAULT_CHANNEL

            # dgdl.g:325:17: ( 'liberal' )
            # dgdl.g:325:19: 'liberal'
            pass 
            self.match("liberal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIBERAL"



    # $ANTLR start "LISTENER"
    def mLISTENER(self, ):

        try:
            _type = LISTENER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:326:17: ( 'listener' )
            # dgdl.g:326:19: 'listener'
            pass 
            self.match("listener")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LISTENER"



    # $ANTLR start "MAGNITUDE"
    def mMAGNITUDE(self, ):

        try:
            _type = MAGNITUDE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:327:17: ( 'magnitude' )
            # dgdl.g:327:19: 'magnitude'
            pass 
            self.match("magnitude")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAGNITUDE"



    # $ANTLR start "MAX"
    def mMAX(self, ):

        try:
            _type = MAX
            _channel = DEFAULT_CHANNEL

            # dgdl.g:328:17: ( 'max' )
            # dgdl.g:328:19: 'max'
            pass 
            self.match("max")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAX"



    # $ANTLR start "MAXTURNS"
    def mMAXTURNS(self, ):

        try:
            _type = MAXTURNS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:329:17: ( 'maxturns' )
            # dgdl.g:329:19: 'maxturns'
            pass 
            self.match("maxturns")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAXTURNS"



    # $ANTLR start "MIN"
    def mMIN(self, ):

        try:
            _type = MIN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:330:17: ( 'min' )
            # dgdl.g:330:19: 'min'
            pass 
            self.match("min")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MIN"



    # $ANTLR start "MOVE"
    def mMOVE(self, ):

        try:
            _type = MOVE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:331:17: ( 'move' )
            # dgdl.g:331:19: 'move'
            pass 
            self.match("move")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOVE"



    # $ANTLR start "MOVEWISE"
    def mMOVEWISE(self, ):

        try:
            _type = MOVEWISE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:332:17: ( 'movewise' )
            # dgdl.g:332:19: 'movewise'
            pass 
            self.match("movewise")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOVEWISE"



    # $ANTLR start "MULTIPLE"
    def mMULTIPLE(self, ):

        try:
            _type = MULTIPLE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:333:17: ( 'multiple' )
            # dgdl.g:333:19: 'multiple'
            pass 
            self.match("multiple")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULTIPLE"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):

        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:334:17: ( 'next' )
            # dgdl.g:334:19: 'next'
            pass 
            self.match("next")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:335:17: ( '!' )
            # dgdl.g:335:19: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NUMTURNS"
    def mNUMTURNS(self, ):

        try:
            _type = NUMTURNS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:336:17: ( 'numturns' )
            # dgdl.g:336:19: 'numturns'
            pass 
            self.match("numturns")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMTURNS"



    # $ANTLR start "OFF"
    def mOFF(self, ):

        try:
            _type = OFF
            _channel = DEFAULT_CHANNEL

            # dgdl.g:337:17: ( 'off' )
            # dgdl.g:337:19: 'off'
            pass 
            self.match("off")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OFF"



    # $ANTLR start "NOTON"
    def mNOTON(self, ):

        try:
            _type = NOTON
            _channel = DEFAULT_CHANNEL

            # dgdl.g:338:17: ( '!on' )
            # dgdl.g:338:19: '!on'
            pass 
            self.match("!on")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTON"



    # $ANTLR start "ON"
    def mON(self, ):

        try:
            _type = ON
            _channel = DEFAULT_CHANNEL

            # dgdl.g:339:17: ( 'on' )
            # dgdl.g:339:19: 'on'
            pass 
            self.match("on")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ON"



    # $ANTLR start "ORDERING"
    def mORDERING(self, ):

        try:
            _type = ORDERING
            _channel = DEFAULT_CHANNEL

            # dgdl.g:340:17: ( 'ordering' )
            # dgdl.g:340:19: 'ordering'
            pass 
            self.match("ordering")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORDERING"



    # $ANTLR start "OWNER"
    def mOWNER(self, ):

        try:
            _type = OWNER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:341:17: ( 'owner' )
            # dgdl.g:341:19: 'owner'
            pass 
            self.match("owner")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OWNER"



    # $ANTLR start "NOTPAST"
    def mNOTPAST(self, ):

        try:
            _type = NOTPAST
            _channel = DEFAULT_CHANNEL

            # dgdl.g:342:17: ( '!past' )
            # dgdl.g:342:19: '!past'
            pass 
            self.match("!past")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTPAST"



    # $ANTLR start "PAST"
    def mPAST(self, ):

        try:
            _type = PAST
            _channel = DEFAULT_CHANNEL

            # dgdl.g:343:17: ( 'past' )
            # dgdl.g:343:19: 'past'
            pass 
            self.match("past")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PAST"



    # $ANTLR start "PLAYER"
    def mPLAYER(self, ):

        try:
            _type = PLAYER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:344:17: ( 'player' )
            # dgdl.g:344:19: 'player'
            pass 
            self.match("player")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLAYER"



    # $ANTLR start "PLAYERS"
    def mPLAYERS(self, ):

        try:
            _type = PLAYERS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:345:17: ( 'players' )
            # dgdl.g:345:19: 'players'
            pass 
            self.match("players")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLAYERS"



    # $ANTLR start "PRIVATE"
    def mPRIVATE(self, ):

        try:
            _type = PRIVATE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:346:17: ( 'private' )
            # dgdl.g:346:19: 'private'
            pass 
            self.match("private")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PRIVATE"



    # $ANTLR start "PUBLIC"
    def mPUBLIC(self, ):

        try:
            _type = PUBLIC
            _channel = DEFAULT_CHANNEL

            # dgdl.g:347:17: ( 'public' )
            # dgdl.g:347:19: 'public'
            pass 
            self.match("public")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PUBLIC"



    # $ANTLR start "QUEUE"
    def mQUEUE(self, ):

        try:
            _type = QUEUE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:348:17: ( 'queue' )
            # dgdl.g:348:19: 'queue'
            pass 
            self.match("queue")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUEUE"



    # $ANTLR start "RELATION"
    def mRELATION(self, ):

        try:
            _type = RELATION
            _channel = DEFAULT_CHANNEL

            # dgdl.g:349:17: ( 'relation' )
            # dgdl.g:349:19: 'relation'
            pass 
            self.match("relation")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RELATION"



    # $ANTLR start "REMOVE"
    def mREMOVE(self, ):

        try:
            _type = REMOVE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:350:17: ( 'remove' )
            # dgdl.g:350:19: 'remove'
            pass 
            self.match("remove")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REMOVE"



    # $ANTLR start "ROLES"
    def mROLES(self, ):

        try:
            _type = ROLES
            _channel = DEFAULT_CHANNEL

            # dgdl.g:351:17: ( 'roles' )
            # dgdl.g:351:19: 'roles'
            pass 
            self.match("roles")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLES"



    # $ANTLR start "RULE"
    def mRULE(self, ):

        try:
            _type = RULE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:352:17: ( 'rule' )
            # dgdl.g:352:19: 'rule'
            pass 
            self.match("rule")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RULE"



    # $ANTLR start "SCOPE"
    def mSCOPE(self, ):

        try:
            _type = SCOPE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:353:17: ( 'scope' )
            # dgdl.g:353:19: 'scope'
            pass 
            self.match("scope")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SCOPE"



    # $ANTLR start "SET"
    def mSET(self, ):

        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # dgdl.g:354:17: ( 'set' )
            # dgdl.g:354:19: 'set'
            pass 
            self.match("set")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SET"



    # $ANTLR start "SHARED"
    def mSHARED(self, ):

        try:
            _type = SHARED
            _channel = DEFAULT_CHANNEL

            # dgdl.g:355:17: ( 'shared' )
            # dgdl.g:355:19: 'shared'
            pass 
            self.match("shared")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHARED"



    # $ANTLR start "SINGLE"
    def mSINGLE(self, ):

        try:
            _type = SINGLE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:356:17: ( 'single' )
            # dgdl.g:356:19: 'single'
            pass 
            self.match("single")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SINGLE"



    # $ANTLR start "SIZE"
    def mSIZE(self, ):

        try:
            _type = SIZE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:357:17: ( 'size' )
            # dgdl.g:357:19: 'size'
            pass 
            self.match("size")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SIZE"



    # $ANTLR start "SMALLER"
    def mSMALLER(self, ):

        try:
            _type = SMALLER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:358:17: ( 'smaller' )
            # dgdl.g:358:19: 'smaller'
            pass 
            self.match("smaller")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SMALLER"



    # $ANTLR start "SPEAKER"
    def mSPEAKER(self, ):

        try:
            _type = SPEAKER
            _channel = DEFAULT_CHANNEL

            # dgdl.g:359:17: ( 'speaker' )
            # dgdl.g:359:19: 'speaker'
            pass 
            self.match("speaker")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SPEAKER"



    # $ANTLR start "STACK"
    def mSTACK(self, ):

        try:
            _type = STACK
            _channel = DEFAULT_CHANNEL

            # dgdl.g:360:17: ( 'stack' )
            # dgdl.g:360:19: 'stack'
            pass 
            self.match("stack")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STACK"



    # $ANTLR start "STATUS"
    def mSTATUS(self, ):

        try:
            _type = STATUS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:361:17: ( 'status' )
            # dgdl.g:361:19: 'status'
            pass 
            self.match("status")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STATUS"



    # $ANTLR start "STORE"
    def mSTORE(self, ):

        try:
            _type = STORE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:362:17: ( 'store' )
            # dgdl.g:362:19: 'store'
            pass 
            self.match("store")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STORE"



    # $ANTLR start "STRICT"
    def mSTRICT(self, ):

        try:
            _type = STRICT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:363:17: ( 'strict' )
            # dgdl.g:363:19: 'strict'
            pass 
            self.match("strict")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRICT"



    # $ANTLR start "STRUCTURE"
    def mSTRUCTURE(self, ):

        try:
            _type = STRUCTURE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:364:17: ( 'structure' )
            # dgdl.g:364:19: 'structure'
            pass 
            self.match("structure")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRUCTURE"



    # $ANTLR start "TERMINATE"
    def mTERMINATE(self, ):

        try:
            _type = TERMINATE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:365:17: ( 'terminate' )
            # dgdl.g:365:19: 'terminate'
            pass 
            self.match("terminate")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TERMINATE"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # dgdl.g:366:17: ( 'then' )
            # dgdl.g:366:19: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "NOTTOP"
    def mNOTTOP(self, ):

        try:
            _type = NOTTOP
            _channel = DEFAULT_CHANNEL

            # dgdl.g:367:17: ( '!top' )
            # dgdl.g:367:19: '!top'
            pass 
            self.match("!top")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTTOP"



    # $ANTLR start "TOP"
    def mTOP(self, ):

        try:
            _type = TOP
            _channel = DEFAULT_CHANNEL

            # dgdl.g:368:17: ( 'top' )
            # dgdl.g:368:19: 'top'
            pass 
            self.match("top")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TOP"



    # $ANTLR start "TURNS"
    def mTURNS(self, ):

        try:
            _type = TURNS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:369:17: ( 'turns' )
            # dgdl.g:369:19: 'turns'
            pass 
            self.match("turns")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TURNS"



    # $ANTLR start "TURNWISE"
    def mTURNWISE(self, ):

        try:
            _type = TURNWISE
            _channel = DEFAULT_CHANNEL

            # dgdl.g:370:17: ( 'turnwise' )
            # dgdl.g:370:19: 'turnwise'
            pass 
            self.match("turnwise")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TURNWISE"



    # $ANTLR start "UNDEFINED"
    def mUNDEFINED(self, ):

        try:
            _type = UNDEFINED
            _channel = DEFAULT_CHANNEL

            # dgdl.g:371:17: ( 'undefined' )
            # dgdl.g:371:19: 'undefined'
            pass 
            self.match("undefined")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNDEFINED"



    # $ANTLR start "VISIBILITY"
    def mVISIBILITY(self, ):

        try:
            _type = VISIBILITY
            _channel = DEFAULT_CHANNEL

            # dgdl.g:372:17: ( 'visibility' )
            # dgdl.g:372:19: 'visibility'
            pass 
            self.match("visibility")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VISIBILITY"



    # $ANTLR start "WARRANT"
    def mWARRANT(self, ):

        try:
            _type = WARRANT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:373:17: ( 'warrant' )
            # dgdl.g:373:19: 'warrant'
            pass 
            self.match("warrant")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WARRANT"



    # $ANTLR start "STRINGLITERAL"
    def mSTRINGLITERAL(self, ):

        try:
            _type = STRINGLITERAL
            _channel = DEFAULT_CHANNEL

            # dgdl.g:375:17: ( '\"' (~ ( '\\\\' | '\"' | '\\r' | '\\n' ) )* '\"' )
            # dgdl.g:375:19: '\"' (~ ( '\\\\' | '\"' | '\\r' | '\\n' ) )* '\"'
            pass 
            self.match(34)
            # dgdl.g:375:23: (~ ( '\\\\' | '\"' | '\\r' | '\\n' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 33) or (35 <= LA3_0 <= 91) or (93 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # dgdl.g:375:24: ~ ( '\\\\' | '\"' | '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRINGLITERAL"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:378:17: ( '/*' ( . )* '*/' )
            # dgdl.g:378:19: '/*' ( . )* '*/'
            pass 
            self.match("/*")
            # dgdl.g:378:24: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 42) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 47) :
                        alt4 = 2
                    elif ((0 <= LA4_1 <= 46) or (48 <= LA4_1 <= 65535)) :
                        alt4 = 1


                elif ((0 <= LA4_0 <= 41) or (43 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # dgdl.g:378:24: .
                    pass 
                    self.matchAny()


                else:
                    break #loop4
            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # dgdl.g:379:17: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # dgdl.g:379:19: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")
            # dgdl.g:379:24: (~ ( '\\n' | '\\r' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # dgdl.g:379:24: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5
            # dgdl.g:379:38: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # dgdl.g:379:38: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # dgdl.g:381:17: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # dgdl.g:381:19: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            self.skip();
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # dgdl.g:1:8: ( T__119 | T__120 | T__121 | T__122 | T__123 | T__124 | T__125 | T__126 | T__127 | T__128 | T__129 | T__130 | Identifier | LowerChar | Number | UpperChar | LESSTHAN | GREATERTHAN | COMMA | COLON | LPAREN | RPAREN | LBRACE | RBRACE | DOLLAR | AND | OR | ACTIVE | ADD | ASSIGN | BACKING | BACKTRACK | COMPLETE | CORRESPONDS | CURRENT | DELETE | ELSE | ELSEIF | NOTEMPTY | EMPTY | NOTEQUAL | EQUAL | EVENT | EXTCONDITION | EXTEFFECT | EXTURI | FUTURE | GREATER | HELLO | ID | IF | NOTIN | IN | INACTIVE | INCOMPLETE | INITIAL | INITIATE | INROLE | INSPECT | INTERACTION | NOTLAST | LAST | LEGALMOVES | LIBERAL | LISTENER | MAGNITUDE | MAX | MAXTURNS | MIN | MOVE | MOVEWISE | MULTIPLE | NEXT | NOT | NUMTURNS | OFF | NOTON | ON | ORDERING | OWNER | NOTPAST | PAST | PLAYER | PLAYERS | PRIVATE | PUBLIC | QUEUE | RELATION | REMOVE | ROLES | RULE | SCOPE | SET | SHARED | SINGLE | SIZE | SMALLER | SPEAKER | STACK | STATUS | STORE | STRICT | STRUCTURE | TERMINATE | THEN | NOTTOP | TOP | TURNS | TURNWISE | UNDEFINED | VISIBILITY | WARRANT | STRINGLITERAL | COMMENT | LINE_COMMENT | WS )
        alt7 = 116
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # dgdl.g:1:10: T__119
            pass 
            self.mT__119()


        elif alt7 == 2:
            # dgdl.g:1:17: T__120
            pass 
            self.mT__120()


        elif alt7 == 3:
            # dgdl.g:1:24: T__121
            pass 
            self.mT__121()


        elif alt7 == 4:
            # dgdl.g:1:31: T__122
            pass 
            self.mT__122()


        elif alt7 == 5:
            # dgdl.g:1:38: T__123
            pass 
            self.mT__123()


        elif alt7 == 6:
            # dgdl.g:1:45: T__124
            pass 
            self.mT__124()


        elif alt7 == 7:
            # dgdl.g:1:52: T__125
            pass 
            self.mT__125()


        elif alt7 == 8:
            # dgdl.g:1:59: T__126
            pass 
            self.mT__126()


        elif alt7 == 9:
            # dgdl.g:1:66: T__127
            pass 
            self.mT__127()


        elif alt7 == 10:
            # dgdl.g:1:73: T__128
            pass 
            self.mT__128()


        elif alt7 == 11:
            # dgdl.g:1:80: T__129
            pass 
            self.mT__129()


        elif alt7 == 12:
            # dgdl.g:1:87: T__130
            pass 
            self.mT__130()


        elif alt7 == 13:
            # dgdl.g:1:94: Identifier
            pass 
            self.mIdentifier()


        elif alt7 == 14:
            # dgdl.g:1:105: LowerChar
            pass 
            self.mLowerChar()


        elif alt7 == 15:
            # dgdl.g:1:115: Number
            pass 
            self.mNumber()


        elif alt7 == 16:
            # dgdl.g:1:122: UpperChar
            pass 
            self.mUpperChar()


        elif alt7 == 17:
            # dgdl.g:1:132: LESSTHAN
            pass 
            self.mLESSTHAN()


        elif alt7 == 18:
            # dgdl.g:1:141: GREATERTHAN
            pass 
            self.mGREATERTHAN()


        elif alt7 == 19:
            # dgdl.g:1:153: COMMA
            pass 
            self.mCOMMA()


        elif alt7 == 20:
            # dgdl.g:1:159: COLON
            pass 
            self.mCOLON()


        elif alt7 == 21:
            # dgdl.g:1:165: LPAREN
            pass 
            self.mLPAREN()


        elif alt7 == 22:
            # dgdl.g:1:172: RPAREN
            pass 
            self.mRPAREN()


        elif alt7 == 23:
            # dgdl.g:1:179: LBRACE
            pass 
            self.mLBRACE()


        elif alt7 == 24:
            # dgdl.g:1:186: RBRACE
            pass 
            self.mRBRACE()


        elif alt7 == 25:
            # dgdl.g:1:193: DOLLAR
            pass 
            self.mDOLLAR()


        elif alt7 == 26:
            # dgdl.g:1:200: AND
            pass 
            self.mAND()


        elif alt7 == 27:
            # dgdl.g:1:204: OR
            pass 
            self.mOR()


        elif alt7 == 28:
            # dgdl.g:1:207: ACTIVE
            pass 
            self.mACTIVE()


        elif alt7 == 29:
            # dgdl.g:1:214: ADD
            pass 
            self.mADD()


        elif alt7 == 30:
            # dgdl.g:1:218: ASSIGN
            pass 
            self.mASSIGN()


        elif alt7 == 31:
            # dgdl.g:1:225: BACKING
            pass 
            self.mBACKING()


        elif alt7 == 32:
            # dgdl.g:1:233: BACKTRACK
            pass 
            self.mBACKTRACK()


        elif alt7 == 33:
            # dgdl.g:1:243: COMPLETE
            pass 
            self.mCOMPLETE()


        elif alt7 == 34:
            # dgdl.g:1:252: CORRESPONDS
            pass 
            self.mCORRESPONDS()


        elif alt7 == 35:
            # dgdl.g:1:264: CURRENT
            pass 
            self.mCURRENT()


        elif alt7 == 36:
            # dgdl.g:1:272: DELETE
            pass 
            self.mDELETE()


        elif alt7 == 37:
            # dgdl.g:1:279: ELSE
            pass 
            self.mELSE()


        elif alt7 == 38:
            # dgdl.g:1:284: ELSEIF
            pass 
            self.mELSEIF()


        elif alt7 == 39:
            # dgdl.g:1:291: NOTEMPTY
            pass 
            self.mNOTEMPTY()


        elif alt7 == 40:
            # dgdl.g:1:300: EMPTY
            pass 
            self.mEMPTY()


        elif alt7 == 41:
            # dgdl.g:1:306: NOTEQUAL
            pass 
            self.mNOTEQUAL()


        elif alt7 == 42:
            # dgdl.g:1:315: EQUAL
            pass 
            self.mEQUAL()


        elif alt7 == 43:
            # dgdl.g:1:321: EVENT
            pass 
            self.mEVENT()


        elif alt7 == 44:
            # dgdl.g:1:327: EXTCONDITION
            pass 
            self.mEXTCONDITION()


        elif alt7 == 45:
            # dgdl.g:1:340: EXTEFFECT
            pass 
            self.mEXTEFFECT()


        elif alt7 == 46:
            # dgdl.g:1:350: EXTURI
            pass 
            self.mEXTURI()


        elif alt7 == 47:
            # dgdl.g:1:357: FUTURE
            pass 
            self.mFUTURE()


        elif alt7 == 48:
            # dgdl.g:1:364: GREATER
            pass 
            self.mGREATER()


        elif alt7 == 49:
            # dgdl.g:1:372: HELLO
            pass 
            self.mHELLO()


        elif alt7 == 50:
            # dgdl.g:1:378: ID
            pass 
            self.mID()


        elif alt7 == 51:
            # dgdl.g:1:381: IF
            pass 
            self.mIF()


        elif alt7 == 52:
            # dgdl.g:1:384: NOTIN
            pass 
            self.mNOTIN()


        elif alt7 == 53:
            # dgdl.g:1:390: IN
            pass 
            self.mIN()


        elif alt7 == 54:
            # dgdl.g:1:393: INACTIVE
            pass 
            self.mINACTIVE()


        elif alt7 == 55:
            # dgdl.g:1:402: INCOMPLETE
            pass 
            self.mINCOMPLETE()


        elif alt7 == 56:
            # dgdl.g:1:413: INITIAL
            pass 
            self.mINITIAL()


        elif alt7 == 57:
            # dgdl.g:1:421: INITIATE
            pass 
            self.mINITIATE()


        elif alt7 == 58:
            # dgdl.g:1:430: INROLE
            pass 
            self.mINROLE()


        elif alt7 == 59:
            # dgdl.g:1:437: INSPECT
            pass 
            self.mINSPECT()


        elif alt7 == 60:
            # dgdl.g:1:445: INTERACTION
            pass 
            self.mINTERACTION()


        elif alt7 == 61:
            # dgdl.g:1:457: NOTLAST
            pass 
            self.mNOTLAST()


        elif alt7 == 62:
            # dgdl.g:1:465: LAST
            pass 
            self.mLAST()


        elif alt7 == 63:
            # dgdl.g:1:470: LEGALMOVES
            pass 
            self.mLEGALMOVES()


        elif alt7 == 64:
            # dgdl.g:1:481: LIBERAL
            pass 
            self.mLIBERAL()


        elif alt7 == 65:
            # dgdl.g:1:489: LISTENER
            pass 
            self.mLISTENER()


        elif alt7 == 66:
            # dgdl.g:1:498: MAGNITUDE
            pass 
            self.mMAGNITUDE()


        elif alt7 == 67:
            # dgdl.g:1:508: MAX
            pass 
            self.mMAX()


        elif alt7 == 68:
            # dgdl.g:1:512: MAXTURNS
            pass 
            self.mMAXTURNS()


        elif alt7 == 69:
            # dgdl.g:1:521: MIN
            pass 
            self.mMIN()


        elif alt7 == 70:
            # dgdl.g:1:525: MOVE
            pass 
            self.mMOVE()


        elif alt7 == 71:
            # dgdl.g:1:530: MOVEWISE
            pass 
            self.mMOVEWISE()


        elif alt7 == 72:
            # dgdl.g:1:539: MULTIPLE
            pass 
            self.mMULTIPLE()


        elif alt7 == 73:
            # dgdl.g:1:548: NEXT
            pass 
            self.mNEXT()


        elif alt7 == 74:
            # dgdl.g:1:553: NOT
            pass 
            self.mNOT()


        elif alt7 == 75:
            # dgdl.g:1:557: NUMTURNS
            pass 
            self.mNUMTURNS()


        elif alt7 == 76:
            # dgdl.g:1:566: OFF
            pass 
            self.mOFF()


        elif alt7 == 77:
            # dgdl.g:1:570: NOTON
            pass 
            self.mNOTON()


        elif alt7 == 78:
            # dgdl.g:1:576: ON
            pass 
            self.mON()


        elif alt7 == 79:
            # dgdl.g:1:579: ORDERING
            pass 
            self.mORDERING()


        elif alt7 == 80:
            # dgdl.g:1:588: OWNER
            pass 
            self.mOWNER()


        elif alt7 == 81:
            # dgdl.g:1:594: NOTPAST
            pass 
            self.mNOTPAST()


        elif alt7 == 82:
            # dgdl.g:1:602: PAST
            pass 
            self.mPAST()


        elif alt7 == 83:
            # dgdl.g:1:607: PLAYER
            pass 
            self.mPLAYER()


        elif alt7 == 84:
            # dgdl.g:1:614: PLAYERS
            pass 
            self.mPLAYERS()


        elif alt7 == 85:
            # dgdl.g:1:622: PRIVATE
            pass 
            self.mPRIVATE()


        elif alt7 == 86:
            # dgdl.g:1:630: PUBLIC
            pass 
            self.mPUBLIC()


        elif alt7 == 87:
            # dgdl.g:1:637: QUEUE
            pass 
            self.mQUEUE()


        elif alt7 == 88:
            # dgdl.g:1:643: RELATION
            pass 
            self.mRELATION()


        elif alt7 == 89:
            # dgdl.g:1:652: REMOVE
            pass 
            self.mREMOVE()


        elif alt7 == 90:
            # dgdl.g:1:659: ROLES
            pass 
            self.mROLES()


        elif alt7 == 91:
            # dgdl.g:1:665: RULE
            pass 
            self.mRULE()


        elif alt7 == 92:
            # dgdl.g:1:670: SCOPE
            pass 
            self.mSCOPE()


        elif alt7 == 93:
            # dgdl.g:1:676: SET
            pass 
            self.mSET()


        elif alt7 == 94:
            # dgdl.g:1:680: SHARED
            pass 
            self.mSHARED()


        elif alt7 == 95:
            # dgdl.g:1:687: SINGLE
            pass 
            self.mSINGLE()


        elif alt7 == 96:
            # dgdl.g:1:694: SIZE
            pass 
            self.mSIZE()


        elif alt7 == 97:
            # dgdl.g:1:699: SMALLER
            pass 
            self.mSMALLER()


        elif alt7 == 98:
            # dgdl.g:1:707: SPEAKER
            pass 
            self.mSPEAKER()


        elif alt7 == 99:
            # dgdl.g:1:715: STACK
            pass 
            self.mSTACK()


        elif alt7 == 100:
            # dgdl.g:1:721: STATUS
            pass 
            self.mSTATUS()


        elif alt7 == 101:
            # dgdl.g:1:728: STORE
            pass 
            self.mSTORE()


        elif alt7 == 102:
            # dgdl.g:1:734: STRICT
            pass 
            self.mSTRICT()


        elif alt7 == 103:
            # dgdl.g:1:741: STRUCTURE
            pass 
            self.mSTRUCTURE()


        elif alt7 == 104:
            # dgdl.g:1:751: TERMINATE
            pass 
            self.mTERMINATE()


        elif alt7 == 105:
            # dgdl.g:1:761: THEN
            pass 
            self.mTHEN()


        elif alt7 == 106:
            # dgdl.g:1:766: NOTTOP
            pass 
            self.mNOTTOP()


        elif alt7 == 107:
            # dgdl.g:1:773: TOP
            pass 
            self.mTOP()


        elif alt7 == 108:
            # dgdl.g:1:777: TURNS
            pass 
            self.mTURNS()


        elif alt7 == 109:
            # dgdl.g:1:783: TURNWISE
            pass 
            self.mTURNWISE()


        elif alt7 == 110:
            # dgdl.g:1:792: UNDEFINED
            pass 
            self.mUNDEFINED()


        elif alt7 == 111:
            # dgdl.g:1:802: VISIBILITY
            pass 
            self.mVISIBILITY()


        elif alt7 == 112:
            # dgdl.g:1:813: WARRANT
            pass 
            self.mWARRANT()


        elif alt7 == 113:
            # dgdl.g:1:821: STRINGLITERAL
            pass 
            self.mSTRINGLITERAL()


        elif alt7 == 114:
            # dgdl.g:1:835: COMMENT
            pass 
            self.mCOMMENT()


        elif alt7 == 115:
            # dgdl.g:1:843: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt7 == 116:
            # dgdl.g:1:856: WS
            pass 
            self.mWS()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\3\45\1\63\1\uffff\4\45\1\104\1\45\13\uffff\5\45\1\131"
        u"\10\45\34\uffff\1\u0086\117\uffff\1\u00a0\11\uffff\1\u00a8\5\uffff"
        u"\1\u00aa\13\uffff\1\u00b0\5\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\u00b3\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\1\156\2\141\1\56\1\uffff\2\141\1\145\1\144\1\60\1\143\13"
        u"\uffff\1\141\1\157\1\145\1\154\1\165\1\145\1\162\1\145\2\141\1"
        u"\146\1\165\1\145\1\141\2\uffff\1\52\2\uffff\2\141\1\151\11\uffff"
        u"\1\156\3\uffff\1\156\2\uffff\1\141\1\143\2\uffff\1\141\7\uffff"
        u"\1\143\1\155\2\uffff\1\163\3\uffff\1\164\1\uffff\1\155\12\uffff"
        u"\1\142\1\147\1\uffff\1\166\11\uffff\1\162\6\uffff\1\171\6\uffff"
        u"\1\143\1\uffff\1\151\6\uffff\1\164\4\uffff\1\153\2\uffff\1\145"
        u"\1\103\5\uffff\1\164\1\145\1\156\1\145\4\uffff\3\151\5\uffff\1"
        u"\167\1\163\1\162\1\141\10\uffff\1\163\1\154\4\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\175\1\162\2\165\1\56\1\uffff\1\151\1\164\1\165\1\156\1\172\1"
        u"\163\13\uffff\1\141\1\165\1\145\1\170\1\165\1\164\1\162\1\145\1"
        u"\151\1\165\1\167\2\165\1\141\2\uffff\1\57\2\uffff\1\144\1\165\1"
        u"\157\11\uffff\1\164\3\uffff\1\172\2\uffff\1\162\1\155\2\uffff\1"
        u"\166\7\uffff\1\143\1\162\2\uffff\1\163\3\uffff\1\164\1\uffff\1"
        u"\161\12\uffff\1\163\1\170\1\uffff\1\166\11\uffff\1\162\6\uffff"
        u"\1\171\6\uffff\1\164\1\uffff\1\165\6\uffff\1\164\4\uffff\1\153"
        u"\2\uffff\1\145\1\125\5\uffff\1\164\1\145\1\156\1\145\4\uffff\1"
        u"\151\1\164\1\151\5\uffff\2\167\1\162\1\141\10\uffff\1\163\1\164"
        u"\4\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\5\uffff\1\5\6\uffff\1\17\1\21\1\22\1\23\1\24\1\25\1\26\1\27\1"
        u"\30\1\32\1\33\16\uffff\1\16\1\161\1\uffff\1\164\1\1\3\uffff\1\122"
        u"\1\126\1\3\1\111\1\113\1\4\1\31\1\6\1\157\1\uffff\1\14\1\134\1"
        u"\136\1\uffff\1\141\1\142\2\uffff\1\132\1\133\1\uffff\1\62\1\63"
        u"\1\20\1\15\1\34\1\35\1\36\2\uffff\1\43\1\44\1\uffff\1\50\1\52\1"
        u"\53\1\uffff\1\57\1\uffff\1\64\1\75\1\115\1\121\1\152\1\112\1\60"
        u"\1\61\1\76\1\77\2\uffff\1\105\1\uffff\1\110\1\114\1\116\1\117\1"
        u"\120\1\127\1\150\1\151\1\153\1\uffff\1\160\1\162\1\163\1\7\1\156"
        u"\1\2\1\uffff\1\13\1\125\1\10\1\135\1\137\1\140\1\uffff\1\145\1"
        u"\uffff\1\11\1\130\1\131\1\12\1\66\1\67\1\uffff\1\72\1\73\1\74\1"
        u"\65\1\uffff\1\41\1\42\2\uffff\1\47\1\51\1\100\1\101\1\102\4\uffff"
        u"\1\143\1\144\1\146\1\147\3\uffff\1\54\1\55\1\56\1\104\1\103\4\uffff"
        u"\1\37\1\40\1\46\1\45\1\107\1\106\1\154\1\155\2\uffff\1\124\1\123"
        u"\1\70\1\71"
        )

    DFA7_special = DFA.unpack(
        u"\u00b3\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\2\50\1\uffff\2\50\22\uffff\1\50\1\34\1\46\1\uffff\1"
        u"\4\1\uffff\1\25\1\uffff\1\21\1\22\2\uffff\1\17\1\uffff\1\5\1\47"
        u"\12\14\1\20\1\uffff\1\15\1\uffff\1\16\2\uffff\32\12\6\uffff\1\13"
        u"\1\27\1\30\1\31\1\32\1\33\1\35\1\36\1\11\2\45\1\37\1\40\1\3\1\41"
        u"\1\2\1\42\1\10\1\7\1\43\1\1\1\6\1\44\3\45\1\23\1\26\1\24"),
        DFA.unpack(u"\1\52\3\uffff\1\51"),
        DFA.unpack(u"\1\55\12\uffff\1\53\5\uffff\1\54\2\uffff\1\56"),
        DFA.unpack(u"\1\57\3\uffff\1\60\17\uffff\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64\7\uffff\1\65"),
        DFA.unpack(u"\1\67\1\uffff\1\70\1\uffff\1\66\2\uffff\1\71\1\72\3"
        u"\uffff\1\73\2\uffff\1\74\3\uffff\1\75"),
        DFA.unpack(u"\1\76\11\uffff\1\77\5\uffff\1\100"),
        DFA.unpack(u"\1\102\1\uffff\1\103\7\uffff\1\101"),
        DFA.unpack(u"\12\105\7\uffff\32\105\6\uffff\32\105"),
        DFA.unpack(u"\1\106\1\107\16\uffff\1\110"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112\5\uffff\1\113"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115\1\116\3\uffff\1\117\4\uffff\1\120\1\uffff\1"
        u"\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123\3\uffff\1\124\2\uffff\1\125\2\uffff\1\126\1"
        u"\127\3\uffff\1\130"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134\3\uffff\1\135\3\uffff\1\136"),
        DFA.unpack(u"\1\137\7\uffff\1\140\5\uffff\1\141\5\uffff\1\142"),
        DFA.unpack(u"\1\143\7\uffff\1\144\3\uffff\1\145\4\uffff\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150\2\uffff\1\151\6\uffff\1\152\5\uffff\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\155\4\uffff\1\156"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\157\2\uffff\1\160"),
        DFA.unpack(u"\1\162\23\uffff\1\161"),
        DFA.unpack(u"\1\164\5\uffff\1\163"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\165\5\uffff\1\166"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\167\13\uffff\1\170"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\171\15\uffff\1\172\2\uffff\1\173"),
        DFA.unpack(u"\1\174\10\uffff\1\175\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0080\1\uffff\1\u0081\5\uffff\1\u0082\10\uffff\1"
        u"\u0083\1\u0084\1\u0085\1\uffff\1\177"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088\4\uffff\1\u0089"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008c\3\uffff\1\u008d"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008e\20\uffff\1\u008f"),
        DFA.unpack(u"\1\u0090\20\uffff\1\u0091"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0095\20\uffff\1\u0096"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0097\13\uffff\1\u0098"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c\1\uffff\1\u009d\17\uffff\1\u009e"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5\12\uffff\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00ab\3\uffff\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b1\7\uffff\1\u00b2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(dgdlLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
