import json
import csv

f=open("C:/Users/Administrator/Desktop/机器学习招新题目/data.csv","r",encoding='gbk') 
ls=[]
for line in f:
        line = line.replace("\n", "")
        line = line.replace("\"\"has_public_page\"\":","")
        line = line.replace("\"{\"\"id\"\":\"\"","")
        line = line.replace("\"\"","")
        line = line.replace("edge_media_to_caption","text")
        line = line.replace("{\"edges\":[{\"node\":{\"text\":\"","")
        line = line.replace("\"}}]}","")
        line = line.replace("’","'")
        line = line.replace("???\\n.\\n.\\n.\\n","")
        line = line.replace("#","")
        line = line.replace("???\\n","")
        line = line.replace("??\\n","")
        line = line.replace("?\\n","")
        line = line.replace("\\n","")
        line = line.replace("\"{edges:[{node:{text:","")
        line = line.replace("???????","")
        line = line.replace(" ??????","")
        line = line.replace(" ?????","")
        ls.append(line.split(","))

f.close()
fw=open("a.json","w",encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
data = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
fw.write(data)
fw.close()
