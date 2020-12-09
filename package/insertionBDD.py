# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

import category
import food
import store

def main():


    connection = mysql.connector.connect(host = "localhost", user = "root", password = "iotabeta85")

    cursor = connection.cursor()

    try:

        cursor.execute("""CREAT DATABASE IF NOT EXISTS eat_well""")

        cursor.execute("""USE eat_well""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS Category (
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
        category SMALLINT NOT NULL,
        store SMALLINT,
        CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(category_id),
        CONSTRAINT fk_store_id FOREIGN KEY (store) REFERENCES Store(store_id))
        ENGINE=InnoDB;""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS Substitute(
        id_substitute SMALLINT,
        id_substited SMALLINT,
        CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(id_food),
        CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(id_food))
        ENGINE=InnoDB;""")

        connection.commit()

        list_category = Category("Boissons")
        for category in list_category.LIST_CATEGORY:
            cursor.execute("""INSERT INTO Category(category_name)
            VALUES(?);""", category)
            connection.commit()
        
        list_store = Store()
        for store in list_store.list_store:
            cursor.execute("""INSERT INTO Category(store_name) VALUES(?);""", store)
            connection.commit()
        
        list_food = Food()
        for food in list_food.list_food:
            cursor.execute("""INSERT INTO Category(name_food, nutriscore, urlOFF, category, store)
            VALUES(%(name_food)s, %(nutriscore)s, %(urlOFF)s, %(category)s, %(store)s);""", food)
            connection.commit()

    except mysql.connector.Error as error:
        print(error)

    finally:
        connection.close()
        cursor.close()

if __name__ == "__main__":
    print("""Lancer le serveur mysql avec votre terminal:
    windows: ./mysqld.exe --console
    linux/mac: sudo service mysql start""")

    print("""Connecter vous au client avec un nouveau terminal:
    windows: /mysql.exe -u root -p
    linux/mac: sudo mysql -u root -p""")

    reponse_user = input("Avez vous lancé le serveur et le client y/n: ")
    if reponse_user == "y":
        main()