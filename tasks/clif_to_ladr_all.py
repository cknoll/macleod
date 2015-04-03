from src import filemgt
from tasks import *
import os, sys
from src.ClifModuleSet import ClifModuleSet
from tasks import clif_to_ladr

def ladr_all(folder):
    filemgt.start_logging()
    ending = filemgt.read_config('cl','ending')
    tempfolder = filemgt.read_config('converters', 'tempfolder')
    ignores = [tempfolder]
    for directory, subdirs, files in os.walk(folder):
        if any(ignore in directory for ignore in ignores):
            pass
        else:
            for single_file in files:
                if single_file.endswith(ending):
                    print single_file
                    filename = os.path.join(directory, single_file)
                    print filename
                    m = ClifModuleSet(filename)
                    clif_to_ladr.ladr(filename, m)



if __name__ == '__main__':

    filemgt.start_logging()
    tempfolder = filemgt.read_config('converters', 'tempfolder')
    
    ignores = [tempfolder]
    
    ending = filemgt.read_config('cl','ending')

    licence.print_terms()
    # global variables
    options = sys.argv
    options.reverse()
    options.pop()
    folder = options.pop()
    
    for directory, subdirs, files in os.walk(folder):
        if any(ignore in directory for ignore in ignores):
            pass
        else:
            for single_file in files:
                if single_file.endswith(ending):
                    filename = os.path.join(directory.replace('qs\\',''), single_file)
                    print filename
                    m = ClifModuleSet(filename)
                    clif_to_ladr.ladr(filename, m, options)
