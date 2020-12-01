# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from category import *
import food
import store

def main():


    connection = sqlite3.connect(database = "eat_well.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Category (
    category_id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(80))
    ;""")
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Store(
    store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    store_name VARCHAR(80) NOT NULL)
    ;""")
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Food(
    id_food SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name_food VARCHAR(20) NOT NULL,
    nutriscore VARCHAR(1) NOT NULL,
    urlOFF TEXT(100) NOT NULL,
    category VARCHAR(80) NOT NULL,
    store VARCHAR(80),
    CONSTRAINT fk_category_name FOREIGN KEY (category) REFERENCES Category(category_name),
    CONSTRAINT fk_store_name FOREIGN KEY (store) REFERENCES Store(store_name))
    ;""")
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Substitute(
    id_substitute SMALLINT,
    id_substited SMALLINT,
    CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(id_food),
    CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(id_food))
    ;""")
    connection.commit()

    list_category = Category()
    for category in list_category.LIST_CATEGORY:
        cursor.execute("""INSERT INTO Category(category_name) VALUES(category_name = ?);""", (category,))
        connection.commit()
    
    list_store = Store()
    for store in list_store.list_store:
        cursor.execute("""INSERT INTO Category(store_name) VALUES(?);""", (store,))
        connection.commit()
    
    list_food = Food()
    for food in list_food.list_food:
        cursor.execute("""INSERT INTO Category(name_food, nutriscore, urlOFF, category, store) VALUES(?);""", (food,))
        connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()