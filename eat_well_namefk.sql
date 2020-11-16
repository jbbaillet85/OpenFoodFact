CREATE DATABASE eat_well CHARACTER SET 'utf8';

CREATE USER jbbaillet@localhost IDENTIFIED WITH mysql_native_password BY "iotebeta85";
GRANT ALL ON eat-well.* TO jbbaillet@localhost;
FLUSH PRIVILEGES;

USE eat_well;

CREATE TABLE IF NOT EXISTS Category (
    category_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    category_name VARCHAR(12) NOT NULL
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Store(
    store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    store_name VARCHAR(20) NOT NULL
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Food(
    id_food SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_food VARCHAR(20) NOT NULL,
    nutriscore VARCHAR(1) NOT NULL,
    urlOFF TEXT(100) NOT NULL,
    category VARCHAR(12) NOT NULL,
    store VARCHAR(20),
    CONSTRAINT fk_category_name FOREIGN KEY (category) REFERENCES Category(category_name),
    CONSTRAINT fk_store_name FOREIGN KEY (store) REFERENCES Store(store_name)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT,
    id_substited SMALLINT,
    CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(id_food),
    CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(id_food)
)
ENGINE=InnoDB;