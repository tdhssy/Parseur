#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

"""
Fonction permettant la récupération de la partie bibliographie d'un fichier pdf
en utilisant une expression régulière
    -In : PdfReader
    -Out : représentation en str de la partie
           bibliographie du document si elle existe
"""

def recuperationBiblio(lecteur: PdfReader) -> str:
    res = []
    nb_pages = len(lecteur.pages)
    trouver = False
    cpt = 0

    #On parcours tout le pdf jusqu'à trouver la partie Référence
    while (cpt < nb_pages) and (not trouver):
        page = lecteur.pages[cpt]

        try:
            biblio = re.findall(r'(?i)[\n]reference[s]?[\s]*[\n][\s\S]*',page.extract_text())[0].split('\n')
        except:
            biblio = []

        if biblio != []:
            for ligne in biblio:
                res += ligne + "\n"
            res.pop(-1) #Pour enlever le numéro de la page
            trouver = True
        cpt += 1
    
    #Une fois la partie Référence trouver on ajoute toute la fin du pdf
    #car la partie Référence est la dernière partie d'un pdf.
    while cpt < nb_pages:
        page = lecteur.pages[cpt]
        for ligne in page.extract_text()[0].split('\n'):
            res += ligne + "\n"
        res.pop(-1) #Pour enlever le numéro de la page
        cpt += 1
    
    return "".join(res)