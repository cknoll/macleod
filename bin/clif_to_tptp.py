'''
Created on 2013-03-28

@author: Torsten Hahmann
'''

import os, sys, datetime

#print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../")


from bin import licence
from macleod.ClifModuleSet import ClifModuleSet

def tptp(filename, m, options=[]):

    m = ClifModuleSet(filename)
    if '-cumulate' in options:
        # translate into a single tptp single_file
        single_file = m.get_single_tptp_file()
        print("")
        print("+++++++++++++++++++++")
        print("Files created:")
        print("")
        print(single_file)
        print("+++++++++++++++++++++")
    elif '-module' in options:
        single_file = m.get_top_module().get_tptp_file_name()
        print("")
        print("+++++++++++++++++++++")
        print("Files created:")
        print("")
        print(single_file)
        print("+++++++++++++++++++++")

    else:
        files = m.get_tptp_files()
        print("")
        print("+++++++++++++++++++++")
        print("Files created:")
        print("")
        for single_file in files:
            print(single_file)
        print("+++++++++++++++++++++")    

if __name__ == '__main__':
    licence.print_terms()
    # global variables
    options = sys.argv
    options.reverse()
    options.pop()
    filename = options.pop()
    tptp(filename, options)


