# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import user, password, host, database
from BDD.constants import LIST_CATEGORY
from BDD.BDDinsertion import InsertionBDD, BDDfoodAll, BDDstoresAll

print("**Bienvenus dans l'application Bien Manger**\n")
# créer la base de donnée:
eat_well = InsertionBDD(user, password, host, database)
eat_well.create_tables()

# purger les tables:
purge = input("Si vous souhaitez purger les tables, tapez p,\n sinon tapez la touche 'entrer' ")
if purge == "p":
    eat_well.purge_tables()

# inserer les données:
load_data = input("Souhaitez-vous télécharger les datas d'OpenFoodFact? o/n: ")
if load_data == "o":
    print("Insertion des datas d'Openfoodfact en cours,\nmerci de patienter")
    eat_well.insert_category(LIST_CATEGORY)
    stores_all = BDDstoresAll()
    eat_well.insert_store(stores_all.list_stores_all)
    foods_all = BDDfoodAll()
    eat_well.insert_food(foods_all.list_food_all)

print("Installation réussi avec succès")
