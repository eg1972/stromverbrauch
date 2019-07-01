#!/usr/bin/python3

# https://www.tutorialspoint.com/python/python_database_access.htm
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
# http://www.mysqltutorial.org/python-mysql/

# import MySQLdb
# import mysql.connector
import sqlalchemy
import sys
import pandas as pd


class db_access():
    def __init__(self, arg):
        '''
        Initialising instance with a dict
        uri = 'mysql+mysqldb://python_user:0Vfe-ims7@192.168.1.10:3306/stromverbrauch'
        strom_dict = {
            'host': '127.0.0.1',
            'database': 'stromverbrauch',
            'user': 'python_user',
            'password': '0Vfe-ims7'
        }
        stromverbrauch = db_access.db_access(strom_dict)
        stromverbrauch = db_access.db_access(uri)
        '''
        if type(arg) is dict:
            self.host = arg.get('host')
            self.port = arg.get('port')
            self.database = arg.get('database')
            self.user = arg.get('user')
            self.password = arg.get('password')
            self.timeout = 5
            self.uri = 'mysql+mysqldb://' + self.user + ':' + self.password + '@' + self.host + ':' + str(
                self.port) + '/' + self.database
            try:
                print("===> Connecting to Database with dict.", arg)
                # create an engine
                engine = sqlalchemy.create_engine(self.uri, echo=False)
                self.metadata = sqlalchemy.MetaData(engine)
                # connect to the DB
                self.conn = engine.connect()
                print('===> Connected.')
            except sqlalchemy.exc.OperationalError as e:
                print('===> ERROR\n', e)
                sys.exit()
        elif type(arg) is str:
            try:
                self.uri = arg
                print("===> Connecting to Database with URI: ", self.uri)
                # create an engine
                engine = sqlalchemy.create_engine(self.uri, echo=False)
                self.metadata = sqlalchemy.MetaData(engine)
                # connect to the DB
                self.conn = engine.connect()
                print('===> Connected.')
            except sqlalchemy.exc.OperationalError as e:
                print('===> ERROR\n', e)
                sys.exit()
        else:
            print(arg)
            print('===> ERROR: construction needs to be with an URI or a dict')
            # sys.exit()

    def close_db(self):
        '''
        Closing the DB-handle for this instance
        '''
        print("===> Closing Database Connection...")
        self.conn.close()
        # if self.conn.is_connected():
        #    self.conn.close()
        #    if self.conn.is_connected() == False:
        #        print('Closed.')
        # return 'closed';

    def execute_query(self, query):
        '''Execute a query.
            Returns EMPTY on error. '''
        rows = ['EMPTY']
        try:
            print("===> Query: ", query)
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
        except sqlalchemy.exc.OperationalError as e:
            print('===> ERROR\n', e)
        finally:
            cursor.close()
        return rows;

    def getone(self, dictArg):
        '''Get (one) row(s) from a table based on the date.
        query_dict = {
            'table': 'waermepumpe',
            'datum': '2018-04-01',
        }
        rows = stromverbrauch.getone(query_dict)
        '''
        table = dictArg.get('table')
        datum = dictArg.get('datum')
        query = "SELECT * FROM " + table + " where datum=\"" + datum + "\""
        rows = self.execute_query(query)
        return rows;

    def getxy(self, table):
        '''Get datum and kosten rows from a table.
        datum,kosten_stromsonst = stromverbrauch.getxy("stromsonst")
        '''
        query = "SELECT datum,kosten FROM " + table + ";"
        rows = self.execute_query(query)
        datum = list()
        kosten = list()
        i = 0
        for row in rows:
            datum.append(row[0])
            kosten.append(row[1])
            i = i + 1
        return datum, kosten;

    def getall(self, table):
        '''Get datum and kosten rows from a table.
            ident, datum, zaehlerstand, verbrauch, preis, kosten = stromverbrauch.getall(stromsonst)
        '''
        query = "SELECT * FROM " + table + ";"
        rows = self.execute_query(query)
        ident = list()
        datum = list()
        zaehlerstand = list()
        verbrauch = list()
        preis = list()
        kosten = list()
        for row in rows:
            # print(row[3])
            ident.append(row[0])
            datum.append(row[1])
            zaehlerstand.append(row[2])
            verbrauch.append(row[3])
            preis.append(row[4])
            kosten.append(row[5])
        return ident, datum, zaehlerstand, verbrauch, preis, kosten;

    def getall_df(self, table):
        '''Get datum and kosten rows from a table as a pandas data-frame.
        The data-frame includes: zaehlerstand, verbrauch, preis, kosten
        df = stromverbrauch.getall_df(stromsonst)
        '''
        print('===> Constructing data-frame from ', table)
        ident, datum, zaehlerstand, verbrauch, preis, kosten = self.getall(table)
        df = pd.DataFrame(
            {'Zaehlerstand-' + table: zaehlerstand, 'Verbrauch-' + table: verbrauch, 'Preis-' + table: preis,
             'Kosten-' + table: kosten}, index=datum)
        return df

    def merge_df(self, df1, df2):
        '''Merge (concatonate) two data-frames. Return the result.
        '''
        dfresult = pd.concat([df1, df2], sort=False, axis=1)
        return dfresult

    def getlastrow(self, table):
        '''Get last row a table.
            row = stromverbrauch.getlastrow("stromsonst")
        '''
        query = "SELECT * FROM " + table + ";"
        rows = self.execute_query(query)
        row = rows[-1]
        return row;

    def addone(self, dictArg):
        '''Add one row to the database.
        query_dict = {
            'table': 'waermepumpe',
            'datum': '2018-04-01',
            'zaehlerstand': 12345.67,
            'preis': 0.123,
        }
        result = stromverbrauch.addone(query_dict)
        '''
        table = dictArg.get('table')
        datum = dictArg.get('datum')
        zaehlerstand = str(dictArg.get('zaehlerstand'))
        preis = str(dictArg.get('preis'))

        try:
            sqltable = sqlalchemy.Table(table, self.metadata, autoload=True)
            rinsert = sqltable.insert()
            rinsert.execute(datum=datum, zaehlerstand=zaehlerstand, preis=preis)
            result = True
        except sqlalchemy.exc.SQLAlchemyError as e:
            print('===> ERROR\n', e)
            result = False
        return result;

    def delone(self, dictArg):
        '''Delete one row from the database.
        query_dict = {
            'table': 'waermepumpe',
            'datum': '2018-04-01',
        }
        result = stromverbrauch.addone(query_dict)
        delete from stromsonst where datum="2019-05-01";
        '''
        table = dictArg.get('table')
        datum = dictArg.get('datum')
        try:
            # delete from a table
            sqltable = sqlalchemy.Table(table, self.metadata, autoload=True)
            rdelete = sqltable.delete(sqltable.c.datum == datum)
            rdelete.execute()
            result = True
        except sqlalchemy.exc.SQLAlchemyError as e:
            print('===> ERROR\n', e)
            result = False
        return result;

    def updateone(self, dictArg):
        # update waermepumpe set zaehlerstand=15309.88 where datum="2019-04-01";
        pass

