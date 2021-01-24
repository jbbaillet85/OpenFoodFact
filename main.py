# !/usr/bin/env python
# -*- coding: utf-8 -*-

from BDD.constants import LIST_CATEGORY
from BDD.BDDinsertion import *
from Manager.managerCategory import ManagerCategoryAll, ManagerCategory
from Manager.managerProduct import Product
from Manager.managerSubstitute import Substitute

print("Bienvenus dans l'application Bien Manger")
#créer la base de donnée:
user = input("Entrez le nom d'utilisateur de votre database: ")
password = input("Entrez le mot de passe de votre database: ")
host = input("Entrez votre localhost: ")
database = input("Entrez le nom de votre database: ")
eat_well = InsertionBDD(user, password, host, database)
eat_well.create_tables()

#purger les tables:
purge = input("Si vous souhaitez purger les tables, tapez: p ")
if purge == "p":
    eat_well.purge_tables()

#inserer les données:
load_data = input("Souhaitez-vous télécharger les datas d'OpenFoodFact? o/n: ")
if load_data == "o" or "O":
    print("Insertion des datas d'Openfoodfact en cours,\nmerci de patienter")
    eat_well.insert_category(LIST_CATEGORY)
    stores_all = BDDstoresAll()
    eat_well.insert_store(stores_all.list_stores_all)
    foods_all = BDDfoodAll()
    eat_well.insert_food(foods_all.list_food_all)

print("\n Menus \n")
# proposer les choix
choice_menus = input("1-Quel aliment souhaitez-vous remplacer?\n2-Retrouver mes aliments substitués.\nchoix 1 ou 2: ")
#while choice_menus != "1" or "2":
#    print("Vous devez taper 1 ou 2 pour valider votre choix : ")
if choice_menus == "1":
    choice_food = ManagerCategoryAll(6, user, password, host, database)
    choice_category = ManagerCategory(choice_food.choice_category, user, password, host, database)

    choice_product = Product(choice_category, user, password, host, database)

    favoris = Substitute(choice_product.choice_product, user, password, host, database)
    favoris.print_substitute()
    favoris.save_substitute()
elif choice_menus == "2":
    favoris = Substitute(1, user, password, host, database)
    favoris.print_favoris()

quit_programme = input("Souhaitez-vous quitter l'aplication Bien Manger? o/n")
if quit_programme == "o" or "O":
    #méthode pour quitter le programme
else:
    #retourner au menus
