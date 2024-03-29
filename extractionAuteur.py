#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader
from extractionTitre import recuperationTitre
import re

"""
Fonction permettant l'extraction du ou des auteurs d'un article pdf
TODO modification à venir
"""

def capitalise(chaine):
    mots = chaine.split()  # séparer les mots de la chaîne
    mots_capitalises = [mot.capitalize() for mot in mots]  # mettre en majuscule la première lettre de chaque mot
    return " ".join(mots_capitalises)  # recombiner les mots en une chaîne avec un espace entre chaque mot


def recuperationAuteurs(pages,titre) -> str:

    texte = pages[0]#.replace("\n","") #aligne tout le texte sur une ligne
    index_debut = texte.find(titre) #récupération de l'index du titre dans le texte
    index_debut+=len(titre) #Incrémentation de l'index pour allez à la fin du titre
    index_fin = texte.lower().find("abstract") #Récupération de l'index du début de l'abstract
    if(index_fin==-1): #Vérification si l'abstract existe
        index_fin = texte.lower().find("introduction") #Si l'abstract n'existe pas on estime que l'auteur est entre le titre et l'intro
    resultat = texte[index_debut:index_fin]
    #print("\ntext :\n", resultat)
    
    #---------------------- Partie pour retrouvé les mails --------------------#
    index_select = -1
    emails=[]

    #RFC2822 Internet Message Format
    email_regex = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"  #r"!\s.*@[a-z\.\-]+"
    
    liste_ligne = texte.split("\n")

    emails = re.findall(email_regex, texte)
    
    """
    #print("liste : "+str(liste_ligne))
    for mail in liste_ligne:
        index_select+=1
        if "@" in mail : #Selection seulement des lignes contenant au moins un @

            if(len(re.findall(r"\w+@",mail)) == 0 ) : #Check s'il n'y a pas de un bout avant le @ manquant dans le mail
                mail = liste_ligne[index_select-1]+mail

            if(len(re.findall(r"@\w+[\-\.]$",mail)) != 0 ) : #Check s'il n'y a pas de un bout après le @ manquant dans le mail
                mail = mail+liste_ligne[index_select+1]

            mail=re.sub(r"[3-9]rd|1st|2nd","", mail) #Traitement des numérotation en fin de page

            #Pose soucis pour le cas de mikheev
            #"""
            #if "," in mail : #Check si on a une liste de préfix
            #    postfix = re.findall(r"@[\w\.\-]+",mail)[0]
            #    prefix = re.sub(r"@[\w\.\-]+|[\(\)\{\}\[\]]","",mail) #Supression de l'entourage
            #    mail = re.sub(r",",postfix+" ",prefix)
            #    print("postfix :"+postfix)
            #    print("prefix :"+str(prefix))
            #"""
            #print("Mail : "+mail)

            #Application des expressions régulières
    """        email = re.findall(email_regex, mail)
            if len(email)>0:
                emails.append(str(email[0]))
    """
    
    # Expression régulière pour extraire les adresses e-mail
    email_regex2 = r'\(([^)\n]*)\)[\n]*(@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)'

    # Recherche des correspondances avec l'expression régulière
    matches = re.search(email_regex2, resultat)

    if matches != None:
        listNom = matches.group(1).split(",")
        for nom in listNom:
            emails.append(nom + matches.group(2))
    
   
    
    #---------------------- Partie pour retrouvé les noms --------------------#

    #nom_test = re.findall(r'(\s*(^\w)*?([A-Z][a-z]+))+', pages[0])
    #print(nom_test)
    #print(pages[0])

    nom_email = []
    if len(emails)>0:
        #print("Emails extraits :\n", emails)
        
        for adresse in emails:
            # Rechercher le nom associé à l'adresse e-mail en supposant que le nom est juste avant l'adresse e-mail
            nom_email.append( capitalise(adresse.split('@')[0].replace('.', ' ').replace('_', ' ')))
            

            #texte = texte.replace(adresse, "")

        #print("mail :"+str(emails))
        #print("Nom mail :"+str(nom_email))

    #---------------------- Partie pour retrouvé les affiliations --------------------#
    #On part du principe que les affiliations sont entre l'email et le nom d'un auteur
    #On cherche la ligne contenant le nom puis celle contenant l'email et on prend ce qu'il y a au milieu
    affiliations = []
    lignes = texte.split("\n")
    if len(emails)>0:
        for nom, adresse in zip(nom_email, emails):
            debut = nom
            fin = adresse.split("@")[1]
            index_debut = -1
            index_fin = -1
            debuTrouve = False
            finTrouve = False
            cpt = 0
            for ligne in lignes:
                cpt += 1
                if (ligne.lower().find(debut.lower()) != -1) and not debuTrouve:
                    index_debut = cpt
                    debuTrouve = True
                elif (ligne.lower().find(fin.lower()) != -1) and debuTrouve:
                    index_fin = cpt -1
                    finTrouve = True
                if finTrouve and debuTrouve:
                    break
            if index_debut != -1 and index_fin != -1:
                if (index_fin-index_debut) > 7: #L'email se trouve en fin de page
                    affiliations.append("".join(lignes[index_debut:index_debut+1])) #On suppose que c'est la ligne après le nom
                else:
                    affiliations.append(" ".join((lignes[index_debut:index_fin])))
            else:
                affiliations.append("N/A")
            

    res = [[elem1, elem2, elem3] for elem1, elem2, elem3 in zip(nom_email, emails, affiliations)]
    #print(str(res))

    #texte = texte.replace("\n"," ").split(" ")

    """
        for nom in nom_email :

            # Chercher la correspondance la plus proche entre le nom dans l'adresse e-mail et les noms dans la liste des auteurs
            correspondance_la_plus_proche = difflib.get_close_matches(nom, texte, n=1, cutoff=0)
            print("compare "+nom)

            if correspondance_la_plus_proche :
                print("correspondance : " + str(correspondance_la_plus_proche))
    """
    




    #V1
    """

    met = lecteur.metadata.author # On obtient les meta datas puis on cherche les autheur
    noms_associés = {}
    author = ""
    if True:
        #authors = met.split(";")  # on les imbrique correctement dans un tableau
        #print("autheur :\n", authors)
        print("adresse :"+str(emails))
        if len(emails)>0:
            
            
            for adresse in emails:# Parcourir les adresses e-mail trouvées

                
                # Rechercher le nom associé à l'adresse e-mail en supposant que le nom est juste avant l'adresse e-mail
                nom_email = adresse.split('@')[0].replace('.', ' ').replace('_', ' ')

                print("Nom mail :"+str(nom_email))

                # Chercher la correspondance la plus proche entre le nom dans l'adresse e-mail et les noms dans la liste des auteurs
                correspondance_la_plus_proche = difflib.get_close_matches(nom_email, authors, n=1, cutoff=0.2)

                # Si une correspondance a été trouvée, ajouter l'association nom-adresse e-mail au dictionnaire
                if correspondance_la_plus_proche:
                    noms_associés[correspondance_la_plus_proche[0]] = adresse

            # Afficher le dictionnaire des noms associés aux adresses e-mail
            #print("dictio: \n", noms_associés)
    """
    return res #noms_associés , emails, authors


    