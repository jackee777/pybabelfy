'''
Created on 02/12/2015

@author: david
'''


from pybabelfy.babelfy import *

text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "key" #This only works for the demo example. Change for the key you get once registered

babelapi = Babelfy()

semantic_annotations = babelapi.disambiguate(text,lang,key, anntype= AnnTypeValues.ALL)
for semantic_annotation in semantic_annotations:
    print(semantic_annotation.frag(text))
    semantic_annotation.pprint()
