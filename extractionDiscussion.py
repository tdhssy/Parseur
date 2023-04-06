#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re



def recupPara(chaine_str , mot, liste_mots_prec=[]) -> str :
    res=""
    sep_re=re.compile(r'[\\n\.]([A-Z0-9][A-Z0-9]*\.*\s)*'+mot[0]+r'\s*('+mot[1:]+r'|'+mot[1:].upper()+r')(\s\w*)*(.*)')
    find=sep_re.findall(repr(chaine_str))
    if len(find)!=0 :
        #print("find")
        res=find[0][3]
        #print(res)
        for m in liste_mots_prec :
            sep_re=re.compile(r'[\\n\.]([A-Z0-9][A-Z0-9]*\.*\s)*'+m[0]+r'\s*('+m[1:]+r'|'+m[1:].upper()+r')(\s\w*)*(.*)')
            res=sep_re.sub("",res)


    return res

"""
Fonction permettant la récupération de la partie Discussion d'un fichier pdf
en utilisant une expression régulière
    -In : PdfReader
    -Out : représentation en str de la partie
           discussion du document si elle existe
"""
def recuperationDiscussion(pages) -> str:
    nb_pages = len(pages)
    pre_occurence = nb_pages

    text=""

    while(pre_occurence): #Navigue jusqu'a trouver la première occurence du mots en partant de la fin
        pre_occurence-=1
        disc = re.compile(r'[D]\s*iscussion|ISCUSSION')

        if disc.search(pages[pre_occurence]) :
            #print("Trouver page "+str(pre_occurence))
            break

    if(pre_occurence):
        while (pre_occurence<nb_pages):
            text +=pages[pre_occurence]
            pre_occurence+=1
            
        
        text = recupPara(text,"Discussion",["Appendix","Conclusions","Acknowledgments"])
    else :
        text = "N/A"

    
     
    return text.replace("\\n","\n")