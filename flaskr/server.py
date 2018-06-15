
import datetime
import functools
import json
import os
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from bson import json_util
from flask import (
   Markup,Session,Flask, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Flask(__name__)
bp.secret_key = os.urandom(50)

connection = MongoClient('localhost', 27017)
db = connection.progettotw
user = db.user
proj = db.proj
iscr = db.iscr
res = db.risultati

@bp.before_request
def start():
	user_id = session.get('user_id')
        if user_id is None:
    	    g.user = None
    	else:
	    
            g.user = user.find({'_id':user_id})
	

@bp.route('/')
def show():
	return render_template('index.html')

@bp.route('/forlogin',methods=['GET','POST'])
def renderlogin():
	if request.method == 'GET':
		return render_template('login.html')

@bp.route('/forsignup',methods=['GET','POST'])
def rendersignup():
	if request.method == 'GET':
		return render_template('signup.html')

@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstName']
        surename = request.form['cognome']
        password = request.form['psw']
        email = request.form['email']
        error = None
      
	
        try:
       		user.insert({'firstname':firstname,'password':generate_password_hash(password),'surename':surename,'email':email})
        except DuplicateKeyError:
       		error = 'user already existent'	
	        flash(error)

    	return render_template('login.html')

@bp.route('/login', methods=[ 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email1']
        password = request.form['psw1']
        error = None
        
        thereis = user.find({'email':email})

        if thereis.count() == 0:
            error = 'Incorrect e-mail.'
	    flash(error)
        else:
		thereis = user.find_one({'email':email})
		if not check_password_hash(thereis['password'], password):
	            error = 'Incorrect password.'
		    flash(error)

        if error is None:
            session.clear()
            session['user_id'] = json_util.dumps(thereis['_id'])
	    return redirect(url_for('meth'))

        return render_template('login.html')


@bp.route('/logout',methods=['GET','POST'])
def logout():
	if request.method == 'POST':
		session.clear()
		return render_template('index.html')

@bp.route('/create_proj', methods=['GET','POST'])
def create():
	if request.method == 'POST':
		error =  None
		record = ''
		try:
			email = user.find_one({'_id':ObjectId(session['user_id'][10:-2])},{'_id':0,'email':1})["email"]
		except Exception:
			error = 'error, maybe not logged in'
			flash(error)
			return render_template('signup.html')			

		record ='{"email":"'+email
		record += '",'


		for campo in request.form.keys():

			if(campo != 'remember') and (campo != 'anno_scadenza') and (campo != 'mese_scadenza') and (campo != 'giorno_scadenza'):
				record += '"'
				record += str(campo)
				record += '"'
				record += ':'
				record += '"'
				record += str(request.form[campo])
				record += '"'
				record += ','
		record =record[:-1]+'}'
		
		try:
			proj.insert(json.loads(record))
			anno = int(request.form['anno_scadenza'])
			mese = int(request.form['mese_scadenza'])
			giorno = int(request.form['giorno_scadenza'])
			proj.update({'nome':request.form['nome']},{"$set":{'scadenza':datetime.datetime(anno,mese,giorno)}})

		except DuplicateKeyError:
			error = 'project already existent'
			flash(error)
            	return redirect(url_for('meth'))




@bp.route('/iscr', methods=['GET','POST'])
def subscribe():
	 if request.method == 'POST':
                error =  None

		try:
			email = user.find_one({'_id':ObjectId(session['user_id'][10:-2])},{'_id':0,'email':1})["email"]
		except Exception:
			error = 'error, maybe not logged in'
			flash(error)
			return render_template('login.html')					

		if iscr.find({"nome":request.form['nome']}).count() == len(proj.find_one({"nome":request.form['nome']}).keys())-5:
			error = 'limit of subscriptions reached'
			flash(error)
		else:	
			if iscr.find({"nome":request.form['nome'],"email":email}).count() == 1:
				error = 'you have already subscribed this project'
				flash(error)
			else :
			        diz = request.form.to_dict(flat=False)	
				diz.pop('remember',None)
				diz['email']=email
				iscr.insert(diz)
		return redirect(url_for('meth'))
@bp.route('/allmeth')
def meth():
		error =  None
		record = ''
		try:
			email = user.find_one({'_id':ObjectId(session['user_id'][10:-2])},{'_id':0,'email':1})["email"]
		except Exception:
			error = 'error, maybe not logged in'
			flash(error)

 	        lis = []
		lis1 = []
	
          	for i in iscr.find({'email':email},{'nome':1,'_id':0}):
	    		lis.append(i['nome'][0])
	    	for i in proj.find({'nome':{"$in":lis}}):
			lis1.append(i)
		for i in proj.find({'email':email},{'nome':1,'_id':0}):
			lis.append(i['nome'])
	    	for i in proj.find({'email':email}):
			lis1.append(i)
	    	lis2 = []
	    	for i in res.find({'email':email}):
			lis2.append(i)
		    
	    	listarisultati=Markup(json_util.dumps(lis2))
	   	listamiei = Markup(json_util.dumps(lis1))
            	listaproj=Markup(json_util.dumps(list(proj.find({'nome':{"$nin":lis}}))))	    
            	return render_template('profile.html',lista_proj = listaproj,lista_miei=listamiei,lista_risultati=listarisultati)




bp.run(host='0.0.0.0',port=80,debug=True)
