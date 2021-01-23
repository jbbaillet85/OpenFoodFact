# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

class ConnexionBDD:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connexion = self.connect_db()
        self.cursor = self.connexion.cursor()

    def connect_db(self):
        try:
            connexion = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                database = self.database)
            return connexion
        except mysql.connector.errors.ProgrammingError:
            print("Vous n'êtes pas connecté")

if __name__ == "__main__":
    connexion = ConnexionBDD("root", "", "localhost", "eat_well")