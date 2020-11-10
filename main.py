# !/usr/bin/env python
# -*- coding: utf-8 -*-

print("Bienvenus dans l'application Bien Manger")

print("\n Menus \n")
choix1 = print(f"1-Quel aliment souhaitez vous remplacer ?")
choix2 = print(f"2-Retrouver mes aliments substitués")

try:
    listeChoixMenus = [1, 2]
    choixMenus = input("Si vous souhaiter remplacer une aliment tapez 1,\nSi vous souhaiter retrouver vos aliments substités tapez 2 \n choix: ")
    assert choixMenus in listeChoixMenus
except AssertionError:
    print("Vous devez rentrer 1 ou 2")
else:
    if choixMenus == "1":
        categorie = []
        choixCategory = input("Selectionner une categorie: ")
    