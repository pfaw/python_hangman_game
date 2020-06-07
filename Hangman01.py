import random
import re

#simple routine for formatting purposes
def spacedWord( fxnString, newLine):
    for n in fxnString:
        print(n, end='')
        print(" ", end='')
    if newLine == 1:
        print("\n")
        
#subroutine that is ran whenever a guess is entered by user
def letterCheck( originalWord, censoredWord, userGuess,nLives  ):
    #detect if it's a hit or miss
    hitFlag = 0
    for index,letter in enumerate(originalWord):
        if userGuess == letter:
            #It's a hit, get index and update censoredWord later
            hitFlag = 1
            print("It's a hit!")
            censoredWord[index] = userGuess
            spacedWord(censoredWord,1)
            #Get the index where the hit occured, updated censoredword, and print it out
    if hitFlag == 0:

        print("It's a miss!")
        nLives[0] = nLives[0] - 1
        print("You have ",end='')
        print(nLives[0],end='')
        print(" tries left")
        
#The hangman word choices are hardcoded, but you could easily have them read from a file    
wordPool = []
wordPool.append("hello")
wordPool.append("arrhythmia")
wordPool.append("sun")
wordPool.append("axe")
wordPool.append("monday")

#The infamous vowel-free word for this game
wordPool.append("rhythm")

wordPool.append("hexakosioihexekontahexaphobia")
wordPool.append("television")
wordPool.append("supermarket")
wordPool.append("velocity")
wordPool.append("racecar")
wordPool.append("icefrog")
wordPool.append("transistor")
wordPool.append("arrogant")
wordPool.append("mustard")
wordPool.append("screwdriver")


word =  random.choice(wordPool)
wordList = list(word)

#The game provides 9 tries
lives = [9]

#Create the censored version of the word
cword = []
for n in wordList:
    cword.append("_")
print("censored Word: ",end='')
spacedWord(cword,1)

#Ask user for a guess
#Process guess based on  three cases: Hit, miss, repeat
#Because of repeat, you need a list  that keeps track of guesses
#cWord is updated as hits and landed by user 
guessList = []
guessPool = []
while(True):
    print("-------------------------------------------")
    uGuess = input('Enter a guess: ')
    print("Your guess: ",end='')
    print(uGuess)

    repeatFlag = 0
    hitFlag   = 0
    incompleteFlag = 0
    #process the guess: check for single character, then alphabet, then lower case
    if len(uGuess) > 1:
        print("Only single character guesses please")
    else:
        if uGuess.isalpha():
            if uGuess.isupper():
                print("Only lowercase characters please")
            else: #valid input, Check if it's a repeat, but before that, check if the guessPool is empty

                #if guessPool is empty, repeats are imposible, just append, else you check

                if len(guessPool) == 0:
                    guessPool.append(uGuess)
                    #Run check sub-routine; if a hit is detected, update and print cWord
                    letterCheck(word,cword,uGuess,lives)
                else:
                    #You check for repeats
                    for letter in guessPool:
                        if letter == uGuess:
                            print("Repeated character")
                            print("Current guesses: ",end='')
                            print(guessPool)
                            repeatFlag = 1
                            break
                        else:
                            pass
                    if repeatFlag == 0:
                        guessPool.append(uGuess)
                        #run check sub-routine to check for hit or miss
                        letterCheck(word,cword,uGuess,lives)
                        
                    #reset repeatFlag
                    repeatFlag = 0
                                            
        else:
            print("Only alphabetical guesses please")

        for n in cword:
            if n == "_":
                incompleteFlag = 1
        if incompleteFlag == 0:
            print("Word complete!")
            print("CONGRATULATIONS!")
            #exit condition met, exit infinite while loop
            break

        if lives[0] == 0:
            print("-------------------------")
            print("OUT OF TRIES!")
            print("The word was: ", end ='')
            print(word)
            print("\n")
            print("Game over")
            break

logout = input('Press the enter key to close program')
 

            
       
  
     





