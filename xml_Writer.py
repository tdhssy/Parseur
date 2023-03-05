#!/usr/bin/env python3
# -- coding: utf-8 --

from PyPDF2 import PdfReader

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionAbstract import recuperationAbstract
from extractionBiblio import recuperationBiblio
from creationFichier import CreatFich

def lecteurPDF(fichier):
    print("Conversion en XML du fichier [" + fichier + "] en cours ..." )

    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)
    
    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 1
    
    
    #Récupération des informations du fichier
    INFO = lecteur.metadata
    TITRE = recuperationTitre(lecteur)
    AUTEURS = ["Pierre dupuis","Jack Dupont"]#recuperationAuteurs(lecteur) #DOIT RENVOYER UNE LISTE DE MAIL
    MAILS = ["ok@gmail.com",""]
    ABSTRACT = recuperationAbstract(lecteur)
    BIBLIOGRAPHIE = recuperationBiblio(lecteur)

    rendu = [
            "<article>\n"+
            "\t<preambule>" + NOM_FICHIER + "</preambule>\n" +
            "\t<titre>" + TITRE +"</titre>\n" +
            "\t<auteurs>\n"
            ]
    
    
    for i in range(len(AUTEURS)):
        rendu.append(
                    "\t\t<auteur>\n"+
                    "\t\t\t<name>"+AUTEURS[i]+"</name>\n"+
                    "\t\t\t<mail>"+MAILS[i]+"</mail>\n"+
                    "\t\t</auteur>\n"
                    )

    rendu.append(
                "\t</auteurs>\n"+
                "\t<abstract>"+ ABSTRACT.replace("\n", "\\n")+"</abstract>\n"+
                "\t<biblio>"+ BIBLIOGRAPHIE.replace("\n", "\\n") + "</bilio>\n"+
                "</article>"
                )
    
    CreatFich("".join(rendu), "./Resultat/" + NOM_FICHIER[:-3] + "xml")
    print("----------------------------------------------------------------\n") 