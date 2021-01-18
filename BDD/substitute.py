# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

class substitute:
    def __init__(self, id_substitute):
        self.food_subtitute = self.get_food_substitute()
        self.category_name = self.get_category_name()
        self.food_subtited = self.comparaison_food(self.category_name)
    
    def get_food_substitute(self):
        query = f"SELECT food_name FROM food WHERE food_id = {id_substitute}"
    
    def get_category_name(self):
        query = f"SELECT category_id FROM food WHERE food_id = {id_substitute}"
    
    def comparaison_food(category_id):
        query = f"""SELECT * FROM food, category WHERE category_id = {category_id} 
        ORDER BY food_nutriscore LIMIT 1"""
    
if __name__ == "__main__":
    pass