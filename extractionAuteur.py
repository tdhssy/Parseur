#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

"""
Fonction permettant l'extraction du ou des auteurs d'un article pdf
TODO modification à venir
"""
def recuperationAuteurs(metadata: PdfReader) -> str:
    auteurs = metadata.author
    #TODO metadata.author peut renvoyer none. A gérer dans ce cas
    return auteurs