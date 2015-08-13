###############################################################################
#                                                                             #
#                   C H E A D E R - M A I N                                   #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Thu Aug 13 16:38:10 BST 2015                                        #
#                                                                             #
###############################################################################

import utils

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

class CFileFactory:

    @staticmethod
    def is_dot_h(filename):
        pass

    @staticmethod
    def is_dot_c(filename):
        pass

    @staticmethod
    def create(filename):
        if CFile.is_dot_c(filename):
            return CSource(filename)
        elif CFile.is_dot_h(filename):
            return CHeader(filename)


class CFile:
    file_path
    symbols
    includes

    def __init__(
          self,
          filename):
        self.file_path = filename

        cparser = CParser(filename)
        self.symbols = cparser.parse_symbols()
        self.includes = cparser.parse_includes()

    def get_file_include_obj(self, incname):
        return self.includes[incname]

    def is_include_unused(self, inc_obj):
        inc_path = inc_obj.resolve_path()
        hfile = CFileFactory.create(inc_path)
        for s in hfile.symbols:
            if s in self.symbols:
                return FALSE
        return TRUE

    def get_unused_includes(self):
        unused = []
        for inc in self.includes:
            if self.is_include_unused(inc):
                unused.append(inc)
        return unused

    def remove_line(self, linenum):
        utils.file_remove_line(self.file_path, linenum)

        for inc in self.includes:
            inc.update_line(linenum)

    def delete_includes(self, includes_name_list):
        for inc in includes_list:
            if inc in self.includes:
                inc_obj = self.get_file_include_obj(inc)
                del self.includes[inc]
                self.remove_line(inc_obj.get_line_number())

class Header(CFile):
    
    def __init__(
          self,
          header_name):
        pass

class Source(CFile):
    
    def __init__(
          self,
          source_name):
        pass
    

def cheader_main(file_list):
    for f in file_list:
      cfile = CFileFactory.create(f)

      includes = cfile.get_unused_includes()
    pass

