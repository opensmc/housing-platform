INSERT_CITY_SQL = "INSERT INTO municipality (name) VALUES ('{name}')"

SELECT_CITY_SQL = "SELECT municipality_id FROM municipality WHERE name = ('{name}')"

INSERT_HOUSING_TYPE_SQL = ("INSERT INTO housing_type(name) "
                           "VALUES ('{name}')")

SELECT_HOUSING_TYPE_SQL = ("SELECT housing_type_id FROM housing_type "
                           "WHERE name = '{name}'")
