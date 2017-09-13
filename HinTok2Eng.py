import goslate
import codecs

gs = goslate.Goslate()

f = codecs.open("he.txt","r+")
fr = f.readlines()

fw = open("Pureng.txt","w")

for  i in fr:
	i = i.strip()
	words = i.split(' ')
	length = len(words)
	for j in words:
		if not isinstance(j,unicode):
			j = gs.translate(j,'eng')
			j = j.strip()
		j = j+' '
		
