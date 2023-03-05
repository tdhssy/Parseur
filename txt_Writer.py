#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionAbstract import recuperationAbstract
from creationFichier import CreatFich
from extractionBiblio import recuperationBiblio

"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(fichier):
    print("Conversion en TXT du fichier [" + fichier + "] en cours ..." )

    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)
    
    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 1
    
    #Récupération des informations du fichier
    INFO = lecteur.metadata
    TITRE = recuperationTitre(lecteur)
    AUTEURS = recuperationAuteurs(lecteur)
    ABSTRACT = recuperationAbstract(lecteur)
    BIBLIOGRAPHIE = recuperationBiblio(lecteur)

    #Formatage des données 
    rendu = [
            "\nNom du fichier :\n\t" + NOM_FICHIER + 
            "\nTitre :\n\t" + TITRE +
            "\nAuteurs :\n\t" + AUTEURS +
            "\nAbstract : \n\t" + ABSTRACT +
            "\nBibliographie : \n\t" + BIBLIOGRAPHIE
            ]

    CreatFich(rendu[0], "./resultat/" + NOM_FICHIER[:-3] + "txt")
    #print(rendu[0])
    print("----------------------------------------------------------------\n") 