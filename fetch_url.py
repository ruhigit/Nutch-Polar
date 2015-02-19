import sys
inputfile=open(sys.argv[1],'r')
urls=dict()
for line in inputfile:
	words=line.split()
	str="Content-Type"
	for index,word in enumerate(words):
		value=word.find(str)
		if(value!=-1):
			type_url=word[13:]
			if type_url not in urls:
				urls[type_url]=0
			else:
				urls[type_url]+=1
print(urls)
inputfile.close()
