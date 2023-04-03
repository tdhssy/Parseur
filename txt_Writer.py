#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

from creationFichier import CreatFich

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionIntro import recuperationIntro
from extractionAbstract import recuperationAbstract
from extractionCorps import recuperationCorps
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
        print(fichier + "est introuvable")
        return 1
    
    #Récupération des informations du fichier
    #INFO = lecteur.metadata
    pages = lecteur.pages
    texte=[]
    for p in pages:
        texte.append(p.extract_text())

    TITRE = recuperationTitre(pages[0],lecteur.metadata)
    AUTEURS = "\n".join([f"{auteur_mail[0]} : {auteur_mail[1]}, {auteur_mail[2]}" for auteur_mail in recuperationAuteurs(texte,TITRE)])
    ABSTRACT = recuperationAbstract(texte)
    INTRODUCTION = recuperationIntro(texte)
    CORPS = recuperationCorps(texte)
    DISCUSSION = recuperationDiscussion(texte)
    CONCLUSION = recuperationConclusion(texte)
    BIBLIOGRAPHIE = recuperationBiblio(texte)

    #Formatage des données 
    
    rendu = [
            "\nNom du fichier :\n\t" + NOM_FICHIER + 
            "\nTitre :\n\t" + TITRE +
            "\nAuteurs :\n\t" + AUTEURS.replace("\n", "\n\t") +
            "\nAbstract : \n\t" + ABSTRACT.replace("\n", "\n\t") +
            "\nIntroduction : \n\t" + INTRODUCTION.replace("\n", "\n\t") +
            "\nCorps : \n\t" + CORPS.replace("\n", "\n\t") +
            "\nDiscussion : \n\t" + DISCUSSION.replace("\n", "\n\t") +
            "\nConclusion : \n\t" + CONCLUSION.replace("\n", "\n\t") +
            "\nBibliographie : \n\t" + BIBLIOGRAPHIE.replace("\n", "\n\t")
            ]

    CreatFich(rendu[0], "./resultat/" + NOM_FICHIER[:-3] + "txt")
    #print(rendu[0])
    
    print("----------------------------------------------------------------\n") 
    