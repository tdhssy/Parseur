#!/usr/bin/env python3
# -- coding: utf-8 --

from creationFichier import CreatFich

from recuperationInfo import recupInfo

def lecteurPDF(info):

    NOM_FICHIER     = info[0]
    TITRE           = info[1]
    AUTEURS         = info[2]
    ABSTRACT        = info[3]
    INTRODUCTION    = info[4]
    CORPS           = info[5]
    DISCUSSION      = info[6]
    CONCLUSION      = info[7]
    BIBLIOGRAPHIE   = info[8]

    print("Conversion en XML du fichier [" + NOM_FICHIER + "] en cours ..." )

    rendu = [
            "<article>\n"+
            "\t<preamble>" + NOM_FICHIER + "</preamble>\n" +
            "\t<titre>" + TITRE +"</titre>\n" +
            "\t<auteurs>\n"
            ]
    
    info_auteurs = AUTEURS.split("\n")
    for i in range(len(info_auteurs)):
        try:
            nom  = info_auteurs[i].split(':')[0]
            mail = info_auteurs[i].split(':')[1].split(',')[0]
            affiliation = info_auteurs[i].split(':')[1].split(',')[1]
            rendu.append(
                        "\t\t<auteur>\n"+
                        "\t\t\t<name>"+nom+"</name>\n"+
                        "\t\t\t<mail>"+mail+"</mail>\n"+
                        "\t\t\t<affiliation>"+affiliation+"</affiliation>\n"+
                        "\t\t</auteur>\n"
                        )
        except:
                rendu.append(
                        "\t\t<auteur>\n"+
                        "\t\t\tN/A"+
                        "\t\t</auteur>\n"
                        )

    rendu.append(
                "\t</auteurs>\n"+
                "\t<abstract>"+ ABSTRACT.replace("\n", " ")+"</abstract>\n"+
                "\t<introduction>"+ INTRODUCTION.replace("\n", " ")+"</introduction>\n"+
                "\t<corps>"+ CORPS.replace("\n", " ")+"</corps>\n"+
                "\t<discussion>"+ DISCUSSION.replace("\n", " ")+"</discussion>\n"+
                "\t<conclusion>"+ CONCLUSION.replace("\n", "")+"</conclusion>\n"+
                "\t<biblio>"+ BIBLIOGRAPHIE.replace("\n", " ") + "</biblio>\n"+
                "</article>"
                )
    
    CreatFich("".join(rendu), "./resultat/" + NOM_FICHIER[:-3] + "xml")
    print("----------------------------------------------------------------\n") 