import json
text = open("database.json","r")
#print text.read()

#print type(text.read())

#new_text = json.dumps(text.read())
#print len(new_text)
#text.close()

#text2 = open("database.json","r+")
#print "the pointer is at %s" % text2.tell()
#a = text2.tell() - 2;
#text2.seek(-1,2);
#text2.write(',' + '{"name":"Migo", "job":"Craftsman"}' + ']');
#text2.close()


data  = json.loads(text.read())
print data[len(data)-1]["org_lead"]
