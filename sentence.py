#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

sent1 = "In sit mit amet enim Tincidunt hendrerit Justo ut consequat Lectus Proin sagittis finibus finibus"
sent2 = "Lorem ipsum dolor sit amet Consectetur adipiscing elit Fusce eu nisi tellus Nullam vestibulum Ultricies arcu nec euismod"
sentences = [sent1,sent2]

# get the keyword out from the sentence 
## methods you can use
###eliminate ones with less than four letters
###keep words starting with capital letter except for beggining of the sentence

#code
#eliminate ones with less than four letters
newless4 = []
for sentence in sentences:
    newless4.append(re.sub(r"\b[a-zA-z]{1,4}\b", '',sentence))

print("less than 4", newless4)

#keep words starting with capital letters except for the beggining of the sentence
allcapital = []
start = []
newcapital = []
for sentence in newless4:
    if(re.search(r"^[A-Z]+[a-z]*",sentence)):
        start.append(re.search(r"^[A-Z]+[a-z]*",sentence).group())
    allcapital.append(re.findall(r"[A-Z]+[a-z]*",sentence))


#get the elements which are in allcapital but not in start
for item in allcapital:
    newcapital.append([i for i in item if i not in start])

print("capital", newcapital)