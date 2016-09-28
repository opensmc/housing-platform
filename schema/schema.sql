CREATE TABLE municipality(
  ID INTEGER,
  name VARCHAR(255),
  PRIMARY KEY (ID)
);

CREATE TABLE status(
  ID INTEGER,
  name VARCHAR(255),
  PRIMARY KEY (ID)
);

CREATE TABLE permits(
  permit_id INTEGER,
  request_date DATETIME,
  issue_date DATETIME NOT NULL,
  completion_date DATETIME,
  applicant VARCHAR(255),
  approving_authority VARCHAR(255),
  PRIMARY KEY(permit_id),
);

CREATE TABLE permit_ids(
  municipality INTEGER,
  external_id INTEGER,
  permit_id INTEGER UNIQUE,
  status INTEGER,
  PRIMARY KEY(municipality, external_id),
  FOREIGN KEY(municipality) REFERENCES municipality(ID),
  FOREIGN KEY(status) REFERENCES status(ID),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id)
);

CREATE TABLE properties(
  APN VARCHAR(255),
  municipality INTEGER,
  street_address VARCHAR(255) NOT NULL,
  unit_number VARCHAR(255),
  postal_code VARCHAR(20) NOT NULL,
  property_size VARCHAR(255),
  PRIMARY KEY (APN, municipality)
);

CREATE TABLE housing_type(
  ID INTEGER,
  name VARCHAR(255)
);

CREATE TABLE planned(
  permit_id INTEGER,
  APN VARCHAR(255),
  type INTEGER,
  units INTEGER,
  rate VARCHAR(255),
  date_planned DATETIME,
  PRIMARY KEY(permit_id, APN, type),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id),
  FOREIGN KEY(type) REFERENCES housing_type(ID),
  FOREIGN KEY(APN) REFERENCES properties(APN)
);

CREATE TABLE completed(
  permit_id INTEGER,
  APN VARCHAR(255),
  type INTEGER,
  units INTEGER,
  rate VARCHAR(255),
  date_planned DATETIME,
  PRIMARY KEY(permit_id, APN, type),
  FOREIGN KEY(permit_id) REFERENCES permits(permit_id),
  FOREIGN KEY(type) REFERENCES housing_type(ID),
  FOREIGN KEY(APN) REFERENCES properties(APN)
);

