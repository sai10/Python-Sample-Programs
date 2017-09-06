import codecs

fp1 = codecs.open('HindiRead.txt','r',encoding='utf-16')
file1 = fp1.read()

fp2 = codecs.open('HindiWrite.txt','w',encoding='utf-16')

for i in file1:
	fp2.write(i)
