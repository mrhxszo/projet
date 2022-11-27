#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os
import re
import json
os.system("clear")

class FileSearch:

    ext = {}
    repertoire = None

    def parse(self, file) :

        print("Je suis dans "+ file)

        liste = os.listdir(file)
        for fichier in liste :
            if os.path.isdir(file + "/" +fichier) :
                self.parse(file + "/"+fichier)
            else :
                #create a dictionary with the name of the file as key
                #then associate it with another dicitonary [sentence no. : sentence]
                chaines = fichier.split(".")
                print(chaines)
                #a method that returns the dictionary of indexed sentences

    def index(self, file):

        i = 0
        content = []
        with open(file) as f:
            Line = f.readline()
            while Line!='':

                a = re.search(".??\.", Line)#search for caracter like Mr. C. etc

                test = "my name is Dr. Dre. And i am a man."
                print(re.split("[.{3,}\.]", test))
                Line1 = Line.split("[.{3,}\.]")

                for sentence in Line1:
                    content.append(sentence)
                Line = f.readline()

        indexed = {
            i : content[i] for i in range(0, len(content))
        }
        with open("sample.json", "w") as outfile:
            json.dump(indexed, outfile)


filee = FileSearch()
#filee.index("./texts/Fromage")

###############################algorithm to rejoin abberviations like Dr. Mr. while splitting sentences with from full stop.################################


# test = "my name is Dr. Dres. Here to say hello."
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
            
