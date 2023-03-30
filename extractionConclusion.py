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
            if (not continuer):
                #TEST 1match = re.search(r'(?:Conclusion|Conclusions)([\s\S]*?)(?:Acknowledgements|References|Appendix|Follow-Up Work|\Z)', text)
                #TEST 2match = re.search(r'(?:(?<=Conclusion[\s\S])([\s\S]*)|Conclusions[\s\S])([\s\S]*)(?=Acknowledgements|References|Appendix|Follow-Up Work|\Z)', text)
                match = re.search(r'(?:C ONCLUSIONS|Conclusions?\w?[.:;]?\s*(?!\s*$)*?)([\s\S]*?)(?:\s*(?:Acknowledgements|Acknowledgments.|Acknowledgment|References|REFERENCES|Appendix|Follow-Up Work|\Z)|\s*\Acknowledgments\b[.:;]?)\s*', text)
                # Expression régulière actuelle qui marche le mieux

                if match:
                    #print("TEST MATCH ICI\n"+match.group(1))
                    conclusion+= match.group(1)
                    #continuer = True
                    #print(conclusion)
            else : #Non utilisé pour l'instant car trop peu fonctionnelle
                matchx = re.search(r'^(^.*?(?=Acknowledgements|ACKNOWLEDGMENT|References|Appendix|Follow-Up Work|$))', text)
                print(matchx.group(1))
                if matchx:
                    conclusion+= matchx.group(1)
                    continuer = False
        if (conclusion==""):
            conclusion = "Pas de conclusion détectée.\n"
    except Exception as e:
        #print(e) 
        conclusion = "Problème d'analyse\n"
    return conclusion