#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

from requests_oauthlib import OAuth1Session
import datetime
import requests
import json
import sys
import random
import setting 
CK=setting.CK
CS=setting.CS
AT=setting.AT
AS=setting.AS
excludes=setting.excludes
url = "https://api.twitter.com/1.1/search/tweets.json?"
urlpost = "https://api.twitter.com/1.1/statuses/update.json"
favurl = "https://api.twitter.com/1.1/favorites/create.json"
params ={"q":"爆発しろ exclude:retweets -http -filter:images -filter:videos -filter:links "+excludes,"result_type": "recent","count":100}
twitter = OAuth1Session(CK, CS, AT, AS) #認証
responce = twitter.get(url, params = params)#爆発しろを含むツイートを100検索
idlist=""#この中にツイートIDを入れていきます。
data=""#この中にツイート本文を入れていきます。
FA="false"
bombed="false"
if responce.status_code == 200:
 SEARCH=json.loads(responce.text)
 for a in SEARCH["statuses"]:
   via=a["source"] #viaの判定
   reply=a["in_reply_to_status_id_str"]
   favid=str(a["id"])#ツイートIDの取得
   H=a["text"]#ツイート本文の取得
   B=int(a["text"].find("爆発しろ"))
   A=int(len(a["text"]))
   if(A-B-4==0):#ツイートの長さとかを測定して後方一致のツイートを絞る
     if not(("定期" in H)or("\n" in H)or(".@" in H)or("@" in H) or("#" in H)) and (A<=80)and(A>8) and not(("bot" in via) or ("twirobo" in via) or("auto" in via) or("地震" in via)or("BOT" in via)or("定期" in via)or("IFTTT" in via))and [not(reply=="")] and (a["entities"]["urls"]==[]):
      #9～80文字でリプライ、ハッシュタグ、改行、画像がない、且つbotで無いと思われるツイートを取得
      try:
       idlist+=favid+","
       data+=H+","#リストの中に入れていきます。
       if("cranky" in H)or("Cranky" in H)or("コナミ社長" in H)or("KONAMI社長" in H):
        #crankyとKONAMI社長は確率UP
        idlist+=favid+","
        data+=H+","
      except UnicodeEncodeError:
       pass
 #↓ツイートIDと本文をリスト化します。
 idlist=idlist.rstrip(",")
 ID=idlist.split(",")
 data=data.rstrip(",")
 ANS=data.split(",")
#ツイートの取得はここまで
m=0
while(m<3):
 if not(ANS[0]==""):
  AAAA=random.randint(0,len(ANS)-1)
  TWEET=ANS[AAAA]
  FAVID=ID[AAAA]#リストとして拾ったツイートの中からランダムで選びます
  if("めかろいど爆発しろ" in TWEET):#ぼむったーっぽく自爆してもらいます
   RE=TWEET.replace("爆発しろ","が自爆しました")
   bombed="true"
  elif("から爆発しろ" in TWEET):
   RE=TWEET.replace("爆発しろ","爆発しました")#～から爆発しろに対応
   bombed="true"
  elif("くりいむろいど爆発しろ" in TWEET):
   RE=TWEET.replace("爆発しろ","が大爆発しました")#くりいむを大爆発
   bombed="true"
  else:
   RE=TWEET.replace("爆発しろ","が爆発しました")
   bombed="true"
 else:#ツイートが引っかからなかったらおとなしく自爆してもらいます。
  self=["爆発させるものがないから代わりにめかろいどが自爆しました","爆発させるものがないから代わりに開発者のくりいむろいどが爆発しました"]
  RE=self[random.randint(0,1)]
 #ここから投稿していきます
 postparams={"status":RE}
 ZZZ=twitter.post(urlpost, params = postparams)#投稿
 if (ZZZ.status_code == 200):#最大で三回リトライします。
  favparams={"id":int(FAVID)}
  FAVEXE=twitter.post(favurl,params=favparams)#元ツイをふぁぼ
  m=3
  FA="true"
 else:
  m+=1
  
if(FA=="false"):#三回リトライしてもダメなとき、自爆します
 RAN1=random.randint(1,1000)
 RAN2=random.randint(1,1000)
 if(RAN1==RAN2):
  RE="チンポ(ﾎﾞﾛﾝ"#0.1%の確率で性器を露出します。よっぽどのことがない限り起きない
 else:
  KKK=["同じツイートばっかり拾おうとするからめかろいどが自爆しました","同じツイートばっかり拾おうとするから開発者のくりいむろいどが爆発しました"]
  RE=KKK[random.randint(0,1)]
 postparams={"status":RE}
 ZZZ=twitter.post(urlpost, params = postparams)#投稿

#ここから下はログの出力。消しても動きます
if(bombed=="true")and(FA=="true"):
 TIMEs=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
 with open("explotion.log",mode="a",encoding="utf-8") as EX:
  EX.write(str(TIMEs)+":"+RE+"\n")#時間と一緒にツイートを出力するです
  EX.close()
