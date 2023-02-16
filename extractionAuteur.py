#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
from extractionTitre import recuperationTitre
import re
"""
Fonction permettant l'extraction du ou des auteurs d'un article pdf
TODO modification à venir
"""
def recuperationAuteurs(lecteur: PdfReader) -> str:
    #TODO metadata.author peut renvoyer none. A gérer dans ce cas
    result = ""

    page=lecteur.pages[0] #on prends la 1ère page
    texte = page.extract_text().replace("\n"," ") #aligne tout le texte sur une ligne
    titre = recuperationTitre(lecteur) #Récupération du titre
    index_debut = texte.find(titre) #récupération de l'index du titre dans le texte
    index_debut+=len(titre) #Incrémentation de l'index pour allez à la fin du titre
    index_fin = texte.lower().find("abstract") #Récupération de l'index du début de l'abstract
    if(index_fin!=-1): #Vérification si l'abstract existe

        result = texte[index_debut:index_fin]
    else:
        result = "pas d'abstract"
    print("Auteurs :\n\t"+result)

    return ""