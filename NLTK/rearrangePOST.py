import nltk
from nltk import word_tokenize

st1 = 'hey whats up'
st2 = 'whats hey up'

tok1 = word_tokenize(st1)
tok2 = word_tokenize(st2)

ptag1 = nltk.pos_tag(tok1)
ptag2 = nltk.pos_tag(tok2)

print ptag1
print ptag2
string = str()
for i in ptag1:
	count = 0
	x = str(i)
	x = x.replace('(','')
	x = x.replace('\'','')
	x = x[0:x.index(',')]
	l = len(ptag1)
	print x
	while count < l:
		ind = -1
		y = str(ptag2[count])
		y = y.replace('(','')
		y = y.replace('\'','')
		y = y[0:y.index(',')]
		print y+'\n'
		if x == y:
			ind = count
			print ind
			break
		count = count + 1
		print count
	if ind!=-1:
		string = string+' '+y

string = string.strip()
print string
