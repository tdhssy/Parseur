#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionAbstract import recuperationAbstract
from creationFichier import CreatFich

"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(fichier):
    print("Analyse de " + fichier + " en cours ..." )

    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)
    
    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 
    
    #Récupération des informations du fichier
    INFO = lecteur.metadata
    TITRE = recuperationTitre(lecteur)
    #print("Titre : "+TITRE+"\n")
    AUTEURS = recuperationAuteurs(INFO)
    ABSTRACT = recuperationAbstract(lecteur)
    rendu = ["\nNom du fichier :\n\t" + NOM_FICHIER + 
            "\nTitre :\n\t" + TITRE +
            "\nAbstract : \n\t" + ABSTRACT
            ]
    CreatFich(rendu[0], "./Résultat/" + NOM_FICHIER[:-3] + "txt")
    print(rendu[0])
    print("----------------------------------------------------------------\n") 