#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

def recuparationIntro(lecteur: PdfReader)->str:
    
    print("\nHello Intro")

    text = "".join([ lecteur.pages[i].extract_text() for i in range(len(lecteur.pages))])
    intro_pattern = re.compile(r"Introduction\n")
    end_pattern = re.compile(r"\n2\. ")

    print(text)
    intro_match = intro_pattern.search(text)
    end_match = end_pattern.search(text, intro_match.end())

    if intro_match and end_match:
        extracted_text = text[intro_match.end():end_match.start()].strip()
        print(extracted_text)
    else:
        print("No match found.")

