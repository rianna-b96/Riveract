import os
import ftplib
import h5py
import time as tm
import numpy as np
import pandas as pd
import datetime
import pip
from datetime import datetime

import urllib
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import cookiejar

now = datetime.now()
year=now.year
month=now.month
day=now.day
hour=now.hour
minute = now.minute

imerg_f= str(day).zfill(2)+str(month).zfill(2)+str(year)+"("+str(now.hour).zfill(2)+':'+str(minute).zfill(2)+')'

airs_path ='https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2RET_NRT.006/' + str(year) + '/'

#need to create a list of filename pick the newest
req = urllib.request.Request(airs_path) #open the airs website
response = urllib.request.urlopen(req).read()
soup = BeautifulSoup(response)

for link in soup.find_all('a'):
    all_folders= (link.get('href'))# a list of folder names
print (all_folders)
#folder = (all_folders[len(all_folders) - 1])  # pick the last folder

airs_path2 =airs_path + all_folders
req2= urllib.request.Request(airs_path2)
response2 = urllib.request.urlopen(req2).read()
soup2 = BeautifulSoup(response2)

links = []

for link in soup2.findAll('a'):
        links.append(link.get('href'))
filename=(links[len(links)-5])
#need to pick newest file

airs_url =airs_path + all_folders + filename

username = 'shravya'
password='Riveract9'
url = "https://urs.earthdata.nasa.gov"
cookie = cookiejar.CookieJar()
cookie_process = urllib.request.httpcookieprocessor(cookie_jar)
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

password_mgr.add_password(None, url, username, password)
opener = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_mgr), urllib.request.httpcookieprocessor(cookie_jar))
urllib.request.install_opener(opener)

request_air = urllib.request.urlopen(airs_url)
response_air = urllib.request.urlopen(request).read()


result = urllib.request.urlopen(request).read()


dataset = urllib.urlretrieve(air_path) #where will it save it?

dirpath = os.getcwd()

localfile = open(dirpath + filename,'wb')

localfile.close()

print (localfile.name)

dataset = h5py.File(localfile.name, 'r')

print(dataset.filename)

ivar = dataset['/Grid/temperature'][1143:1144, 501:502].astype(IMERG_vtype) #check the name on grid is correct

csv_filename=dirpath+'IMERG_F_'+imerg_f+'_'+ 'precip'+'.csv', 'w'
print (csv_filename)


oneTvar=pd.DataFrame(ivar) #nparray => pd


f = open(dirpath+'airs'+'date'+ 'Air_Temperature'+'.csv', 'w')

print (oneTvar)

oneTvar.to_csv(f,header=False,index=False,float_format='%8.2f',na_rep=-999.)



