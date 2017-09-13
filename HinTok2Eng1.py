#!/usr/bin/python
# -*- coding: utf-8 -*-

import googletrans
import codecs

gs = googletrans.Translator()

fr =  codecs.open("he.txt","r").readlines()

fw = open("pureng.txt","w")

count = 1
for i in fr :
	print count
	count  = count+1
	i = i.strip()
	lst = i.split(' ')
	k = list()
	string = str()
	for j in lst:
		lang_lst = gs.detect(j)
		lng = lang_lst.lang
		if lng == 'hi':
			word_lst = gs.translate(j)
			word = str(word_lst.text) 
		else:
			word = str(j) 
		k.append(word)
	
	string = ''.join(str(x)+' ' for x in k)
	fw.write(string+'\n')

