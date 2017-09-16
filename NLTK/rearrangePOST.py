import nltk
from nltk import word_tokenize

st1 = 'this is a boy'
st2 = 'a is this boy'

tok1 = word_tokenize(st1)
tok2 = word_tokenize(st2)

ptag1 = nltk.pos_tag(tok1)
ptag2 = nltk.pos_tag(tok2)

print ptag1
print ptag2
string = str()
for i in ptag1:
	count = 0
	print i
	l = len(ptag1)
	while count < l:
		if i == ptag2[count]:
			ind = count
			break
		count = count + 1
		print count
	string = string+' '+str(ptag2[ind])

string = string.strip()

