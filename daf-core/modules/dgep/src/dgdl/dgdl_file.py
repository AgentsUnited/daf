import antlr3
import os.path
import os
from antlr3 import *
from antlr3.tree import *
from .dgdl_antlr.dgdlLexer import *
from .dgdl_antlr.dgdlParser import *
from io import BytesIO as StringIO
import sys
import traceback

class dgdl_file:

    def __init__(self):
        self.tree = None
        self.dgdl_base = os.getcwd() + "/src/assets/protocols/{filename}.dgdl"

    def create(self, name, dgdl):
        """ Creates a new DGDL file with name, using the given dgdl spec
            :param name the filename to create
            :param dgdl the DGDL to put in the file
            :type name str
            :type dgdl str
        """
        filename = self.get_file(name)

        file = open(filename, 'w+')
        file.write(dgdl)

    def test(self, file):
        """ Tests the given DGDL file
            :param file the name of the DGDL file
            :type file str
        """
        filename = self.get_file(file)

        if os.path.isfile(filename):
            with open(filename) as dgdl_file:
                dgdl = dgdl_file.read()
                return self.do_test(dgdl)

    def load(self, filename):
        """Loads the given dgdl file
            :param filename the name of the DGDL file to load
            :type filename str
        """

        filename = self.get_file(filename);

        if os.path.isfile(filename):
            try:
                char_stream = antlr3.ANTLRFileStream(filename)
                lexer = dgdlLexer(char_stream)
                tokens = antlr3.CommonTokenStream(lexer)
                parser = dgdlParser(tokens)
                return parser.system().tree
            except Exception as e:
                traceback.print_exc()
                return None
        else:
            return None


    def get_file(self, filename):
        """Get the full path to the given DGDL filename
            :param filename the filename to get
            :type filename str
        """
        placeholder = "{filename}"

        '''If the filename has been given with the .dgdl extension, extend the
            placeholder to account for this'''
        if filename[-5:] == ".dgdl":
            placeholder = placeholder + ".dgdl"

        return self.dgdl_base.replace(placeholder, filename)

    def do_test(self, dgdl):
        """Test the given dgdl specification
            :param dgdl the DGDL specification
            :type dgdl str
        """
        try:

            '''To catch parse errors, redirect the output of sys.stderr
                to a variable'''
            old_stderr = sys.stderr
            sys.stderr = mystdout = StringIO()

            '''Attempt to parse the DGDL spec with antlr'''
            char_stream = antlr3.ANTLRStringStream(dgdl)
            lexer = dgdlLexer(char_stream)
            tokens = antlr3.CommonTokenStream(lexer)
            parser = dgdlParser(tokens)
            tree = parser.system().tree

            ''' Reassign sys.stderr to its previous location '''
            sys.stderr = old_stderr

            '''Return value will be any parse errors, or an empty string if
                no errors'''
            return mystdout.getvalue()

        except Exception as e:
            ''' This is an error with even trying to parse, not a parse error'''
            return None
