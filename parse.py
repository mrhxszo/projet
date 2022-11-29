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
    """"
    indexed_word = {}
    matches = [[]]
    """

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
            
        
        with open("sample.json", "w") as outfile:#json file to check how the dictionary looks like
            json.dump(self.indexedFile, outfile)

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

filee = FileSearch()
filee.parse("./texts")

###############################algorithm to rejoin abberviations like Dr. Mr. while splitting sentences with fullstop.################################


# test = "my name is Dr. Dres. Here to say hello." qsdhcbiqsudciqusd
# list = re.search("\\s.{1,2}\\.", test).group()

# #split the line but keep the delimiter to identify the Dr. later
# d = "."
# for line in test:
#     line1 =  [e+d for e in test.split(d) if e]

# line2 = []

# iter=iter(range(0,len(line1)))#this required for next() to work
# for i in iter:
#     pattern = re.search("\\s.{1,2}\\.", line1[i])
#     if (pattern): #checks if pattern exists otherwise .group method error
#         if pattern.group() in list:
#             line2.append(''.join([line1[i],line1[i+1]]))#if pattern found join the next and current
#             next(iter,None)#to avoid 
#     else :
#         line2.append(line1[i])#if not found join the rest
#     print(i)
        
        
# print(line2)
            