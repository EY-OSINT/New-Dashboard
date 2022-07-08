import re 
import iptools
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    free_regex = r'\b[A-Za-z0-9._%+-]+@[hotmail+\.]|[yahoo+\.]|[gmail+\.]+[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print('it as email')
        if(not(re.fullmatch(free_regex, email))):
           return True
    return False
def get_three_files(file,target_name,scan_name):
    f=open(file).read()
    outfile_domain = open( "scans_folder/"+target_name+"/"+scan_name+"/domain_input", "w")
    outfile_ip = open("scans_folder/"+target_name+"/"+scan_name+"/ip_input", "w")
    outfile_email = open("scans_folder/"+target_name+"/"+scan_name+"/email_input", "w")
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