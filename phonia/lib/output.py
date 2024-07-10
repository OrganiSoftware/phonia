#!/usr/bin/env python3

import sys
import json
from lib.colors import *
from lib.args import args
from lib.logger import Logger

def plus(string):
    print("%s[+]%s %s%s" % (G % 1, S, string, E))

def warn(string):
    print("%s[!]%s %s%s" % (Y % 1, S, string, E))

def error(string):
    print("%s[-]%s %s%s" % (R % 1, S, string, E))

def test(string):
    print("%s[*]%s %s%s" % (B % 1, S, string, E))

def info(string):
    print("%s[i]%s %s%s" % (W % 1, S, string, E))

def more(string):
    print(" %s|%s  %s%s" % (W % 0, string, E))

def title(string):
    print("%s%s%s%s" % (BOLD, Y % 1, string, E))


def throw(string):
    error(string)
    sys.exit()


def askForExit():
    user_input = ask('\033[1;77m'+'[?]'+'\033[0m'+' Continue scan? (y/n): '+'\033[0m')

    if user_input.lower() == 'y':
        return -1
    else:
        sys.exit()

def ask(text):
    sys.stdout = sys.__stdout__
    res = input(text).strip(" ")
    sys.stdout = Logger()

    return res
