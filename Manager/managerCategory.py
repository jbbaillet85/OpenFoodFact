# !/usr/bin/env python
# -*- coding: utf-8 -*-

#faire hériter ManagerCategory de connexionBDD

import mysql.connector

from Manager.connexionBDD import ConnexionBDD

class ManagerCategory(ConnexionBDD):
    def __init__(self, id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.id = id
        self.category_name = self.get_category_name()

    def get_category_name(self):
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        self.cursor.execute(query)
        category_name = self.cursor.fetchone()
        category_name = str(category_name)[1:-2]
        return category_name
    
    def print_category(self):
        return f"{self.id} : {category_name}"

class ManagerCategoryAll(ConnexionBDD):
    def __init__(self, number_category, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.number_category = number_category
        self.list_category_all = self.get_manager_category_all()
        self.choice_category = self.get_choice_category()

    def get_manager_category_all(self):
        list_category_all = []
        for category_id in range(1,self.number_category):
            category = ManagerCategory(category_id, self.user, self.password, self.host, self.database)
            category = f"{category_id} : {category.category_name}"
            list_category_all.append(category)
        return list_category_all
    
    def get_choice_category(self):
            print(self.list_category_all)
            choice_category = input(f"Selectionner la catégorie: ")
            return choice_category


if __name__ == "__main__":
    boissons = ManagerCategory("1", "root", "","localhost", "eat_well")
    print(boissons.category_name)
    cat_all = ManagerCategoryAll(6, "root","","localhost","eat_well")
    print(cat_all.choice_category)
