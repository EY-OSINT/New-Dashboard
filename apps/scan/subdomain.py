from re import sub
from wsgiref.util import request_uri
from .. import  database as db
import   os
import   json
import   sys 
import subprocess
import hashlib
dirname = os.path.dirname(__file__)
dir = os.getcwd()
    #file = os.path.join(dir,r"scans_folder",target_name,scan_name,r"domain/domains.txt")
    #amass_output = os.path.join(dir,r"scans_folder/",target_name,scan_name,r"subdomain/amass_output.txt")
    #subfinder_output = os.path.join(dir,r"scans_folder",target_name,scan_name,r"subdomain/subfinder_output.txt")
    #shuffledns_output = os.path.join(dir,r"scans_folder",target_name,scan_name,r"subdomain/shuffledns_output.txt")
    #subdomain_output = os.path.join(dir,target_name,scan_name,r"subdomain/subdomain_output.txt")

""" THIS FUNCTION LOADS DOMAINS FROM DB /// NOT USEFUL ANYMORE
def load_domains(target_name,scan_name):    
    try:
        dir_name= "subdomain"
        os.mkdir(os.path.join(dir,dir_name))
    except FileExistsError:
        pass 
    file = os.path.join(dir,r"scans_folder",target_name,scan_name,r"domain/domains.txt")
    f=open(file).read()
    #domains = db.fetch_all_domains_by_scan_name(scan_name,target_name)
    #with open(file,'a') as file:
    #   file.write(json.dumps(domains))
    return file 
"""
def remove_duplicates(target_name,scan_name):
    os.system('figlet removing dublicates')
    file = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"subdomain/subdomain_output.txt")
    openFile = open(file, "r")
    file3=os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"subdomain/clean_subdomain_output.txt")
    writeFile = open(file3, "w") 
    #Store traversed lines
    tmp = set() 
    for txtLine in openFile: 
    #Check new line
        if txtLine not in tmp: 
            writeFile.write(txtLine) 
    #Add new traversed line to tmp 
            tmp.add(txtLine)         
    openFile.close() 
    writeFile.close()   
    
#main passive function

    
    




########################################## TOOLS FUNCTIONS ########################################################""""


def amass(type:str,target_name,scan_name): 
    os.system("figlet 'AMASS RUNNING ")
    strtype='-'+type
    file = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"domain/upload.txt")
    amass_output = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"subdomain/amass_output.txt")
    subprocess.run(["sudo","amass", "enum",strtype,"-df" ,file,"-o",amass_output])
    print("YEET")
    return
   # result= subprocess.run ([sys.executable,"-c","amass enum -active -d"+sub+ "-o amass_output.txt"])
   # else :
   # result= subprocess.run ([sys.executable,"-c","amass enum -brute -d"+sub+ "-o amass_output.txt"])
   # print (result)
   # return result
    
def subfinder(target_name,scan_name): 
    os.system("figlet 'subfinder RUNNING ")
    file = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"domain/upload.txt")
    subfinder_output = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"subdomain/subfinder_output.txt")
    subprocess.run(['sudo','subfinder', '-dL', file,'-o',subfinder_output])
    return 
def shuffledns(target_name,scan_name):
    os.system("figlet 'shuffledns RUNNING ")
    file = os.path.join(dir,r"scans_folder",target_name,scan_name,r"domain/upload.txt")
    shuffledns_output = os.path.join(dir,target_name,scan_name,r"subdomain/shuffledns_output.txt")
    subprocess.run(['sudo','shuffledns','-r',file,'-o',shuffledns_output])
    return

###################################################################          PASSIVE     FUNCTION        ###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def Passive (target_name,scan_name):
    subdomain_output = os.path.join(dir,target_name,scan_name,r"subdomain/subdomain_output.txt")
    amass_output = os.path.join(dir,r"scans_folder/",target_name,scan_name,r"subdomain/amass_output.txt")
    subfinder_output = os.path.join(dir,r"scans_folder",target_name,scan_name,r"subdomain/subfinder_output.txt")
    open(subdomain_output, 'w').close()
    amass("passive",target_name,scan_name)
    subfinder(target_name,scan_name)
    filenames = [amass_output, subfinder_output]
    with open(subdomain_output, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    remove_duplicates(target_name,scan_name)    

    return



###################################################################          ACTIVE     FUNCTION        ###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def Active(target_name,scan_name):
    subdomain_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/subdomain_output.txt")
    shuffledns_output = os.path.join(dir,r"apps/scan/scans_folder",target_name,scan_name,r"subdomain/shuffledns_output.txt")
    amass_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/amass_output.txt")
    shuffledns(target_name,scan_name)
    amass("active",target_name,scan_name)
    filenames = [amass_output, shuffledns_output ]
    with open(subdomain_output, 'w+') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    remove_duplicates(target_name,scan_name)    
    return 
######################################################################## CUSTON FUNCTION ################################################################################################
def Custom(target_name,scan_name):
    amass_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/amass_output.txt")
    shuffledns_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/shuffledns_output.txt")
    subfinder_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/subfinder_output.txt")
    subdomain_output = os.path.join(dir,r"apps/scan/scans_folder/",target_name,scan_name,r"subdomain/subdomain_output.txt")

    amass("active",target_name,scan_name)
    #shuffledns(target_name,scan_name)
    subfinder(target_name,scan_name)

    filenames = [amass_output, subfinder_output,shuffledns_output]
    with open(subdomain_output, 'w+') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    remove_duplicates(target_name,scan_name) 
    return