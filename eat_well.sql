CREATE DATABASE eat_well CHARACTER SET 'utf8';

CREATE USER jbbaillet@localhost IDENTIFIED WITH mysql_native_password BY "iotebeta85";
GRANT ALL ON eat-well.* TO jbbaillet@localhost;
FLUSH PRIVILEGES;


USE eat_well;

CREATE TABLE IF NOT EXISTS Category (
    id_category SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(12)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Store(
    id_store SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Nutriscore(
    id_nutriscore SMALLINT,
    score VARCHAR(1)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Food(
    id_food SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_food VARCHAR(20),
    category SMALLINT NOT NULL,
    ingredients TEXT,
    nutriscore SMALLINT,
    store SMALLINT,
    urlOFF TEXT(100),
    CONSTRAINT fk_nutriscore_id FOREIGN KEY (nutriscore) REFERENCES Nutriscore(id_nutriscore),
    CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(id_category),
    CONSTRAINT fk_store_id FOREIGN KEY(store) REFERENCES Store(store)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT ,
    id_substited SMALLINT ,
    CONSTRAINT fk_substitute FOREIGN KEY(substitute) REFERENCES Food(id_food),
    CONSTRAINT fk_substituted FOREIGN KEY(substituted) REFERENCES Food(id_food)
)
ENGINE=InnoDB;