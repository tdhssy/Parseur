#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

"""
Fonction permettant la récupération de la partie abstract d'un fichier pdf
    -lecteur : objet obtenu grâce à la méthode PdfReader(x) 
                de la bibliothèque PyPDF2
    -return : partie abstract du document
"""
def recuperationAbstract(lecteur):
    page=lecteur.pages[0] #on prends la 1ère page
    try:
        abstract = re.findall(r'(?i)abstract([\s\S]*?)(?i)i[\s]?ntroduction', page.extract_text())[0].split('\n') #TODO tout ne marche pas
        abstract.pop(-1)
    except:
        abstract="Aucun Abstract."
    return "".join(abstract)