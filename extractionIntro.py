#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

def recuperationIntro(pages)->str:

    
    text = "".join([pages[i] for i in range(len(pages))])
    # Le texte que nous allons analyser

    # La regex qui correspond à ce qui est entre "Introduction" et "2."
    regex = r"(I\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n\s*|I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N\s*)\n([\s\S]*?)\n\s*(II|2)\.*\s"
 
    # Utilisation de la fonction search pour trouver la première occurrence de la regex dans la chaîne texte
    correspondance = re.search(regex, text)
    
    # Si une correspondance est trouvée, on affiche le résultat
    if correspondance:
        resultat = correspondance.group(2)
        return resultat
    """
    else:
        print(text)
        print("\n\nIntroduction : ", re.search(r"I\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n\s*|I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N\s*", text))
        print("Fin Intro : ", re.search(r"\n\s*(II|2)\.", text))
    """
    return "N/A"