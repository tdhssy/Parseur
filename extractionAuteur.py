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
    met = lecteur.metadata #lecture des métadonnées
    resultat = met.author  #lecture de l'auteur dans les métadonnées


    if resultat == None or resultat == "" : #Si les métadata ne fonctionne pas
        page=lecteur.pages[0] #on prends la 1ère page
        texte = page.extract_text().replace("\n"," ") #aligne tout le texte sur une ligne
        titre = recuperationTitre(lecteur) #Récupération du titre
        index_debut = texte.find(titre) #récupération de l'index du titre dans le texte
        index_debut+=len(titre) #Incrémentation de l'index pour allez à la fin du titre
        index_fin = texte.lower().find("abstract") #Récupération de l'index du début de l'abstract
        if(index_fin==-1): #Vérification si l'abstract existe
            index_fin = texte.lower().find("introduction") #Si l'abstract n'existe pas on estime que l'auteur est entre le titre et l'intro
        resultat = texte[index_debut:index_fin]
        
    #print("Auteurs :\n\t"+resultat)

    return resultat