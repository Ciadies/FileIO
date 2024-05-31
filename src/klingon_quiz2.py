'''
Created on Oct. 4, 2023
A self guided practice quiz for the user where they choose the starting consonant they would like to practice
@author: Sebastian
'''

file = open("klingon-english.txt", "r", encoding="utf-8") #opens the file in read mode
lines = file.readlines() #creates a list with all lines separated
consonant = ""
is_consonant = False
word = ""

while not is_consonant :
    consonant = input("Please choose a valid Klingon consonant: ") 
    if consonant in (" b ch D gh H j l m n p q Q r S t v w y '") : #compares the input to the list of possible valid terms
        is_consonant = True# end the loop

for idx in range(len(lines)): #goes over every word in the list
    if lines[idx].startswith(consonant) : #checks the word to see if it starts with the correct consonant
        word = lines[idx] 
        break #ends the loop
        
divisor = word.find("|") #finds the divisor between the english and klingon word
english = word[divisor+1:-1] #Finds the english word and excludes the new line character
klingon = word[:divisor] #find the klingon word

if input(f"Please translate {english} to Klingon: ") == klingon : 
    print("Correct")
else: 
    print(f"Sorry, you're wrong! The answer is {klingon}")