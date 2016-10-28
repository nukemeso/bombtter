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
namelist=""#この中にツイート主の@抜きIDを保存
idlist=""#この中にツイートIDを入れていきます。
data=""#この中にツイート本文を入れていきます。
if responce.status_code == 200:
 SEARCH=json.loads(responce.text)
 for a in SEARCH["statuses"]:
   scrname = a["user"]["screen_name"]#ツイート主の判定
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
       namelist+=scrname+","#リストの中に入れていきます。
       if("cranky" in H)or("Cranky" in H)or("コナミ社長" in H)or("KONAMI社長" in H):
        #crankyとKONAMI社長は確率UP
        data+=H+","
        idlist+=str(favid)+","
        namelist+=scrname+","
      except UnicodeEncodeError:
       pass
 #↓ツイートIDと本文をリスト化します。
 idlist=idlist.rstrip(",")
 ID=idlist.split(",")
 data=data.rstrip(",")
 ANS=data.split(",")
 namelist=namelist.rstrip(",")
 IDs=namelist.split(",")
#ツイートの取得はここまで
 
if not(ANS[0]==""):
 AAAA=random.randint(0,len(ANS)-1)
 SCRNAME=IDs[AAAA]
 TWEET=ANS[AAAA]
 FAVID=ID[AAAA]#リストとして拾ったツイートの中からランダムで選びます
 if("めかろいど爆発しろ" in TWEET):#ぼむったーっぽく自爆してもらいます
  RE=TWEET.replace("爆発しろ","が自爆しました")
 elif("から爆発しろ" in TWEET):#～(だ)から爆発しろを自然に爆発させます。
  RE=TWEET.replace("爆発しろ","爆発しました")
 elif("俺爆発しろ" in TWEET):#俺爆発しろとか言ってるやつのIDを抜き出してみます。
  RE=TWEET.replace("俺爆発しろ",SCRNAME+"が爆発しました")
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
