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

CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(12),
    description VARCHAR(200),
    url VARCHAR(30)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Shop(
    id_shop SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Food(
    id_food SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    CONSTRAINT fk_category_id FOREIGN KEY (id_category) REFERENCES Category(id),
    CONSTRAINT fk_substitute_id FOREIGN KEY (id_substitute) REFERENCES Substitute(id),
    CONSTRAINT fk_shop_id FOREIGN KEY(id_shop) REFERENCES Shop(id)
)
ENGINE=InnoDB;
