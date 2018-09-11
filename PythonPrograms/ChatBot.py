##imports the ability to get a random number (we will learn more about this later!)
from random import *
import time
#doAgain will be the variable for the while loop confirming you want to continue any of the chatbot functions
doAgain = 'yes'
#variable for loop asking for more numbers
moreNums = 'yes'
#lists for checking many user responses that share a single intention:
greetingList = ["hi","hello","sup","hey","greetings",'yo','hola']
yesList = ['yes','yeah','sure','okay','ok','why not','yeet','yep','yup','si','affirmative','of course','always']
noList = ['no','nope','not at all','absolutely not',"yesn't","yesnt",'negative','never','of course not']
#doAgain (no its companion checker for noList vs error) and lists are not yet integrated into all functions

def intro():
    answer = input("I'm your personal chatbot, Billy Bob Joe Bob Joe the 17th and a half.\nWhat's your name?\n")
    print("\nHi, " + answer +'!')

def process_input(prompt):
    prompt = prompt.lower()
    if greet(prompt, greetingList) == True:
        print(prompt, ' back!')
    elif prompt == "calculator":
        calc()
    elif prompt == "kpop":
        kpopNameGenerator()
    elif prompt == "rps" or prompt == "rock paper scissors":
        rps()
    elif prompt == "evenorodd":
        evenOrOdd()
    elif prompt == "guessTheWord":
        guessTheWord()
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
        doAgain = input(doAgainQuestion).lower()
        if doAgain in yesList or doAgain in noList:
            #If in yesList, function will loop again, and if in noList it will not loop
            return(doAgain)
        else:
            print("Error! Try again.")

def calc():
    print("""
Would you like to do summation (+), subtraction (-), multiplication (*), division (/), averaging (avg), or an even or odd check (evenOrOdd)?
(Please note that this calculator will only take single numbers, not expressions, when 'a number' is requested.)""")
    answer = input().lower()
    doAgain = 'yes'
    
    #NEED TO ADD DOAGAIN loops and error checks TO REST OF FUNCTIONS AND numchecks AND MORENUMSCHECKS TO REST OF NUMBER FUNCTIONS
    if answer == '+' or answer == 'summation':
        while doAgain in yesList:
            numList = []
            numList.append(numCheck(input('Type in the first number of the summation.\n')))
            moreNumsCheck("to add", numList)
            print("Here's your sum:", summation(numList))
            doAgain = doAgainErrorCheck("\nDo you want to calculate another sum?\n")

    elif answer == '-' or answer == 'subtraction':
        while doAgain in yesList:
            numList = []
            startingNum = numCheck(input('Type in the starting number.\n'))
            moreNumsCheck("to subtract", numList)
            print("Here's your difference:", subtraction(startingNum, numList))
            doAgain = doAgainErrorCheck("\nDo you want to calculate another difference?\n")

    #see above summation section for what needs to be updated below
    elif answer == '*' or answer == 'multiplication':
        #error check for non-numbers
        while True:
            num1 = input("1st number: ")
            if (num.isdigit() == True):    
                break
            else:
                print("That's not a number. Try again.")
        #error check for non-numbers
        while True:
            num2 = input ('2nd number: ')
            if (num.isdigit() == True):
                break
            else:
                print("That's not a number. Try again.")
        print(float(num1) * float(num2))

    elif answer == '/' or answer == 'division':
        #error check for non-numbers
        while True:
            num1 = input("Dividend: ")
            if (num1.isdigit() == True):
                break
            else:
                print("That's not a number. Try again.")
        #error check for non-numbers
        while True:
            num2 = input ('Divisor: ')
            if (num2.isdigit() == True):
                break
            else:
                print("That's not a number. Try again.")
        print(float(num1) / float(num2))

    elif answer == 'averaging' or answer == 'avg':
        numList = []
        moreNums = 'yes'
        while doAgain in yesList:
            while True:
                num = input("Type the first number in the group to average.\n")
                if num.isdigit() == True:
                    break
                else:
                    print("That's not a number. Try again.")
            numList.append(float(num))
            while moreNums in yesList:
                while True:
                    num = input("\nType in the next number.\n")
                if (num.isdigit() == True):
                    break
                else:
                    print("That's not a number. Try again.")
                numList.append(float(num))
                moreNums = input("\nAre there more numbers in your group to average?\n").lower()
            avg = summation(numList)/len(numList)
            print("\nHere's your average:", avg)
            doAgain = input("\nDo you want to calculate another average?\n").lower()

    elif answer == 'evenorodd':
        while (doAgain in yesList):
            #round() rounds to nearest integer (or n digits if parameter n given) based on the number input and checked
            roundedNum = round(numCheck(input("Give me a number to deem even or odd. (This function will round if given a decimal number.)\n")))
            if roundedNum % 2 == 0:
                print(roundedNum, "is an even number.")
            elif roundedNum % 2 == 1:
                print(roundedNum, 'is an odd number.')
            doAgain = doAgainErrorCheck("\nDo you want to check another number?\n")

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

def kpopNameGenerator():
    #list of words that can go into the band names
    wordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]
    print("\nWelcome to the Kpop Band Name Generator!")
    #doAgain = 'yes'
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
        print(''.join(i[0] for i in name_str.split() if i[0].isupper()))
        #apparently this also works but idk why: print(''.join(x[0] for x in name_str.split()))
        print("""\nThis stands for...""")
        #prints full form of acronym
        print(name_str)

        #keeps asking until receives response in noList
        while True:
            doAgain = input("\nDo you want to generate another band name?\n").lower()
            if doAgain in yesList:
                break
            elif doAgain in noList:
                print("That's boring. :( Good bye.")
                break
                #will also break from larger while loop b/c not in yesList
            else:
                print("Error! You got no jams.")

def rps():
    answer = ("\nDo you want to play Rock Paper Scissors? ('yes' or 'no')")
    answer = answer.lower()
    if answer == "yes":
        user = input("Choose 'rock', 'paper', or 'scissors'.")
        user = user.lower()

        while user != 'rock' and user != 'paper' and user != 'scissors':
            user = input ("Error! Type your choice again: ")
            user = user.lower()

        if user == "rock":
            user_num = 1
        elif user == "paper":
            user_num = 2
        elif user == "scissors":
            user_num = 3

#RPS GAME UNFINISHED
        computer = randint(2,4)
        print("Rock")
        time.speed(1)
        print("Paper")
        time.speed(1)
        print("Scissors")
        time.speed(1)
        print("Shoot! \n")
        time.speed(0.2)

#you lose
        if computer - 1 == user:
            if user_num == 1:
                print("Computer: paper")
            elif user_num == 2:
                print("Computer: scissors")
            elif user_num == 3:
                print("Computer: rock")

            print ("You lost!")
#tie
        elif computer == user_num:
            print("You tied!")

#you win
        else:
            if user == 1:
                print("Computer: paper")
            elif user == 2:
                print("Computer: scissors")
            elif user == 3:
                print("Computer: rock")

            print ("You won!")


def guessTheWord():
    #Create the list of words you want to choose from.
    wordList = ("thaumaturgy", "serenditipity", "prestidigitation", "thorough", "rhythm", "squirrel")
    ##Generates random index location
    randomIndex = randint(0, len(wordList)-1)
    #select mystery word
    mysteryWord = wordList[randomIndex]

    #make blanks in a way that matches formatting w/ mysteryWord
    displayedLetters = []
    for i in range(len(mysteryWord)):
        displayedLetters += '_'

    lives = 7
    guessed = []
    print("Welcome to Guess the Word!")

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


def default():
    print("Error. I don't understand what you want. Try again.")


# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("""
Type 'calculator' to do some basic math calculations,
type 'kpop' to go to the Kpop Band Name Generator,
type 'rps' to play Rock, Paper, Scissors (unfinished),
type 'evenOrOdd' to check if a number is even or odd,
or type 'guessTheWord' to play a word-guessing game.
""")
        process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function. They need to be at the bottom of all of your programs.
if __name__ == "__main__":
  main()
