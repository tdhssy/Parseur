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
def recuperationAbstract(page) -> str:
    abstract = ""
    try:
        abstract = re.findall(r'(?i)abstract([\s\S]*?)((1[.]?|I[.]?)[\s]*)?i[\s]?ntroduction', page)[0][0]
    except Exception as e:
        #print(e) 
        abstract = "N/A"
    return abstract