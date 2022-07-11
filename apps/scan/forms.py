# -*- encoding: utf-8 -*-


from tkinter.tix import InputOnly
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,FileField,SelectField,SubmitField,RadioField
from wtforms.validators import Email, DataRequired

# login and registration


class ScanForm(FlaskForm):
    TargetName  = StringField   ('TargetName',
                                id='target_name',
                                validators=[DataRequired()])
    ScanName    = StringField   ('ScanName',
                                id='scan_name',
                                validators=[DataRequired()])
    GithubToken = StringField   ('GithubToken',
                                id='github_token')
    ShodanKey   = StringField   ('ShodanKey',
                                id='Shodan_Key')
    Input       = FileField     ('InputFile',id='input_file')
    
    StartScan   = SubmitField   ('StartScan', id ='start_scan')


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    github = StringField('Github',
                             id='gth_create',
                             validators=[DataRequired()])
