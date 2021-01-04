# !/usr/bin/env python
# -*- coding: utf-8 -*-

from insertionBDD import *
from store import *
from food import *
from constants import LIST_CATEGORY

mysql1 = InsertionBDD("root", "", "localhost", "eat_well")
mysql1.create_tables()
mysql1.insert_category(LIST_CATEGORY)

stores_all = Stores_all()
mysql1.insert_store(stores_all.list_stores_all)

boissons = Food("Boissons")
boissons = boissons.list_food
mysql1.insert_food(boissons)

desserts = Food("Desserts")
desserts = desserts.list_food
mysql1.insert_food(desserts)

pizzas = Food("Pizzas")
pizzas = pizzas.list_food
mysql1.insert_food(pizzas)