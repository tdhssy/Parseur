#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from creationFichier import CreatFich

from recuperationInfo import recupInfo


"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(fichier):
    print("Conversion en TXT du fichier [" + fichier + "] en cours ..." )

    res = recupInfo(fichier)

    NOM_FICHIER     = res[0]
    TITRE           = res[1]
    AUTEURS         = res[2]
    ABSTRACT        = res[3]
    INTRODUCTION    = res[4]
    CORPS           = res[5]
    DISCUSSION      = res[6]
    CONCLUSION      = res[7]
    BIBLIOGRAPHIE   = res[8]

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
    