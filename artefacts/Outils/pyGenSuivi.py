#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:23:46 2023

@author: T.D
"""
import textwrap
import datetime
from fpdf import FPDF

#Credit
print("\n\t\t\t===================================")
print("\t\t\t||Version 1.0 de pyGenSuivi de T.D||")
print("====================================================================================")
print("||Programme permettant la génération de fiche de suivi respectant une même template||")
print("====================================================================================\n")

#Liste des identifier prédéfinis
idents = ['identifiant : ', 'Numéro de la tâche : ', 'Durée de réalisation estimée (heure(s)) : ', 'Objectif de la tâche : ', 'Courte explication : ', 'Difficulté(s) (si rencontrée(s)) : ', 'Source(s) : ']

#Demande des entrées utilisateur
inputs = []
for i in range(7):
    inputs.append(input(idents[i]))
    print("\n--------------")

#Choix à choix multiple
options = ['Fonctionnelle', 'Majoritairement fonctionnelle', 'Partiellement fonctionnelle', 'Non fonctionnelle', 'Rien']
print(" 0) Fonctionnelle \n 1) Majoritairement fonctionnelle \n 2) Partiellement fonctionnelle \n 3) Non fonctionnelle \n 4) Rien ")
choice = input("Choisissez une option (0, 1, 2, 3, 4) : ")

#Vérification de la validité de la réponse
while not choice in ['0', '1', '2', '3', '4'] :
	print("\n--------------")
	choice = input("Option non valide. Choisissez une option valide (0, 1, 2, 3, 4) : ")
    	
choice = int(choice)

#Génération du nom du fichier PDF
today = datetime.datetime.now()
file_name = inputs[1] +"_"+str(choice)+ "_@" + inputs[0]+ "_" + today.strftime("%d-%m-%Y") + ".pdf"

#Initialisation du PDF
pdf = FPDF()
pdf.add_page()

#Ajout du titre principal centré
pdf.set_font("Arial", size=24, style='BU')
pdf.cell(190, 30, txt="Suivi de projet", ln=1, align="C")
pdf.ln(10)

pdf.line(10, pdf.get_y(), 190, pdf.get_y())
pdf.line(10, pdf.get_y()+1, 190, pdf.get_y()+1)

#Date
#Sous titre
pdf.set_font("Arial", size=14,style='B')
pdf.cell(95, 8, txt="Date du rapport : ", ln=0, align="L")
#Contenus
pdf.set_font("Arial", size=14)
pdf.cell(95, 8, txt=today.strftime("%d/%m/%Y"), ln=1,align="C")


#Première section
for i in range(3):
    #Sous titre
    pdf.set_font("Arial", size=14,style='B')
    pdf.cell(95, 8, txt=idents[i], ln=0, align="L")
    
    #Contenus
    pdf.set_font("Arial", size=14)
    pdf.cell(95, 8, txt=inputs[i], ln=1,align="C")
pdf.line(10, pdf.get_y(), 190, pdf.get_y())
pdf.line(10, pdf.get_y()+1, 190, pdf.get_y()+1)
pdf.ln(5)



#Seconde section
for i in range(3, 7):
    #Sous titre
    pdf.set_font("Arial", size=14, style='BU')
    pdf.cell(190, 5, txt=idents[i], ln=1, align='L')
    pdf.ln(5)
    
    #Contenus
    pdf.set_font("Arial", size=10)
    #gestion des retours chariot
    lines = inputs[i].split("\\n")
    for line in lines:
        pdf.multi_cell(180, 5, txt=line)

    pdf.line(10, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)
    
#Ajout du choix à choix unique
#Sous titre
pdf.set_font("Arial", size=14, style='BU')
pdf.cell(190, 5, txt="Avancé de la tâche :", ln=1, align='L')
pdf.ln(5)

#Contenus
for i in range(5):
    if (options[i] != options[choice]):
        pdf.set_font("Arial", size=10, style='I')
        pdf.set_text_color(0,0,0)  
        pdf.cell(95, 5, txt=str(i)+") "+options[i]+"*", ln=1,align='L')
    else:
        pdf.set_font("Arial", size=10, style='B')
        pdf.set_text_color(255,0,0)  
        pdf.cell(95, 5, txt=str(i)+") "+options[choice]+"*", ln=1,align='L')
        
pdf.line(10, pdf.get_y(), 190, pdf.get_y())
pdf.ln(5)
pdf.set_font("Arial", size=8, style='I')
pdf.set_text_color(0,0,0)  
pdf.multi_cell(180, 3, txt="*Rien : Tâche non faite.\n*Non fonctionnelle : La tâche de ne fonctionne pas et/ou ne renvoie pas le résultat attendu.\n*Partiellement fonctionnelle : Une petite partie de la tâche fonctionne mais le résultat attendu n'est pas atteint.\n*Semi fonctionnelle : La tâche a été réalisé et renvoie un résultat légèrement différent et/ou avec des bugs.\n*Fonctionnelle : La tâche a été faites et renvoie le résultat attendu.")

#Enregistrement du PDF
pdf.output(file_name)
print("\n\n========================================================================")
print("Pdf créé sous le nom de "+file_name+" dans le repertoire courant.\n")
