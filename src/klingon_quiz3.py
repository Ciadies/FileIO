'''
Created on Oct. 4, 2023
Self guided practice involving hints and multiple attempts per question
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

for attempt in range(3):
    if input(f"Please translate {english} to Klingon: ") == klingon : 
        print("Correct")
        break
    elif attempt == 0 or attempt == 1: #if the answer is wrong and it's the first or second try
        hint = klingon[0] + ((len(klingon)-2) * "*") + klingon[-1] #takes the total number of characters in the answer minus two for the first and last letter, and adds that many *s between the first and last letter
        print(f"Your hint is {hint}") #HINT
    else : 
        print(f"Sorry, you're wrong! The answer is {klingon}")
        