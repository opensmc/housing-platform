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

    
def test_insert_city():
    """
    Can we put in a municipality and read it?
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        sql_filename = os.path.join(temp_dir, 'test.sql')
        create_backend(sql_file=sql_filename)
        backend = HousingBackend(sql_filename=sql_filename)

        backend.insert_city(city_name='Happyville')
        city_id = backend.select_city_id(city_name='Happyville')
        assert city_id == 1


def test_insert_housing_type():
    """
    Can we insert and then select housing types?
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        sql_filename = os.path.join(temp_dir, 'test.sql')
        create_backend(sql_file=sql_filename)
        backend = HousingBackend(sql_filename=sql_filename)

        backend.insert_housing_type(housing_type='Below market')
        housing_id = backend.select_housing_type_id(housing_type='below market')
        assert housing_id == 1

        
def test_status():
    """
    Can we insert and get the ID for a status?
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        sql_filename = os.path.join(temp_dir, 'test.sql')
        create_backend(sql_file=sql_filename)
        backend = HousingBackend(sql_filename=sql_filename)

        backend.insert_status(status_name='Something')
        status_id = backend.select_status_id(status_name='something')
        assert status_id == 1


def test_apn():
    """
    APN insertion turns out to be the first of the complicated ones.
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        sql_filename = os.path.join(temp_dir, 'test.sql')
        create_backend(sql_file=sql_filename)
        backend = HousingBackend(sql_filename=sql_filename)

        backend.insert_city(city_name='Camelot')
        backend.insert_apn(apn='00001', city_name='Camelot')
        result = backend.select_apn(apn='00001', city_name='Camelot')
        print(result)
