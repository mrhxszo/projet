#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import customtkinter
from PIL import Image, ImageTk
from parse import FileSearch

### FENETRE PRINCIPALE

fenetre_pr = customtkinter.CTk(fg_color='#FFFFFF')
fenetre_pr.title("moteur de recherche")


loupe = ImageTk.PhotoImage(Image.open("loupe.png").resize((20,20),Image.ANTIALIAS))
image_google = ImageTk.PhotoImage(Image.open("google.png").resize((300,140),Image.ANTIALIAS))

google = customtkinter.CTkButton(fenetre_pr,image=image_google, fg_color='#FFFFFF',state='disabled',text='')
google.pack(side='top')

titre = customtkinter.CTkLabel(fenetre_pr, text="saisissez le mot-clé",text_font=("Helvetica","12"))
titre.pack(pady=10)

mot_cle = customtkinter.CTkEntry(fenetre_pr, corner_radius=15, width=400,height=40, text_font=("Helvetica","12"))
mot_cle.pack(pady=10)


def affiche_res():  
    mots_cle = mot_cle.get()
    mots_cle_final=mots_cle.split()
    print(mots_cle_final)
    filee = FileSearch()
    filee.parse("./texts")
 
    filee.wordIndex()

    filee.search(filee.wordIndex(),mots_cle_final)


rechercher = customtkinter.CTkButton(master=fenetre_pr, text="rechercher", command=affiche_res, image=loupe, 
                        compound="left", fg_color='#FFFFFF',text_font=("Helvectica","15"))
rechercher.pack(side='bottom')

fenetre_pr.mainloop()
