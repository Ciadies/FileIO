'''
Created on Oct. 4, 2023
Tests the users knowledge of the translation of computer in klingon
@author: Sebastian
'''

file = open("klingon-english.txt", "r", encoding="utf-8") #opens the file in read mode
lines = file.readlines() #creates a list with all lines separated

divisor = lines[2].find("|") #finds the divisor between the english and klingon word
english = lines[2][divisor+1:-1] #Finds the english word and excludes the new line character
klingon = lines[2][:divisor] #find the klingon word

if input(f"Please translate {english} to Klingon: ") == klingon : 
    print("Correct")
else: 
    print(f"Sorry, you're wrong! The answer is {klingon}")