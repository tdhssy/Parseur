#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from txt_Writer import lecteurPDF as txt_writer
from xml_Writer import lecteurPDF as xml_writer
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
        exit(1)
    
    for i in range(1, argc):
        fichier = sys.argv[i]
        
        #Verification du format du fichier
        verifPDF = fichier.split(".")[-1] #Récupère seulement l'extension
        try:
            if verifPDF != "pdf":
                raise Exception
        except:
            print(fichier + " n'est pas au format pdf")
            continue

        #Analyse du fichier pdf
        txt_writer(fichier) #VERSION TXT
        xml_writer(fichier) #VERSION XML
        
    print("Fin de la génération")
    exit(0)