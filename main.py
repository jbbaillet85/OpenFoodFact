# !/usr/bin/env python
# -*- coding: utf-8 -*-

print("Bienvenus dans l'application Bien Manger")

print("Menus")

choix1 = print(f"1-Quel aliment souhaitez vous remplacer ?")
choix2 = print(f"2-Retrouver mes aliments substitués")

choixMenus = input("Si vous souhaiter remplacer une aliment tapez 1,\n Si vous souhaiter retrouver vos aliments substités tapez 2 \n")

if choixMenus == "1":
    categorie = []
    print(f"Selectionner une categorie: ")
    