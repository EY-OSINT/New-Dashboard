from calendar import calendar
import datetime
import sqlite3
##############################################################################################################################################################################################################################################################################################################################
def fetch_by_name(table_name:str,name:str) -> list:
    database = r"apps/database.db"
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

#####################################################SCAN FUNCTIONS #####################################################################################################################################################################################################################################################################################################################################################
def insert_new_scan(text: str,target_name:str) ->  int:
    database = r"app/database.db"
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
    database = r"apps/database.db"
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
    database = r"app/database.db"
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
#########################################################################################################################################################################################################################################################################################################################################################################################################################################################

#don't change this is used in target.py [GENERAL FUNCTION COULD BE REUSED ]    
def fetch_by_name(table_name:str,name:str) -> list:
    database = r"app/database.db"
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
    database = r"app/database.db"
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
    database = r"app/database.db"
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