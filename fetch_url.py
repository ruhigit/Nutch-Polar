import sys
import json
 if len(sys.argv) != 2:
    print ('usage: python3 fetch_url.py inputFile')
    sys.exit(1)
inputfile=open(sys.argv[1],'r',errors='ignore')
urls=dict()
str='Content-Type'
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
#print(urls)
json.dump(urls, open("mime_types.txt",'w'))
inputfile.close()
