# -*- coding:UTF-8 -*-
import math
import os
import sys
import psutil
import warnings

import pandas as pd
import pymongo
import requests


def in_severs():
    if sys.platform.startswith( 'linux' ):
        return True
    return False


def get_mongodb():
    return os.environ.get( 'MONGODB_URL' )


def get_db_info(db):
    db_evn = get_mongodb()
    bank_client = pymongo.MongoClient( db_evn )
    bank_col = bank_client['db-info']['raw_db']
    db_info = bank_col.find_one( {'_id': db} )
    if not db_info:
        db_info = bank_col.find_one( {'_id': '_key_'} )
        db_info['db'] = db
        del db_info['_id']
    return db_info


def df_creator(data, index=None, delitem=None):
    if delitem is None:
        delitem = []
    if index:
        df = pd.DataFrame( data, index=index )
    else:
        df = pd.DataFrame( data )
    for i in delitem:
        del df[i]
    return df


class DBWorker( object ):

    def __init__(self, db):
        """
        Initialize a MongoDB database worker.

        Args:
            db (str): The name of the database.
        """
        db_info = get_db_info( db )
        public_uri = os.environ.get( 'MONGODB_PUB_URI' )
        uri = db_info['uri'] if in_severs() else db_info['uri'].split( '@' )[0] + '@' + public_uri + ':' + \
                                                 db_info['uri'].split( ':' )[-1]
        self.db_code = db
        self.client = pymongo.MongoClient( uri )
        self.db = self.client[db_info['db']]
        self.col = {}

    def _link(self, col):
        if col not in self.col:
            self.col[col] = self.db[col]

    def link(self, col):
        """
        Get a reference to the specified collection in the database.

        Args:
            col (str): The name of the collection.

        Returns:
            pymongo.collection.Collection: The collection object.
        """
        self._link( col )
        return self.col[col]

    def get_col_stats(self, col):
        """
            Get the statistics of a collection in the database.

            Args:
                col (str): The name of the collection.

            Returns:
                dict: The statistics of the collection.
        """
        self._link( col )
        return self.db.command( 'collstats', col )

    def get_db_stats(self):
        """
              Get the statistics of the database.

              Returns:
                  dict: The statistics of the database.
        """
        return self.db.command( 'dbstats' )

    def get_cols_name(self):
        """
              Get the names of all collections in the database.

              Returns:
                  list: The names of the collections.
        """
        return self.db.list_collection_names()

    def _to_df_base(self, col: object, match: object = None, projection: object = None, sort: object = None,
                    skip: object = 0, limit: object = 0) -> object:
        self._link( col )
        return df_creator(
            list( self.col[col].find( filter=match, projection=projection, sort=sort, skip=skip, limit=limit ) ) )

    def _to_df_large(self, col: object, match: object = None, projection: object = None, verbose=True) -> object:
        """
            Convert a large collection into a DataFrame by splitting it into multiple parts.

            Args:
                col (str): The name of the collection.
                match (dict, optional): The query filter. Defaults to None.
                projection (dict, optional): The projection query. Defaults to None.
                verbose (bool, optional): Whether to display progress messages. Defaults to True.

            Returns:
                pandas.DataFrame: The DataFrame created from the collection data.
        """

        self._link( col )
        col_status = self.get_col_stats( col )
        st_size = col_status['size'] / 1024 ** 2
        st_count = col_status['count']
        n = math.ceil( st_size / 200 )
        step = math.ceil( st_count / n )

        if n > 1:
            if verbose:
                print(
                    '{col} has {count:,d} records, {size:,.2f} MB, split to {n} parts'.format( col=col, count=st_count,
                                                                                               size=st_size, n=n ) )
            mem = psutil.virtual_memory()
            if mem.total < col_status['size']:
                raise MemoryError( 'Not enough memory to process {col}'.format( col=col ) )

            if mem.available < col_status['size']:
                warnings.warn(
                    'Please note that there may be insufficient memory when reading the {col} in the current system environment.'.format(
                        col=col ) )

            dfs = []
            for i in range( n ):
                if verbose:
                    print( 'processing {i:>2d} part ...'.format( i=i + 1 ) )
                _df = self._to_df_base( col, match=match, projection=projection, skip=i * step, limit=step )
                dfs.append( _df )
            df = pd.concat( dfs )
            # df.drop_duplicates(subset=['_id'], inplace=True)
            # df.reset_index(inplace=True, drop=True)
            if verbose:
                print( 'done' )

        else:
            if verbose:
                print( '{col} has {count:,d} records, {size:,.2f} MB, processing ...'.format( col=col, count=st_count,
                                                                                              size=st_size ) )
            df = self._to_df_base( col, match=match, projection=projection )

        return df

    def to_df(self, col: str, match: dict = None, projection: dict = None, sort: str = None, skip: int = 0,
              limit: int = 0) -> pd.DataFrame:
        """
        Convert the data from a collection into a DataFrame.

        Args:
            col (str): The name of the collection.
            match (dict, optional): The query filter. Defaults to None.
            projection (dict, optional): The projection query. Defaults to None.
            sort (list, optional): The sort order. Defaults to None.
            skip (int, optional): The number of documents to skip. Defaults to 0.
            limit (int, optional): The maximum number of documents to return. Defaults to 0.

        Returns:
            pandas.DataFrame: The DataFrame created from the collection data.
        """

        if any( match, sort, projection, limit, skip ):
            return self._to_df_base( col, match, projection, sort, skip, limit )
        else:
            return self._to_df_large( col )

    def to_df_many(self, cols, match=None, projection=None):
        """
         Convert multiple collections into a single DataFrame.

         Args:
             cols (list): The names of the collections.
             match (dict, optional): The query filter. Defaults to None.
             projection (dict, optional): The projection query. Defaults to None.

         Returns:
             pandas.DataFrame: The DataFrame created from the collections' data.
         """
        dfs = [self.to_df( c, match=match, projection=projection ) for c in cols]
        df = pd.concat( dfs )
        df.reset_index( inplace=True, drop=True )
        return df

    def insert_df(self, df, col):
        """
          Insert a DataFrame into a collection.

          Args:
              df (pandas.DataFrame): The DataFrame to be inserted.
              col (str): The name of the collection.
        """
        self._link( col )
        data = df.to_dict( 'records' )
        self.col[col].insert_many( data )

    def update_df(self, df, col, key):
        """
            Update documents in a collection using data from a DataFrame.

            Args:
                df (pandas.DataFrame): The DataFrame containing the updated data.
                col (str): The name of the collection.
                key (str): The key field used to match and update documents.
        """
        self._link( col )
        data = df.to_dict( 'records' )
        # data = json.loads(df.T.to_json()).values()
        for r in data:
            self.col[col].update_one( {key: r[key]}, {'$set': r}, upsert=True )

    def collection_sample(self, col, sample_size=100):
        """
        Get a sample of documents from a collection.

        Args:
            col (str): The name of the collection.
            sample_size (int, optional): The number of documents to retrieve. Defaults to 100.

        Returns:
            pandas.DataFrame: The sampled data as a DataFrame.
        """
        self._link( col )
        return self.to_df( col, limit=sample_size )

    def data_insert(self, col, data):
        """
        Insert data into a collection.

        Args:
            col (str): The name of the collection.
            data (dict): The data to be inserted.
        """
        self._link( col )
        self.col[col].insert( data )

    def data_update(self, col, data):
        """
        Update data in a collection.

        Args:
            col (str): The name of the collection.
            data (dict): The data to be updated.
        """
        self._link( col )
        self.col[col].update( data )

    def drop_col(self, col):
        """
        Drop a collection from the database.

        Args:
            col (str): The name of the collection to be dropped.
        """
        self._link( col )
        self.col[col].dorp()


def _dblink():
    db_evn = get_mongodb()
    bank_client = pymongo.MongoClient( db_evn )
    bank_col = bank_client['db-info']['raw_db']
    return bank_col


def dblink(db, col):
    db_info = _dblink().find_one( {'_id': db} )
    client = pymongo.MongoClient( db_info['uri'] )
    db = client[db_info['db']]
    collection = db[col]
    return collection


def col_stats(db, col):
    db_info = _dblink().find_one( {'_id': db} )
    client = pymongo.MongoClient( db_info['uri'] )
    db = client[db_info['db']]
    return db.command( 'collstats', col )


def db_stats(db):
    db_info = _dblink().find_one( {'_id': db} )
    client = pymongo.MongoClient( db_info['uri'] )
    db = client[db_info['db']]
    return db.command( 'dbstats' )


def dblink_help(db=False):
    if db:
        db_info = _dblink().find_one( {'_id': db} )
        client = pymongo.MongoClient( db_info['uri'] )
        db = client[db_info['db']]
        return db.collection_names()
    else:
        dbs = _dblink().find()
        return [i['_id'] for i in dbs]


def df2mongo(df, col):
    data = df.to_dict( 'records' )
    col.insert_many( data )


def mongo2df(col, match=None, projection=None, sort=None, skip=0, limit=0):
    return df_creator( list( col.find( filter=match, projection=projection, sort=sort, skip=skip, limit=limit ) ) )


def collection_show(db, col):
    return mongo2df( dblink( db, col ), limit=100 )


def dblink_add(_id, uri, db=False):
    _dblink().insert( {'_id': _id, 'uri': uri, 'db': db if db is not False else uri.split( '/' )[-1]} )
    return _id in dblink_help()


def dblink_remove(_id):
    _dblink().remove( {'_id': _id} )


def dblink_update(_id, uri, db=False):
    _dblink().update( {'_id': _id}, {'uri': uri, 'db': db if db is not False else uri.split( '/' )[-1]} )


def get_token(job, on):
    db_evn = get_mongodb()
    bank_client = pymongo.MongoClient( db_evn )
    bank_col = bank_client['tk'][job]
    tk = bank_col.find_one( {'on': on} )
    return tk['token'], tk['servers']


def crawler_starter(db: str, col: str, work_on: str):
    db = get_db_info( db )['db']
    token, servers = get_token( 'crawler_starter', work_on.upper() )
    body = {"db": db, "table": col, "token": token}
    return requests.post( url=servers, json=body )


def log_db(data, db):
    db = DBWorker( db )
    col = db.link( 'log' )
    col.insert( data )


def read_log(db, _type):
    db = DBWorker( db )
    df = db.to_df( "log", match={"type": _type} )
    return df
