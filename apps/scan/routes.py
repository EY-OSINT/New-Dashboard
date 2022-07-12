from distutils.command.config import config
from re import X
from flask import render_template, redirect, request, url_for
from fileinput      import filename
from wtforms        import Form
import datetime
from . import subdomain
from apps.scan import blueprint
from flask_login import login_required 
from werkzeug.utils import secure_filename
import os
import apps.database  as db_helper
from flask import flash
from .. import Library
from apps.scan.forms import ScanForm
@blueprint.route('/scan_config',methods=["GET","POST"])
@login_required
def scan_config():
    scan_form=ScanForm(request.form)
    #Saving user's form input after user pushed start scan button
    
    print("POST")
    if 'start_scan' in request.form:
        print("yeeeet")
        data=request.form
        print(data)
        if 'TargetName' in request.form:
            print('azazzzzzzzzzzzzzzzzzzzaaaaaaa')
            target_name=request.form['TargetName']
            print(target_name)
        #   if not bool(db_helper.fetch_by_name("target",target_name)):
        #     target_id=db_helper.insert_new_target(target_name)
        if 'ScanName' in request.form:
            scan_name=request.form['ScanName']
            #if not bool(db_helper.fetch_scan_by_name_and_target_id(scan_name,target_name)):
                #db_helper.insert_new_scan(scan_name,target_name)
            try:
                os.system("mkdir scans_folder/"+target_name+"/"+scan_name)
            except:
                print("do not create the same folder twice")
        if 'GithubToken' in request.form:
            github_name=request.form['GithubToken']
        if 'ShodanKey' in request.form:
            shodan_name=request.form['ShodanKey']
        #function to be created IMPORTANT FETCH TARGET BY ... IMPORTANT 
        #  if not bool(db_helper.fetch_scan_by_name_and_target_id(target_name,"target_name")):
        #    db_helper.insert_new_scan(target_name,"target_name")

        print(target_name)

        print(scan_name)

        print(github_name)

        print(scan_name)

        if request.form['passive_scan']:
            print("passive")
            subdomain.Passive(target_name,scan_name)
        if request.form['active_scan']:
            print("active")
            subdomain.Active(target_name,scan_name)
        if request.form['custom_scan']:
            print("elimiante error")
            if request.form['Custom_Domain']:
                if request.form.get('checkbox')!='Custom_Domain':
                    print('ee')
                    print('ENTER YOUR OWN LIST')
                elif request.form.get('checkbox')=='Custom_Domain':
                    print('whois module')
                    print('validation')
                f=request.files['input']
                f.save(os.path.join(os.getcwd(),r"scans_folder/",target_name,scan_name,r"domain/upload.txt"))   
                print("custom Domain Module NOT CHECKED file must be uploaded")
                if request.form.get('checkbox') == 'Custom_Subdomain':
                    subdomain.Custom(target_name,scan_name)
                if request.form.get('checkbox')=='Custom_Directory':
                    print('Custom_dir')
        return render_template(url_for('scan_blueprint.all_scans',form=scan_form))
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
   scans= db_helper.fetch_scan_by_name("target_name") 
   if request.method == 'POST' and not(str(request.get_data()) == "b'add='") :
         data = request.get_data()
         name=(str(data).split('=')[1])
         name_clean=name.split('&')[0]

         if not bool(db_helper.fetch_scan_by_name_and_target_id(name_clean,"target_name")):
               db_helper.insert_new_scan(name_clean,"target_name") 
               
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
    
    



  

        

 
