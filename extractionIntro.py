#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

def recuparationIntro(lecteur: PdfReader)->str:

    text = "".join([ lecteur.pages[i].extract_text() for i in range(len(lecteur.pages))])
    # Le texte que nous allons analyser

    # La regex qui correspond à ce qui est entre "Introduction" et "2."
    regex = r"I\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n\s*\n([\s\S]*?)\n\s*(II|2)"
 
    # Utilisation de la fonction search pour trouver la première occurrence de la regex dans la chaîne texte
    correspondance = re.search(regex, text)

    print(text)

    # Si une correspondance est trouvée, on affiche le résultat
    if correspondance:
        resultat = correspondance.group(1)
        return resultat
    return ""