
import os
from flask          import render_template, request, url_for, redirect
from flask          import Flask
from flask_login    import login_user, logout_user, current_user, login_required
from wtforms        import Form
from apps import database as db_helper



#@app.route('/aquatone/<scan_name>/',methods=['POST','GET'])

def aquatone(scan_name):
    

    if not current_user.is_authenticated:
        return redirect(url_for('login')) 
   

    dir = os.getcwd()
    print(dir)
    """ 
    create_dir_scan = 'cd '+dir+'/templates/home/aquatone_urls ; mkdir -p  '+scan_name
    """
    aquatone_cmd= 'cat app/urls.txt | aquatone -out '+dir+'/apps/templates/home/aquatone_urls/'+scan_name
    os.system(aquatone_cmd)

    scan_id=9
    db_helper.insert_new_screenshot_link (scan_name+'aquatone_report.html',scan_id)
    
    return redirect(url_for('screenshots',scan_name=scan_name))
   
@app.route("/aquatone_urls/<scan_name>/", methods=['GET'])
def report(scan_name):
    path='home/aquatone_urls/'+scan_name+'/aquatone_report.html'
    print(path)
    return render_template(path)
