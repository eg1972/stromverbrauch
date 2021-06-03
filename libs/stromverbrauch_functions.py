#!/usr/bin/python3

import sys

# extend the search path for my module 'db_access' and the functions
#sys.path.append('/home/eddgest/PycharmProjects/stromverbrauch/libs')
sys.path.append('/home/eddgest/.local/lib/python3.6/site-packages/stromverbrauch')
#import stromverbrauch.db_access
import db_access
import pandas as pd
#for matplotlib
import matplotlib.pyplot as plt

def connect_db(args):
    '''Connect to the DB
    args should contain:
        host
        port
        database
        user
        password
    '''
    strom_dict = {
        'host': args.host,
        'port': args.port,
        'database': args.database,
        'user': args.user,
        'password': args.password
    }
    # construct the class:
    #    db_access: class name from import
    #    .db_access: initialisation method
    stromverbrauch = db_access.db_access(strom_dict)
    return stromverbrauch;


def get_plotdata(stromverbrauch):
    ''' get datum and kosten rows from the tables'''
    print('===> get_plotdata():')
    datum, kosten_stromsonst = stromverbrauch.getxy("stromsonst", "Kosten")
    datum, kosten_waermepumpe = stromverbrauch.getxy("waermepumpe", "Kosten")
    datum, kosten_wasser = stromverbrauch.getxy("wasser", "Kosten")
    datum, verbrauch_stromsonst = stromverbrauch.getxy("stromsonst", "Verbrauch")
    datum, verbrauch_waermepumpe = stromverbrauch.getxy("waermepumpe", "Verbrauch")
    datum, verbrauch_wasser = stromverbrauch.getxy("wasser", "Verbrauch")
    return datum, kosten_wasser, kosten_stromsonst, kosten_waermepumpe, verbrauch_wasser, verbrauch_waermepumpe, verbrauch_stromsonst


def merge_df(df1, df2):
    '''Merge (concatonate) two data-frames. Return the result.
    '''
    dfresult = pd.concat([df1, df2], sort=False, axis=1)
    return dfresult

def plotall(args):
    stromverbrauch = connect_db(args)
    datum, kosten_wasser, kosten_stromsonst, kosten_waermepumpe, verbrauch_wasser, verbrauch_waermepumpe, verbrauch_stromsonst = get_plotdata(
        stromverbrauch)
    stromverbrauch.close_db()
    # construct Pandas DF and plot
    data = {'Kosten Wasser': kosten_wasser, 'Kosten Haushaltsstrom': kosten_stromsonst,
            'Kosten Wärmepumpe': kosten_waermepumpe}
    # data2 = {'datum': datum, 'Kosten Wasser': kosten_wasser, 'Kosten Haushaltsstrom': kosten_stromsonst, 'Kosten Wärmepumpe': kosten_waermepumpe}
    index = datum
    try:
        df = pd.DataFrame(data, index)
        df2 = pd.DataFrame({
            'datum': datum,
            'kosten_wasser': kosten_wasser,
            'kosten_stromsonst': kosten_stromsonst,
            'kosten_waermepumpe': kosten_waermepumpe
        })
    except:
        print('===> ERROR: could not construct Pandas DataFrame')
        sys.exit()
    #    df.plot(kind='bar',stacked='True')
    #    plt.title("Stromverbrauch Steinwachs")
    #    plt.xlabel('Zeit')
    #    plt.ylabel('Kosten')
    #    plt.show()
    ax = plt.gca()  # gca stands for 'get current axis'
    df.plot(kind='bar', stacked='True')
    df2.plot(kind='line', x='datum', y='kosten_wasser', ax=ax)
    df2.plot(kind='line', x='datum', y='kosten_stromsonst', ax=ax)
    df2.plot(kind='line', x='datum', y='kosten_waermepumpe', ax=ax)
    plt.xlabel('Zeit')
    plt.ylabel('Kosten')
    plt.show()

def gettable(args):
    stromverbrauch = connect_db(args)
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


def addone(args):
    offset_wasser = 845                                                                                                 # offset due to new counter
    offset_stromsonst = 26570
    offset_waermepumpe = 20802
    try:
        #print('===> addone: connecting to DB...')
        stromverbrauch = connect_db(args)
    except:
        print('===> ERROR: could not init stromverbrauch from sfunc.connect_db(args). Try \'... -h\'')
        sys.exit()
    #print('===> addone: getting last row...')
    row = stromverbrauch.getlastrow(args.table)
    index_old, datum_old, zaehlerstand_old, verbrauch_old, verbrauch_old, kosten_old = row
    if args.table == "wasser":                                                                                          # add offset to zaehlerstand
        zaehlerstand_mod = float(args.zaehlerstand) + offset_wasser
        verbrauch = zaehlerstand_mod - zaehlerstand_old
    elif args.table == "stromsonst":                                                                                    # add offset to zaehlerstand
        zaehlerstand_mod = float(args.zaehlerstand) + offset_stromsonst
        verbrauch = zaehlerstand_mod - zaehlerstand_old
    elif args.table == "waermepumpe":                                                                                   # add offset to zaehlerstand
        zaehlerstand_mod = float(args.zaehlerstand) + offset_waermepumpe
        verbrauch = zaehlerstand_mod - zaehlerstand_old
    else:
        zaehlerstand_mod = float(args.zaehlerstand)
        verbrauch = zaehlerstand_mod - zaehlerstand_old
    kosten = verbrauch*float(args.preis)
    # NOTE: verbrauch is calculated on the DB
    query_dict = {
        'table': args.table,
        'datum': args.datum,
        'zaehlerstand': zaehlerstand_mod,
        'verbrauch': verbrauch,
        'preis': args.preis,
        'kosten': kosten
    }
    if verbrauch <= 0:
      print('===> ERROR: verbrauch < 0 (',verbrauch,'): check your parameters. Last entry: ', zaehlerstand_old)
      print('===> current parameters: ',query_dict)
      sys.exit()
    # all checks pass... execute query
    #print('===> addone: adding new row...')
    #print(query_dict)
    result = stromverbrauch.addone(query_dict)
    if result==False:
      print('===> ERROR: addone() failed. Check your parameters.')
    print('===> NOTE: Result from addone(): ',result)
    stromverbrauch.close_db()

def delone(args):
    stromverbrauch = connect_db(args)
    query_dict = {
        'table': args.table,
        'datum': args.datum,
    }
    result = stromverbrauch.delone(query_dict)
    if result==False:
      print('===> ERROR: addone() failed. Check your parameters.')
    print('===> NOTE: Result from addone(): ',result)
    stromverbrauch.close_db()


def updateone(args):
    pass;

def examples(args):
    print(
        '''
  Script to add, get and plot values from the stromverbrauch database.
  Examples:
  ./stromverbrauch.py plotall --password 0Vfe-ims7 --host 127.0.0.1
  ./stromverbrauch.py plotall --password 0Vfe-ims7 --user python_user --database stromverbrauch
  ./stromverbrauch.py addone --table wasser --password 0Vfe-ims7 --host 127.0.0.1 --datum 2019-05-01 --zaehlerstand 22345.67
  ./stromverbrauch.py addone --host 192.168.1.10 --table wasser --password 0Vfe-ims7 --zaehlerstand 649
  ./stromverbrauch.py delone --table wasser --password 0Vfe-ims7 --host 127.0.0.1 --datum 2019-05-01
  ./stromverbrauch.py delone --table wasser --password 0Vfe-ims7 --host 192.168.1.10 --datum 2019-05-01
  ./stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 127.0.0.1
  ./stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10

  Each month:
  stromverbrauch.py addone --host 192.168.1.10 --table wasser --password 0Vfe-ims7 --zaehlerstand 649
  stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10|tail
  stromverbrauch.py addone --host 192.168.1.10 --table stromsonst --password 0Vfe-ims7 --zaehlerstand 17553.98
  stromverbrauch.py gettable --table stromsonst --password 0Vfe-ims7 --host 192.168.1.10|tail
  stromverbrauch.py addone --host 192.168.1.10 --table waermepumpe --password 0Vfe-ims7 --zaehlerstand 15456.76
  stromverbrauch.py gettable --table waermepumpe --password 0Vfe-ims7 --host 192.168.1.10|tail

  To quickly create a DB:
      mysqldump --lock-tables -h 192.168.1.10 -u python_user -p0Vfe-ims7 stromverbrauch > /mnt/data-aldi-admin/gereon/backup/mysql-backup/stromverbrauch-dbbackup_NUC_`date +"%Y%m%d"`.bak
      docker run --publish 127.0.0.1:3306:3306 --name mariadb -e MYSQL_ROOT_PASSWORD=12test34 -d mariadb:latest

      mysql -h"127.0.0.1" -P"3306" -u"root" -p"12test34"
      create database stromverbrauch;
      create user 'python_user'@'%' identified by '12test34';
      grant all privileges on stromverbrauch.* to 'python_user'@'%' identified by '12test34';
      flush privileges;
      use stromverbrauch;
      source python_test-dbbackup_NUC_20190412.bak

      show grants for 'python_user'@'%';

      mysql -h"127.0.0.1" -P"3306" -u"python_user" -p"12test34" stromverbrauch
      show grants;
      show triggers;
  ''')

