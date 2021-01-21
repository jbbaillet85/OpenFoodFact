# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from connexionBDD import ConnexionBDD

class substitute(ConnexionBDD):
    def __init__(self, id_substitute, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.id_substitute = id_substitute
        query_food_substitute = f"SELECT food_id, food_name FROM food WHERE food_id = {self.id_substitute}"
        self.food_subtitute = self.get_attribut_substitute(query_food_substitute)
        query_category_id = f"SELECT category FROM food WHERE food_id = {self.id_substitute}"
        self.category_id = self.get_attribut_substitute(query_category_id)
        query_comparaison = f"SELECT food_id, food_name FROM food, category WHERE category_id = '{self.category_id}' ORDER BY food_nutriscore LIMIT 1"
        self.food_subtited = self.get_attribut_substitute(query_comparaison)
    
    def get_attribut_substitute(self, query):
        self.cursor.execute(query)
        attribut_substitute = self.cursor.fetchone()
        return attribut_substitute 
    
if __name__ == "__main__":
    substitute1 = substitute(45,"root","","localhost","eat_well")
    print(f"category n° : {substitute1.category_id}")
    print(substitute1.food_subtitute)
    print(substitute1.food_subtited)
