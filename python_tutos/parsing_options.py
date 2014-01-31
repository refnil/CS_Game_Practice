#!/usr/bin/env python

#import the parsing module
from optparse import OptionParser

#define usage of the command-line (optional)
my_usage = "Usage: parsing_options.py [options] [args]"

#create a parser object (usage is optional)
parser = OptionParser(usage=my_usage)
#add options
parser.add_option("-o", "--option", dest="option_list_name", help="help text for the option")
parser.add_option("-p", "--predicate", action="store_true", dest="predicate_list_name", help="help text for the predicate")
#parse the command line
options, args = parser.parse_args()

#now all options and all args are stored in corresponding arrays
if options.predicate_list_name:
    print("A predicate was parsed!")
    
if options.option_list_name:
    print(options.option_list_name)

print("args:")
for arg in args:
    print("  " + arg)

#examples:
#   command:
#       python parsing_options.py -p
#   output:
#       A predicate was parsed!
#       args:
#
#   command:
#       python parsing_options.py --option testing
#   output:
#       testing
#       args:
#
#   command:
#       python parsing_options.py foo bar
#   output:
#       args:
#         foo
#         bar
#
#   command:
#       python parsing_options.py -p -o foo bar
#   output:
#       A predicate was parsed!
#       foo
#       args:
#           bar
#
#   command:
#       python parsing_options.py -h
#   output:
#       Usage: parsing_options.py [options] [args]
#
#       Options:
#          -h, --help            show this help message and exit
#          -o OPTION_LIST_NAME, --option=OPTION_LIST_NAME
#                                help text for the option
#          -p, --predicate       help text for the predicate