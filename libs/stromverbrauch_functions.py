#!/usr/bin/python3

import sys

# extend the search path for my module 'db_access' and the functions
#sys.path.append('/home/eddgest/PycharmProjects/stromverbrauch/libs')
sys.path.append('/home/eddgest/.local/lib/python3.6/site-packages/stromverbrauch')
#import stromverbrauch.db_access
import db_access
import pandas as pd


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
    datum, kosten_stromsonst = stromverbrauch.getxy("stromsonst")
    datum, kosten_waermepumpe = stromverbrauch.getxy("waermepumpe")
    datum, kosten_wasser = stromverbrauch.getxy("wasser")
    return datum, kosten_wasser, kosten_stromsonst, kosten_waermepumpe


def merge_df(df1, df2):
    '''Merge (concatonate) two data-frames. Return the result.
    '''
    dfresult = pd.concat([df1, df2], sort=False, axis=1)
    return dfresult
