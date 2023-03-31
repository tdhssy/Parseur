#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
from extractionDiscussion import recupPara
import re

def recuperationCorps(lecteur: PdfReader) -> str:
    text = "".join([ lecteur.pages[i].extract_text() for i in range(len(lecteur.pages))])
    #print(repr(lecteur.pages[0].extract_text()))
    res = "Aucun corps trouver"
    res = recupPara(text,"Introduction",["Discussion","Conclusion","Conclusions"])
    #print("texte corps : "+res)
    #print(text)
        

    return res.replace("\\n","\n")