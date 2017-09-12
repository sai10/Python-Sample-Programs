import goslate
import codecs

gs = goslate.Goslate()

fW = open('Translated.txt','w')
with codecs.open('ToBTranslated.txt','r') as f:
	fr = f.readlines()
	for i in fr:
		i = i.strip()
		text = gs.translate(i,'eng')
		print text+'\n'
		fW.write(text+'\n')

