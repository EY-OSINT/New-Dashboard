from re import X
from flask import render_template, redirect, request, url_for
from fileinput      import filename
from wtforms        import Form
import datetime
import apps 
from apps.scan import blueprint
from flask_login import login_required  
from werkzeug.utils import secure_filename
import os
import apps.database  as db_helper
from flask import flash



@blueprint.route('/scan',methods=["GET","POST"])
@login_required
def scan():
    #Saving user's form input after user pushed start scan button
    if request.method=='POST':
        if request.form['start_scan'] == 'start_scan':
            if request.form['target_name'] == 'target_name':
                target_name=request.form['target_name']
            if request.form['scan_name']== 'scan_name':
                scan_name=request.form['scan_name']
            if request.form['github_name'] == 'github_name':
                github_name=request.form['github_name']
            if request.form['shodan_name'] == 'shodan_name':
                shodan_name=request.form['shodan_name']
            #function to be created IMPORTANT FETCH TARGET BY ... IMPORTANT 
          #  if not bool(db_helper.fetch_scan_by_name_and_target_id(target_name,"target_name")):
           #    db_helper.insert_new_scan(target_name,"target_name")
            

        print(target_name)
        print(scan_name)
        print(github_name)
        print(scan_name)
        if request.form['passive_scan']:
            print("passive")
        if request.form['active_scan']:
            print("active")
        if request.form['custom_scan']:
            if request.form['Custom_Domain']:
               if request.form.get('checkbox')='Custom_Domain':
                f=request.files['input']
                f.save(os.path.join(os.getcwd(),secure_filename(f.filename)))   
            print("custom")  
            f=request.files['input']
            f.save(os.path.join(os.getcwd(),secure_filename(f.filename)))
        
    return render_template('home/conf-scan.html',segment='conf-scan')

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
    
    



  

        

 
