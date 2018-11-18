#doctest (used to check for errors using a behind-the-scenes sample run):
#"""
#>>>function(example args)
#expected return value
#"""

#important: if you want to print a succession of things in the same line:
#forever loop: print("string w/ looping variable", end=" ")
#this sets the print end character as a space rather than a default new line

#line cont. formatting: press enter, put a \ at the very end of the first line
#(no spaces can be after the \. Alt Z to toggle the word wrap to check)
#wildcard imports using * should be avoided
#imports the ability to get a random number:
from random import randint 
#imports stuff that lets you manipulate flow time of program:
import time 
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
    calcTypeList = ['addition','subtraction','multiplication',
                  'division','averages']
    while doAgain in yesList:
        calcChosen = input(
            '\nChoose one of the following calculations:'
            f"{', '.join(map(str, calcTypeList))}."
            'This calculator will only take single numbers,'
            "not expressions, when 'a number' is requested."
        ).strip().lower()

    # while doAgain in yesList:
    #     calcChosen = input(f"\nChoose one of the following calculations: {', '.join(map(str, calcTypeList))}. This calculator will only take single numbers, not expressions, when 'a number' is requested.").strip().lower()

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
    #try executes a block of code but if it doesn't work, it doesn't print an error and goes to the except block instead:
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
#range(#) starts @ 0 and approaches but doesn't reach 2. There're 2 iterations:
            for x in range(2): 
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
    #doctest:
    """
    >>> calculate('averages', [3,4,4,1])
    3.0

    """
    currentNum = numList[0]
    if calcType == 'addition' or 'averages':
    #range(inclusive start, exclusive end, step size):
        for i in range(1, len(numList)): 
            currentNum += numList[i]
        if calcType == 'averages':
            currentNum = currentNum/(len(numList))
    elif calcType == 'subtraction':
        for i in range(1, len(numList)):
            currentNum -= numList[i]
    elif calcType == 'multiplication':
        for i in range(1, len(numList)):
            currentNum *= numList[i]
    elif calcType == 'division':
        for i in range(1, len(numList)):
            currentNum /= numList[i]
    return currentNum

def kpopBandNameGenerator():
    doAgain = 'yes'
    possibleWordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic",
                        "Mystical", "Awesome", "Super"]
    while doAgain in yesList:
        nameList = []
        #chooses reasonable name length
        while len(nameList) < randint(3,7):
            #chooses name parts (doesn't show) w/o repeating words:
            randIndex = randint(0, len(possibleWordList)-1)
            if possibleWordList[randIndex] not in nameList:
                nameList.append(possibleWordList[randIndex])
        nameStr = ' '.join(map(str, nameList)) 
#^Purpose: turns list of strings into one string;  #map({function data type},{sequence to apply function to}) 
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

        while user != 'rock' and user != 'paper' and user != 'scissors': #error check for responses other than rock, paper, or scissors:
            user = input(f"Error! Type your choice again.\n").strip().lower()

        if user == "rock":
            user_num = 1
        elif user == "paper":
            user_num = 2
        elif user == "scissors":
            user_num = 3

        #computer chooses; 2 == scissors, 3 == paper, 4 == rock:
        computer = randint(2,4) 

        print("\nRock")
        #time.sleep(sec) pauses program for that number of seconds:
        time.sleep(1) 
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
    possibleWordList = ("thaumaturgy", "serendipity", "prestidigitation",
                        "thorough", "rhythm", "squirrel")

    while doAgain in yesList:
        lives = 6
        guessedList = []
        #Generates random index location to select the mystery word:
        randomIndex = randint(0, len(possibleWordList)-1) 
        mysteryWord = possibleWordList[randomIndex]

        #make blanks in a way that matches number of letters in mysteryWord:
        displayedLetters = []
        blank = "__"
        for i in range(len(mysteryWord)): 
            displayedLetters.append(blank)
        
        while lives > 0:
            guessedStr = ' '.join(guessedList[i] for i in range(len(guessedList)))
            display = ' '.join(displayedLetters[i] for i in range(len(displayedLetters)))
            if lives == 6:
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
                    #if guess is in mysteryWord at index i, replaces the displayed _ at index i w/ the guess:
                    if guess == mysteryWord[i]: 
                        displayedLetters[i] = guess
                #if no more _ displayed: win, break out of loop & end program:
                if blank not in displayedLetters: 
                    #to justify a string (r for right or l for left):
                    #[string].rjust([width],'[single separator]')
                    #replace rjust with center to put between separator
                    print(
                        "".rjust(72, '~'), #just wanted to try .rjust()
                        f"\n{mysteryWord}\n"
                        "Congratulations! You won!"
                    )
                    break
            
            #guess not in mysteryWord:
            else: 
                #if user inputted more than one letter (no penalty):
                if len(guess) > 1: 
                    print(
                        "That was more than one letter,"
                        "but you won't be penalized. Try again."
                    )
                #letter was previously guessed:
                elif guess in guessedList: 
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
                            "".rjust(72, '~'),
                            "\nGame over! You lost."
                            f"\nThe word was {mysteryWord}."
                        )
        doAgain = doAgainCheck("\nDo you want to guess a new mystery word?\n")

def testPassword():
    doAgain = 'yes'
    while doAgain in yesList:
        #.strip() strips whitespace and new lines from the file and passwords:
        userPassword = input(
            f"\nType a trial password that starts with a letter\n"
        ).strip().lower() 
        #.isalpha() checks if the characters in a string are all letters:
        while userPassword[0].isalpha() != True: 
            print(f"{userPassword[0]} starts")
            userPassword = input(
                f"\nThat doesn't start with a letter. Try again.\n"
            ).strip().lower()
        passwordUnknown = True
        #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration:
        with open("mostCommonPasswords.txt","r") as f: 
            for line in f:
                line1 = line.strip()

    #checks if password entered is line in text file + # up to current year:
                if line1 in userPassword: 
                    for i in range(2019):
                        lineNum = line1 + str(i)
                        if lineNum == userPassword:
                            print(
                                f"\nYour password ({lineNum}) is weak;"
                                "putting a number after a common password"
                                "does not make it strong."
                            )
                            passwordUnknown = False
        #breaks out of the second for loop going through the text file lines:
                            break 
                    if passwordUnknown == False:
         #breaks out of the first for loop going through the text file lines:
                        break 

#checks for a password that is two words in text file, include " " + [word]; actually faster than looking for single word/line in file b/c " " comes first: 
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
        #breaks out of the second for loop going through the text file lines:
                                break 
                    if passwordUnknown == False:
        #breaks out of the first for loop going through the text file lines:
                        break 

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
#str.format() string format: '{position:#ofSpaces.precision type}'.format(tuple of things to substitute) 
# ex: print('{0:8.2f}'.format(4.059))  prints:    4.06
# positions default to corresponding indices in ()
#'{variable}'.format(variable = __) also works

#fstring string format: f'string w/ {variables/expressions}'
#ex below:
#dogs = ['terrier', 5.3, 9]
#print(f'Number {int(4/2)} {dogs[0]} {dogs[1]} {dogs[2]} wow')
#prints:  Number 2 terrier 5.3 9 wow

#more formatting: f'{[num]:[width].[decimal precision][type (if converts)]}'
#if num is already an integer, you can just do :[width]
#e.g. f'{8.01888:6.2f}' == '  8.01'
#types: %s = string, %d = integer, %f = float (# of decimals: %.{#}f)

    print(f'\nHi, {userName}!') 
    while True:
        userInput = input(
            "Type 'math' to do some basic math calcs,"
            "type 'kpop' to go to the Kpop Band Name Generator,"
            "type 'rps' to play Rock Paper Scissors,"
            "type 'guessTheWord' to play a word-guessing game,"
            "type 'password' to test the strength of a password,"
            "or type 'quit' to end the program.\n"
        ).strip().lower()

        if greet(userInput, greetingList) == True:
            greetBack = f'{userInput}!'
            #makes letters spaced out stylistically
            print(
                f"{' '.join(greetBack[i] for i in range(len(greetBack)))}"
            )
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
    import doctest
    doctest.testmod()
    main()