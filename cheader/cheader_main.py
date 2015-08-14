###############################################################################
#                                                                             #
#                   C H E A D E R - M A I N                                   #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Thu Aug 13 16:38:10 BST 2015                                        #
#                                                                             #
###############################################################################

class SelfHeaderDeleteError(Exception):
    pass

class Include:
    line
    includename

    def __init__(
          self,
          line,
          name):
        pass

    def get_line_number(self):
        return self.line

    def get_include_name(self):
        return self.includename

    def update_line(self, linenum):
        if linenum > self.line:
            self.line = self.line - 1
        elif linenum == self.line:
            raise SelfHeaderDeleteError

    def resolve_path(self):
        pass


def cheader_main(file_list):
    for f in file_list:
      cfile = CFileFactory.create(f)

      includes = cfile.get_unused_includes()
    pass

