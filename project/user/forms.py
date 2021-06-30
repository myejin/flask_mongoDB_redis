import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
import re
from project import mongo 

def Signup_Valid_Id(form, field):
    cnt = mongo.db.user.count_documents({'id':field.data})
    if cnt:
        raise ValidationError('The ID already exists.')

def Signup_Valid_Password(form, field):
    chk = re.compile(r'(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[^\w\s]).*')
    if not chk.search(field.data):
        raise ValidationError('Must contain alphabetic, numeric, and special characters.')

class Signup_Form(FlaskForm):
    userid = StringField('userid', [InputRequired(message = 'blank'), Length(min = 7, max = 15, message = 'Please match the ID length.'), Signup_Valid_Id])
    password = PasswordField('password', [InputRequired(message = 'blank'), Length(min = 7, max = 15, message = 'Please match the Password length.'), Signup_Valid_Password])
    re_pw = PasswordField('re-pw', [InputRequired(message = 'blank'), EqualTo('password', message = 'The password does not match.')])


def Login_Valid(form, field):
    if not mongo.db.user.count_documents({'id':field.data}):
        raise ValidationError('The ID does not exist.')
    data = mongo.db.user.find({'id':field.data})
    if data[0]['pw'] != form['password'].data:
        raise ValidationError('The password does not match.')

class Login_Form(FlaskForm):
    userid = StringField('userid', [InputRequired(message = 'blank'), Login_Valid])
    password = PasswordField('password', [InputRequired(message = 'blank')])
