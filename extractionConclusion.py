from PyPDF2 import PdfReader
import re

def recuperationConclusion(lecteur: PdfReader) -> str:
    pages=[]
    for num_page in range(len(lecteur.pages)):
        page=lecteur.pages[num_page]
        pages.append(page)
    #page = lecteur.pages[26]
    try:
        for page in pages:
            conclusion = re.findall(r'(?i)Conclusion([\s\S]*?)Acknowledgements', page.extract_text())[0]
            print(conclusion)
        #conclusion = re.findall(r'(?i)Conclusion([\s\S]*?)(Acknowledgements|References)', page.extract_text())[0]

    except Exception as e:
        #print(e) 
        conclusion = "Pas de conclusion je crois ? peut-être..\n"
    return conclusion