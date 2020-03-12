# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:29:29 2020

@author: Teilnehmer
"""
#%% 
person1 = {"name": "Xinmei", "Geburtstag": "01021974", "GeburtsOrt": "Jiangsu"}
person2 = {"name": "Mark", "Geburtstag": "01021974", "GeburtsOrt": "Jiangsu"}
person3 = {"name": "Jonas", "Geburtstag": "01021974", "GeburtsOrt": "Jiangsu"}

liste_von_personen = [person1, person2, person3]

#%%
for person in liste_von_personen:
    if "Geburtstag" in person:
        del person["Geburtstag"]

X = person1["name"]
Y = person1.get("name")

if X == Y:
    print("great!")

person1["GeburtsOrt"] = "Nanjing"

#%%
if "Ort" in person1:
    print("Ort")
else:
    print("not given")




    
#del person1["Geburtstag"]
