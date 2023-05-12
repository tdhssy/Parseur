
from PyPDF2 import PdfReader
from extractionAbstract import recuperationAbstract
from extractionAuteur import recuperationAuteurs
from extractionBiblio import recuperationBiblio
from extractionConclusion import recuperationConclusion
from extractionCorps import recuperationCorps
from extractionDiscussion import recuperationDiscussion
from extractionIntro import recuperationIntro
from extractionNomFichier import extractionNomFichier
from extractionTitre import recuperationTitre


def recupInfo(fichier):
    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)

    print("Conversion en XML du fichier [" + NOM_FICHIER + "] en cours ..." )

    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + "est introuvable")
        return []
    
    #Récupération des informations du fichier
    #INFO = lecteur.metadata
    pages = lecteur.pages
    texte=[]
    for p in pages:
        texte.append(p.extract_text().
                     replace("\v", "ff").
                     replace("\f", "fi").
                     replace("\x0E", "ffi").
                     replace("\x0F", "•").
                     replace("\x13", "é").
                     replace("&", "&amp;").
                     replace("<", "&lt;").
                     replace(">", "&gt;").
                     replace("`", "&apos;").
                     replace('"', "&quot;").
                     replace("", ""))
        
    TITRE = recuperationTitre(pages[0],lecteur.metadata)
    AUTEURS = "\n".join([f"{auteur_mail[0]} : {auteur_mail[1]}, {auteur_mail[2]}" for auteur_mail in recuperationAuteurs(texte,TITRE)])
    ABSTRACT = recuperationAbstract(texte)
    INTRODUCTION = recuperationIntro(texte)
    CORPS = recuperationCorps(texte)
    DISCUSSION = recuperationDiscussion(texte)
    CONCLUSION = recuperationConclusion(texte)
    BIBLIOGRAPHIE = recuperationBiblio(texte)


    return [NOM_FICHIER, TITRE, AUTEURS, ABSTRACT, INTRODUCTION, CORPS, DISCUSSION, CONCLUSION, BIBLIOGRAPHIE]