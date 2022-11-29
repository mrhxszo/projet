#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os
import re
import json
os.system("clear")

class FileSearch:

    #defined i and indexedfile as static attributes because parse is called recursively and calling them inside the method won't conserve the value
    i = 0 
    indexed_doc={}
    indexedFile = {}

    def parse(self, files) :

        list = os.listdir(files)
        for file in list:
            if os.path.isdir(files + "/" + file) :
                self.parse(files + "/"+ file)
            else :
                chain = file.split(".")
                #index the sentence in the file and put it inside indexedfile dictionary
                indexed = self.index(files + "/" + file, self.i)


                self.indexed_doc[self.i]=chain[0]

                #self.indexedFile[self.i] = indexed #{"index de document":{"index de phrase": "la phrase"}}

                
                self.i += 1

        with open("sample.json", "w") as outfile:#json file to check how the dictionary looks like
            json.dump(indexed, outfile, iterable_as_array=True)



    def index(self, file, ind):
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
                i : [(content[i] for i in range(0, len(content))), ind]#associate each sentence with a number
            }
            
        return indexed

filee = FileSearch()
filee.parse("./texts")

###############################algorithm to rejoin abberviations like Dr. Mr. while splitting sentences with fullstop.################################


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
            