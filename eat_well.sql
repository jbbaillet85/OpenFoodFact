CREATE DATABASE eat_well CHARACTER SET 'utf8';

CREATE USER jbbaillet@localhost IDENTIFIED BY iotebeta85;
GRANT ALL ON eat-well.* TO jbbaillet@localhost;
FLUSH PRIVILEGES;

USE eat_well;

CREATE TABLE IF NOT EXISTS Category (
    id_category SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(12)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Shop(
    id_shop SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
    shop SMALLINT,
    urlOFF URL,
    CONSTRAINT fk_nutriscore_id FOREIGN KEY (nutriscore) REFERENCES Nutriscore(id_nutriscore)
    CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(id_category),
    CONSTRAINT fk_shop_id FOREIGN KEY(shop) REFERENCES Shop(id_shop)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_food VARCHAR(12),
    category SMALLINT,
    ingredients TEXT,
    nutriscore VARCHAR(1),
    urlOFF URL
    shop SMALLINT

)
ENGINE=InnoDB;