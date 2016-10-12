import sqlite3

from housing_platform.queries import INSERT_CITY_SQL
from housing_platform.queries import SELECT_CITY_SQL
from housing_platform.queries import INSERT_HOUSING_TYPE_SQL
from housing_platform.queries import SELECT_HOUSING_TYPE_SQL


class HousingBackend():
    """
    This class should hold basically all of the handlers that
    operate on SQL.
    """

    def __init__(self, sql_filename):

        self.conn = sqlite3.connect(sql_filename)
        self.cursor = self.conn.cursor()


    def insert_city(self, city_name):
        self.cursor.execute(INSERT_CITY_SQL.format(name=city_name))

    def select_city_id(self, city_name):
        self.cursor.execute(SELECT_CITY_SQL.format(name=city_name))
        return self.cursor.fetchone()[0]

    def insert_housing_type(self, housing_type):
        housing_type = housing_type.lower()
        self.cursor.execute(INSERT_HOUSING_TYPE_SQL.format(name=housing_type))

    def select_housing_type_id(self, housing_type):
        self.cursor.execute(SELECT_HOUSING_TYPE_SQL.format(name=housing_type))
        return self.cursor.fetchone()[0]
