# !/usr/bin/env python
# -*- coding: utf-8 -*-


from Manager.connexionBDD import ConnexionBDD


class Substitute(ConnexionBDD):
    def __init__(self, substituted_id, user, password, host, database):
        """Class creating substitute objects from the Food table

        Args:
            substituted_id (int): product id to be substituted
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        ConnexionBDD.__init__(self, user, password, host, database)
        # substituted attributes
        self.substituted_id = substituted_id
        query_substituted = f"SELECT food_name FROM food WHERE food_id = '{self.substituted_id}'"
        self.substituted_name = self.get_attribut(query_substituted)
        # category_id attribute of substituted
        query_category_id = f"SELECT category FROM food WHERE food_id = '{self.substituted_id}'"
        self.category_id = self.get_attribut(query_category_id)[1:-2]
        query_category_name = f"SELECT category_name FROM category WHERE category_id = '{self.category_id}'"
        self.category_name = self.get_attribut(query_category_name)
        # substitute attributes
        query_comparaison = f"SELECT food_id FROM food WHERE category = '{self.category_id}' ORDER BY food_nutriscore LIMIT 1"
        self.substitute_id = self.get_attribut(query_comparaison)[1:-2]
        query_get_subtitut_name = f"SELECT food_name FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_name = self.get_attribut(query_get_subtitut_name)
        query_get_substitut_url = f"SELECT food_urlOFF FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_url = self.get_attribut(query_get_substitut_url)
        query_get_store_id = f"SELECT store FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_store_id = self.get_attribut(query_get_store_id)[1:-2]
        query_get_store_name = f"SELECT store_name FROM store WHERE store_id = '{self.substitut_store_id}'"
        self.substitut_store_name = self.get_attribut(query_get_store_name)
        query_get_subtituted_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = '{self.substituted_id}'"
        self.substituted_nutriscore = self.get_attribut(query_get_subtituted_nutriscore)
        query_get_substitut_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = '{self.substitute_id}'"
        self.substitut_nutriscore = self.get_attribut(query_get_substitut_nutriscore)

    def print_substitute(self):
        """function displaying the substitute with its nutriscore, its web page, and the store where to buy it
        """
        print(f"{self.category_id}-{self.category_name}")
        print(f"""A la place du produit {self.substituted_name} d'un nutriscore de {self.substituted_nutriscore},
        vous pouvez consommer le produit de substitution {self.substitute_id}-{self.substitut_name} avec un nutriscore de {self.substitut_nutriscore}""")
        print(f"La fiche web est à l'adresse {self.substitut_url}")
        print(f"Vous pouvez acheter {self.substitut_name} chez {self.substitut_store_name}")

    def save_substitute(self):
        """function recording the subtitle in the Substitute table
        """
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
        """function showing saved favorites
        """
        query_substituted = "SELECT substited_id FROM substitute"
        query_favoris = "SELECT * FROM substitute"
        self.cursor.execute(query_favoris)
        favoris = self.cursor.fetchall()
        print(favoris)
        for substitute in favoris:
            print(substitute)
            query_substituted = f"SELECT food_id, food_nutriscore, food_name FROM food WHERE food_id = '{substitute[0]}'"
            substituted = self.get_attribut(query_substituted)
            query_substitut = f"SELECT food_id, food_nutriscore, food_name, food_urlOFF FROM food WHERE food_id = '{substitute[1]}'"
            substitut = self.get_attribut(query_substitut)
            query_store_id = f"SELECT store FROM food WHERE food_id = '{substitute[1]}'"
            store_id = self.get_attribut(query_store_id)[1:-1]
            query_substitut_store_name = f"SELECT store_name FROM store WHERE store_id = '{store_id}'"
            store_name = self.get_attribut(query_substitut_store_name)
            print(f"Produit à remplacer: {substituted} par le")
            print(f"Produit de substitution: {substitut}")
            print(f"Vous pouvez acheter le produit chez {store_name}\n")


if __name__ == "__main__":
    substitute1 = Substitute(80, "root", "", "localhost", "eat_well")
    print(f"category n° : {substitute1.category_id}")
    substitute1.save_substitute()
    substitute1.print_favoris()
