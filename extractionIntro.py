#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

def recuperationIntro(pages)->str:

    
    text = "".join([pages[i] for i in range(len(pages))])
    # Le texte que nous allons analyser

    # La regex qui correspond à ce qui est entre "Introduction" et "2."
    regex = r"(?i)introduction\n([\s\S]*?)\n\s*(II|2|\Z)\.*\s"
    #regex = r"(I\sn\st\sr\so\sd\su\sc\st\si\so\sn\s|I\sN\sT\sR\sO\sD\sU\sC\sT\sI\sO\sN\s)\n([\s\S]?)\n\s(II|2).*\s"

    # Utilisation de la fonction search pour trouver la première occurrence de la regex dans la chaîne texte
    correspondance = re.search(regex, text)
    #print(correspondance)
    # Si une correspondance est trouvée, on affiche le résultat
    if correspondance:
        resultat = correspondance.group(1)
        return resultat

    return "N/A"