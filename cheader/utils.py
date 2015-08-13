###############################################################################
#                                                                             #
#                   U T I L S                                                 #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Thu Aug 13 16:38:10 BST 2015                                        #
#                                                                             #
###############################################################################

def file_remove_line(filename, lineno):
    fro = open(filename, "rb")

    current_line = 0
    while current_line < lineno:
        fro.readline()
        current_line += 1

    seekpoint = fro.tell()
    frw = open(filename, "r+b")
    frw.seek(seekpoint, 0)

    fro.readline()

    chars = fro.readline()
    while chars:
      frw.writelines(chars)
      chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()
