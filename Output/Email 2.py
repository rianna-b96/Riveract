
import re
import os
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#fromaddr = "YOUR EMAIL"
#toaddr = "EMAIL ADDRESS YOU SEND TO"

fromaddr = "riveractflood@gmail.com"
toaddr = ['shravya.manchanda9@gmail.com', 'jialuo.ke@student.unsw.edu.au', 's.veluru@student.unsw.edu.au','rianna.bernal96@gmail.com','e.esmero@student.unsw.edu.au']
Email_password = "riveract09!"



msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "Flash Flood Warning"

#create folder and place all of the body text message

#if warning = Low Flood
#then dirpath="C:\Users\shrav\Documents\Python Scripts\Email\Low Flood.txt]" #this changes according to where the txt is saved
dirpath="C:\Users\shrav\Documents\Python Scripts\Email\Low Flood.txt]"
f =open (dirpath, 'r')
message = f.read()
f.close()

#if warning = Large Flood
#then dirpath="C:\Users\shrav\Documents\Python Scripts\Email\Large Flood.txt]" #this changes according to where the txt is saved
#dirpath="C:\Users\shrav\Documents\Python Scripts\Email\Large Flood.txt]"
#f =open (dirpath, 'r')
#message = f.read()
#f.close()

#if warning = false
#then dirpath="C:\Users\shrav\Documents\Python Scripts\Email\False Warning.txt]" #this changes according to where the txt is saved
#dirpath="C:\Users\shrav\Documents\Python Scripts\Email\False Warning.txt]"
#f =open (dirpath, 'r')
#message = f.read()
#f.close()



msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

server.login(fromaddr, Email_password)

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


