###############################################################################
#                                                                             #
#                   C I N CP A R S E R                                        #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Mon Aug 17 18:09:09 BST 2015                                        #
#                                                                             #
###############################################################################

from subprocess import call

class CIncParser:

    __filename
    __inc_dirs

    def __init__(self, filename):
        pass

    def __cpp_out(self):
        call("cpp -M -I " + self.get_inc_dirs_str() + " " + self.__filename,
            shell=True)
        

def parse_includes(filename):
    pass
    
