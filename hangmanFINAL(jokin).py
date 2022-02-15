import json
import random

with open('C:\\Users\\alumno\\Desktop\\words.json','r') as file:
    data = json.load(file)
    


def play_hangman(i):
    if i == 1: #play from selected category
        print("a")
    else: #play from random category
        word_guess = random.choice(list(data[random.choice(list(data))])) #choose a random word from a random category
        word_decreasing = word_guess.lower()
        
        print("\nThe word to be guessed is: ",word_guess)
        
        word_blank = [] #we create the blank spaces
        for a in word_guess:
            word_blank.append("_")
        
        victory = False
        
        for i in range(6,0,-1): #repeat 6 timess
            print("-------------------------------------------------------------------------------\n")
            print("You have",i,"tries") 
        
            print("ILUSTRACION Y PALABRA CON ESPACIOS")
            print(word_blank)
            
            guess = input("Guess a letter or the word: ")
            
            if guess.lower() in word_guess.lower():
                if guess.lower() == word_guess.lower(): #user has guessed the word
                    print("You won!!!!")
                    victory = True
                    break
                elif guess.lower() in word_guess.lower(): #user has guessed a letter
                    word_blank[word_decreasing.find(guess.lower())] = guess
                    word_decreasing = word_decreasing.replace(guess.lower(),"-",1)
                
                    
                    
                    
                    print("\n",guess,"is in the word")
                    
                    
                    
            else: #user didn't guess anything
                print(guess,"is not in the word")
                
        if not victory:
            print("You lost!!!!!!!!!")
            
play_hangman(2)
        
            
    