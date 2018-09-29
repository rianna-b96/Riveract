

import os
import ftplib
import h5py
import time as tm
import numpy as np
import pandas as pd
import datetime
from datetime import datetime

from pandas import HDFStore


#for current time
now = datetime.now()

##paths
imsidir = 'Documents/Python Scripts/'

date_fmt = '%d/%m/%YT%H:%M'
gpmflist = []

##parameters
illat, iulat = 1101, 1450 #latitude range given in example
illon, irlon = 501, 1200 #longitude range given in example
GPM_precip=['precipitationCal'] #IMERG parameter to be extracted
IMERG_vtype=np.float32 #type of IMERG_var, here it is 4-byte float

illat, iulat = 1101, 1450 #latitude range
illon, irlon = 501, 1200 #longitude range


##selecting IMERG data from the FTP server
year=now.year

month=now.month

day=now.day

hour=now.hour

minute = "00"

gpm_path= 'NRTPUB/imerg/early/'+str(year)+str(month).zfill(2)

imerg_f= str(year)+str(month).zfill(2)+str(day).zfill(2)+"-S"+str(now.hour).zfill(2)+str(minute).zfill(2)+"00"

ftp = ftplib.FTP('jsimpson.pps.eosdis.nasa.gov')
ftp.login('shravya.manchanda9@gmail.com', 'shravya.manchanda9@gmail.com')
ftp.cwd(gpm_path)

ftp.pwd() #print working directory

gpm_files=ftp.nlst() # a list of file names

filename =(gpm_files[len(gpm_files)-1]) # print the last file from ftp year and month file
#this chooses the last file for hour and minute

#import os

dirpath = os.getcwd()
print("current directory is : " + dirpath)

#creates a new file

dirpath=dirpath + "\\"

print (dirpath + filename)

localfile = open(dirpath + filename,'wb')

ftp.retrbinary('RETR %s' % filename, localfile.write)
ftp.quit()

localfile.close()
print (localfile.name)
dataset = h5py.File(localfile.name, 'r')

print(dataset.filename)


ivar = dataset['/Grid/precipitationCal'][1143:1144, 501:502].astype(IMERG_vtype)


csv_filename=dirpath+'IMERG_F_'+imerg_f+'_'+ 'precip'+'.dat', 'w'
print (csv_filename)


oneTvar=pd.DataFrame(ivar) #nparray => pd


f = open(dirpath+'IMERG_F_'+imerg_f+'_'+ 'Precip'+'.dat', 'w')

print (oneTvar)

oneTvar.to_csv(f,header=False,index=False,float_format='%8.2f',na_rep=-999.)