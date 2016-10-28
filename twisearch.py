#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import string
import codecs
import json
CK = 'JwuvR50gm2WTwT3Lp5KkAMj85' #Consumer Key	
CS = 'dDNEAcqDOvYGa8ujBJfhnoDbF2TpFrnN5ijJ92gKODtQVvjdIi' # Consumer Secret
AT = '815236832-vxFnjhzO1ofKhHlC0viH202pLCL5IfsSJxacLYZr' # Access Token
AS = 'mSdeSjSHKnbYrhDI0bSmaB7gcPy1CbeFnC7r5VhKn55Ea'# Accesss Token Secert

url = "https://api.twitter.com/1.1/statuses/update.json"

f=codecs.open("TATSUTA.txt","r")
RES=f.read()
an=RES.split("\n")

tw=an[0]+an[1]+an[2]
tw.replace("\\n","\n")
tw.strip("\n")
PPP=""
if(len(tw+an[1])<=70):
 for i in an[1]:
  if (i!="゛")and(i!="゜")and(i!="、")and(i!="。"):
   PPP+=i+"゛"
  else:
   PPP+=i
 print(PPP)
 tw=an[0]+PPP+an[2]
 tw.strip("\n")
 tw.replace("\\n","\n")
 params={"status":tw}
 twitter = OAuth1Session(CK, CS, AT, AS)
 req = twitter.post(url, params = params)
else:
 ("死んでどうぞ")


