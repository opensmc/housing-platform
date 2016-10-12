import pytest
import sqlite3
import os.path
import tempfile
from schema.sql_schema import CREATION_SQL
from housing_platform.sql_backend import HousingBackend


def create_backend(sql_file):

    connection = sqlite3.connect(sql_file)
    cursor = connection.cursor()
    cursor.executescript(CREATION_SQL)
    connection.commit()
    connection.close()


def test_init():
    """
    Simple test to make sure that my initialization works.
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        sql_filename = os.path.join(temp_dir, 'test.sql')
        create_backend(sql_file=sql_filename)
        backend = HousingBackend(sql_filename=sql_filename)

    

