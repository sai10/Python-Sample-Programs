import goslate

gs = goslate.Goslate(service_urls=['https://translate.google.com/'])

f = open('Translated.txt','w')
with open('ToBTranslated.txt','r') as f:
	text = f.read()
	text = text.strip()
	f.write(gs.translate(text,'eng')+'\n')

