#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--phone', metavar="<phone>", dest='phone', type=str, help='The phone number to scan.')
parser.add_argument('-i', '--input', metavar="<input_file>", dest="inputfile", type=str, help='List of phone numbers.')
parser.add_argument('-o', '--output', metavar="<output_path>", dest="outputfile", type=str, help='Output to the specified path.')
parser.add_argument('-s', '--scanner', metavar="<scanner>", dest="scanner", type=str, default="all", help='The scanner to use.')
parser.add_argument('--recon', action='store_true', help='Launch custom format reconnaissance.')
parser.add_argument('--no-ansi', action='store_true', help='Disable colored output.')
parser.add_argument('-u', '--update', action='store_true', help='Update Phonia Toolkit.')
parser.add_argument('--version', action='store_true', help='Show Phonia Toolkit version.')

args = parser.parse_args()
