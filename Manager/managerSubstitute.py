# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from Manager.connexionBDD import ConnexionBDD

class Substitute(ConnexionBDD):
    def __init__(self, substituted_id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        #recuperer l'id du produit à remplacer
        self.substituted_id = substituted_id
        #récuperer le food_name du produit à remplacer
        query_substituted = f"SELECT food_name FROM food WHERE food_id = '{self.substituted_id}'"
        self.substituted_name = self.get_attribut_substitute(query_substituted)
        #recuperer l'id de la category du food_name à remplacer
        query_category_id = f"SELECT category FROM food WHERE food_id = '{self.substituted_id}'"
        self.category_id = self.get_attribut_substitute(query_category_id)
        #recuperer l'id du substitut
        query_comparaison = f"SELECT food_id FROM food WHERE category = '{self.category_id}' ORDER BY food_nutriscore LIMIT 1 OFFSET 2"
        self.substitute_id = self.get_attribut_substitute(query_comparaison)
        #recuperer le food_name du substitut:
        query_get_subtitut_name = f"SELECT food_name FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_name = self.get_attribut_substitute(query_get_subtitut_name)
        #recuperer l'url de substitute
        query_get_substitut_url = f"SELECT food_urlOFF FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_url = self.get_attribut_substitute(query_get_substitut_url)
        #recuperer le store_id du substitut
        query_get_store_id = f"SELECT store FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_store_id = self.get_attribut_substitute(query_get_store_id)
        #recuperer le store_name du substitut
        query_get_store_name = f"SELECT store_name FROM store WHERE store_id = '{self.substitut_store_id}'"
        self.substitut_store_name = self.get_attribut_substitute(query_get_store_name)
        query_get_subtituted_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = '{self.substituted_id}'"
        self.substituted_nutriscore = self.get_attribut_substitute(query_get_subtituted_nutriscore)
        query_get_substitut_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_nutriscore = self.get_attribut_substitute(query_get_substitut_nutriscore)

    def get_attribut_substitute(self, query):
        self.cursor.execute(query)
        attribut_substitute = self.cursor.fetchone()
        attribut_substitute = str(attribut_substitute)[1:-2]
        return attribut_substitute

    def print_substitute(self):
        print(f"""A la place du produit {self.substituted_name} d'un nutriscore de {self.substituted_nutriscore},
        vous pouvez consommer le produit de substitution {self.substitut_name} avec un nutriscore de {self.substitut_nutriscore}""")
        print(f"La fiche web est à l'adresse {self.substitut_url}")
        print(f"Vous pouvez acheter {self.substitut_name} chez {self.substitut_store_name}")

    def save_substitute(self):
        save = input(f"Souhaitez vous enregistrer votre produit de substitution: {self.substitut_name} dans vos favoris? o/n : ")
        if save == "o":
            query_select = f"SELECT id_substited FROM substitute WHERE id_substited = '{self.substituted_id}'"
            self.cursor.execute(query_select)
            if self.cursor.rowcount == -1:
                self.cursor.fetchall()
            if self.cursor.rowcount == 0:
                query_save = f"INSERT INTO Substitute (id_substitute, id_substited) VALUES ('{self.substitute_id}' , '{self.substituted_id}') "
                self.cursor.execute(query_save)
                self.connexion.commit()
                print(f"Votre favoris {self.substitut_name} a bien été enregistré")

    def print_favoris(self):
        query_substituted = "SELECT substited_id FROM substitute"
        query_favoris = "SELECT * FROM substitute"
        self.cursor.execute(query_favoris)
        favoris = self.cursor.fetchall()
        print(favoris)
        for substitute in favoris:
            print(substitute)
            print(f"Produit à remplacer: {self.substituted_name} par le")
            print(f"Produit de substitution: {self.substitut_name} \n")


if __name__ == "__main__":
    substitute1 = Substitute(80, "root", "", "localhost", "eat_well")
    print(f"category n° : {substitute1.category_id}")
    substitute1.save_substitute()
    substitute1.print_favoris()
