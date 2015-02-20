import sys
inputfile=open(sys.argv[1],'r')
urls=dict()
str=sys.argv[2]
for line in inputfile:
	words=line.split()
	for index,word in enumerate(words):
		value=word.find(str)
		if(value!=-1):
			type_url=word
			if type_url not in urls:
				urls[type_url]=1
			else:
				urls[type_url]+=1
print(urls)
inputfile.close()
