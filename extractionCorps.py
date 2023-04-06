#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
from extractionDiscussion import recupPara
from extractionIntro import recuperationIntro
import re

def recuperationCorps(pages) -> str:
    text = "".join([ pages[i] for i in range(len(pages))])
    #print(repr(lecteur.pages[0].extract_text()))
    res = "N/A"
    res = recupPara(text,"Introduction",["Discussion","Conclusion","Conclusions"])

    #Remet les saut à la ligne
    res = res.replace("\\n","\n")
    
    #recherche de la fin de l'intro
    index = res.find(recuperationIntro(pages)[-10:])

    return res[index+10:]