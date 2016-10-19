import sqlite3

from housing_platform.queries import INSERT_CITY_SQL
from housing_platform.queries import SELECT_CITY_SQL
from housing_platform.queries import INSERT_HOUSING_TYPE_SQL
from housing_platform.queries import SELECT_HOUSING_TYPE_SQL
from housing_platform.queries import SELECT_STATUS_SQL
from housing_platform.queries import INSERT_STATUS_SQL


class HousingBackend():
    """
    This class should hold basically all of the handlers that
    operate on SQL.
    """

    def __init__(self, sql_filename):

        self.conn = sqlite3.connect(sql_filename)
        self.cursor = self.conn.cursor()


    def select_single(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]


    def insert_city(self, city_name):
        self.cursor.execute(INSERT_CITY_SQL.format(name=city_name))

    def select_city_id(self, city_name):
        return self.select_single(SELECT_CITY_SQL.format(name=city_name))

    def insert_housing_type(self, housing_type):
        housing_type = housing_type.lower()
        self.cursor.execute(INSERT_HOUSING_TYPE_SQL.format(name=housing_type))

    def select_housing_type_id(self, housing_type):
        housing_type = housing_type.lower()
        return self.select_single(
            SELECT_HOUSING_TYPE_SQL.format(name=housing_type)
        )

    def insert_status(self, status_name):
        status_name = status_name.lower()
        self.cursor.execute(INSERT_STATUS_SQL.format(name=status_name))

    def select_status_id(self, status_name):
        status_name = status_name.lower()
        return self.select_single(
            SELECT_STATUS_SQL.format(name=status_name)
        )
