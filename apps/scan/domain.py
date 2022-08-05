import ipaddress
import os 
import iptools
import shutil
from pathlib import Path
from apps.models import domain
import requests
import json
from typing import List
from bs4 import BeautifulSoup as bs4
from .. import  database as db

import re
 
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    free_regex = r'\b[A-Za-z0-9._%+-]+@[hotmail+\.]|[yahoo+\.]|[gmail+\.]+[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print('it as email')
        if(not(re.fullmatch(free_regex, email))):
           return True
    return False


#function puts domains into database

def main(keyjson,scan_id):
    
    key = json.loads(keyjson)
    domain_name =str(key['domain'])
    db.insert_new_domain(domain_name,scan_id)
    link = "https://viewdns.info/reversewhois/?q=" + str(key['domain'])
    print("[-] " +link)
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
    
    headers = {"User-Agent": user_agent}
    req = requests.get(link, headers=headers)
    table = bs4(req.content, "html5lib")
    table = table.findAll('table')[3].encode()

    tr = bs4(table, "html5lib")
    rows = tr.findAll('tr')
    
 
    try:
        for element in rows:
            element = str(element)
            value = element[element.index("<td>") + 4: element.index("</td>")]
            if value == "Domain Name":
                print()

            else:
                db.insert_new_domain(value,scan_id)
                

    except:
        print()
        print("[-] " + key['domain'] + " doesn't have any registered domain names")
        

#function puts domains related to ip into database

def main_ip(keyjson,scan_id):
   
    print(type(keyjson))
    key = json.loads(keyjson)
    
    link = "https://viewdns.info/reverseip/?host=" + str(key['ip']) + "&t=1"
    print("[-] " +link)
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
    
    headers = {"User-Agent": user_agent}
    headers = {
    'authority': 'viewdns.info',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Opera";v="84"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__utmc=126298514; PHPSESSID=nidtvv3fgbi3ooh2cl63k4gb11; __gads=ID=4f3dbaf258bc4b43-2273e8692ad000e6:T=1645452711:RT=1645452711:S=ALNI_MbBINrYTpn2GtJtAwyvpaYkvknnEw; __utmz=126298514.1646216889.12.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=126298514.1713912151.1644397483.1646821893.1646835540.19; __utmt=1; __utmb=126298514.8.10.1646835540',
}
    params = (
    ('host', str(key['ip'])),
    ('t', '1'),
    )
    req = requests.get('https://viewdns.info/reverseip/', headers=headers, params=params)
    
    table = bs4(req.content, "html5lib")
    
    table = table.findAll('table')[3].encode()

    tr = bs4(table, "html5lib")
    rows = tr.findAll('tr')   
    l=[]
    try:
        for element in rows:
            element = str(element)
            value = element[element.index("<td>") + 4: element.index("</td>")]
            
            if value == "Domain":
                print()
                    
            else:
                l.append(value)
                db.insert_new_domain(value,scan_id)
        
    except:
        print()
        new_var = print("[-] " + key['ip'] + " doesn't have any registered domain names")
        
    return l
   
def domains(target_name,scan_name):
    dirname = os.path.dirname(__file__)
    dir = os.getcwd()
    file = os.path.join(dir, r"apps/scan/scans_folder/"+target_name+"/"+scan_name+"/domain/upload.txt")

    target=db.fetch_by_name('target',target_name)
    target_id=target.get('id')
    scan=db.fetch_by_name_and_id("scan",scan_name,"target_id",target_id)
    scan_id=scan.get('id')
    try:    
        
        f=open(file).read() 
        for ligne in f.split('\n'):
                x = '{"domain" :'+ '"'+ligne +'"'+ '}'
                if not iptools.ipv4.validate_ip(ligne):
                    if(check(ligne)):
                        domain_from_mail=ligne.split('@')[1]
                        x = '{"domain" :'+ '"'+domain_from_mail +'"'+ '}'
                        print(x)
                    main(x,scan_id)
                else:
                    x = '{"ip" :'+ '"'+ligne +'"'+ '}'
                    print(x +' this is  an ip ')
                    l=main_ip(x,scan_id)

                    for line in l:
                        x = '{"domain" :'+ '"'+line +'"'+ '}'
                        print(x +' this is  an ip from domain ')
                        main(x,scan_id)
                    
    except:
	    print("you have been banned  ")



            
            
        
       
