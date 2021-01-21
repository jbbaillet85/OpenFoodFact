# !/usr/bin/env python
# -*- coding: utf-8 -*-

from connexionBDD import ConnexionBDD
class Store(ConnexionBDD):
    def __init__(self, store_id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.store_id = store_id
        query_store_name = f"SELECT store_name FROM store WHERE store_id = {self.store_id}"
        self.store_name = self.get_attribut_store(query_store_name)
    
    def get_attribut_store(self, query):
        self.cursor.execute(query)
        attribut_store = self.cursor.fetchone()
        self.cursor.close()
        return attribut_store

if __name__ == "__main__":
    store1 = Store(1, "root", "","localhost","eat_well")
    print(store1.store_name)