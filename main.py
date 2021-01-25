# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import user, password, host, database
from Manager.managerCategory import ManagerCategoryAll, ManagerCategory
from Manager.managerProduct import Product
from Manager.managerSubstitute import Substitute

print("**Bienvenus dans l'application Bien Manger**\n")

print("\n Menus \n")
# proposer les choix
choice_menus = input("1-Quel aliment souhaitez-vous remplacer?\n2-Retrouver mes aliments substitués.\nchoix 1 ou 2: ")
while choice_menus != "1" or "2":
    if choice_menus != "1" or "2":
        print("Vous devez taper 1 ou 2 pour valider votre choix : ")
        choice_menus = input("1-Quel aliment souhaitez-vous remplacer?\n2-Retrouver mes aliments substitués.\nchoix 1 ou 2: ")

    if choice_menus == "1":
        choice_food = ManagerCategoryAll(user, password, host, database)
        choice_category = ManagerCategory(choice_food.choice_category, user, password, host, database)

        choice_product = Product(choice_category, user, password, host, database)

        favoris = Substitute(choice_product.choice_product, user, password, host, database)
        favoris.print_substitute()
        favoris.save_substitute()

    elif choice_menus == "2":
        favoris = Substitute(1, user, password, host, database)
        favoris.print_favoris()
