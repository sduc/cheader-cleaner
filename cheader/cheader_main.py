###############################################################################
#                                                                             #
#                   C H E A D E R - M A I N                                   #
#                                                                             #
#   Author: Sebastien Duc                                                     #
#   Date: Thu Aug 13 16:38:10 BST 2015                                        #
#                                                                             #
###############################################################################

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='CHeader: C header cleaner')
    parser.add_argument('flist', metavar='file_list', type=str, nargs='+', 
        help='list of file names to clean the included header files')
    parser.add_argument('--remove','-r', action='store_true',
        help='remove the unused includes instead of just printing')
    return parser.parse_args()

def cheader_main(file_list):
    for f in file_list:
      cfile = CFileFactory.create(f)

      includes = cfile.get_unused_includes()
    pass

if __name__ == "__main__":
    parsed_args = parse_args()
    print(parsed_args)
