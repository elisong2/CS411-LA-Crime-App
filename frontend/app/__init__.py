"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader
import pandas as pd
import pymysql


def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )
    return pool


app = Flask(__name__)
db = init_connection_engine()

conn = db.connect()
# Crime_status = pd.read_sql_table('Crime_status', conn)
# Crime_Type = pd.read_sql_table('Crime_Type', conn)
# Event = pd.read_sql_table('Event', conn)
# LAPD_Area = pd.read_sql_table('LAPD_Area', conn)
# Premise = pd.read_sql_table('Premise', conn)


# Premise = conn.execute("Select * from Premise;").fetchall()


conn.close()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
