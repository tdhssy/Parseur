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
    

    rendu = [
            "<?xml version='1.0' encoding='UTF-8'?>\n" +
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
                "\t<abstract>\n"+ ABSTRACT.replace("\n", " ")+"\n\t</abstract>\n"+
                "\t<introduction>\n"+ INTRODUCTION.replace("\n", " ")+"\n\t</introduction>\n"+
                "\t<body>\n"+ CORPS.replace("\n", " ")+"\n\t</body>\n"+
                "\t<discussion>\n"+ DISCUSSION.replace("\n", " ")+"\n\t</discussion>\n"+
                "\t<conclusion>\n"+ CONCLUSION.replace("\n", "")+"\n\t</conclusion>\n"+
                "\t<biblio>\n"+ BIBLIOGRAPHIE.replace("\n", " ") + "\n\t</biblio>\n"+
                "</article>"
                )

    rendu[-1].replace("\nN/A\n\t", "N/A")
    CreatFich("".join(rendu), "./resultat/" + NOM_FICHIER[:-3] + "xml")
    print("----------------------------------------------------------------\n") 