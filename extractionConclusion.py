from PyPDF2 import PdfReader
import re

"""
    Différents cas : Conclusion / Acknowledgements|References
                     Conclusions and future work
                     Conclusions and future work
                     Conclusion and perspectives
                     Discussion / Appendix
                     Conclusion / 


"""

def recuperationConclusion(pages) -> str:
    try:
        conclusion= ''
        continuer = False # cas pour quand la conclusion prends + d'une page (pas fait)
        Lettreenmaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for page in pages:
            text = page
            
            verif_mot=page
            if (not continuer):
                match = re.search(r'(?:C ONCLUSIONS?\w?[.:;]?\s*(?!\s*$)*|Conclusions?\w?[.:;]?\s*(?!\s*$)*?)([\s\S]*?)(?:\s*(?:Acknowledgements|Acknowledgments.|Acknowledgment|References|REFERENCES|Appendix|Follow-Up Work|\Z)|\s*\Acknowledgments\b[.:;]?)\s*', text)
                #match experience= re.search(r'(?:C ONCLUSIONS[\s\S]*|Conclusion(?s)[\s\S]*?)([\s\S]*?)(?:\s*(?:Acknowledgements|Acknowledgments.|Acknowledgment|References|REFERENCES|Appendix|Follow-Up Work|\Z)|\s*\Acknowledgments\b[.:;]?)',text)
                # Expression régulière actuelle qui marche le mieux
                test = re.search(r'(?:Acknowledg(?:ements|ment)s?|REFERENCES|R EFERENCES|References|Appendix|ACKNOWLEDGMENT|Follow-Up Work)',verif_mot)
                #testv2 = re.search(r'(?:C ONCLUSIONS?\w?[.:;]?\s*(?!\s*$)*|Conclusions?\w?[.:;]?\s*(?!\s*$)*?)([\s\S]*?)(?:References)',verif_mot)

                if match:
                    #print("check")
                    retirer_txt_inutile=match.group(1)
                    retirer_txt_inutile=retirer_txt_inutile.split("\n")
                    if not (retirer_txt_inutile[0][0] in Lettreenmaj): #verifie que c'est le début de la ligne
                        retirer_txt_inutile.pop(0)
    
                    #print(retirer_txt_inutile[0])
                    goodTxt="\n".join(retirer_txt_inutile)

                    #print(goodTxt)
                    conclusion+= goodTxt
                    #print(test)
                    if not test:
                        #print("AHOUIOUI")
                        continuer=True
                    #print(conclusion)
            else : 
                matchx = re.search(r'([\s\S]*?)(?:ACKNOWLEDGMENT|Acknowledgements|ACKNOWLEDGMENT|References|Appendix|Follow-Up Work|\Z)', text)
                #print(matchx.group(1))
                test = re.search(r'(?:Acknowledg(?:ements|ment)s?|REFERENCES|R EFERENCES|References|Appendix|ACKNOWLEDGMENT|Follow-Up Work)',verif_mot)
                #print("#######")
                if matchx:
                    conclusion+="\n"+matchx.group(1)
                    #continuer=False
                    if test:
                        #print("AHOUIOUI")
                        continuer=False
        if (conclusion==""):
            conclusion = "Pas de conclusion détectée.\n"
    except Exception as e:
        #print(e) 
        conclusion = "N/A"
    return conclusion


"""
from PyPDF2 import PdfReader
import re


    Différents cas : Conclusion / Acknowledgements|References
                     Conclusions and future work
                     Conclusions and future work
                     Conclusion and perspective
                     Conclusion / Appendix


def recuperationConclusion(lecteur: PdfReader) -> str:
    pages=[]
    for num_page in range(len(lecteur.pages)):
        page=lecteur.pages[num_page]
        pages.append(page)
    try:
        conclusion= ''
        continuer = False # cas pour quand la conclusion prends + d'une page (pas fait)
        for page in pages:
            text = page.extract_text()
            verif_mot=page.extract_text()
            if (not continuer):
                #TEST 1match = re.search(r'(?:Conclusion|Conclusions)([\s\S]*?)(?:Acknowledgements|References|Appendix|Follow-Up Work|\Z)', text)
                #TEST 2match = re.search(r'(?:(?<=Conclusion[\s\S])([\s\S]*)|Conclusions[\s\S])([\s\S]*)(?=Acknowledgements|References|Appendix|Follow-Up Work|\Z)', text)
                match = re.search(r'(?:C ONCLUSIONS?\w?[.:;]?\s*(?!\s*$)*|Conclusions?\w?[.:;]?\s*(?!\s*$)*?)([\s\S]*?)(?:\s*(?:Acknowledgements|Acknowledgments.|Acknowledgment|References|REFERENCES|Appendix|Follow-Up Work|\Z)|\s*\Acknowledgments\b[.:;]?)\s*', text)
                # Expression régulière actuelle qui marche le mieux
                test = re.search(r'(?:Acknowledg(?:ements|ment)s?|REFERENCES|R EFERENCES|Appendix|Follow-Up Work)',verif_mot)
                if match:
                    #print("TEST MATCH ICI\n"+match.group(1))
                    conclusion+= match.group(1)
                    print(test)
                    print("huhuh")
                    if not test:
                        #print("AHOUIOUI")
                        continuer=True
                    #print(conclusion)
            else : #Non utilisé pour l'instant car trop peu fonctionnelle
                matchx = re.search(r'/([\s\S]*?)(?:ACKNOWLEDGMENT|Acknowledgements|ACKNOWLEDGMENT|References|Appendix|Follow-Up Work)/gm', text)
                print(matchx)
                if matchx:
                    conclusion+= matchx.group(1)
                    continuer = False
                if test:
                    #print("AHOUIOUI")
                    continuer=True
        if (conclusion==""):
            conclusion = "Pas de conclusion détectée.\n"
    except Exception as e:
        #print(e) 
        conclusion = "Problème d'analyse\n"
    return conclusion
"""