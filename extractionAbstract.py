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
def recuperationAbstract(pages : list) -> str:
    abstract = ""
    
    #print(re.findall(r'(?i)abstract([\s\S]*?)((1[.]?|I[.]?)[\s]*)?i[\s]?ntroduction', pages[1])[0][0])
    try:
        abstract = re.findall(r'(?i)abstract([\s\S]*?)((1[.]?|I[.]?)[\s]*)?i[\s]?ntroduction', pages[0])

        #Si rien n'a été trouvé, c'est que le document commence peut être sur la page 2
        if abstract == []:
            abstract = re.findall(r'(?i)abstract([\s\S]*?)((1[.]?|I[.]?)[\s]*)introduction', pages[1])
        
            if abstract == []:
                abstract = re.findall(r'(?i)abstract([\s\S]*?)\n(1|I)', pages[0])
            
                if abstract == []:
                    abstract = re.findall(r'(?i)abstract([\s\S]*?)\n(1|I)', pages[1])
                    
            
    except Exception as e:
        print(e) 
        return "N/A"
    
    res = ""
    
    try:
        #Si rien n'a été trouvé
        if abstract == []:
            return "N/A"
        res= abstract[0][0]
        
        if res == "":
            raise Exception
        
    except:
        res= abstract[0][1]
        
    return res