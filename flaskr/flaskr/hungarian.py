from munkres import Munkres
from pymongo import MongoClient
from decimal import Decimal
import datetime
import json
#passing nome progetto
connection = MongoClient('localhost', 27017)
db = connection.progettotw
proj = db.proj
scaduti = proj.find({"scadenza":{"$lte":datetime.datetime.today()}})
iscr = db.iscr
res = db.risultati
m = Munkres()
for k in scaduti:
	emailproj = k['email'] #email committente
	now = iscr.find({"nome":k['nome']})
	if len(k.keys())-5 == now.count():
		matrix = []
		tasks = []
		agents = []
		for h in k.keys():
			if (h != 'nome') and (h != 'email') and (h != '_id') and (h != 'desc') and (h != 'scadenza'):
				tasks.append(str(k[h]))
		for y in now:
			list = []
			for t in y.keys():
				if (t != 'nome') and (t != 'emailproj') and (t != 'email') and (t != '_id'):
					list.append(Decimal(y[t][0]))	
			agents.append(y['email'])
			matrix.append(list) 
		indexes = m.compute(matrix)
		doc = '{"email":"'
		doc += str(k['email'])
		doc += '","nome":"'
		doc += str(k['nome'])
		doc += '",'
		for r,c in indexes:
			doc += '"'
			doc += str(tasks[c])
			doc += '":'
			doc += '["'
			doc += agents[r]+'","'+str(matrix[r][c])+'"],'
		doc = doc[:-1]+'}'
		print doc
		res.insert(json.loads(doc),check_keys=False)
	db.iscr.remove({"nome":k['nome']})
	db.proj.remove({"nome":k['nome']})


