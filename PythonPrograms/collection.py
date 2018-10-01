#line cont. formatting: press enter, put a \ at the very end of the first line
#(no spaces can be after the \. Alt Z to toggle the word wrap to check)
#wildcard imports using * should be avoided
from random import randint #imports the ability to get a random number (we will learn more about this later!)
import time #imports stuff that lets you manipulate flow time of program
#lists for checking many user responses that share a single intent:
greetingList = ["hi","hello","sup","hey","greetings",'yo','hola']
yesList = ['yes','yeah','sure','okay','ok','why not','yeet','yep','yup',
           'si','affirmative','of course','always']
noList = ['no','nope','not at all','absolutely not',"yesn't","yesnt",
          'negative','never','of course not']

def greet(user_greeting, greetingList):
    return(user_greeting in greetingList)

#function keeps asking until receives response in noList or yesList:
def doAgainCheck(doAgainQuestion):
    doAgain = 'yes'
    while True:
        doAgain = input(doAgainQuestion).strip().lower()
        if doAgain in yesList or doAgain in noList:
            return(doAgain)
        else:
            print(f"Error! Try again.")

def math():
    doAgain = 'yes'
    calcTypeList = ['addition', 'subtraction', 'multiplication',
                    'division', 'averages']
    while doAgain in yesList:
        calcChosen = input(
            "\nChoose one of the following calculations:"
            f"{', '.join(map(str, calcTypeList))}."
            "This calculator will only take single numbers,"
            "not expressions, when 'a number' is requested."
        ).strip().lower()
    
        while calcChosen not in calcTypeList:
            calcChosen = input(
                "\nThat's not an available calculation. Try again."
            ).strip().lower()

        while doAgain in yesList:
            numList = []
            numList.append(numCheck(input('\nType in the starting number.\n')))
            moreNumsCheck(calcChosen, numList)
            print(f"Here's your answer: {calculate(calcChosen, numList)}\n")
            doAgain = doAgainCheck(f"Would you like to do more {calcChosen}?")
        doAgain = doAgainCheck(
            "\nDo you want to do another math calculation of any sort?\n"
        )

#function checks if a string either starts with is a number:
def numCheck(num):
    #try executes a block of code but if it doesn't work, it doesn't print an error and goes to the except block instead
    while True:
        try: #checks that string can be in float form and thus is a number
            num = float(num)
        except ValueError:
            num = input(f"That's not a number. Type a number.\n")
        else:
            return(num)
        

def moreNumsCheck(calcChosen, numList):
    doAgain = 'yes'
    if calcChosen == 'addition':
        instruction = 'to add'
    elif calcChosen == 'subtraction':
        instruction = 'to subtract'
    elif calcChosen == 'multiplication':
        instruction = 'to multiply'
    elif calcChosen == 'division':
        instruction = 'to divide'
    elif calcChosen == 'averages':
        instruction = 'to include in the average'
    while doAgain in yesList:
        num = input(f'\nType in the next number {instruction}.\n')
        if calcChosen == 'division' and num == '0':
            for x in range(2): #range(#) starts @ 0 and goes up to but doesn't reach 2, although there are 2 iterations
                print("Warning")
                time.sleep(1)
            print(
                'You have started brush fires in eastern Washington.\n'
                'Do not try to divide by 0 again or they may spread west.'
            )
        else:
            numList.append(numCheck(num))
        doAgain = doAgainCheck('\nDo you have another number to include?\n')

def calculate(calcType, numList):
    currentNum = numList[0]
    if calcType == 'addition':
        for i in range(1, len(numList)): #range(inclusive start, exclusive end, step size)
            currentNum += numList[i]
    elif calcType == 'subtraction':
        for i in range(1, len(numList)):
            currentNum -= numList[i]
    elif calcType == 'multiplication':
        for i in range(1, len(numList)):
            currentNum *= numList[i]
    elif calcType == 'division':
        for i in range(1, len(numList)):
            currentNum /= numList[i]
    elif calcType == 'averages':
        for i in range(1, len(numList)):
            currentNum += numList[i]
        currentNum = currentNum/(len(numList))
    return currentNum

def kpopBandNameGenerator():
    doAgain = 'yes'
    possibleWordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic",                       "Mystical", "Awesome", "Super"]
    while doAgain in yesList:
        nameList = []
        #chooses reasonable name length
        while len(nameList) < randint(3,7):
            #chooses name parts (doesn't show) w/o repeating words; first generates a random integer to choose words.
            randIndex = randint(0, len(possibleWordList)-1)
            if possibleWordList[randIndex] not in nameList:
                nameList.append(possibleWordList[randIndex])
        nameStr = ' '.join(map(str, nameList)) #Purpose: turns list of strings into one string;  #map({function data type},{sequence to apply function to}) 
        #str.join(separator) returns string in which string elements of sequence are joined by str separator
        #str.split(separator) returns list of strings formed from breaking up the str string at the separators; default separator is whitespace 
        #in this case, returns string in which 1st element in every word in name_str is joined directly together (by nothing)
        acronym = ''.join(x[0] for x in nameStr.split())
        print(
            f'\nYour band name is ready!: {acronym}\n'
            f'This stands for {nameStr}.'
        )

        #function keeps asking until receives response in noList, but with special error responses:
        while True:
            doAgain = input(
                f"\nDo you want to generate another band name?\n"
            ).strip().lower()
            if doAgain in yesList:
                break
            elif doAgain in noList:
                print("That's boring. :( Good bye.")
                break #will also break from larger while loop b/c not in yesList
            else:
                print("Error! You got no jams. Try again.")

def rps():
    doAgain = 'yes'
    while doAgain in yesList:
        user = input(
            "\nChoose 'rock', 'paper', or 'scissors'.\n"
        ).strip().lower()

        while user != 'rock' and user != 'paper' and user != 'scissors': #error check for responses other than rock, paper, or scissors
            user = input(f"Error! Type your choice again.\n").strip().lower()

        if user == "rock":
            user_num = 1
        elif user == "paper":
            user_num = 2
        elif user == "scissors":
            user_num = 3

        computer = randint(2,4) #computer chooses; 2 == scissors, 3 == paper, 4 == rock 

        print("\nRock")
        time.sleep(1) #time.sleep(sec) pauses program for that number of seconds
        print("Paper")
        time.sleep(1)
        print("Scissors")
        time.sleep(1)
        print("Shoot!\n")
        time.sleep(0.3)

        if user_num + 1 == computer: #you lose
            if user_num == 1: #user == 'rock'
                print("Computer: paper")
            elif user_num == 2: #user == 'paper'
                print("Computer: scissors")
            elif user_num == 3: #user == 'scissors'
                print("Computer: rock")
            print ("\nYou lost!")

        elif computer == user_num: #tie
            print(f"Computer: {user}\nYou tied.")

        else: #you win
            if user_num == 1: #user == 'rock'
                print("Computer: scissors")
            elif user_num == 2: #user == 'paper'
                print("Computer: rock")
            elif user_num == 3: #user == 'scissors'
                print("Computer: paper")

            print ("\nYou won!")
        doAgain = doAgainCheck("\nDo you want to play again?\n")


def guessTheWord():
    doAgain = 'yes'
    possibleWordList = ("thaumaturgy", "serendipity", "prestidigitation",                          "thorough", "rhythm", "squirrel")

    while doAgain in yesList:
        lives = 7
        guessedList = []
        randomIndex = randint(0, len(possibleWordList)-1) #Generates random index location to select the mystery word
        mysteryWord = possibleWordList[randomIndex]

        displayedLetters = []
        blank = "__"
        for i in range(len(mysteryWord)): #make blanks in a way that matches number of letters in mysteryWord
            displayedLetters.append(blank)
        
        while lives > 0:
            guessedStr = ' '.join(guessedList[i] for i in range(len(guessedList)))
            display = ' '.join(displayedLetters[i] for i in range(len(displayedLetters)))
            if lives == 7:
                statusMessage = '\nYou have 7 lives to guess the mystery word.'
            elif lives == 1:
                statusMessage = (
                    f'\nThis is your last life.'
                    f'\nGuessed letters not in mystery word: {guessedStr}'
                )
            else:
                statusMessage = (
                    f'\nYou have {lives} lives left.'
                    f'\nGuessed letters not in mystery word: {guessedStr}'
                )
            guess = input(
                        f'{statusMessage}\n'
                        f'Mystery word: {display}\n'
                        'Guess a letter.\n'
                    ).strip().lower()
            if guess in mysteryWord:
                for i in range(len(mysteryWord)):
                    if guess == mysteryWord[i]: #if guess is in mysteryWord at index i, replaces the displayed _ at index i w/ the guess
                        displayedLetters[i] = guess

                if blank not in displayedLetters: #if no more _ displayed: win and break out of loop and program will end.
                    print(
                        f"{mysteryWord}\n"
                        "Congratulations! You won!"
                    )
                    break

            else: #if guess not in mysteryWord
                if len(guess) > 1: #if user inputted more than one letter (no penalty)
                    print(
                        "That was more than one letter,"
                        "but you won't be penalized. Try again."
                    )
                elif guess in guessedList: #if letter was previously guessed
                    print(
                        "You already guessed that letter,"
                        "but you won't be penalized. Try again."
                    )
                else:
                    lives -= 1
                    print(f"{guess} is not in the mystery word.")
                    guessedList.append(guess)
                    if lives == 0: #lost game; the while loop will end
                        print(
                            f"\nGame over! You lost."
                            f"\nThe word was {mysteryWord}."
                        )
        doAgain = doAgainCheck("\nDo you want to guess a new mystery word?\n")

def testPassword():
    doAgain = 'yes'
    while doAgain in yesList:
        userPassword = input(
            f"\nType a trial password that starts with a letter\n"
        ).strip().lower() #.strip() strips whitespace and new lines from the file and passwords
        while userPassword[0].isalpha() != True: #.isalpha() checks if the characters in a string are all letters
            print(f"{userPassword[0]} starts")
            userPassword = input(
                f"\nThat doesn't start with a letter. Try again.\n"
            ).strip().lower()
        passwordUnknown = True
        with open("mostCommonPasswords.txt","r") as f: #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
            for line in f:
                line1 = line.strip()
                # The commented out code is unnecessary b/c " " is being counted as a line, so any password that's a single common word is being caught as a double: " " + [word] 
                # if line1 == userPassword:
                #     print("\nYour password (",line1,") is weak; it's too common.")
                #     passwordUnknown = False
                #     break #breaks out of the first for loop going through the text file lines

                if line1 in userPassword: #checks if password entered is line in text file + # up to current year
                    for i in range(2019):
                        lineNum = line1 + str(i)
                        if lineNum == userPassword:
                            print(
                                f"\nYour password ({lineNum}) is weak;"
                                "putting a number after a common password"
                                "does not make it strong."
                            )
                            passwordUnknown = False
                            break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

                    #checks for a password that is two words in text file, include " " + [word], which is actually faster than looking for the single word in the file b/c " " comes first: 
                    with open("mostCommonPasswords.txt","r") as f:
                        for line in f:
                            line2 = line.strip()
                            line12 = line1 + line2
                            if line12 == userPassword:
                                print(
                                    f"\nYour password ({line12}) is weak;"
                                    "it's too simple for a program to crack."
                                )
                                passwordUnknown = False
                                break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

        if passwordUnknown == True:
            print("\nGood! Your password is strong.")

        doAgain = doAgainCheck("\nDo you want to test another password?\n")
        

def default():
    print("Error. I don't understand what you want. Try again.")

def main():    
    userName = input(
        f"Welcome to Katie's random collection of programs!\n"
        "What's your name?\n"
    )
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
        userInput = input(
            "Type 'math' to do some basic math calcs,"
            "type 'kpop' to go to the Kpop Band Name Generator,"
            "type 'rps' to play Rock Paper Scissors,"
            "type 'guessTheWord' to play a word-guessing game,"
            "type 'password' to test the strength of a password,"
            "or type 'quit' to end the program."
        ).strip().lower()
        
        if greet(userInput, greetingList) == True:
            greetBack = f'{userInput}!'
            print(
                f"{' '.join(greetBack[i] for i in range(len(greetBack)))}"
            ) #makes letters spaced out stylistically
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

#Setup code that runs main() function needs to be at bottom of all programs
if __name__ == "__main__":
  main()