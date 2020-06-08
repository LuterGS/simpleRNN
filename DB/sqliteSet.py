import datetime
import sqlite3
from customLibrary import library


def get_db_data(type="kospi", past=25):

    date = library.get_pastdays_as_list(datetime.datetime.now())

