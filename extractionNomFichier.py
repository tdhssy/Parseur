#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fonction permettant la récupération du nom d'un ficher
    -fichier : chemin d'accès au fichier
    -return : nom du fichier
"""
def extractionNomFichier(fichier):
    return fichier.split('/')[-1]  #.split('.')[0] Pour retirer le '.pdf'   