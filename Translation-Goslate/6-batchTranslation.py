import goslate
import codecs

gs = goslate.Goslate()

fW = open('Translated.txt','w')
with codecs.open('ToBTranslated.txt','r') as f:
	text = f.read()
	text = text.strip()
	print gs.translate(text,'eng')+'\n'
	fW.write(gs.translate(text,'eng')+'\n')

