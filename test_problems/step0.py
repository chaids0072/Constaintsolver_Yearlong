import re
import sys
filename =sys.argv[1]
file = open(filename, 'r')

lines = [line.lower() for line in file]
newlines=[]
for line in lines:	
	line=re.sub(r"\bontable\b","on-table",line)
	line=re.sub(r"\bhandempty\b","arm-free",line)
	line=re.sub(r"\bblocks\b","blocksworld",line)
	# line=line.replace("ontable","on-table")
	# line=line.replace('handempty','arm-free')
	# line=line.replace('blocks','blocksworld')
	newlines.append(line)
with open(filename, 'w') as out:
     out.writelines(newlines)