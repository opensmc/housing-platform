CREATION_SQL = """
CREATE TABLE municipality(
  municipality_id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE status(
  status_id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE permits(
  permit_id INTEGER PRIMARY KEY,
  request_date DATETIME,
  issue_date DATETIME NOT NULL,
  completion_date DATETIME,
  applicant VARCHAR(255),
  approving_authority VARCHAR(255)
);

CREATE TABLE permit_ids(
  municipality_id INTEGER,
  external_id INTEGER,
  permit_id INTEGER UNIQUE,
  status_id INTEGER,
  PRIMARY KEY(municipality_id, external_id),
  FOREIGN KEY(municipality_id) REFERENCES municipality(municipality_id),
  FOREIGN KEY(status_id) REFERENCES status(status_id),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id)
);

CREATE TABLE properties(
  APN VARCHAR(255),
  municipality_id INTEGER,
  street_address VARCHAR(255) NOT NULL,
  unit_number VARCHAR(255),
  postal_code VARCHAR(20) NOT NULL,
  property_size VARCHAR(255),
  PRIMARY KEY (APN, municipality_id),
  FOREIGN KEY (municipality_id) REFERENCES municipality(municipality_id)
);

CREATE TABLE housing_type(
  housing_type_id INTEGER PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE planned(
  permit_id INTEGER,
  APN VARCHAR(255),
  housing_type_id INTEGER,
  units INTEGER,
  rate VARCHAR(255),
  date_planned DATETIME,
  PRIMARY KEY(permit_id, APN, housing_type_id),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id),
  FOREIGN KEY(housing_type_id) REFERENCES housing_type(housing_type_id),
  FOREIGN KEY(APN) REFERENCES properties(APN)
);

CREATE TABLE completed(
  permit_id INTEGER,
  APN VARCHAR(255),
  housing_type_id INTEGER,
  units INTEGER,
  rate VARCHAR(255),
  date_planned DATETIME,
  PRIMARY KEY(permit_id, APN, housing_type_id),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id),
  FOREIGN KEY(housing_type_id) REFERENCES housing_type(housing_type_id),
  FOREIGN KEY(APN) REFERENCES properties(APN)
);
"""