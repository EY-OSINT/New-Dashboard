from calendar import calendar
import datetime
import sqlite3
from . import db
##############################################################################################################################################################################################################################################################################################################################
def fetch_by_name(table_name:str,name:str) -> list:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    query_results = conn.execute("Select * from "+table_name+" Where name =='"+name+"';").fetchall()
   # print (query_results)
    conn.close()
    item={}
    for result in query_results: 
        item = {
            "id": result[0],
            "name": result[1]    }
    return item

def fetch_all_domains_by_scan_name(scan_name:str,target_name:str) -> dict:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    scan= fetch_scan_by_name(scan_name,target_name)
    scan_id=scan[0].get('id')
    query_results = conn.execute("Select * from domain where scan_id="+scan_id+";").fetchall()
    conn.close()
    domains_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "name": result[1],        }
        domains_list.append(item)
    return domains_list

def insert_new_domain(text: str,scan_id:int) ->  int:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    
    #conn = db.connect()
    query = 'insert into domain (name,scan_id) VALUES ("{}","{}");'.format(text,scan_id)
    conn.execute(query)
    
    conn.commit()
    query_results = conn.execute("Select * from domain where scan_id="+str(scan_id)+";")
    query_results = [x for x in query_results]
    domain_id = query_results[0][0]
    conn.commit()
    conn.close()
    return domain_id
#####################################################SCAN FUNCTIONS #####################################################################################################################################################################################################################################################################################################################################################
def insert_new_scan(text: str,target_name:str) ->  int:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    #conn = db.connect()
    target=fetch_by_name('target',target_name)
    print(target)
    target_id= target.get('id')
    query = 'insert into scan (name,date,target_ID) VALUES ( "{}","{}","{}");'.format(text,datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),target_id)
    conn.execute(query)
    conn.commit()
    query_results = conn.execute("Select * from scan;")
    query_results = [x for x in query_results]
    scan_id = query_results[0][0]
    conn.commit()
    conn.close()
    return scan_id 
####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#######################################################Target FUNCTIONS #################################################################################################################################################################################################################################################################################################################################################################################
def insert_new_target(text: str) ->  int:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    #conn = db.connect()
    query = 'insert into target (name) VALUES ( "{}");'.format(text)
    conn.execute(query)
    conn.commit()
    query_results = conn.execute('Select * from target where name="{}";'.format(text))
    query_results = [x for x in query_results]
    target_id = query_results[0][0]
    conn.commit()
    conn.close()
    return target_id 
def fetch_target() -> dict:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)

    query_results = conn.execute("Select * from target;").fetchall()
   # print (query_results)
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "name": result[1],        }
        todo_list.append(item)
    return todo_list
    ############################################################################# DOMAIN FUNCTION ####################################################################################################
    
#don't change this is used in url.py [GENERAL FUNCTION COULD BE REUSED ] 
def fetch_by_name_and_id(table_name:str,name:str,column_name:str,id_value:int) -> list:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    query_results = conn.execute("Select * from "+table_name+" Where name=='"+name+"' AND "+column_name+"=='"+str(id_value)+"';").fetchall()
   # print (query_results)
    conn.close()
    item={}
    for result in query_results: 
        item = {
            "id": result[0],
            "name": result[1]    }
    return item
######################################################################URL_FUNCTION################################################################################################################################################################################################################################################################################################################################################################################"
def insert_new_url(text: str,code: str,leng: str,titre: str,tech: str,scan_id:int) ->  int:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    #conn = db.connect()
    query = 'insert into url (name,stcode,content_length,title,technologie,scan_id) VALUES ( "{}","{}","{}","{}","{}","{}");'.format(text,code,leng,titre,tech,scan_id)
    print(query)
    conn.execute(query)
    conn.commit()
    query_results = conn.execute("Select * from scan;")
    query_results = [x for x in query_results]
    url_id = query_results[0][0]
    conn.commit()
    conn.close()
    return url_id 

########################################################################################################################################################""
#don't change this is used in target.py [GENERAL FUNCTION COULD BE REUSED ]    
def fetch_by_name(table_name:str,name:str) -> list:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    query_results = conn.execute("Select * from "+table_name+" Where name =='"+name+"';").fetchall()
   # print (query_results)
    conn.close()
    item={}
    for result in query_results: 
        item = {
            "id": result[0],
            "name": result[1]    }
    return item

#don't change this is used in scan.py [SPECIFIC FUNCTION]
def fetch_scan_by_name(target_name:str) -> dict:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    target=fetch_by_name('target',target_name)
    print(target)
    target_id= target.get('id')
    query_results = conn.execute("Select * from scan Where target_id=="+str(target_id)+";").fetchall()
   # print (query_results)
    conn.close()
    liste = []
    for result in query_results: 
        item = {
            "id": result[0],
            "name": result[1],
            "date":result[2]    }
        liste.append(item)
    return liste

#don't change this is used in scan.py [SPECIFIC FUNCTION]
def fetch_scan_by_name_and_target_id(name:str,target_name:str) -> dict:
    database = r"apps/db.sqlite3"
    conn= sqlite3.connect(database)
    target=fetch_by_name('target',target_name)
    target_id= target.get('id')
    query_results = conn.execute("Select * from scan Where name=='"+name+"' AND target_id=='"+str(target_id)+"';").fetchall()
    print (query_results)
    conn.close()
    list = []
    for result in query_results: 
        item = {
            "id": result[0],
            "name": result[1]    }
        list.append(item)
    return list
