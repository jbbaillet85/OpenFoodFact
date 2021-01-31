# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

from BDD.BDDcategory import LIST_CATEGORY, BDDcategory


class BDDfood:
    def __init__(self, category_name):
        """ class returning a list of attributes name, nutriscore, url, category, store of a product

        Args:
            category_name (str): name of category
        """
        self.name_category = category_name
        self.list_urljson_category = self.get_category()
        self.list_food = self.get_food()

    def get_category(self):
        """function retrieving the list of urls in json format of a category

        Returns:
            list: urls in json format
        """
        return BDDcategory(self.name_category).list_urljson_category

    def get_food(self):
        """function retrieving the attributes name, nutriscore, url, category, store
        products from a category of the OpenFoodFact API

        Returns:
            list: products with their attributes name, nutriscore, url, category, store
        """
        list_food = []
        product_content = []
        for category in self.list_urljson_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for product in category_data.get("products"):
                if product.get("nutriscore_grade") is not None:
                    if product.get("stores") is not None:
                        if product.get("stores") != '':
                            product_content.append((
                            product.get("product_name"),
                            product.get("nutriscore_grade"),
                            product.get("url"),
                            self.name_category,
                            product.get("stores")))
                            list_food.extend(product_content)
        return list_food


class BDDfoodAll:
    def __init__(self):
        """class returning a list of all the products with their attributes
        """
        self.list_food_all = self.get_list_food_all()

    def get_list_food_all(self):
        """function retrieving all products with their attributes from all categories
        to insert into the mysql database

        Returns:
            list: products with their attributes
        """
        list_foods_all = []
        for cat in LIST_CATEGORY:
            food = BDDfood(cat)
            foods = food.list_food
            list_foods_all.extend(foods)
        return list_foods_all


if __name__ == "__main__":
    food_all = BDDfoodAll()
    print(food_all.list_food_all)
    print(len(food_all.list_food_all))
