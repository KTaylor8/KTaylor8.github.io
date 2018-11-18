##imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
wordList = ("append", "programming", "thorough", "rhythm", "squirrel")
##Generates random index location
randomIndex = randint(0, len(wordList)-1)
#select mystery word
mysteryWord = wordList[randomIndex]

#make blanks in a way that matches formatting w/ mysteryWord
displayed = []
for i in range(len(mysteryWord)):
    #displayed.append('_')
    displayed += '_'

lives = 7
guessed = []
print("Welcome to Guess the Word!")

while lives > 0:
    #asks user to guess
    if lives == 1:
        print("""
This is your last life.
Here are the letters you have guessed:""", guessed, """
Guess another letter. Please only guess lowercase letters.""")

    else:
        print("""
You have""", lives, """lives to guess the word.
Here are the letters you have guessed:""", guessed, """
Guess another letter. Please only guess lowercase letters.""")

    print(displayed)

    #take user input
    guess = input()

    if guess in mysteryWord:
        #detect correct letter's place
        for i in range(len(mysteryWord)):
            #detect if correct guessed letter is in this item in the list
            if guess == mysteryWord[i]:
                #replace letter: {listName.insert(index,item)}
                del displayed[i]
                displayed.insert(i,guess)

#if win, break out of loop and program will end.
        if "_" not in displayed:
            print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
            print(mysteryWord,"""
Congratulations! You won!""")
            break

    #if guess not in mysteryWord
    else:
        print("Nope!")
        #check if the user inputted more than one letter (no penalty)
        if len(guess) > 1:
            print("That was more than one letter, silly. I won't penalize you. Try again.")
        else:
            lives -= 1
            #check if letter was previously guessed
            if guess in guessed:
                print("You already guessed that letter, silly.")

            else:
                print(guess,"is not in the mystery word.")
                guessed.append(guess)

            #lost game; the while loop will end and the program will end
            if lives == 0:
                print("""~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
Game over! You lost.
The word was""", mysteryWord)

#print("End program.")
