#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import glob
import sys, os
import re
import json
from pathlib import Path
os.system("clear")
from stanzafr import lemma

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
            if os.path.isdir(files + "/" + file):
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
        with open(file, encoding="utf8") as f:#outer loop to read eachline and create indexed file
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
        if(os.path.isfile('./keywords.json')):
            f = open('keywords.json')
            merged = json.load(f)
            return merged
        else:
            less4 = self.lessThan(self.indexedFile)
            #keep only the words that are in tfidf from less than 4
            # loop to check if the word in less4 is in tfidf if not remove
            tifdif = self.tfidf("./texts")
            for item in less4.keys():
                if item not in tifdif:
                    del less4[item]

            #add words starting with capitals to the file 
            capital = self.startCapital(self.indexedFile)
            merged = less4.copy()
            merged.update(capital)



            with open("keywords.json", "w", encoding="utf8") as outfile:#json file to check how the dictionary looks like
                json.dump(merged, outfile)
            
            return merged

    def lessThan(self, phrases):

        """takes in a list of phrases filters them for non alphabetic characters and gives and returns
         a dictionary of words with index(es) of sentence(s)"""
        
        newless4 = {}
        for k in phrases:
            words = phrases[k][0].split(' ')
            for word in words:
                word = re.sub(r"[^a-zA-zÀ-Üà-øoù-ÿŒœé]*", '',word)#filters all non alphabetic characters
                word = re.sub(r"[\[\]]*", '',word)#above didn't work for '[]' so added this
                word =re.sub(r"\b[\wa-zA-zÀ-Üà-øoù-ÿŒœ]{1,4}\b", '',word)#eliminates words less than 5 letters
                word = word.lower()#turn every word to lower case
                
                if (word != '') & (word not in newless4.keys()):
                    word = lemma(word) #converts the word into 'standard' form using stanza
                    newless4[word] =[k]
                elif(word in newless4.keys()):
                    if(word):
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
                    word =re.sub(r"\b[\wa-zA-zÀ-Üà-øoù-ÿŒœ]{1,4}\b", '',word)#eliminates words less than 3 letters
                    word = word.lower()#turn every word to lower case
                    
                else:
                    word = ''
                
                if (word != '') & (word not in capital.keys()):
                    word = lemma(word) #converts the word into 'standard' form using stanza
                    capital[word] = [k]
                elif(word in capital.keys()):
                    if (word):
                        capital[word].append(k)
        return capital

    def search(self,dico,mot_cle):
        #stanza conversion
        stanzamot_cle = []
        for mot in mot_cle:
            stanzamot_cle.append(lemma(mot.lower()))

        #return une liste avec les index des phrases qui matchent 
        for mot_sign in dico.keys():
            for mot in stanzamot_cle:
                if mot == mot_sign:
                    self.match.extend(dico[mot_sign])

        #supprime les doublons
        new_list = [] 
        for i in self.match : 
            if i not in new_list: 
                new_list.append(i)
        self.match.clear()
        #affiche les phrases qui matche
        res_final=[]
        for i in new_list:
            res_final.append(self.indexedFile[i])
        print(res_final)
        res_final=[]

    def tfidf(self, files):
        #retourne un dataframe avec les mots significatifs pour chaque documents 

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

            res = self.indexedFile


        
            text_files = glob.glob(f'./texts/txt/*.txt')
            text_titles = [Path(text).stem for text in text_files]

            tfIdfVectorizer=TfidfVectorizer(input='filename',stop_words=['de','la','le','et','du','ce','les','en','des','un','une','est','aprés','ou','dans','son','sa','ses','par'])
            tfIdf = tfIdfVectorizer.fit_transform(text_files)
            df = pd.DataFrame(tfIdf.toarray(), index=text_titles, columns = tfIdfVectorizer.get_feature_names_out())
            df = df.stack().reset_index()
            df = df.rename(columns={0:'tfidf','level_0':'document','level_1':'term','level_2':'term'})
            df = df.sort_values(by=['document','tfidf'],ascending=[True,False])
            
            dflist = df.values.tolist()
            filterlist = []
            for item in dflist:                
                if item[2] >= 0.10:
                    stanz = lemma(item[1])
                    filterlist.append(stanz)

            return filterlist
            

filee = FileSearch()
filee.wordIndex()