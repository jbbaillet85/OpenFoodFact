# !/usr/bin/env python
# -*- coding: utf-8 -*-


from Manager.connexionBDD import ConnexionBDD
from BDD.constants import LIST_CATEGORY


class ManagerCategory(ConnexionBDD):
    def __init__(self, id, user, password, host, database):
        """Class creating category objects

        Args:
            id (int): id of the category in the Category table
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        ConnexionBDD.__init__(self, user, password, host, database)
        self.id = id
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        self.category_name = self.get_attribut(query)

    def print_category(self):
        """function displaying the id and the name of the category

        Returns:
            str: the category id and name
        """
        return f"{self.id} : {self.category_name}"


class ManagerCategoryAll(ConnexionBDD):
    def __init__(self, user, password, host, database):
        """Class creating a category list

        Args:
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        ConnexionBDD.__init__(self, user, password, host, database)
        self.number_category = len(LIST_CATEGORY)+1
        self.list_category_all = self.get_manager_category_all()
        self.choice_category = self.get_choice_category()

    def get_manager_category_all(self):
        """function retrieving all categories with their id

        Returns:
            list: list of names and id of categories
        """
        list_category_all = []
        for category_id in range(1, self.number_category):
            category = ManagerCategory(category_id, self.user, self.password, self.host, self.database)
            category = f"{category_id} : {category.category_name}"
            list_category_all.append(category)
        return list_category_all

    def get_choice_category(self):
        """function to select the desired category id

        Returns:
            str: id digit
        """
        print(self.list_category_all)
        choice_category = input("Selectionner la catégorie: ")
        while not choice_category.isdigit():
            print("Rentrez un chiffre qui est dans la liste: ")
            choice_category = input("Selectionner la catégorie: ")
        return choice_category


if __name__ == "__main__":
    drinks = ManagerCategory("1", "root", "", "localhost", "eat_well")
    print(drinks.category_name)
    cat_all = ManagerCategoryAll("root", "", "localhost", "eat_well")
    print(cat_all.choice_category)
