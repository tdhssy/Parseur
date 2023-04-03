#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from recuperationInfo import recupInfo
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
    info_text = recupInfo(chemin + selectfic)
    if option =="-t": 
        txt_writer(info_text) #VERSION TXT 
        #print("-t " + chemin +  selectfic)
    elif option =="-x":  
        xml_writer(info_text) #VERSION XML
        #print("-x " + selectfic)
    elif option =="-tx" or option == "-xt":  
        xml_writer(info_text) #VERSION XML
        txt_writer(info_text) #VERSION TXT
        #print("-tx " + selectfic)
    else :
        print("\nUsage: python3 "+sys.argv[0]+" [type]\n")
        print("type:\t-t -> sortie texte\n\t-x -> sortie xml\n\t-xt | -tx -> sortie xml et texte")



def saisie(L):
    inp = input("\nSaisir un chiffre dans la liste ou * : ")
    
    try:
        if inp == "*":
            for i in  L :
                convert(i)
        elif int(inp) >0 and int(inp)<len(L)+1 : 
            selectfic = L[int(inp)-1]
            convert(selectfic)
        else:
            raise Exception
    except:
        print("Erreur veuillez choisir parmis les propositions ")
        saisie(L)
        

if __name__ == '__main__':
    argc = len(sys.argv)


    if argc < 2:
        print("Usage: python3 " + sys.argv[0] + " -t|-x|-tx " )
        exit(1)

    L = []
    selectfic = ""
    chemin = "./pdf_apprentissage/"
    fich = os.listdir(chemin)

    for i in fich:
        #Verification du format du fichier
        verifPDF = i.split(".")[-1] #Récupère seulement l'extension
        try:
            if verifPDF != "pdf":
                raise Exception
        except:
            print(i + " n'est pas au format pdf")
            continue

        #Rajout dans la liste de fichiers
        L.append(i)

        
    #Affichage de menu de selection
    for j in range( len(L)):
        print(str(j+1) + ". " + L[j])
    
    print("*. Tous les fichiers")
    saisie(L)


        
    print("Fin de la génération")
    exit(0)

