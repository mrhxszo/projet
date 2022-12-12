#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os
import re
import json
os.system("clear")

class FileSearch:

    #defined i and indexedfile as static attributes because parse is called recursively and calling them inside the method won't conserve the value
    i = 0
    j=0
    indexed_doc={}
    indexedFile = {}
    match=[]

    def parse(self, files) :

        list = os.listdir(files)
        for file in list:
            if os.path.isdir(files + "/" + file) :
                self.parse(files + "/"+ file)
            else :
                chain = file.split(".")
                #index the sentence in the file and put it inside indexedfile dictionary
                indexed = self.index(files + "/" + file)


                self.indexed_doc[self.i]=chain[0]

                #self.indexedFile[self.i] = [indexed[1], self.i] #{"index de document":{"index de phrase": "la phrase"}}


                self.i += 1

                for self.j in range (len(indexed)):
                    self.indexedFile[self.j] = [indexed[self.j],self.i]
            
        
        with open("sample.json", "w") as outfile:#json file of sentences to check how the dictionary looks like
            json.dump(self.indexedFile, outfile)



    def index(self, file):
        """takes in a text file as an argument and returns indexed list of each sentence"""
        i = 0
        content = []
        with open(file) as f:#outer loop to read eachline and create indexed file
            Line = f.readline()
            while Line!='':#inner loop to split the line with "."

                Line1 = Line.split(".")

                for sentence in Line1:
                    content.append(sentence)
                Line = f.readline()

            indexed = {
                i : content[i] for i in range(0, len(content))#associate each sentence with a number
            }
            
        return indexed

    def wordIndex(self):
        """ generates a dictionary of significative words from a dictionary of list of sentences in python"""
        less4 = self.lessThan(self.indexedFile)
        capital = self.startCapital(self.indexedFile)
        merged = less4.copy()
        merged.update(capital)

        with open("keywords.json", "w", encoding="utf8") as outfile:#json file to check how the dictionary looks like
            json.dump(merged, outfile)

    def lessThan(self, phrases):

        """takes in a list of phrases filters them for non alphanumeric characters and gives and returns
         a dictionary of words with index of sentence"""
        
        newless4 = {}
        for k in phrases:
            words = phrases[k][0].split(' ')
            for word in words:
                word = re.sub(r"[^a-zA-zÀ-Üà-øoù-ÿŒœé]*", '',word)#filters all non alphabetic characters
                word = re.sub(r"[\[\]]*", '',word)#above didn't work for '[]' so added this
                word =re.sub(r"\b[\wa-zA-zÀ-Üà-øoù-ÿŒœ]{1,4}\b", '',word)#eliminates words less than 5 letters
                word = word.lower()#turn every word to lower case
                if (word != '') & (word not in newless4.keys()):
                    newless4[word] =[k]
                elif(word in newless4.keys()):
                    newless4[word].append(k)
        
        return newless4

    def startCapital(self, phrases):
        """takes a list of phrases filters unnecessary symbols and returns a dictionary with all words starting with capital letters (turned to lowercase)"""
        capital = {}
        
        for k in phrases:
            words = phrases[k][0].split(' ')
            for word in words:
                if (re.search(r"^[A-Z]+[a-zà-øoù-ÿŒœé]*",word)):
                    word =re.search(r"^[A-ZÀ-Ü][a-zà-øoù-ÿŒœé]*",word).group()#words starting with capital letters
                    word =re.sub(r"\b[\wa-zA-zÀ-Üà-øoù-ÿŒœ]{1,3}\b", '',word)#eliminates words less than 5 letters
                    word = word.lower()#turn every word to lower case
                else:
                    word = ''
                
                if (word != '') & (word not in capital.keys()):
                    capital[word] = [k]
                elif(word in capital.keys()):
                    capital[word].append(k)
        return capital

    def search(self,dico,mot_cle):
        #return une liste avec les index des phrases qui matchent 
        for mot_sign in dico.keys():
            for mot in mot_cle:
                if mot == mot_sign:
                    self.match.extend(dico[mot_sign])

        #supprime les doublons
        new_list = [] 
        for i in self.match : 
            if i not in new_list: 
                new_list.append(i)

        #affiche les phrases qui matche
        res_final=[]
        for i in new_list:
            res_final.append(self.indexedFile[i])
        print(res_final)

filee = FileSearch()
filee.parse("./texts")
filee.wordIndex()