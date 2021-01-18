# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Category:
    def __init__(self, id):
        self.id = id
        self.category_name = self.get_category_name()

    def get_category_name(self):
        query = f"SELECT category_name FROM category WHERE category_id = {self.id}"
        