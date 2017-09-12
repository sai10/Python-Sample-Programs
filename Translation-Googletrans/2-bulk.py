#!/usr/bin/python
# -*- coding: utf-8 -*-


import googletrans

gs = googletrans.Translator()

string = ["मुझे","विधाता","मुट्ठी"]

lst = gs.translate(string)


st = list()

for i in lst:
	st.append(str(i.text))
	

print st


