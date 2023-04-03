#!/usr/bin/env python3
# -- coding: utf-8 --

from creationFichier import CreatFich

from recuperationInfo import recupInfo

def lecteurPDF(fichier):
    print("Conversion en XML du fichier [" + fichier + "] en cours ..." )

    res = recupInfo(fichier)

    NOM_FICHIER     = res[0]
    TITRE           = res[1]
    AUTEURS         = res[2]
    ABSTRACT        = res[3]
    INTRODUCTION    = res[4]
    CORPS           = res[5]
    DISCUSSION      = res[6]
    CONCLUSION      = res[7]
    BIBLIOGRAPHIE   = res[8]

    rendu = [
            "<article>\n"+
            "\t<preambule>" + NOM_FICHIER + "</preambule>\n" +
            "\t<titre>" + TITRE +"</titre>\n" +
            "\t<auteurs>\n"
            ]
    
    info_auteurs = AUTEURS.split("\n")
    for i in range(len(info_auteurs)):
        try:
            nom  = info_auteurs[i].split(':')[0]
            mail = info_auteurs[i].split(':')[1].split(',')[0]
            affiliation = info_auteurs[i].split(':')[1].split(',')[1]
        except:
            nom = ""
            mail = ""
            affiliation = ""

        rendu.append(
                    "\t\t<auteur>\n"+
                    "\t\t\t<name>"+nom+"</name>\n"+
                    "\t\t\t<mail>"+mail+"</mail>\n"+
                    "\t\t\t<affiliation>"+affiliation+"</affiliation>\n"+
                    "\t\t</auteur>\n"
                    )

    rendu.append(
                "\t</auteurs>\n"+
                "\t<abstract>"+ ABSTRACT.replace("\n", "\\n")+"</abstract>\n"+
                "\t<introduction>"+ INTRODUCTION.replace("\n", "\\n")+"</>\n"+
                "\t<corps>"+ CORPS.replace("\n", "\\n")+"</corps>\n"+
                "\t<discussion>"+ DISCUSSION.replace("\n", "\\n")+"</discussion>\n"+
                "\t<conclusion>"+ CONCLUSION.replace("\n", "\\n")+"</conclusion>\n"+
                "\t<biblio>"+ BIBLIOGRAPHIE.replace("\n", "\\n") + "</bilio>\n"+
                "</article>"
                )
    
    CreatFich("".join(rendu), "./resultat/" + NOM_FICHIER[:-3] + "xml")
    print("----------------------------------------------------------------\n") 