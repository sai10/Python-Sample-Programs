import sys;
file1 = open(str(sys.argv[1]),'r');	# SOURCE FILE
file2 = open(str(sys.argv[2]),'w');	# TARGET FILE
skip  = int(sys.argv[3]);		# STARTING LINE
count = int(sys.argv[4]);		# HOW MUCH FROM STARTING LINE i.e. starting line + <this val>

for i in file1:
   skip = skip - 1;
   if skip>0:
	continue;
   file2.write(i);
   count = count -1 ;
   if count < 0:
	break;

