#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

def recuperationIntro(pages)->str:

    
    text = "".join([pages[i] for i in range(len(pages))])
    # Le texte que nous allons analyser

    # La regex qui correspond à ce qui est entre "Introduction" et "2."
    #regex = r"(?i)introduction\s([\s\S]*?)(\s*(II|2)\.*\s[A-Z])"
    regex = r"(?i)introduction\s([\s\S]*?)(?:[^a-zA-Z.\ ]((II|2)\.*\s[A-Z]))"
    #(?i)introduction\n([\s\S]*?)(?:\n\s*^(?!2$)(?:2|II|2.)\s?)
    #regex = r"(I\sn\st\sr\so\sd\su\sc\st\si\so\sn\s|I\sN\sT\sR\sO\sD\sU\sC\sT\sI\sO\sN\s)\n([\s\S]?)\n\s(II|2).*\s"

    # Utilisation de la fonction search pour trouver la première occurrence de la regex dans la chaîne texte
    correspondance = re.search(regex, text)
    # Si une correspondance est trouvée, on affiche le résultat
    if correspondance:
        resultat = correspondance.group(1)
        return resultat

    return "N/A"

"""
Fichier : resultatTest-1684010104.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			94.74%
Titre				98.99%
Auteurs				91.29%
Introduction			99.74%
abstract			99.5%
Discussion			N/A
Conclusion			82.2%
Bibliographie			97.13%
Total				94.8%

Fichier : resultatTest-1684010127.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			96.0%
Titre				98.99%
Auteurs				6.56%
Introduction			93.88%
abstract			99.5%
Discussion			N/A
Conclusion			95.88%
Bibliographie			95.66%
Total				83.78%

Fichier : resultatTest-1684010146.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			100.0%
Titre				99.47%
Auteurs				79.97%
Introduction			99.6%
abstract			99.79%
Discussion			N/A
Conclusion			88.7%
Bibliographie			64.32%
Total				90.27%

Fichier : resultatTest-1684010171.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			95.65%
Titre				25.97%
Auteurs				0.0%
Introduction			51.39%
abstract			99.11%
Discussion			N/A
Conclusion			48.9%
Bibliographie			95.96%
Total				59.57%

Fichier : resultatTest-1684010214.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			96.0%
Titre				100.0%
Auteurs				14.27%
Introduction			99.8%
abstract			99.4%
Discussion			N/A
Conclusion			97.62%
Bibliographie			71.74%
Total				82.69%

Fichier : resultatTest-1684010235.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			98.92%
Titre				100.0%
Auteurs				0.0%
Introduction			0.0%
abstract			98.85%
Discussion			N/A
Conclusion			96.14%
Bibliographie			96.48%
Total				70.06%

Fichier : resultatTest-1684010295.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			95.65%
Titre				99.07%
Auteurs				70.4%
Introduction			99.75%
abstract			99.53%
Discussion			N/A
Conclusion			97.81%
Bibliographie			95.52%
Total				86.12%

Fichier : resultatTest-1684010311.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			98.77%
Titre				99.29%
Auteurs				40.01%
Introduction			98.85%
abstract			99.44%
Discussion			N/A
Conclusion			88.63%
Bibliographie			98.3%
Total				89.04%

Fichier : resultatTest-1684010340.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			97.3%
Titre				1.71%
Auteurs				70.71%
Introduction			38.3%
abstract			32.53%
Discussion			N/A
Conclusion			93.38%
Bibliographie			93.85%
Total				61.11%

Fichier : resultatTest-1684010375.txt<br>Precision choisie : souple (90%)
section  		  Precision
--------------------------------------------------------
Preamble			97.96%
Titre				96.36%
Auteurs				12.17%
Introduction			78.88%
abstract			71.32%
Discussion			N/A
Conclusion			55.05%
Bibliographie			89.09%
Total				71.55%
"""