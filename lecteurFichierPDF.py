#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(fichier):
    print("Analyse de " + fichier + " en cours ..." )

    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)
    
    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 
    
    #Récupération des informations du fichier
    INFO = lecteur.metadata
    TITRE = recuperationTitre(lecteur)
    print(TITRE)
    AUTEURS = recuperationAuteurs(INFO)
    #rendu = ["Titre :\n\t" + TITRE + 
    #        " test"]
    #print(rendu[0])


def extractionNomFichier(fichier):
    return fichier.split('/')[-1]  #.split('.')[0] Pour retirer le '.pdf'

def recuperationTitre(lecteur):
    info=lecteur.metadata
    titre = info.title

    def taille_entête(text,cm,tm,fontDict,fontSize): #on s'interesse à la taille de la police fontsize
            y=tm[5] #tm pour text matrice
            if fontSize > 14 and y>550: #si supérieur à taille basique alors c'est le titre et si assez haut dans le document
                titretmp_ligne.append(text) # on ajoute dans la variable temporaire la ligne en question

    if(titre==None):
        page=lecteur.pages[0] #on prends la 1ère page
        titretmp_ligne = [] #on crée tableau vide
        titre= "" # on transforme titre de None a string
        

        page.extract_text(visitor_text=taille_entête) # appelle de la définition taille_entete
        titretmp_ligne= "".join(titretmp_ligne).split("\n") # on regroupe toutes les lignes et on les sépare en fonction des retour à la ligne
        
        """
            pour toutes les lignes on ajoute à la variable titre la ligne i avec un espace à la fin.
            Si dernière ligne à rajouter, pas d'espace à la fin
        """
        for i in range(len(titretmp_ligne)): 
            if (i!=len(titretmp_ligne)-1) :
                titre += titretmp_ligne[i]+" "
            else:
                titre += titretmp_ligne[i]
        
    if titre.startswith("/"): #Reparation de fortune pas opti
        page=lecteur.pages[0]
        tmptitre= page.extract_text(visitor_text=taille_entête)
        tmptitre= tmptitre.split("\n")[0]
        titre = tmptitre
    return titre

def recuperationAuteurs(metadata):
    auteurs = metadata.author
    #TODO metadata.author peut renvoyer none. A gérer dans ce cas
    return auteurs