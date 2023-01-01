#!/usr/bin/python3

import sys
# extend the search path for my module 'db_access' and the functions
# in shell: export PYTHONPATH=/home/eddgest/PycharmProjects/stromverbrauch/libs
sys.path.append('/home/eddgest/PycharmProjects/stromverbrauch/libs')
#sys.path.append('/home/eddgest/.local/lib/python3.6/site-packages/stromverbrauch')
#functions for this program
import stromverbrauch_functions as sfunc

# for Pandas DataFrame
import pandas as pd
# for argparse
import argparse
import datetime

#TODO: Authentication
#TODO: make sure two decimals can be input to DB
#TODO: plot verbrauch into to same graph as line
parser = argparse.ArgumentParser(add_help=False)
subparsers = parser.add_subparsers(help='Command to execute.')
# Parser for plotall
parser_plotall = subparsers.add_parser('plotall', parents=[parser], help='type \'plotall -h\' for options')
parser_plotall.add_argument('--host', action='store', default='192.168.1.10', help='host for DB (default: 192.168.1.10).')
parser_plotall.add_argument('--port', action='store', type=int, default='3306', help='port on which the DB runs (default: 3306)')
parser_plotall.add_argument('--database', action='store', default='stromverbrauch', help='database to work with (default: stromverbrauch)')
parser_plotall.add_argument('--user', action='store', default='python_user', help='User for DB (default: python_user)')
parser_plotall.add_argument('--password', action='store', required=True, default='password', help='password for user against DB (default: password)')
parser_plotall.set_defaults(preis='0.123')
parser_plotall.set_defaults(command='plotall')
# Parser for gettable
parser_gettable = subparsers.add_parser('gettable', parents=[parser], help='type \'gettable -h\' for options')
parser_gettable.add_argument('--host', action='store', default='192.168.1.10', help='host for DB (default: 192.168.1.10).')
parser_gettable.add_argument('--database', action='store', default='stromverbrauch', help='database to work with (default: stromverbrauch)')
parser_gettable.add_argument('--port', action='store', type=int, default='3306', help='port on which the DB runs (default: 3306)')
parser_gettable.add_argument('--user', action='store', default='python_user', help='User for DB (default: python_user)')
parser_gettable.add_argument('--password', action='store', required=True, default='password', help='password for user against DB (default: password)')
parser_gettable.add_argument('--table', action='store', required=True, help='table to work with (default: None)')
parser_gettable.set_defaults(preis='0.123')
parser_gettable.set_defaults(command='gettable')
# Parser for addone
parser_addone = subparsers.add_parser('addone', parents=[parser], help='type \'addone -h\' for options')
parser_addone.add_argument('--host', action='store', default='192.168.1.10', help='host for DB (default: 192.168.1.10).')
parser_addone.add_argument('--database', action='store', default='stromverbrauch', help='database to work with (default: stromverbrauch)')
parser_addone.add_argument('--port', action='store', type=int, default='3306', help='port on which the DB runs (default: 3306)')
parser_addone.add_argument('--user', action='store', default='python_user', help='User for DB (default: python_user)')
parser_addone.add_argument('--password', action='store', required=True, default='password', help='password for user against DB (default: password)')
parser_addone.add_argument('--table', action='store', required=True, choices=['wasser', 'stromsonst', 'waermepumpe'], help='table to work with (default: None)')
datum_tmp=datetime.date.today()
default_datum = str(datum_tmp.year) + '-' + str('{:02d}'.format(datum_tmp.month)) + '-01'
parser_addone.add_argument('--datum', action='store', default=default_datum, help='datum to work with (defaults to the 1st of the current month: ' + default_datum + ')')
parser_addone.add_argument('--zaehlerstand', action='store', required=True, default='12345.67', type=float, help='zaehlerstand to work with (default: 12345.67)')
#parser_addone.add_argument('--preis', action='store', required=True, default='0.123', type=float, help='preis to work with (wasser: 1.8032, stromsonst: 0.2463, waermepumpe: 0.1903; default: 0.123)')
parser_addone.add_argument('--preis', action='store', type=float, help='preis to work with (wasser: 1.8032, stromsonst: 0.2463, waermepumpe: 0.1903; default: 0.123)')
parser_addone.set_defaults(command='addone')
# Parser for delone
parser_delone = subparsers.add_parser('delone', parents=[parser], help='type \'delone -h\' for options')
parser_delone.add_argument('--host', action='store', default='192.168.1.10', help='host for DB (default: 192.168.1.10).')
parser_delone.add_argument('--database', action='store', default='stromverbrauch', help='database to work with (default: stromverbrauch)')
parser_delone.add_argument('--port', action='store', type=int, default='3306', help='port on which the DB runs (default: 3306)')
parser_delone.add_argument('--user', action='store', default='python_user', help='User for DB (default: python_user)')
parser_delone.add_argument('--password', action='store', required=True, default='password', help='password for user against DB (default: password)')
parser_delone.add_argument('--table', action='store', required=True, help='table to work with (default: wasser)')
parser_delone.add_argument('--datum', action='store', required=True, default=default_datum, help='datum to work with (defaults to the 1st of the current month: ' + default_datum + ')')
parser_delone.set_defaults(preis='0.123')
parser_delone.set_defaults(command='delone')
# Parser for examples
parser_examples = subparsers.add_parser('examples', parents=[parser], help='Examples for usage.')
parser_examples.set_defaults(preis='0.123')
parser_examples.set_defaults(command='examples')
#args = parser.parse_args(parser_plotall)

args = parser.parse_args()
if args.preis == None:
    print('===> NOTE: --preis not specified; using pre-defined values.')
    if args.table == 'wasser':
        #args.preis = 1.8032
        args.preis = 1.9963  # 1.9963 (von Rechnung)
    elif args.table == 'stromsonst':
        # change on 1.5.2021: 0.2683      # laut letzter Preisänderung (5/2021)
        #args.preis = 0.2651               # 22,41 (von letzter Rechnung)
        # change on 1.11.2022
        args.preis = 0.3176
    elif args.table == 'waermepumpe':
        # change on 1.5.2021: 0.2191      # laut letzter Preisänderung (5/2021);
        #args.preis = 0.2123               # 17,48 (von letzter Rechnung)
        # change on 1.11.2022
        args.preis = 0.2683

if args.command == 'plotall':
    print('===> plotall')
    sfunc.plotall(args)
elif args.command == 'gettable':
    print('===> gettable')
    sfunc.gettable(args)
elif args.command == 'addone':
    print('===> addone')
    sfunc.addone(args)
elif args.command == 'delone':
    print('===> delone')
    sfunc.delone(args)
elif args.command == 'updateone':
    print('===> updateone')
elif args.command == 'examples':
    print('===> examples')
    sfunc.examples(args)
else:
    print('===> Wrong command.')
    sys.exit()

