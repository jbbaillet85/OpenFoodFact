# !/usr/bin/env python
# -*- coding: utf-8 -*-

#faire hériter ManagerCategory de connexionBDD

import mysql.connector

from connexionBDD import ConnexionBDD
from BDD.constants import LIST_CATEGORY

class ManagerCategory(ConnexionBDD):
    def __init__(self, id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.id = id
        self.category_name = self.get_category_name()

    def get_category_name(self):
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        self.cursor.execute(query)
        category_name = self.cursor.fetchone()
        return category_name
    
    def print_category(self):
        category_name = str(self.category_name)
        return f"{self.id} : {category_name}"

class ManagerCategoryAll:
    def __init__(self, list_category):
        self.list_category = LIST_CATEGORY
        self.list_category_all = self.get_manager_category_all()

    def get_manager_category_all(self):
        list_category_all = []
        for category_name in self.list_category:
            query = f"SELECT category_id, category_name FROM category"
            category = self.cursor.fetchone()
            list_category_all.append(category)
        return list_category_all


if __name__ == "__main__":
    boissons = ManagerCategory("1", "root", "","localhost", "eat_well")
    print(boissons.category_name)
    print(boissons.print_category())
    cat_all = ManagerCategoryAll(LIST_CATEGORY)
    print(cat_all.list_category_all)