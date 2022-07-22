from ctypes import LibraryLoader
from distutils.command.config import config
from re import X
from flask import render_template, redirect, request, url_for
from fileinput      import filename
import requests
from wtforms        import Form
import datetime
from . import subdomain
from . import domain
from . import url
from . import aquatone
from . import screenshots
from apps.scan import blueprint
from flask_login import login_required 
from werkzeug.utils import secure_filename
import os
import apps.database  as db
from flask import flash
from ..Library import Library
from apps.scan.forms import ScanForm
@blueprint.route('/scan_config',methods=["GET","POST"])
@login_required
def scan_config():
    scan_form=ScanForm(request.form)
    #Saving user's form input after user pushed start scan button
    
    print("POST")
    if 'start_scan' in request.form:
        print("Starting Scan")
        data=request.form
        print(data)
        if 'TargetName' in request.form:
            print('TARGET')
            target_name=request.form['TargetName']
            print(target_name)
        if not bool(db.fetch_by_name("target",target_name)):
           target_id=db.insert_new_target(target_name)
        if 'ScanName' in request.form:
            scan_name=request.form['ScanName']
            if not bool(db.fetch_scan_by_name_and_target_id(scan_name,target_name)):
                scan_id= db.insert_new_scan(scan_name,target_name)
            try:
                print(os.getcwd())
                os.system("mkdir -p apps/scan/scans_folder/"+target_name+"/"+scan_name)
            except:
                print("do not create the same folder twice")
        if 'GithubToken' in request.form:
            github_name=request.form['GithubToken']
        if 'ShodanKey' in request.form:
            shodan_name=request.form['ShodanKey']
        #function to be created IMPORTANT FETCH TARGET BY ... IMPORTANT 
        #  if not bool(db.fetch_scan_by_name_and_target_id(target_name,"target_name")):
        #    db.insert_new_scan(target_name,"target_name")

        print(target_name)

        print(scan_name)

        print(github_name)

        print(scan_name)

        #if 'passive_scan' in request.form:
        #   print("passive")
        #   subdomain.Passive(target_name,scan_name)
        #if 'active_scan' in request.form:
        #   print("active")
        #   subdomain.Active(target_name,scan_name)
        #DOMAIN MODULE

        
        if 'Domain_Module' in request.form:
            print('whois module')
            f=request.files['input']
            Library.create_dir_under_scans_folder("domain", target_name, scan_name)
            f.save(os.path.join(os.getcwd(),r"apps/scan/scans_folder/",target_name,scan_name,r"domain/upload.txt"))
            domain.domains(target_name,scan_name)
        else:

            print('ENTER YOUR OWN LIST')
            print('validation')
            f=request.files['input']
            f.save(os.path.join(os.getcwd(),r"scans_folder/",target_name,scan_name,r"domain/upload.txt"))   
            print("custom Domain Module NOT CHECKED file must be uploaded")
        #Subdomain Module
        if 'Subdomain_Module' in request.form:
            subdomain.Custom(target_name,scan_name)
        #Directory Listing Module
        if 'Directory_Module' in request.form:
            print('Custom_dir')
        if 'URL_Module' in request.form:
            print('URL_Module')
        if 'Shodan_Module' in request.form:
            print ('Shodan_Module')
        if 'Google_Module' in request.form:
            print ('Google_Module')
        if 'Github_Module' in request.form:
            print ('Github_Module')
        if 'JS_Module' in request.form:
            print ('JS_Module')
        if 'JS_Module' in request.form:
            print ('JS_Module')
        return render_template(url_for('scan_blueprint.all_scans'))
    return render_template('home/conf-scan.html',segment='conf-scan',form=scan_form)


@blueprint.route('/all_scans',methods=["GET","POST"])
@login_required
def all_scans():

    return render_template('home/')
# Errors

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
"""
   scans= db.fetch_scan_by_name("target_name") 
   if request.method == 'POST' and not(str(request.get_data()) == "b'add='") :
         data = request.get_data()
         name=(str(data).split('=')[1])
         name_clean=name.split('&')[0]

         if not bool(db.fetch_scan_by_name_and_target_id(name_clean,"target_name")):
               db.insert_new_scan(name_clean,"target_name") 
               
         else:
           flash("scan already exists")   
           return render_template('pages/scan.html',scans=scans) 

   if request.form.get('add') == 'add': 
       return redirect(url_for('scan',target_name="target_name", scans=scans)) 
 
   return render_template('pages/scan.html',target_name="target_name",scans=scans)

@blueprint.route("/start_scan/<target_name>/<scan_name>", methods=['POST'])
def start_scan(target_name,scan_name):
       
           if request.method == 'POST' and request.form.get('Send') == 'Send': 

              return redirect(url_for('url',target_name=target_name,scan_name=scan_name,pagination=1)) 
              """
    
    



  

        

 
