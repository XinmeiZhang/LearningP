# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:11:56 2020

@author: Teilnehmer
"""

c = 5
d = 10

def myadd(aa, bb, kk):
    cc = aa + bb
    return cc

e = myadd(aa=10,bb=29, kk=None)

e = myadd(10,29,kk=None)
e = myadd(c,d,kk=None)

def myFunc(par,par1,par2, *args, **kwargs):
    print(par)
    if "name" in kwargs:
        print(kwargs["name"])
    
# myFunc("aaa")
par = 3
par1 ="df"
par2 = 3
args=[]
kwargs={"name": "Xinmei"}
#myFunc("aaa", par1=None, par2=None)
myFunc(par, par1, par2, args, kwargs)

    