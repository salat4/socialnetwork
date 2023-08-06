#!/usr/bin/python
import psycopg2

from config.config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

