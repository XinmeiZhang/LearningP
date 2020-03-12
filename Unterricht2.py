# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:27:56 2020

@author: Teilnehmer
"""

# benutzname as string

benutze = "Jonas"
benutze1 = "Xinmei"
Nachbar2 = "Richard"
# test of der user meine name hat oder Nachabar hat
# vergleich = benutze == "Xinmei"
vergleich1 = benutze1 == benutze
vergleich2 = Nachbar2 == benutze

# wir mächten Nachbar gegursen

#wenn gleich xinmei, then print Xinmei
if vergleich1 == True:  #a == benutze, # a == "Xinmei"
    print ("Hello Xinmei")
#wenn nicht print hello world
else:
    # wir möchten nachbegrüsen
    #wenn ja
    if vergleich2 == True:
    #wenn nein
        print ("Hello Richard")
    else:
         print ("Hello World")



        