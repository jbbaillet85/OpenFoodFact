
        CREATE TABLE IF NOT EXISTS Category (
        category_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        category_name VARCHAR(12) NOT NULL)
        ENGINE = InnoDB;

        CREATE TABLE IF NOT EXISTS Store(
        store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        store_name VARCHAR(20) NOT NULL)
        ENGINE = InnoDB;

        CREATE TABLE IF NOT EXISTS Food(
        id_food SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name_food VARCHAR(20) NOT NULL,
        nutriscore VARCHAR(1) NOT NULL,
        urlOFF TEXT(100) NOT NULL,
        category SMALLINT NOT NULL,
        store SMALLINT,
        CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(category_id),
        CONSTRAINT fk_store_id FOREIGN KEY (store) REFERENCES Store(store_id))
        ENGINE=InnoDB;

        CREATE TABLE IF NOT EXISTS Substitute(
        id_substitute SMALLINT,
        id_substited SMALLINT,
        CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(id_food),
        CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(id_food))
        ENGINE=InnoDB;

