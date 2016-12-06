#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import requests
import json
import string
import sys
import setting
import primecheck as PCH
CK=setting.CK
CS=setting.CS
AT=setting.AT
AS=setting.AS
MYID=815236832
MYSCRNAME="pizza05132"
url = 'https://userstream.twitter.com/1.1/user.json'
urlpost = "https://api.twitter.com/1.1/statuses/update.json"
auth = OAuth1(CK, CS, AT, AS) #認証
twitter = OAuth1Session(CK, CS, AT, AS) #認証
data={}
r = requests.get(url,auth=auth,stream=True,data=data) #userstreamの読み込み
for line in r.iter_lines():
 A=line.decode("utf-8")
 try:
  S=json.loads(A)
  if(S["in_reply_to_user_id"]==MYID)and("-prime"in S["text"]):
   RES=S["text"].lstrip("@"+MYSCRNAME)
   RES=RES.lstrip(" -prime")
   A=int(RES)
   ID=S["user"]["screen_name"]
   RE="@"+ID+" " #リプから数字を抽出
   T=PCH.PRIME(A)
   if(T==1):
    RE+=str(A)+"は素数です"
   elif(T==-1 or T==-2):
    RE+="エラーです"
   elif(T==0):
    RE+="エラーです"
   else:
    RE+=str(A)+"は"+str(T)+"で割れます"
   postparams={"status":RE,"in_reply_to_status_id":ID}
   ZZZ=twitter.post(urlpost, params = postparams)#投稿
 except:
  pass
