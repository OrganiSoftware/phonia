#!/usr/bin/env python3

import sys
import os
from lib.args import args

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        
        error = '\033[1;31m[-] \033[0m'
        
        outputfile = str(args.outputfile)
        
        if outputfile != "":
            if os.path.isdir(outputfile):
                if os.path.exists(outputfile):
                    if outputfile[-1] == "/":
                        outputfile = outputfile + 'output.txt'
                        self.log = open(outputfile, "a")
                    else:
                        outputfile = outputfile + '/output.txt'
                        self.log = open(outputfile, "a")
                else:
                    print(error+"Output directory: "+outputfile+": does not exist!")
                    sys.exit()
            else:
                direct = os.path.split(outputfile)[0]
                if direct == "":
                    direct = "."
                else:
                    pass
                if os.path.exists(direct):
                    if os.path.isdir(direct):
                        self.log = open(outputfile, "a")
                    else:
                        print(error+"Error: "+direct+": not a directory!")
                        sys.exit()
                else:
                    print(error+"Output directory: "+direct+": does not exist!")
                    sys.exit()
        else:
            pass

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def close_file(self):
        self.log.close()

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass
