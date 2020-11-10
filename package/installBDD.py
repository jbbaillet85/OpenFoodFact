# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

try:
    connection = mysql.connector.connect(host = "localhost", database = "eat_well", user = "root", password = "",)
    
    cursor = connection.cursor()

    TABLES = {}

    NAME_DATABASE = "eat_well"

    TABLES['Category'] = (
        "CREATE TABLE `Category` ("
        "  `id_category` int(2) NOT NULL AUTO_INCREMENT,"
        "  `name` varchar(14) NOT NULL,"
        "  PRIMARY KEY (`id_category`)"
        ") ENGINE=InnoDB")

    TABLES['Store'] = (
        "CREATE TABLE `Store` ("
        "  `id_stores` int(2) NOT NULL AUTO_INCREMENT,"
        "  `name` varchar(40) NOT NULL,"
        "  PRIMARY KEY (`id_store`),"
        ") ENGINE=InnoDB")

    TABLES['Nutriscore'] = (
        "CREATE TABLE `Nutriscore` ("
        "  `id_nutriscore` int(2) NOT NULL AUTO_INCREMENT,"
        "  `score` varchar(1) NOT NULL,"
        "  PRIMARY KEY (`id_nutriscore`),"
        ") ENGINE=InnoDB")

    TABLES['Food'] = (
        "CREATE TABLE `Food` ("
        " 'id_food' SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
        " 'name_food' VARCHAR(20),"
        " 'category' SMALLINT NOT NULL, "
        " 'ingredients' TEXT, "
        " 'nutriscore' SMALLINT, "
        " 'store' SMALLINT, "
        " 'urlOFF' URL, "
        " CONSTRAINT 'fk_nutriscore_id' FOREIGN KEY ('nutriscore') REFERENCES Nutriscore('id_nutriscore')"
        " CONSTRAINT 'fk_category_id' FOREIGN KEY ('category') REFERENCES Category('id_category'),"
        " CONSTRAINT 'fk_store' FOREIGN KEY('store') REFERENCES Shop('id_store')"
        ") ENGINE=InnoDB;")

    TABLES['Sustitute'] = (
        "CREATE TABLE `Substitute` ("
        " 'id_substitute' SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
        " 'name_food' VARCHAR(20),"
        " 'category' SMALLINT NOT NULL, "
        " 'ingredients' TEXT, "
        " 'nutriscore' SMALLINT, "
        " 'store' SMALLINT, "
        " 'urlOFF' URL, "
        " CONSTRAINT 'fk_name_food' FOREIGN KEY ('food') REFERENCES Food('id_name_food')"
        " CONSTRAINT 'fk_category' FOREIGN KEY ('category') REFERENCES Category('name_category')"
        " CONSTRAINT 'fk_ingredients' FOREIGN KEY ('ingredients') REFERENCES Food('ingredients')"
        " CONSTRAINT 'fk_nutriscore_id' FOREIGN KEY ('nutriscore') REFERENCES Nutriscore('id_nutriscore')"
        " CONSTRAINT 'fk_lienOFF' FOREIGN KEY ('urlOFF') REFERENCES Food('lienOFF'),"
        " CONSTRAINT 'fk_store' FOREIGN KEY('store') REFERENCES Shop('id_store')"
        ") ENGINE=InnoDB;")

except mysql.connector.Error as error:
    print(error)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
