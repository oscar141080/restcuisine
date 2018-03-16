#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
from BeautifulSoup import BeautifulSoup
import os, sys
import re
import requests
import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import smtplib
#os.environ["http_proxy"] = ""
#os.environ["https_proxy"] = ""
proxies = {
  "http": "http://proxy.server:3128",
  "https": "http://proxy.server:3128",
}
login = "oml1980oscar@gmail.com"
password = 'Vero*1517'
sender = 'oml1980oscar@gmail.com'
receivers = ['oscar.martinez@etecsa.cu']
message = """From: Oscar Martinez Lopez <oml1980oscar@gmail.com>
To: To Person <oscar.martinez@etecsa.cu>
Subject: Aviso sitio UP
El sitio de panama esta disponible.
"""
url = 'http://186.5.136.188/SIVA/verif_citas_beijing_es/' # China
#url = 'http://186.5.136.188/SIVA/verif_citas/' # Cuba
print response
soup = BeautifulSoup(response.text)
for item in soup.findAll('img', {'src': 'boton-amarillo.png'}):
    if item.get('src') == 'boton-amarillo.png':
        print "El sitio de panama esta disponible."
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.starttls()
            server.login(login,password)
            problems = server.sendmail(sender, receivers, message)
            server.quit()
            print "Successfully sent email", problems
        except SMTPException:
            print "Error: unable to send email"
        break
    else:
        print "Panama esta cerrado"
if __name__ == '__main__':
    pass
        
