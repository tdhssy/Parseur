#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from creationFichier import CreatFich

from recuperationInfo import recupInfo


"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(info):

    NOM_FICHIER     = info[0]
    TITRE           = info[1]
    AUTEURS         = info[2]
    ABSTRACT        = info[3]
    INTRODUCTION    = info[4]
    CORPS           = info[5]
    DISCUSSION      = info[6]
    CONCLUSION      = info[7]
    BIBLIOGRAPHIE   = info[8]

    print("Conversion en TXT du fichier [" + NOM_FICHIER + "] en cours ..." )

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
    