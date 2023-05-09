#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
import re

"""
Fonction permettant la récupération du titre d'un fichier pdf
    -In : PdfReader
    -Out : titre du document en str
"""
def recuperationTitre(pages,info) -> str:
    titre = info.title

    #print("Meta info : "+str(info))

    def taille_entête(text,cm,tm,fontDict,fontSize): #on s'interesse à la taille de la police fontsize
        y=tm[5] #tm pour text matrice
        if fontSize > 14 and y>550: #si supérieur à taille basique alors c'est le titre et si assez haut dans le document
            titretmp_ligne.append(text) # on ajoute dans la variable temporaire la ligne en question
        #print(titretmp_ligne)

    if(titre==None):
        
        for index in range(2):
            page=pages[index] #on prends la 1ère page
            titretmp_ligne = [] #on crée tableau vide
            titre= "" # on transforme titre de None a string
            

            page.extract_text(visitor_text=taille_entête) # appelle de la définition taille_entete
            titretmp_ligne= "".join(titretmp_ligne).split("\n") # on regroupe toutes les lignes et on les sépare en fonction des retour à la ligne
            
            
            #    pour toutes les lignes on ajoute à la variable titre la ligne i avec un espace à la fin.
            #    Si dernière ligne à rajouter, pas d'espace à la fin
            
            for i in range(len(titretmp_ligne)): 
                if (i!=len(titretmp_ligne)-1) :
                    titre += titretmp_ligne[i]+" "
                else:
                    titre += titretmp_ligne[i]

    try:
        if (not titre[0].isupper()): #Cas ou la métadonné ne correspond pas a un titre
            for index in range(2):
                page=pages[index]
                tmptitre= page.extract_text(visitor_text=taille_entête)
                tmptitre= tmptitre.split("\n")[0]
                titre = re.findall(r'(?<=[a-z]{5})[A-Z].*$', tmptitre)[0]
    except:
        titre="N/A"
        
    
    return titre