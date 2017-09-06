
file1 = open('test2.txt','r')    # File which is to be matched
fp1 = file1.readlines()


file2 = open('test1.txt','r')    # File where matching will take place
fp2 = file2.readlines()

FW = open('Hintext.txt','w')	 # File where matched line numbers of file2 will be saved

for i in fp1:
	i = i.strip()
	count =0
	for j in fp2:
		j = j.strip()
		count = count+1	
		if i==j :
			FW.write(str(count)+'\n')
			break
			

	
