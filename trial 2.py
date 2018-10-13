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
import bs4
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from pandas import HDFStore


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
response = urllib.request.urlopen(req)
soup = bs4.BeautifulSoup(response)

for link in soup.find_all('a'):
    all_folders= (link.get('href'))# a list of folder names
print (all_folders)
#folder = (all_folders[len(all_folders) - 1])  # pick the last folder

airs_path2 =airs_path + all_folders
req2= urllib.request.Request(airs_path2)
response2 = urllib.request.urlopen(req2).read()
soup2 = BeautifulSoup(response2)

dirpath = os.getcwd()
dirpath = dirpath + '\\'
print (dirpath)
#localfile = open(dirpath + filename, 'wb')
# ftp.retrbinary('RETR %s' % filename, localfile.write) # retrieve data

links = []

for link in soup2.findAll('a'):
        links.append(link.get('href'))
filename=(links[len(links)-5])
#need to pick newest file

url =airs_path + all_folders + filename

username = 'shravya'
password='Riveract9'

# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# password_mgr.add_password(None, "https://urs.earthdata.nasa.gov", username, password)

# cookie_jar = cookiejar()

# opener = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_mgr), urllib.request.HTTPCookieProcessor(cookie_jar))
# urllib.request.install_opener(opener)

# request = urllib.request(airs_url)
# reponse = urllib.request.urlopen(request)


# s = requests.Session()
# s.cookies = cj


class SessionWithHeaderRedirection(requests.Session):
    AUTH_HOST = "urs.earthdata.nasa.gov"
    def __init__(self,username, password):
        super().__init__()
        self.auth = (username, password)

    def rebuild_auth(self, prepared_request, reponse):
        heders = prepared_request.headers
        url=prepared_request.url

        if "Authorization" in headers:
            original_parsed = requests.utils.urlparse(reponse.request.url)
            redirect_parsed = requests.utils.urlparse(url)
        return

session = SessionWithHeaderRedirection(username, password)

filename = url[url.rfind('/')+1:]

response = session.get(url)
print (response.status_code)

with open(filename, 'wb') as fd:
    for chunk in response.iter_content(chunk_size=1024*1024):
        fd.write(chunk)
        fd.close()

import urllib.request

urllib.request.urlretrieve(url, filename)

