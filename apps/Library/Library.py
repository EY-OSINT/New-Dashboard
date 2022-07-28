import re 
import iptools
import os 

#Function that verifies input user if it was an email
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    free_regex = r'\b[A-Za-z0-9._%+-]+@[hotmail+\.]|[yahoo+\.]|[gmail+\.]+[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print('it as email')
        if(not(re.fullmatch(free_regex, email))):
           return True
    return False

#Function that devides input user  into three files     
def get_three_files(file,target_name,scan_name):
    f=open(file).read()
    outfile_domain = open( "scans_folder/"+target_name+"/"+scan_name+"/domain/domain_input", "w")
    outfile_ip = open("scans_folder/"+target_name+"/"+scan_name+"/domain/ip_input", "w")
    outfile_email = open("scans_folder/"+target_name+"/"+scan_name+"/domain/email_input", "w")
    for ligne in f.split('\n'):
        
        if not iptools.ipv4.validate_ip(ligne):
            if(check(ligne)):
                domain_from_mail=ligne.split('@')[1]
                outfile_email.write(domain_from_mail)
            if(not check(ligne)):
                outfile_domain.write(ligne)
        
        else:
            outfile_ip.write(ligne)
            x = '{"ip" :'+ '"'+ligne +'"'+ '}'    


#FUNCTION THAT MERGES ANY NUMBER OF FILES INTO output_file concatinates them in queue.
def merge_files(file1,file2,file3,output_file):
    
    filenames = [file1, file2,file3,output_file ]
    with open(output_file, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    return

#Function that removes duplicate LINES from file to output_file
import os
def remove_duplicates(file,output_file):
    openFile = open(file, "r")
    writeFile = open(output_file, "w") 
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

def create_dir_under_scans_folder(module_name, target_name, scan_name):
   
    path_dir=os.getcwd()+"/apps/scan/scans_folder/"+target_name+"/"+scan_name+"/"+module_name
    print(path_dir)
    try:
        os.makedirs(path_dir)
        
    except OSError as err:
        print(err)

    
    




