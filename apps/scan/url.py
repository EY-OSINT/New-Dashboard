import os
from flask          import render_template, request, url_for, redirect
from flask          import Flask
from wtforms        import Form
from apps import database as db_helper
import datetime



def clean_domain(line: str) -> str:
    value_with_closing_bracket = line.split(" ")
    domain = value_with_closing_bracket[0]
    value_with_closing_bracket[0]
    return domain

def status_code(line: str) -> str:
    value_with_closing_bracket = line.split("[")
    status = value_with_closing_bracket[1].split("]")[0]
    return status   

def content_length(line: str) -> str:
    value_with_closing_bracket = line.split("[")
    content = value_with_closing_bracket[2].split("]")[0]
    return content

def title(line: str) -> str:
    value_with_closing_bracket = line.split("[")
    titre = value_with_closing_bracket[3].split("]")[0]
    return titre

def technologie(line: str) -> str:
    value_with_closing_bracket = line.split("[")
    tech = value_with_closing_bracket[4].split("]")[0]
    return tech
    

def read_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        lines = f.readlines()
    return lines


#@app.route('/url/<target_name>/<scan_name>/<pagination>',methods=['POST','GET'])

def url(target_name,scan_name,pagination):
    ROWS_PER_PAGE = 5

    #commentit bech neviti httpx ye5dem  kol mantesti 
    http_extract= 'cat'+ ' app/subdomains.txt' + '| httpx -nc -sc -title -cl -td -p 80,443,4443,8443,8080,8000 -o output1.txt'
    os.system( http_extract)
    target=db_helper.fetch_by_name('target',target_name)
    target_id=target.get('id')

    scan=db_helper.fetch_by_name_and_id("scan",scan_name,"target_id",target_id)
    scan_id=scan.get('id')
    lines = read_file("output1.txt")
    for line in lines:
        line+="[]"
        
        clean = clean_domain(line)
        status = status_code(line) 
        content = content_length(line)
        titre = title(line)
        tech= technologie(line)
       
        #commentit bech neviti insertion kol mantesti 
        #db_helper.insert_new_url(clean,status,content,titre,tech,scan_id)
        items = db_helper.fetch_url()
        outfile = open("app/urls.txt", "w")
        for item in items:
                nom=item['name']
                outfile.write(nom+'\n' )
                
        outfile.close()   

        items_length=int(len(items)/10)
        items_display=items[(int(pagination)-1)*10:int(pagination)*10]

    if request.form.get('Send') == 'Send': 
        return redirect(url_for('aquatone',scan_name=scan_name))     
    return render_template('pages/url.html',items=items,items_display=items_display ,items_length=items_length)     
