#imports the ability to get a random number (we will learn more about this later!)
from random import *
#imports stuff that lets you manipulate flow time of program
import time
#doAgain will be the variable for the while loop confirming you want to continue any of the chatbot functions
#for some reason its not working as a global variable, so I'm also declaring it locally
doAgain = 'yes'
#variable for loop asking for more numbers
moreNums = 'yes'
#lists for checking many user responses that share a single intention:
greetingList = ["hi","hello","sup","hey","greetings",'yo','hola']
yesList = ['yes','yeah','sure','okay','ok','why not','yeet','yep','yup','si','affirmative','of course','always']
noList = ['no','nope','not at all','absolutely not',"yesn't","yesnt",'negative','never','of course not']

def intro():
    answer = input("Welcome to Katie's random collection of prorgams!\nWhat's your name?\n")
    print("\nHi, " + answer +'!')

def process_input(prompt):
    prompt = prompt.strip().lower()
    if greet(prompt, greetingList) == True:
        print(prompt, ' back!')
    elif prompt == "math":
        calc()
    elif prompt == "kpop":
        kpopBandNameGenerator()
    elif prompt == "rps" or prompt == "rock paper scissors":
        rps()
    elif prompt == "guesstheword":
        guessTheWord()
    elif prompt == "password":
        testPassword()
    else:
        default()

#return breaks out of function definition and returns thing in parentheses
def greet(user_greeting, greetingList):
    return(user_greeting in greetingList)

#checks if a string either starts with is all digits or starts w/ - (for negative numbers)
def numCheck(num):
    while True:
        #try a block of code but if it doesn't work, don't print an error, go to the except block instead
        try:
            num = float(num)
        #if not convertable to float, request new number
        except ValueError:
            num = input("That's not a number. Try again.\nType another number.\n")
        #if convertable to float, return float
        else:
            return(num)

def moreNumsCheck(instruction, numList):
    doAgain = 'yes'
    while doAgain in yesList:
        numRequestStr = "\nType a number " + instruction + ".\n"
        num = input(numRequestStr)
        #apply numCheck() to all calculations following number input to check that string consists of only digits
        numList.append(numCheck(num))
        moreNumConfirmStr = "\nDo you want " + instruction + " another number in this calculation/check?\n"
        doAgain = doAgainErrorCheck(moreNumConfirmStr)

#keeps asking until receives response in noList or yesList
def doAgainErrorCheck(doAgainQuestion):
    doAgain = 'yes'
    while True:
        doAgain = input(doAgainQuestion).strip().lower()
        if doAgain in yesList or doAgain in noList:
            #If in yesList, function will loop again, and if in noList it will not loop
            return(doAgain)
        else:
            print("Error! Try again.")

def calc():
    doAgain = 'yes'
    while doAgain in yesList:
        answer = input("""
Would you like to do summation (+), subtraction (-), multiplication (*), division (/), averaging (avg), or an even or odd check (evenOrOdd)?
(This calculator will only take single numbers, not expressions, when 'a number' is requested.)
""").strip().lower()
    
        if answer == '+' or answer == 'summation':
            while doAgain in yesList:
                numList = []
                numList.append(numCheck(input('\nType in the first number of the summation.\n')))
                moreNumsCheck("to add", numList)
                print("Here's your sum:", summation(numList))
                doAgain = doAgainErrorCheck("\nDo you want to calculate another sum?\n")
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")

        elif answer == '-' or answer == 'subtraction':
            while doAgain in yesList:
                numList = []
                startingNum = numCheck(input('\nType in the starting number.\n'))
                moreNumsCheck("to subtract", numList)
                print("Here's your difference:", subtraction(startingNum, numList))
                doAgain = doAgainErrorCheck("\nDo you want to calculate another difference?\n")
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")

        #see above summation section for what needs to be updated below
        elif answer == '*' or answer == 'multiplication':
            while doAgain in yesList:
                numList = []
                startingNum = numCheck(input('\nType in the starting number.\n'))
                moreNumsCheck("to multiply", numList)
                print("Here's your product:", multiply(startingNum, numList))
                doAgain = doAgainErrorCheck("\nDo you want to calculate another product?\n")
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")

        elif answer == '/' or answer == 'division':
            while doAgain in yesList:
                numList = []
                startingNum = numCheck(input('\nType in the starting number.\n'))
                moreNumsCheck("to divide", numList)
                print("Here's your quotient:", divide(startingNum, numList))
                doAgain = doAgainErrorCheck("\nDo you want to calculate another quotient?\n")
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")

        #the fill in the blank wording that works for the functions in the other calculations don't work as well here but oh well
        elif answer == 'averaging' or answer == 'avg':
            numList = []
            while doAgain in yesList:
                startingNum = numCheck(input('\nType in the starting number.\n'))
                moreNumsCheck("to include", numList)
                avg = summation(numList)/len(numList)
                print("\nHere's your average:", avg)
                doAgain = input("\nDo you want to calculate another average?\n").strip().lower()
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")                

        elif answer == 'evenorodd':
            while doAgain in yesList:
                #round() rounds to nearest integer (or n digits if parameter n given) based on the number input and checked
                roundedNum = round(numCheck(input("\nGive me a number to deem even or odd. (This function will round if given a decimal number.)\n")))
                if roundedNum % 2 == 0:
                    print(roundedNum, "is an even number.")
                elif roundedNum % 2 == 1:
                    print(roundedNum, 'is an odd number.')
                doAgain = doAgainErrorCheck("\nDo you want to check another number?\n")
            doAgain = doAgainErrorCheck("\nDo you want to do another math calculation/check of any sort?\n")
                
        else:
            print("Error. Try again.")


def summation(numList):
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
    return sum

def subtraction(startingNum, numList):
    diff = startingNum
    for i in range(len(numList)):
        diff -= numList[i]
    return diff

def multiply(startingNum, numList):
    product = startingNum
    for i in range(len(numList)):
        product *= numList[i]
    return product

def divide(startingNum, numList):
    quotient = startingNum
    for i in range(len(numList)):
        quotient /= numList[i]
    return quotient

def kpopBandNameGenerator():
    doAgain = 'yes'
    #list of words that can go into the band names
    wordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]
    print("\nWelcome to the Kpop Band Name Generator!")
    while doAgain in yesList:
        #creates empty list for name
        name = []
        #chooses reasonable name length
        while len(name) < randint(3,7):
            #chooses name parts (doesn't show) w/o repeating words; first Generates a random integer to choose words.
            randIndex = randint(0, len(wordList)-1)
            if wordList[randIndex] not in name:
                name.append(wordList[randIndex])
        #prints name acronym (tuple?); I wanted it to be in the same line; it should work for any length name below the max
        print("""\nYour band's name is ready!:""")
        #turns list strings into one string; map({function},{sequence to apply function to})
        name_str = ' '.join(map(str, name))
        #Turns one string into acronym & prints (I don't 100% understand how it works)
        print(''.join(x[0] for x in name_str.split()))
        #apparently this also works but idk why: print(''.join(i[0] for i in name_str.split() if i[0].isupper()))
        print("""\nThis stands for...""")
        #prints full form of acronym
        print(name_str)

        #keeps asking until receives response in noList, but with special error responses
        while True:
            doAgain = input("\nDo you want to generate another band name?\n").strip().lower()
            if doAgain in yesList:
                break
            elif doAgain in noList:
                print("That's boring. :( Good bye.")
                break
                #will also break from larger while loop b/c not in yesList
            else:
                print("Error! You got no jams.")

def rps():
    doAgain = 'yes'
    while doAgain in yesList:
        user = input("\nChoose 'rock', 'paper', or 'scissors'.\n")
        user = user.strip().lower()

        #error check for responses other than rock, paper, or scissors
        while user != 'rock' and user != 'paper' and user != 'scissors':
            user = input ("Error! Type your choice again: ")
            user = user.strip().lower()

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
            print("Computer:", user,"\nYou tied.")

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
    wordList = ("thaumaturgy", "serenditipity", "prestidigitation", "thorough", "rhythm", "squirrel")

    while doAgain in yesList:
        #Generates random index location to select the mystery word
        randomIndex = randint(0, len(wordList)-1)
        #select mystery word
        mysteryWord = wordList[randomIndex]

        #make blanks in a way that matches formatting w/ mysteryWord
        displayedLetters = []
        for i in range(len(mysteryWord)):
            displayedLetters += '_'

        lives = 7
        guessed = []
        print("\nWelcome to Guess the Word!")

        while lives > 0:
            #asks user to guess
            if lives == 1:
                print("""This is your last life.
Here are the letters you have guessed:""", guessed, """
Guess another letter. Please only guess lowercase letters.""")

            else:
                print("""
You have""", lives, """lives to guess the word.
Here are the letters you have guessed:""", guessed, """
Guess another letter. Please only guess lowercase letters.""")

            print(displayedLetters)

            #take user input
            guess = input()

            if guess in mysteryWord:
                #detect correct letter's place
                for i in range(len(mysteryWord)):
                    #detect if correct guessed letter is in this item in the list
                    if guess == mysteryWord[i]:
                        #replace letter: {listName.insert(index,item)}
                        del displayedLetters[i]
                        displayedLetters.insert(i,guess)

                #if win, break out of loop and program will end.
                if "_" not in displayedLetters:
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
            doAgain = doAgainErrorCheck("\nDo you want to guess a new mystery word?\n")

def testPassword():
    doAgain = 'yes'
    while doAgain in yesList:
        #Take input from the keyboard, storing in the variable test_password
        #Note - You will have to use .strip() to strip whitespace and newlines from the file and passwords
        test_password = input("\nType a trial password that starts with a letter\n").strip().lower()
        passwordUnknown = True
        #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
        with open("mostCommonPasswords.txt","r") as f:
            for line in f:
                line1 = line.strip()
                # The commented out code is unnecessary b/c " " is being counted as a line, so any password that's a single common word is being caught as a double: " " + [word] 
                # if line1 == test_password:
                #     print("\nYour password (",line1,") is weak; it's too common.")
                #     passwordUnknown = False
                #     break #breaks out of the first for loop going through the text file lines

                #checks if password entered is line in text file + # up to current year (range needs to be 1 more than year)
                if line1 in test_password:
                    #checks for a password that 
                    for i in range(2019):
                        lineNum = line1 + str(i)
                        if lineNum == test_password:
                            print("\nYour password (",lineNum,") is weak; putting a number after a common password is not strong.")
                            passwordUnknown = False
                            break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

                    #checks for a password that is two words in text file, include " " + [word], which is actually faster than looking for the single word in the file b/c " " comes first 
                    with open("mostCommonPasswords.txt","r") as f:
                        for line in f:
                            line2 = line.strip()
                            line12 = line1 + line2
                            if line12 == test_password:
                                print("\nYour password (",line12,") is weak; it's too simple for a program to crack.")
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
    intro()
    while True:
        answer = input("""
Type 'math' to do some basic math calculations/checks,
type 'kpop' to go to the Kpop Band Name Generator,
type 'rps' to play Rock, Paper, Scissors (unfinished),
type 'guessTheWord' to play a word-guessing game,
or type 'password' to test the strength of a password.
""")
        process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function. They need to be at the bottom of all of your programs.
if __name__ == "__main__":
  main()
