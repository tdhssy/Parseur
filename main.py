#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lecteurFichierPDF import readerPDF
import sys

"""
Fonction principale du Parseur.
Permet la vérification du format des fichiers passé en
arguments et lance l'analyse si ceux-ci sont valide.
"""
if __name__ == '__main__':
    argc = len(sys.argv)

    if argc < 2:
        print("Usage: python3 " + sys.argv[0] + " <FICHIER.pdf ...>" )
    
    for i in range(1, argc):
        fichier = sys.argv[i]
        
        #Verification du format du fichier
        verifPDF = fichier.split(".")
        try:
            if verifPDF[1] != "pdf":
                raise Exception
        except:
            print(fichier + " n'est pas au format pdf")
            continue

        #Analyse du fichier pdf
        readerPDF(fichier)
        
    exit(0)