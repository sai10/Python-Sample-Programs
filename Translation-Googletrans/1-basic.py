#!/usr/bin/python
# -*- coding: utf-8 -*-
import googletrans

gs = googletrans.Translator()
st = 'मानचित्रण प्रदर्शित करें'

lst = gs.translate(st,'en')

trans_string = lst.text

trans_string = str(trans_string)

print 'Translated String is:'+trans_string
