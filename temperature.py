
import os
from datetime import datetime

import urllib
from http.cookiejar import CookieJar
from wsgiref import headers

import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from pandas import HDFStore


now = datetime.now()
year=now.year

month=now.month

day =now.day

hour=now.hour

minute = now.minute

imerg_f= str(day).zfill(2)+str(month).zfill(2)+str(year)+"("+str(now.hour).zfill(2)+':'+str(minute).zfill(2)+')'

airs_path ='https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2RET_NRT.006/' + str(year) + '/'


#need to create a list of filename pick the newest
request = requests.get(airs_path)
soup = BeautifulSoup (request.content, 'html.parser')

for link in soup.find_all('a'):
    all_folders= (link.get('href'))# a list of folder names
print (all_folders)
#folder = (all_folders[len(all_folders) - 1])  # pick the last folder

airs_path2 = airs_path + all_folders

request2 = requests.get(airs_path2)
soup2 = BeautifulSoup (request2.content, 'html.parser')

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

print (url)

username = 'shravya'
password = 'Riveract9'

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, "https://urs.earthdata.nasa.gov", username, password)

cookie_jar = CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager),
                                     urllib.request.HTTPCookieProcessor(cookie_jar))
urllib.request.install_opener(opener)

request = urllib.request.Request(url)
response= urllib.request.urlopen(request)

nameFILE = "Temperature" + " " +str(day).zfill(2)+str(month).zfill(2)+str(year)

with open (nameFILE, 'wb') as output:
    output.write(response.read())

dataset = h5py.File(nameFILE, 'r')




