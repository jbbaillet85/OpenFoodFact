# !/usr/bin/env python
# -*- coding: utf-8 -*-


from Manager.connexionBDD import ConnexionBDD
from BDD.constants import LIST_CATEGORY


class ManagerCategory(ConnexionBDD):
    def __init__(self, id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.id = id
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        self.category_name = self.get_attribut(query)

    def print_category(self):
        return f"{self.id} : {self.category_name}"


class ManagerCategoryAll(ConnexionBDD):
    def __init__(self, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.number_category = len(LIST_CATEGORY)+1
        self.list_category_all = self.get_manager_category_all()
        self.choice_category = self.get_choice_category()

    def get_manager_category_all(self):
        list_category_all = []
        for category_id in range(1, self.number_category):
            category = ManagerCategory(category_id, self.user, self.password, self.host, self.database)
            category = f"{category_id} : {category.category_name}"
            list_category_all.append(category)
        return list_category_all

    def get_choice_category(self):
        print(self.list_category_all)
        choice_category = input("Selectionner la catégorie: ")
        while not choice_category.isdigit():
            print("Rentrez un chiffre qui est dans la liste: ")
            choice_category = input("Selectionner la catégorie: ")
        return choice_category


if __name__ == "__main__":
    boissons = ManagerCategory("1", "root", "", "localhost", "eat_well")
    print(boissons.category_name)
    cat_all = ManagerCategoryAll("root", "", "localhost", "eat_well")
    print(cat_all.choice_category)
