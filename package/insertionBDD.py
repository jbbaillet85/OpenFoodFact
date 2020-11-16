# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

import pakage.dataOFF as dataOFF

try:
    connection = mysql.connector.connect(host = "localhost", database = "eat_well", user = "root", password = "",)
    
    cursor = connection.cursor()

    NAME_DATABASE = "eat_well"

    cursor.execute('''USE eat_well;''')

    cursor.execute("""(
    CREATE TABLE IF NOT EXISTS Category (
    category_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    category_name VARCHAR(12) NOT NULL)
    ENGINE = InnoDB;""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Store(
    store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    store_name VARCHAR(20) NOT NULL)
    ENGINE = InnoDB;""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Food(
    id_food SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_food VARCHAR(20) NOT NULL,
    nutriscore VARCHAR(1) NOT NULL,
    urlOFF TEXT(100) NOT NULL,
    category VARCHAR(12) NOT NULL,
    store VARCHAR(20),
    CONSTRAINT fk_category_name FOREIGN KEY (category) REFERENCES Category(category_name),
    CONSTRAINT fk_store_name FOREIGN KEY (store) REFERENCES Store(store_name))
    ENGINE=InnoDB;""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT,
    id_substited SMALLINT,
    CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(id_food),
    CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(id_food))
    ENGINE=InnoDB;""")

    connection.commit()

    list_pizzas = DataOFF ("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json")
    list_pizzas = list_pizzas.list_food

    for data in list_pizzas:
        cursor.execute("""INSERT INTO Food (name_food, nutriscore, urlOFF, category, store) VALUES (?,?,?,?,?),""" , data)
    
    connection.commit()

except mysql.connector.Error as error:
    print(error)

finally:
    connection.close()
    cursor.close()