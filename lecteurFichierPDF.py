#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

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
    TITRE = recuperationTitre(INFO)
    AUTEURS = recuperationAuteurs(INFO)

    #rendu = ["Titre :\n\t" + TITRE + 
    #        " test"]
    #print(rendu[0])


def extractionNomFichier(fichier):
    return fichier.split('/')[-1]  #.split('.')[0] Pour retirer le '.pdf'

def recuperationTitre(metadata):
    titre = metadata.title
    #TODO metadata.title peut renvoyer none. A gérer dans ce cas
    return titre

def recuperationAuteurs(metadata):
    auteurs = metadata.author
    #TODO metadata.author peut renvoyer none. A gérer dans ce cas
    return auteurs