# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Manager.connexionBDD import ConnexionBDD


class Store(ConnexionBDD):
    def __init__(self, store_id, user, password, host, database):
        """Class creating store objects from the Store table

        Args:
            store_id (int): store id of the Store table
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        ConnexionBDD.__init__(self, user, password, host, database)
        self.store_id = store_id
        query_store_name = f"SELECT store_name FROM store WHERE store_id = {self.store_id}"
        self.store_name = self.get_attribut(query_store_name)


if __name__ == "__main__":
    store1 = Store(1, "root", "", "localhost", "eat_well")
    print(store1.store_name)
