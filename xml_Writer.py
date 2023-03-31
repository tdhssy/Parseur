#!/usr/bin/env python3
# -- coding: utf-8 --

from PyPDF2 import PdfReader
from creationFichier import CreatFich

from extractionTitre import recuperationTitre
from extractionNomFichier import extractionNomFichier
from extractionAuteur import recuperationAuteurs
from extractionAbstract import recuperationAbstract
from extractionCorps import recuperationCorps
from extractionDiscussion import recuperationDiscussion
from extractionBiblio import recuperationBiblio


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
    AUTEURS = recuperationAuteurs(lecteur) #["Pierre dupuis","Jack Dupont"] #DOIT RENVOYER UNE LISTE DE MAIL
    ABSTRACT = recuperationAbstract(lecteur)
    CORPS = recuperationCorps(lecteur)
    DISCUSSION = recuperationDiscussion(lecteur)
    BIBLIOGRAPHIE = recuperationBiblio(lecteur)

    #print(str(AUTEURS))

    rendu = [
            "<article>\n"+
            "\t<preambule>" + NOM_FICHIER + "</preambule>\n" +
            "\t<titre>" + TITRE +"</titre>\n" +
            "\t<auteurs>\n"
            ]
    
    
    for i in range(len(AUTEURS)):
        rendu.append(
                    "\t\t<auteur>\n"+
                    "\t\t\t<name>"+AUTEURS[i][0]+"</name>\n"+
                    "\t\t\t<mail>"+AUTEURS[i][1]+"</mail>\n"+
                    "\t\t</auteur>\n"
                    )

    rendu.append(
                "\t</auteurs>\n"+
                "\t<abstract>"+ ABSTRACT.replace("\n", "\\n")+"</abstract>\n"+
                "\t<corps>"+ CORPS.replace("\n", "\\n")+"</corps>\n"+
                "\t<discussion>"+ DISCUSSION.replace("\n", "\\n")+"</discussion>\n"+
                "\t<biblio>"+ BIBLIOGRAPHIE.replace("\n", "\\n") + "</bilio>\n"+
                "</article>"
                )
    
    CreatFich("".join(rendu), "./resultat/" + NOM_FICHIER[:-3] + "xml")
    print("----------------------------------------------------------------\n") 