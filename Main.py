#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import sys

def readerPDF(fichier):

    #Lecture du fichier pdf
    try:
        reader = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 
    
    #Récupération des informations du fichier
    info = reader.metadata
    titre = info.title
    auteurs = info.author


    nb_page = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    #print(text)

if __name__ == '__main__':
    argc = len(sys.argv)

    if argc < 2:
        print("Usage: python3 " + sys.argv[0] + " FILE.pdf ..." )
    
    for i in range(1, argc):
        fichier = sys.argv[i]
        verifPDF = fichier.split(".")

        #Verification du format du fichier
        try:
            if verifPDF[1] != "pdf":
                print(fichier + " n'est pas au format pdf")
                continue
        except:
            print(fichier + " n'est pas au format pdf")
            continue

        #Analyse du fichier pdf
        print("Analyse de " + fichier + " en cours ..." )
        readerPDF(fichier)
        print("Analyse terminée")
    
    exit(0)