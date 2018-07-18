# Project #5: Hangman
# July 17 2018
# Julia Zhao

from random import randint

def displayGuessed(): #displays the letters that have already been guessed by the player
    for item in guessed:
        print (item, end="")
    print ("")
        
print ("Welcome to Hangman! You may guess until you guess incorrectly 5 times!")

words = ["apple pie", "banana pie", "peach pie", "mango pie", "pear pie"] #word bank
guessed = []
numGuesses=5

random = randint(0,4) #randomly choose a letter from the word bank
word=words[random] #this is the word that was chosen

hiddenWord="" #this will be the word that the player sees

#put dashes and spaces
for letters in word:
    if letters==" ": #current letter is a space
        hiddenWord+=" " #add a space
    else:
        hiddenWord+="-" #add a dash

while (hiddenWord!=word and numGuesses>0): #while word hasn't been guessed and there are still chances left
    print ("Your word is: " + hiddenWord) #display information
    print ("Letters that have already been guessed: ")
    displayGuessed()
    
    valid=False

    while (valid==False): #make sure the guess is valid
        print ("Chances left: " + str(numGuesses))
        guess = input("Please enter your guess: ")
        if (len(guess)==1 and guess.isalpha()==True and (guess in guessed)==False): #guessed a letter that hasn't been guessed before
            #get out of the loop
            valid=True
        else:
            print ("Invalid! Please enter a valid letter that has not been guessed.")

    #add letter to the guessed list
    guessed.append(guess)

    #search through the word to see if the letter exists
    if (word.find(guess)>-1): #was found
        temp=""
        start=0
        while (word.find(guess, start)!=-1):
            index=word.find(guess, start)
            temp+=hiddenWord[start:index] + word[index]
            start=index+1
        #add the rest of the word onto temp
        if (start<len(word)):
            temp+=hiddenWord[start:]
        hiddenWord=temp
    else:
        print ("Sorry! That letter isn't in the word...")
        numGuesses-=1

#game has ended
if hiddenWord==word:
    print ("Congratulations! You guessed it!")
    print ("Thanks for playing Hangman!")
else:
    print ("You ran out of chances!")
    print ("The word was " + word)
