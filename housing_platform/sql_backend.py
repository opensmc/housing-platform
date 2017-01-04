import sqlite3

from housing_platform.queries import INSERT_CITY_SQL
from housing_platform.queries import SELECT_CITY_SQL
from housing_platform.queries import INSERT_HOUSING_TYPE_SQL
from housing_platform.queries import SELECT_HOUSING_TYPE_SQL
from housing_platform.queries import SELECT_STATUS_SQL
from housing_platform.queries import INSERT_STATUS_SQL
from housing_platform.queries import SELECT_APN_SQL
from housing_platform.queries import INSERT_APN_SQL
from housing_platform.queries import CREATE_PERMIT_SQL
from housing_platform.queries import CREATE_PERMIT_DATA_SQL
from housing_platform.queries import SELECT_PERMIT_DATA_SQL


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

    def format_fetchone(self):
        row = self.cursor.fetchone()
        result = {}
        for idx, col in enumerate(self.cursor.description):
            result[col[0]] = row[idx]
        return result
    
    def insert_city(self, city_name):
        city_name = city_name.lower()
        self.cursor.execute(INSERT_CITY_SQL.format(name=city_name))

    def select_city_id(self, city_name):
        city_name = city_name.lower()
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

    def insert_apn(
            self,
            apn,
            city_name,
            street_address=None,
            unit_number=None,
            postal_code=None,
            property_size=None
    ):
        """
        Insert a new APN. Depends on a pre-existing city.
        """

        city_name = city_name.lower()
        self.cursor.execute(
            INSERT_APN_SQL,
            dict(
                APN=apn,
                city_name=city_name,
                street_address=street_address,
                unit_number=unit_number,
                postal_code=postal_code,
                property_size=property_size,
            ),
        )

    def select_apn(self, apn, city_name):
        city_name = city_name.lower()
        # TODO Handle missing city
        municipality_id = self.select_city_id(city_name=city_name)
        self.cursor.execute(
            SELECT_APN_SQL,
            dict(
                APN=apn,
                city_name=city_name,
                ),
            )
        return self.format_fetchone()


    def create_permit(self, permit_id, city_name):
        """
        Create a new permit. This does NOT have to be a unique
        permit_id and municipality.
        """

        city_name = city_name.lower()
        self.cursor.execute(
            CREATE_PERMIT_SQL,
            dict(
                permit_id=permit_id,
                city_name=city_name,
            ),
        )


    def add_permit_data(
            self, permit_id, city_name, status,
            project_name=None, tenure=None,
            assistance_programs=None,
            request_date=None, issue_date=None,
            completion_date=None, applicant=None,
            approving_authority=None
    ):
        """
        Add all the data for a permit. Try to organize it.
        """
        city_name = city_name.lower()
        self.cursor.execute(
            CREATE_PERMIT_DATA_SQL,
            dict(
                external_id=permit_id,
                city_name=city_name,
                status=status,
                project_name=project_name,
                tenure=tenure,
                assistance_programs=assistance_programs,
                request_date=request_date,
                issue_date=issue_date,
                completion_date=completion_date,
                applicant=applicant,
                approving_authority=approving_authority,
            ),
        )

        
    def get_permit_data(self, permit_id, city_name):
        """
        Permit Data is returned in a giant chunk.
        """
        city_name = city_name.lower()

        self.cursor.execute(
            SELECT_PERMIT_DATA_SQL,
            dict(
                external_id=permit_id,
                city_name=city_name,
                )
            )
        fetched = self.cursor.fetchone()
        descriptions = [x[0] for x in self.cursor.description]
        result = dict(zip(descriptions, fetched))
        return result

        

        
