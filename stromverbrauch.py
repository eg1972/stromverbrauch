#!/usr/bin/python3

import sys
# extend the search path for my module 'db_access' and the functions
sys.path.append('/home/eddgest/PycharmProjects/stromverbrauch/libs')
#import db_access
#functions for this program
import stromverbrauch_functions as sfunc

#for matplotlib
#import numpy as np
import matplotlib.pyplot as plt
# for Pandas DataFrame
import pandas as pd
# for argparse
import argparse
import textwrap
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
        args.preis = 1.8032
    elif args.table == 'stromsonst':
        args.preis = 0.2463
    elif args.table == 'waermepumpe':
        args.preis = 0.1903

if args.command == 'plotall':
    print('===> plotall')
    stromverbrauch = sfunc.connect_db(args)
    datum, kosten_wasser, kosten_stromsonst, kosten_waermepumpe = sfunc.get_plotdata(stromverbrauch)
    stromverbrauch.close_db()
    # construct Pandas DF and plot
    data = {'Kosten Wasser': kosten_wasser, 'Kosten Haushaltsstrom': kosten_stromsonst, 'Kosten Wärmepumpe': kosten_waermepumpe}
    index = datum
    try:
        df = pd.DataFrame(data, index)
    except:
        print('===> ERROR: could not construct Pandas DataFrame')
        sys.exit()
    df.plot(kind='bar',stacked='True')
    plt.title("Stromverbrauch Steinwachs")
    plt.xlabel('Zeit')
    plt.ylabel('Kosten')
    plt.show()
elif args.command == 'gettable':
    print('===> gettable')
    stromverbrauch = sfunc.connect_db(args)
    ident, datum, zaehlerstand, verbrauch, preis, kosten = stromverbrauch.getall(args.table)
    stromverbrauch.close_db()
    # construct Pandas DF and plot
    data = {'ID': ident, 'Datum': datum, 'Zaehlerstand': zaehlerstand, 'Verbrauch': verbrauch, 'Preis': preis, 'Kosten': kosten}
    try:
        df = pd.DataFrame(data)
        print(df)
    except:
        print('===> ERROR: could not construct Pandas DataFrame')
        sys.exit()
elif args.command == 'addone':
    print('===> addone')
    try:
        #print('===> addone: connecting to DB...')
        stromverbrauch = sfunc.connect_db(args)
    except:
        print('===> ERROR: could not init stromverbrauch from sfunc.connect_db(args). Try \'... -h\'')
        sys.exit()
    #print('===> addone: getting last row...')
    row = stromverbrauch.getlastrow(args.table)
    index_old, datum_old, zaehlerstand_old, verbrauch_old, verbrauch_old, kosten_old = row
    verbrauch = float(args.zaehlerstand) - zaehlerstand_old
    kosten = verbrauch*float(args.preis)
    query_dict = {
        'table': args.table,
        'datum': args.datum,
        'zaehlerstand': args.zaehlerstand,
        'verbrauch': verbrauch,
        'preis': args.preis,
        'kosten': kosten
    }
    if verbrauch <= 0:
      print('===> ERROR: verbrauch < 0 (',verbrauch,'): check your parameters. Last entry: ', zaehlerstand_old)
      print('===> current parameters: ',query_dict)
      print('===> previous row: ',rows[-1])
      sys.exit()
    # all checks pass... execute query
    #print('===> addone: adding new row...')
    #print(query_dict)
    result = stromverbrauch.addone(query_dict)
    if result==False:
      print('===> ERROR: addone() failed. Check your parameters.')
    print('===> NOTE: Result from addone(): ',result)
    stromverbrauch.close_db()
elif args.command == 'delone':
    print('===> delone')
    stromverbrauch = sfunc.connect_db(args)
    query_dict = {
        'table': args.table,
        'datum': args.datum,
    }
    result = stromverbrauch.delone(query_dict)
    if result==False:
      print('===> ERROR: addone() failed. Check your parameters.')
    print('===> NOTE: Result from addone(): ',result)
    stromverbrauch.close_db()
elif args.command == 'updateone':
    print('===> updateone')
elif args.command == 'examples':
    print('===> examples')
    print(
      '''
Script to add, get and plot values from the stromverbrauch database.
Examples:
./stromverbrauch_v7.py plotall --password 0Vfe-ims7 --host 127.0.0.1
./stromverbrauch_v7.py plotall --password 0Vfe-ims7 --user python_user --database stromverbrauch
./stromverbrauch_v7.py addone --table wasser --password 0Vfe-ims7 --host 127.0.0.1 --datum 2019-05-01 --zaehlerstand 22345.67
./stromverbrauch_v7.py addone --host 192.168.1.10 --table wasser --password 0Vfe-ims7 --zaehlerstand 649
./stromverbrauch_v7.py delone --table wasser --password 0Vfe-ims7 --host 127.0.0.1 --datum 2019-05-01
./stromverbrauch_v7.py delone --table wasser --password 0Vfe-ims7 --host 192.168.1.10 --datum 2019-05-01
./stromverbrauch_v7.py gettable --table wasser --password 0Vfe-ims7 --host 127.0.0.1
./stromverbrauch_v7.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10

Each month:
stromverbrauch_v7.py addone --host 192.168.1.10 --table wasser --password 0Vfe-ims7 --zaehlerstand 649
stromverbrauch_v7.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10|tail
stromverbrauch_v7.py addone --host 192.168.1.10 --table stromsonst --password 0Vfe-ims7 --zaehlerstand 17553.98
stromverbrauch_v7.py gettable --table stromsonst --password 0Vfe-ims7 --host 192.168.1.10|tail
stromverbrauch_v7.py addone --host 192.168.1.10 --table waermepumpe --password 0Vfe-ims7 --zaehlerstand 15456.76
stromverbrauch_v7.py gettable --table waermepumpe --password 0Vfe-ims7 --host 192.168.1.10|tail

To quickly create a DB:
    mysqldump --lock-tables -h 192.168.1.10 -u python_user -p0Vfe-ims7 stromverbrauch > /mnt/data-aldi-admin/gereon/backup/mysql-backup/stromverbrauch-dbbackup_NUC_`date +"%Y%m%d"`.bak
    docker run --publish 127.0.0.1:3306:3306 --name mariadb -e MYSQL_ROOT_PASSWORD=0Vfe-ims7 -d mariadb:latest

    mysql -h"127.0.0.1" -P"3306" -u"root" -p"0Vfe-ims7"
    create database stromverbrauch;
    create user 'python_user'@'%' identified by '0Vfe-ims7';
    grant all privileges on stromverbrauch.* to 'python_user'@'%' identified by '0Vfe-ims7';
    flush privileges;
    use stromverbrauch;
    source python_test-dbbackup_NUC_20190412.bak

    show grants for 'python_user'@'%';

    mysql -h"127.0.0.1" -P"3306" -u"python_user" -p"0Vfe-ims7" stromverbrauch
    show grants;
    show triggers;
''')
else:
    print('===> Wrong command.')
    sys.exit()

