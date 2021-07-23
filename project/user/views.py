import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask import render_template, redirect, flash, session
from flask.views import MethodView
from .forms import Signup_Form, Login_Form
from project import mongo 

class Home(MethodView):
    def get(self):
        userid = session.get('userid', None)
        return render_template('home.html', userid=userid) 

class Signup(MethodView):
    def post(self):
        form = Signup_Form()
        if form.validate_on_submit() == False:            
            for msg in form.errors.values():
                if msg:
                    flash(str(msg[0]), 'error')
                    return redirect('/signup/')

        userid = form.data.get('userid')
        password = form.data.get('password') # 해쉬 X

        doc = {
            'id':userid,
            'pw':password
        }
        mongo.db.user.insert_one(doc)
        
        flash('Signed up successfully.', 'no error') 
        return redirect('/')
        
    def get(self):
        return render_template('signup.html', form = Signup_Form()) 

class Login(MethodView):
    def post(self):
        form = Login_Form()
        if form.validate_on_submit() == False:            
            for msg in form.errors.values():
                if msg:
                    flash(str(msg[0]), 'error')
                    return redirect('/login/')

        session['userid'] = form.data.get('userid')
        flash('You are logged in.', 'no error')
        return redirect('/')
        
    def get(self):
        return render_template('login.html', form = Login_Form()) 

class Logout(MethodView):        
    def get(self):
        session.pop('userid', None)
        return redirect('/')