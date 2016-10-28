#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import requests
import json
import sys
import random


CK = '' #Consumer Key	
CS = '' # Consumer Secret
AT = '' # Access Token
AS = ''# Accesss Token Secert
 
url = "https://api.twitter.com/1.1/search/tweets.json?"
urlpost = "https://api.twitter.com/1.1/statuses/update.json"
favurl = "https://api.twitter.com/1.1/favorites/create.json"
params ={"q":"爆発しろ exclude:retweets","result_type": "recent","count":100}
twitter = OAuth1Session(CK, CS, AT, AS) #認証
responce = twitter.get(url, params = params)#爆発しろを含むツイートを100検索
idlist=""#この中にツイートIDを入れていきます。
data=""#この中にツイート本文を入れていきます。
if responce.status_code == 200:
 SEARCH=json.loads(responce.text)
 for a in SEARCH["statuses"]:
   via=a["source"] #viaの判定
   favid=a["id"]#ツイートIDの取得
   H=a["text"]#ツイート本文の取得
   B=int(a["text"].find("爆発しろ"))
   A=int(len(a["text"]))
   if(A-B-4==0):#ツイートの長さとかを測定して後方一致のツイートを絞る
     if not(("定期" in H)or("\n" in H)or("pic." in H) or ("@" in H) or("#" in H)) and (A<=80)and(A>8) and not(("bot" in via) or ("twirobo" in via) or("auto" in via) or("地震" in via)or("BOT" in via)or("定期" in via)or("IFTTT" in via)):
      #9～80文字でリプライ、ハッシュタグ、改行、画像がない、且つbotで無いと思われるツイートを取得
      try:
       data+=H+","
       idlist+=str(favid)+","
       if("cranky" in H)or("Cranky" in H)or("コナミ社長" in H)or("KONAMI社長" in H):
        #crankyとKONAMI社長は確率UP
        data+=H+","
        idlist+=str(favid)+","
      except UnicodeEncodeError:
       pass
 idlist=idlist.rstrip(",")
 ID=idlist.split(",")
 #↓ツイートIDと本文をリスト化します。
 data=data.rstrip(",")
 ANS=data.split(",")
#ツイートの取得はここまで
 
if not(ANS[0]==""):
 AAAA=random.randint(0,len(ANS)-1)
 TWEET=ANS[AAAA]
 FAVID=ID[AAAA]#リストとして拾ったツイートの中からランダムで
 if("めかろいど爆発しろ" in TWEET):#ぼむったーっぽく自爆してもらいます
  RE=TWEET.replace("爆発しろ","が自爆しました")
 else:
  RE=TWEET.replace("爆発しろ","が爆発しました")
elif(ANS[0]==""):#ツイートが引っかからなかったらおとなしく自爆してもらいます。
 self=["爆発させるものがないから代わりにめかろいどが自爆しました","爆発させるものがないから代わりに開発者のくりいむろいどが爆発しました"]
 RE=self[random.randint(0,1)]

#ここから投稿していきます
postparams={"status":RE}
ZZZ=twitter.post(urlpost, params = postparams)#投稿
favparams={"id":int(FAVID)}
FAVEXE=twitter.post(favurl,params=favparams)#元ツイをふぁぼ
if not(ZZZ.status_code == 200):
 print("投稿できなかったみたいですよ")
if not(FAVEXE.status_code == 200):
 print("ふぁぼれなかったみたいですよ")
