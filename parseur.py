#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from txt_Writer import lecteurPDF as txt_writer
from xml_Writer import lecteurPDF as xml_writer
import sys
import os

"""

Fonction principale du Parseur.
Permet la vérification du format des fichiers passé en
arguments et lance l'analyse si ceux-ci sont valide.
"""

def convert(selectfic):
    option = sys.argv[1]
    #print("option :"+option)
    if option =="-t": 
        txt_writer(chemin + selectfic) #VERSION TXT 
        print("-t " + chemin +  selectfic)
    elif option =="-x":  
        xml_writer(chemin + selectfic) #VERSION XML
        print("-x " + selectfic)
    elif option =="-tx " or option == "-xt":  
        xml_writer(chemin + selectfic) #VERSION XML
        txt_writer(chemin + selectfic) #VERSION TXT
        print("-tx " + selectfic)
    else :
        print("usage: [type] [nomFichier]\n")
        print(" type:       -t -> sortie txt\n      -x -> sortie xml\n")
        print(" Rappel: Vous pouvez mettre plusieurs fichiers a la suite")


if __name__ == '__main__':
    argc = len(sys.argv)


    if argc < 2:
        print("Usage: python3 " + sys.argv[0] + " -t|-x|-tx <FICHIER.pdf ...>" )
        exit(1)

    L = []
    selectfic = ""
    chemin = "./pdf_apprentissage/"
    fich = os.listdir(chemin)

    for i in fich:


        L.append(i)

        

    for j in range( len(L)):
        print(str(j+1) + ". " + L[j])
    
    print("13. *")

    inp = input("saisir un chiffre dans la liste ")
    if inp == "*":
        for i in  L :
            convert(i)
    elif int(inp) >0 and int(inp)<len(L)+1 : 
        selectfic = L[int(inp)-1]
        convert(selectfic)
    
     
    #Verification du format du fichier
    #    verifPDF = selectfic.split(".")[-1] #Récupère seulement l'extension
    #    try:
    #        if verifPDF != "pdf":
    #            raise Exception
    #    except:
    #        print(selectfic + " n'est pas au format pdf")
    #        continue


        #Analyse du fichier pdf 



        
    print("Fin de la génération")
    exit(0)

