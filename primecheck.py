#!/usr/bin/env python
#coding:utf-8

import codecs
import time
import math
F=codecs.open("primer.txt","r")
LI=F.read().split(",")
F.close()
def PRIME(S):
 try:
  SQROOT=math.sqrt(S)
 except:
  return(-2)
 if(S>100000000000000):
  return(-1)
 prime=True
 for n in LI:
  i=int(n)
  if (SQROOT>=i):
   if(S%i==0):
    IN=i
    prime=False
    break
  else:
   if(S==0 or S==1):
    return(0)
 if(prime==True):
  return(1)
 elif(prime==False):
  return(IN)
