#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fonction permettant la récupération du nom d'un ficher
    -In : chemin d'accès au fichier
    -Out : nom du fichier en str
"""
def extractionNomFichier(fichier: str) -> str:
    return fichier.split('/')[-1]  #.split('.')[0] Pour retirer le '.pdf'   