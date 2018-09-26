

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

imerg_f= str(year)+str(month).zfill(2)+str(day).zfill(2)+"/"+"-S"+str(now.hour).zfill(2)+str(minute).zfill(2)+"00"

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

print(dataset.keys())

precip = dataset['/Grid/precipitationCal']

precip = np.transpose(precip)

theLats = dataset['Grid/lat']


theLons = dataset['Grid/lon']



# Code produced through UMBC's Joint Center for Earth Systems Technology
# If you have any questions or concerns regarding the following script, please contact Amanda Rumsey at arumsey@umbc.edu
# The purpose of this code is to convert datasets within gmi hdf files to txt files

# start of the program
print("starting the conversion from hdf to txt file:")
print("")

# import all necessary packages
print("importing packages")
import os
import glob
import numpy as np
import h5py

print("packages imported")
print("")

# list of methods
# this method will print all of the names of the hdf internal files
print("defining methods")


def printname(name):
    print(name)


print("method definitions complete")
print("")

# assign current working directory
dir = os.getcwd()
print("the current directory is: " + dir)
print("")

# make directory folder (if it does not already exist) and directory variable for output text files
print("creating a directory for output text files")
if not os.path.exists(dir + "//text_files/"):
    os.makedirs(dir + "//text_files/")
txtdir = dir + "\\" + "text_files"
print("text file directory created")
print("")

# list of hdf files to be converted
print("list of hdf files")
hdflist = glob.glob(os.path.join('filename'))
print(hdflist)
print("")

# available datasets in hdf files
print("available datasets in HDF5 files: ")
singlehdflist = hdflist[0]
insidehdffile = h5py.File(singlehdflist, "r+")
insidehdffile.visit(printname)
insidehdffile.close()
print("")

# datatype conversion
# this loop outputs the indvidual lat long and precip datasets available within the hdf file as indivdual text files
for hdffile in hdflist:
    # read and write hdf file
    print("reading the hdf file: " + hdffile)
    currenthdffile = h5py.File(hdffile, "r+")
    print("reading hdf file complete")
    print("")

    # data retrieval
    # This is where you extract the datasets you want to output as text files
    # you can add more variables if you would like
    # this is done in the format varible=hdffilename['dataset']
    print("creating arrays for latitude, longitude and surface precipitation")
    lat = currenthdffile['S1/Latitude']
    long = currenthdffile['S1/Longitude']
    precip = currenthdffile['S1/surfacePrecipitation']
    latitude = np.array(lat)
    longitude = np.array(long)
    precipitation = np.array(precip)
    print("creation of arrays complete")
    print("")

    # converting to text file
    print("converting arrays to text files")
    outputlat = txtdir + "\\" + hdffile[:-5] + "_lat.txt"
    outputlong = txtdir + "\\" + hdffile[:-5] + "_long.txt"
    outputprecip = txtdir + "\\" + hdffile[:-5] + "_precip.txt"
    np.savetxt(outputlat, latitude, fmt='%f')
    np.savetxt(outputlong, longitude, fmt='%f')
    np.savetxt(outputprecip, precipitation, fmt='%f')
    print("")

print("script complete!")

