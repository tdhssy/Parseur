#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

"""
Fonction permettant la récupération de la partie abstract d'un fichier pdf
en utilisant une expression régulière
    -In : PdfReader
    -Out : représentation en str de la partie
           abstarct du document si elle existe
"""
def recuperationAbstract(lecteur: PdfReader) -> str:
    page=lecteur.pages[0] #on prends la 1ère page
    res = ""
    try:
        abstract = re.findall(r'(?i)abstract([\s\S]*?)(?i)i[\s]?ntroduction', page.extract_text())[0].split('\n')
        for ligne in abstract:
            res += ligne + "\n"
        abstract.pop(-1) #On enlève la dernière ligne
    except:
        res = "Aucun Abstract."
    return res