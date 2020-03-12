# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:57:43 2020

@author: Teilnehmer
"""

# 2 input from user
# userName = input() 
# userZahl = input()

userName = "Xinmei" 
userZahl = 5

# wenn der 2ter input ein Zahl ist, 
# userZahl1 = int(userZahl)

output = " "
#if userZahl1  == int(userZahl):
for i in range(userZahl):
    output = output + userName

is_correct = output == "aaaaa"
print(is_correct)
#else:
#    print("error")
# möchte ich den 1 input so oft ausgeben wie hoch die Zahl ist
a', i 