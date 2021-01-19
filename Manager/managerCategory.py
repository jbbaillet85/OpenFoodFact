# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

import connexionBDD

class ManagerCategory:
    def __init__(self, id):
        self.id = id
        self.category_name = self.get_category_name()
        self.connexion_db = ConnexionBDD("root", "","localhost","eat_well")
        self.cursor = self.connexion_db.cursor()
        
    def get_category_name(self):
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        self.cursor.execute(query)
        category_name = self.cursor.fetchone()
        return category_name
    
if __name__ == "__main__":
    boissons = ManagerCategory(1)

    print(boissons.category_name)
