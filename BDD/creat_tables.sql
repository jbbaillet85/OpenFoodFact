CREATE TABLE IF NOT EXISTS Category (
category_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
category_name VARCHAR(45) NOT NULL)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Store(
store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
store_name VARCHAR(150) NOT NULL)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Food(
food_id SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
food_name VARCHAR(100) NOT NULL,
food_nutriscore VARCHAR(10) NOT NULL,
food_urlOFF TEXT(100) NOT NULL,
category SMALLINT NOT NULL,
store SMALLINT,
CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(category_id),
CONSTRAINT fk_store_id FOREIGN KEY (store) REFERENCES Store(store_id))
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Substitute(
id_substitute SMALLINT,
id_substited SMALLINT,
CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(food_id),
CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(food_id))
ENGINE=InnoDB;