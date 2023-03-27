#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionAbstract import recuperationAbstract
from creationFichier import CreatFich
from extractionDiscussion import recuperationDiscussion
from extractionBiblio import recuperationBiblio
from extractionConclusion import recuperationConclusion


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
    AUTEURS = "\n".join([f"{auteur_mail[0]} : {auteur_mail[1]}" for auteur_mail in recuperationAuteurs(lecteur)])
    ABSTRACT = recuperationAbstract(lecteur)
    DISCUSSION = recuperationDiscussion(lecteur)
    CONCLUSION = recuperationConclusion(lecteur)

    BIBLIOGRAPHIE = recuperationBiblio(lecteur)

    #Formatage des données 
    rendu = [
            "\nNom du fichier :\n\t" + NOM_FICHIER + 
            "\nTitre :\n\t" + TITRE +
            "\nAuteurs :\n\t" + AUTEURS.replace("\n", "\n\t") +
            "\nAbstract : \n\t" + ABSTRACT.replace("\n", "\n\t") +
            "\nDiscussion : \n\t" + DISCUSSION.replace("\n", "\n\t") +
            "\nConclusion : \n\t" + CONCLUSION.replace("\n", "\n\t") +
            "\nBibliographie : \n\t" + BIBLIOGRAPHIE.replace("\n", "\n\t")
            ]

    CreatFich(rendu[0], "./resultat/" + NOM_FICHIER[:-3] + "txt")
    #print(rendu[0])
    print("----------------------------------------------------------------\n") 