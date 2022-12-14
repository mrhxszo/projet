#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import customtkinter
from parse import FileSearch
from stanzafr import lemma

### FENETRE PRINCIPALE

fenetre_pr = customtkinter.CTk(fg_color='#FFFFFF')
fenetre_pr.title("moteur de recherche")

titre = customtkinter.CTkLabel(fenetre_pr, text="saisissez le mot-clé")
titre.pack(pady=10)

mot_cle = customtkinter.CTkEntry(fenetre_pr, corner_radius=15, width=400,height=40)
mot_cle.pack(pady=10)


def affiche_res():  
    mots_cle = mot_cle.get()
    mots_cle_final=mots_cle.split()
    print(mots_cle_final)
    filee = FileSearch()
    filee.parse("./texts")
    filee.search(filee.wordIndex(),mots_cle_final)


rechercher = customtkinter.CTkButton(master=fenetre_pr, text="rechercher", command=affiche_res, compound="left", fg_color='#FFFFFF')
rechercher.pack(side='bottom')

fenetre_pr.mainloop()
