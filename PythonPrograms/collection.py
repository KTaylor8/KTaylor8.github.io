#imports the ability to get a random number (we will learn more about this later!)
from random import *
#imports stuff that lets you manipulate flow time of program
import time
#lists for checking many user responses that share a single intent:
greetingList = ["hi","hello","sup","hey","greetings",'yo','hola']
yesList = ['yes','yeah','sure','okay','ok','why not','yeet','yep','yup','si','affirmative','of course','always']
noList = ['no','nope','not at all','absolutely not',"yesn't","yesnt",'negative','never','of course not']

#return breaks out of function definition and returns thing in parentheses
def greet(user_greeting, greetingList):
    return(user_greeting in greetingList)

#keeps asking until receives response in noList or yesList
def doAgainErrorCheck(doAgainQuestion):
    doAgain = 'yes'
    while True:
        doAgain = input(doAgainQuestion).strip().lower()
        if doAgain in yesList or doAgain in noList:
            #If in yesList, function will loop again, and if in noList it will not loop
            return(doAgain)
        else:
            print(f"Error! Try again.")

def math():
    doAgain = 'yes'
    calculationTypeList = ['addition', 'subtraction', 'multiplication', 'division', 'averages']
    while doAgain in yesList:
        calculationChosen = input(f"""
Choose one of the following calculations: {', '.join(map(str, calculationTypeList))}.
(This calculator will only take single numbers, not expressions, when 'a number' is requested.)
""").strip().lower()
    
        while calculationChosen not in calculationTypeList:
            calculationChosen = input("\nError! That's not an available calulation. Type a calculation type again.\n").strip().lower()

        while doAgain in yesList:
            numList = []
            startingNum = numCheck(input(f'\nType in the starting number.\n'))
            moreNumsCheck(calculationChosen, numList)
            print(f"Here's your answer: {calculate(calculationChosen, startingNum, numList)}")
            doAgain = doAgainErrorCheck(f"\nDo you want to do more {calculationChosen}?\n")
        doAgain = doAgainErrorCheck("\nDo you want to do another math calculation of any sort?\n")

#checks if a string either starts with is all digits or starts w/ - (for negative numbers)
def numCheck(num):
    while True:
        #try a block of code but if it doesn't work, don't print an error, go to the except block instead
        try:
            num = float(num)
        #if not convertable to float, request new number
        except ValueError:
            num = input(f"That's not a number. Type a number.\n")
        #if convertable to float, return float
        else:
            return(num)

def moreNumsCheck(calculationChosen, numList):
    doAgain = 'yes'
    if calculationChosen == 'addition':
        instruction = 'to add'
    elif calculationChosen == 'subtraction':
        instruction = 'to subtract'
    elif calculationChosen == 'multiplication':
        instruction = 'to multiply'
    elif calculationChosen == 'division':
        instruction = 'to divide'
    elif calculationChosen == 'averages':
        instruction = 'to include in the average'
    while doAgain in yesList:
        num = input(f'\nType in the next number {instruction}.\n')
        #apply numCheck() to all calculations following number input to check that string consists of only digits
        numList.append(numCheck(num))
        doAgain = doAgainErrorCheck(f'\nDo you have another number to include?\n')

def calculate(calculationType, startingNum, numList):
    currentNum = startingNum
    if calculationType == 'addition':
        for i in range(len(numList)):
            currentNum += numList[i]
    elif calculationType == 'subtraction':
        for i in range(len(numList)):
            currentNum -= numList[i]
    elif calculationType == 'multiplication':
        for i in range(len(numList)):
            currentNum *= numList[i]
    elif calculationType == 'division':
        for i in range(len(numList)):
            currentNum /= numList[i]
    elif calculationType == 'averages':
        for i in range(len(numList)):
            currentNum += numList[i]
        currentNum = currentNum/(len(numList)+1)
    return currentNum

def kpopBandNameGenerator():
    doAgain = 'yes'
    #list of words that can go into the band names
    wordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]
    while doAgain in yesList:
        #creates empty list for name
        nameList = []
        #chooses reasonable name length
        while len(nameList) < randint(3,7):
            #chooses name parts (doesn't show) w/o repeating words; first Generates a random integer to choose words.
            randIndex = randint(0, len(wordList)-1)
            if wordList[randIndex] not in nameList:
                nameList.append(wordList[randIndex])
        #map({function data type},{sequence to apply function to}) 
        nameStr = ' '.join(map(str, nameList)) #Purpose: turns list of strings into one string
        #str.join(separator) returns string in which string elements of sequence are joined by str separator
        #str.split(separator) returns list of strings formed from breaking up the str string at the separators; default separator is whitespace 
        #x = # elements in in name_str string list from .split();     also, strings are lists of characters
        #in this case, returns string in which 1st element in every word in name_str is joined directly together (by nothing)
        #apparently this also works but idk why: print(''.join(i[0] for i in name_str.split() if i[0].isupper()))
        acronym = ''.join(x[0] for x in nameStr.split())
        print(f'\nYour band name is ready!: {acronym}\nThis stands for {nameStr}.')

        #keeps asking until receives response in noList, but with special error responses
        while True:
            doAgain = input(f"\nDo you want to generate another band name?\n").strip().lower()
            if doAgain in yesList:
                break
            elif doAgain in noList:
                print(f"That's boring. :( Good bye.")
                break
                #will also break from larger while loop b/c not in yesList
            else:
                print(f"Error! You got no jams. Try again.")

def rps():
    doAgain = 'yes'
    while doAgain in yesList:
        user = input(f"\nChoose 'rock', 'paper', or 'scissors'.\n")
        user = user.strip().lower()

        #error check for responses other than rock, paper, or scissors
        while user != 'rock' and user != 'paper' and user != 'scissors':
            user = input(f"Error! Type your choice again.\n").strip().lower()

        if user == "rock":
            user_num = 1
        elif user == "paper":
            user_num = 2
        elif user == "scissors":
            user_num = 3

        #computer chooses; 2 == scissors, 3 == paper, 4 == rock 
        computer = randint(2,4)

        #time.sleep(sec) pauses program for that number of seconds
        print("\nRock")
        time.sleep(1)
        print("Paper")
        time.sleep(1)
        print("Scissors")
        time.sleep(1)
        print("Shoot!\n")
        time.sleep(0.3)

#you lose
        if user_num + 1 == computer:
            #user == 'rock'
            if user_num == 1:
                print("Computer: paper")
            #user == 'paper'
            elif user_num == 2:
                print("Computer: scissors")
            #user == 'scissors'
            elif user_num == 3:
                print("Computer: rock")

            print ("\nYou lost!")
#tie
        elif computer == user_num:
            print(f"Computer: {user}\nYou tied.")

#you win
        else:
            #user == 'rock'
            if user_num == 1:
                print("Computer: scissors")
            #user == 'paper'
            elif user_num == 2:
                print("Computer: rock")
            #user == 'scissors'
            elif user_num == 3:
                print("Computer: paper")

            print ("\nYou won!")
        doAgain = doAgainErrorCheck("\nDo you want to play again?\n")


def guessTheWord():
    doAgain = 'yes'
    #Create the list of words you want to choose from.
    wordList = ("thaumaturgy", "serendipity", "prestidigitation", "thorough", "rhythm", "squirrel")

    while doAgain in yesList:
        lives = 7
        guessedList = []
        #Generates random index location to select the mystery word
        randomIndex = randint(0, len(wordList)-1)
        #select mystery word
        mysteryWord = wordList[randomIndex]

        #make blanks in a way that matches formatting w/ mysteryWord
        displayedLetters = []
        blank = "__"
        for i in range(len(mysteryWord)):
            displayedLetters.append(blank)
        
        while lives > 0:
            guessedStr = ' '.join(guessedList[i] for i in range(len(guessedList)))
            display = ' '.join(displayedLetters[i] for i in range(len(displayedLetters)))
            if lives == 7:
                statusMessage = f'\nYou have 7 lives to guess the mystery word.'
            elif lives == 1:
                statusMessage = f'\nThis is your last life.\nGuessed letters not in mystery word: {guessedStr}'
            else:
                statusMessage = f'\nYou have {lives} lives left.\nGuessed letters not in mystery word: {guessedStr}'
            guess = input(f"{statusMessage}\nMystery word: {display}\nGuess a letter.\n").strip().lower()
            if guess in mysteryWord:
                #detect correct letter's index
                for i in range(len(mysteryWord)):
                    #detect if correct guessed letter is in this item in the list
                    if guess == mysteryWord[i]:
                        #replace letter: {listName.insert(index,item)}
                        del displayedLetters[i]
                        displayedLetters.insert(i,guess)

                #if no more _ displayed: win and break out of loop and program will end.
                if blank not in displayedLetters:
                    print(f"{mysteryWord}\nCongratulations! You won!")
                    break

            #if guess not in mysteryWord
            else:
                #check if the user inputted more than one letter (no penalty)
                if len(guess) > 1:
                    print("That was more than one letter, but you won't be penalized. Try again.")
                #check if letter was previously guessed
                elif guess in guessedList:
                    print("You already guessed that letter, but you won't be penalized. Try again.")
                else:
                    lives -= 1
                    print(f"{guess} is not in the mystery word.")
                    guessedList.append(guess)
                    #lost game; the while loop will end
                    if lives == 0:
                        print(f"\nGame over! You lost.\nThe word was {mysteryWord}.")
        doAgain = doAgainErrorCheck("\nDo you want to guess a new mystery word?\n")

def testPassword():
    doAgain = 'yes'
    while doAgain in yesList:
        #Use .strip() to strip whitespace and newlines from the file and passwords
        userPassword = input(f"\nType a trial password that starts with a letter\n").strip().lower()
        #checks if password starts with letter
        #strings are just lists of characters; .isalpha() checks if the characters in a string are all letters
        while userPassword[0].isalpha() != True:
            print(f"{userPassword[0]} starts")
            userPassword = input(f"\nThat doesn't start with a letter. Try again.\n").strip().lower()
        passwordUnknown = True
        #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
        with open("mostCommonPasswords.txt","r") as f:
            for line in f:
                line1 = line.strip()
                # The commented out code is unnecessary b/c " " is being counted as a line, so any password that's a single common word is being caught as a double: " " + [word] 
                # if line1 == userPassword:
                #     print("\nYour password (",line1,") is weak; it's too common.")
                #     passwordUnknown = False
                #     break #breaks out of the first for loop going through the text file lines

                #checks if password entered is line in text file + # up to current year (range needs to be 1 more than year)
                if line1 in userPassword:
                    #checks for a password that 
                    for i in range(2019):
                        lineNum = line1 + str(i)
                        if lineNum == userPassword:
                            print(f"\nYour password ({lineNum}) is weak; putting a number after a common password does not make it strong.")
                            passwordUnknown = False
                            break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

                    #checks for a password that is two words in text file, include " " + [word], which is actually faster than looking for the single word in the file b/c " " comes first 
                    with open("mostCommonPasswords.txt","r") as f:
                        for line in f:
                            line2 = line.strip()
                            line12 = line1 + line2
                            if line12 == userPassword:
                                print(f"\nYour password ({line12}) is weak; it's too simple for a program to crack.")
                                passwordUnknown = False
                                break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

        if passwordUnknown == True:
            print("\nGood! Your password is strong.")

        doAgain = doAgainErrorCheck("\nDo you want to test another password?\n")
        

def default():
    print("Error. I don't understand what you want. Try again.")

# --- Put your main program below! ---
def main():
    userName = input(f"Welcome to Katie's random collection of programs!\nWhat's your name?\n")
    #% string format: print('\nHi, %s!' (userInput,)) 
    #(% ({flags}) ({# spaces for characters/symbols/digits}) ({precision}) {type}   e.g. %8.2f)
    #types: %s = string, %d = integer, %f = float (specify number of decimals: %.{#}f)

    #str.format() string format: '{position:#ofSpaces.precision type}'.format(tuple of things to substitute) 
    # ex: print('{0:8.2f}'.format(4.059))  prints:    4.06
    # positions default to corresponding indices in ()
    #'{variable}'.format(variable = __) also works

    #fstring string format: f'string w/ {variables/expressions}'
    #ex below:
    #dogs = ['terrier', 5.3, 9]
    #print(f'Number {int(4/2)} {dogs[0]} {dogs[1]} {dogs[2]} wow')
    #prints:  Number 2 terrier 5.3 9 wow
    print(f'\nHi, {userName}!') 
    while True:
        userInput = input("""
Type 'math' to do some basic math calculations,
type 'kpop' to go to the Kpop Band Name Generator,
type 'rps' to play Rock Paper Scissors,
type 'guessTheWord' to play a word-guessing game,
type 'password' to test the strength of a password,
or type 'quit' to end the program.
""").strip().lower() #.strip() removes extra (accidental) spaces; .lower() converts string to lowercase
        if greet(userInput, greetingList) == True:
            #makes letters be spaced out stylistically
            greetingResponseStr = f'{userInput}!'
            print(f"{' '.join(greetingResponseStr[i] for i in range(len(greetingResponseStr)))}")
        elif userInput == "math":
            math()
        elif userInput == "kpop":
            kpopBandNameGenerator()
        elif userInput == "rps" or userInput == "rock paper scissors":
            rps()
        elif userInput == "guesstheword":
            guessTheWord()
        elif userInput == "password":
            testPassword()
        elif userInput == 'quit':
            break
        else:
            default()

# DON'T TOUCH! Setup code that runs your main() function. They need to be at the bottom of all of your programs.
if __name__ == "__main__":
  main()