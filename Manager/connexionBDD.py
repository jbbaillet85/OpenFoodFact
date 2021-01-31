# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


class ConnexionBDD:
    def __init__(self, user, password, host, database):
        """Class to connect to the server and create a cursor

        Args:
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connexion = self.connect_db()
        self.cursor = self.connexion.cursor()

    def connect_db(self):
        """function to connect to the server

        Returns:
            MySQLConnection: Connection to the server
        """
        try:
            connexion = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database)
            return connexion
        except mysql.connector.errors.ProgrammingError:
            print("Vous n'êtes pas connecté")

    def get_attribut(self, query):
        """function to transmit SQL commands to the server

        Args:
            query (str): SQL command

        Returns:
            [tuple]: the result of the SQL query
        """
        self.cursor.execute(query)
        attribut = self.cursor.fetchall()
        attribut = str(attribut)[1:-1]
        return attribut


if __name__ == "__main__":
    connexion = ConnexionBDD("root", "", "localhost", "eat_well")
