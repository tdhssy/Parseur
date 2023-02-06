#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fonction pour crée un fichier et y ecrire une chaine caractère en respectant
les sauts de lignes, les espaces etc...
"""

def CreatFich(text, nom):
    fichier = open(nom, 'w+')
    fichier.write(text)
    fichier.close()
   
    