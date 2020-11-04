# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jbbaillet",
  password="iotabeta85",
  auth_plugin='mysql_native_password'
)

mydb.close()

print(mydb)

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

connection = mysql.connector.connect(user='jbbaillet')
cursor = connection.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(NAME_DATABASE))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(NAME_DATABASE))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(NAME_DATABASE))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(NAME_DATABASE))
        connection.database = NAME_DATABASE
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
connection.close()