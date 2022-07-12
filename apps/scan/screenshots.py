from fileinput      import filename
from flask          import render_template, request, url_for, redirect
from flask          import Flask, render_template ,request
import os
from flask_login    import login_user, logout_user, current_user, login_required
from wtforms        import Form
from apps import database as db_helper

#@app.route('/screenshots/<scan_name>',methods=['GET'])
def screenshots(scan_name):
    dir = os.getcwd()
    print(dir)
    os.system('mkdir apps/static/screenshots')
    os.system('cp apps/templates/home/aquatone_urls/'+scan_name+'/screenshots/* apps/static/screenshots/')
    f=open('apps/templates/home/aquatone_urls/'+scan_name+'/aquatone_report.html','r').read()
    f=f.replace('"screenshotPath":"','"screenshotPath":"/static/')
    f2=open('apps/templates/home/aquatone_urls/'+scan_name+'/aquatone_report.html','w')
    f2.write(f)
    return render_template('home/screenshots.html',scan_name=scan_name)

        
