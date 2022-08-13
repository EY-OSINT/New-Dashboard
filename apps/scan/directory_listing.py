
from asyncio import subprocess
import ipaddress
from pickle import FALSE, TRUE
import shutil
from pathlib import Path
from xmlrpc.client import boolean
import requests as rq 
import httpx
import json
from typing import List
from bs4 import BeautifulSoup as bs4
from re import sub
from wsgiref.util import request_uri 
from flask import Flask,render_template, request, url_for, redirect
from .. import database as db
import   sys 
import   os
import hashlib


dirname = os.path.dirname(__file__)
dir = os.getcwd() 

def clean_domain(line: str) -> str:
    value_with_closing_bracket = line.split(" ")
    domain = value_with_closing_bracket[0]
    value_with_closing_bracket[0]
    return domain


def dirserach(url,target_name,scan_name):
    file=os.path.join(dir,r"scans_folder",target_name,scan_name,r"url/urls.txt")
    dirserach_output=os.path.join(dir,r"scans_folder",target_name,scan_name,r"directory/dirsearch_output.txt")
    subprocess.run('dirsearch', '-l',file, '-o',dirserach_output)
    return
def read_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        lines = f.readlines()
    return lines 

def up_or_down (url:str)-> boolean : 
    r=httpx.get(url)
    if r.status_code == 200 :
        return(TRUE)
    else :
        return(False)
    
def gau_function(file_name:str,scan_id:int):
    file = "filetemps/nodkhlou/yala/ipinfo.txt"
    #for test purposes we staticaly use file 
    lines = read_file(file) 
    for line in lines : 
        r = httpx.get(line)
        status=r.status_code
        print(r.status_code)
        if status == 200 : 
            db.path(r,status)
