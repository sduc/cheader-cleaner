###############################################################################
#                                                                             #
#                   C P A R S E R                                             #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Thu Aug 13 16:38:10 BST 2015                                        #
#                                                                             #
###############################################################################

class CParser:

    file_path

    def __init__(self, cfile):
        self.file_path = cfile 


class CParsed:

    __filename
    __parsed_symbols
    __parsed_includes

    def __init__(self, filename):
        self.__filename = filename

    def parsed_symbols(self):
        return self.__parsed_symbols

    def parsed_includes(self):
        return self.__parsed_includes
