# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Store:
    def __init__(self, id):
        self.id = id
        self.name = get_store_name()
    
    def get_store_name(self):
        query = f"SELECT store_name FROM store WHERE store_id = {self.id}"
