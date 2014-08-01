import json
fo = open("info.txt", "a+")
I1 = 'i eat case'
data = [{'Email':'%s'%(I1)}]
info = json.dumps(data)
fo.write(info);
fo.close()