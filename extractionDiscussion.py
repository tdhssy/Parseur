#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re



def recupPara(chaine_str , mot) -> str :

    #sep = "SEPARATEUR" #Séparateur arbitraire
    pot_mot= ["[A]*\s*ppendix","[C]*\s*onclusions","[A]*\s*cknowledgments"]
    
    #supprime tout les index de chapitre 
    chap_sep_re = r"(?=\b[XLVI]{1,6}\b)(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})\.|(\n\d\.\s)"
    etape_1 = re.sub(chap_sep_re,"",chaine_str).replace("\n","\\n") 
    #etape_1 =chaine_str.replace("\n","\\n")
    #print("Etape 1 : "+etape_1)

    #Récupération du mot rechercher en sous-titre et prévois si 1er lettre séparer espace
    sub_avant_re = re.compile(r"(.*)["+mot[0]+"]{0,1}\s*"+mot[1:],re.IGNORECASE) 
    etape_2 = sub_avant_re.sub("",etape_1) 
    #print("\nEtape 2 : "+str(etape_2))

    #supprime les possibles partie après 
    etape_3 = etape_2
    for part in pot_mot :
        sub_après_re = re.compile(part+".*",re.IGNORECASE) 
        if re.search(sub_après_re,etape_3):
            etape_3 = sub_après_re.sub("",etape_3)
            #print("\nmot : "+part+"\nEtape 3 : "+str(etape_3))

    

    return etape_3

"""
Fonction permettant la récupération de la partie Discussion d'un fichier pdf
en utilisant une expression régulière
    -In : PdfReader
    -Out : représentation en str de la partie
           discussion du document si elle existe
"""
def recuperationDiscussion(lecteur: PdfReader) -> str:
    nb_pages = len(lecteur.pages)
    pre_occurence = nb_pages

    text=""

    while(pre_occurence): #Navigue jusqu'a trouver la première occurence du mots en partant de la fin
        pre_occurence-=1
        disc = re.compile(r'[D]\s*iscussion|ISCUSSION')

        if disc.search(lecteur.pages[pre_occurence].extract_text()) :
            #print("Trouver page "+str(pre_occurence))
            break

    if(pre_occurence):
        while (pre_occurence<nb_pages):
            text +=lecteur.pages[pre_occurence].extract_text()
            pre_occurence+=1
            
        
        text = recupPara(text,"DISCUSSION")
    else :
        text = "Aucune discussion trouvée."

    
     
    return text.replace("\\n","\n")