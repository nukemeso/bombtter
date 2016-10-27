#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import requests
import json
import sys
import random
CK = '' #Consumer Key	
CS = ''#Consumer Secret
AT = '' # Access Token
AS = ''# Accesss Token Secert

url = "https://api.twitter.com/1.1/search/tweets.json?"
urlpost = "https://api.twitter.com/1.1/statuses/update.json"
params ={"q":"爆発しろ -RT -filter:replies","result_type": "recent","count":100}
twitter = OAuth1Session(CK, CS, AT, AS)
responce = twitter.get(url, params = params)
loop =0
data=""
if responce.status_code == 200:
 SEARCH=json.loads(responce.text)
 for a in SEARCH["statuses"]:
  if(loop==0):
   via=a["source"]
   H=a["text"]
   B=int(a["text"].find("爆発しろ"))
   A=int(len(a["text"]))
   if(A-B-4==0):
     if not(("定期" in H)or("\n" in H)or("pic." in H) or ("@" in H) or("#" in H)) and (A<80)and(A>8) and not(("bot" in via) or ("twirobo" in via) or("auto" in via) or("地震" in via)or("BOT" in via)or("定期" in via)or("IFTTT" in via)):
      try:
       data+=H+","
       if("cranky" in H)or("Cranky" in H)or("コナミ社長" in H)or("KONAMI社長" in H):
        data+=H+","
      except UnicodeEncodeError:
       pass
 data=data.rstrip(",")
 ANS=data.split(",")
 TWEET=ANS[random.randint(0,len(ANS)-1)]
 RE=re.sub("/爆発しろ.*$/","が爆発しました",TWEET)
 postparams={"status":RE}
 ZZZ=twitter.post(urlpost, params = postparams)
