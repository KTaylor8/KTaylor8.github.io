#imports the ability to get a random number (from [module] import [specific thing]); * means all functions and constants
from random import *
#static lists that apply to whole program for checking many user responses that share a single intent:
yesList = ['yes','yeah','sure','okay','ok','why not', 'why not?','yeet','yep','yup','si','affirmative','of course','definitely','always']
noList = ['no','nope', 'naw', 'not at all','absolutely not','definitely not',"yesn't","yesnt",'negative','never','of course not']

def kpopBandNameGenerator():
    doAgain = 'yes'
    wordList = ["Best", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]
    while doAgain in yesList:
        nameList = []
        #chooses name parts (doesn't show) that are added to the nameList to make a name of reasonable length
        while len(nameList) < randint(3,7):
            #first generates a random integer to choose words from wordList
            randIndex = randint(0, len(wordList)-1)
            #ensures no word repeating
            if wordList[randIndex] not in nameList:
                nameList.append(wordList[randIndex])
        #prints name acronym; it should work for any length name below the max
        print("\nHere is your band name:")
        #Purpose: turns list of strings into one string
        #map({function},{sequence to apply function to})
        name_str = ' '.join(map(str, nameList))
        #Purpose: Turns one string into acronym & prints
        #str.join(separator) returns string in which string elements of sequence are joined by str separator
        #str.split(separator) returns list of strings formed from breaking up the str string at the separators; default separator is whitespace 
        #x = # elements in in name_str string list from .split();     also, strings are lists of characters
        #in this case, returns string in which 1st element in every word in name_str is joined directly together (by nothing)
        print(''.join(x[0] for x in name_str.split()))
        print("\nThis stands for...\n", name_str)

        doAgain = doAgainErrorCheck("\nDo you want to generate another band name?\n")

def testPassword():
    doAgain = 'yes'
    while doAgain in yesList:
        #.strip() to strips whitespace and newlines from the file and passwords
        test_password = input("\nType a password that starts with a letter.\n").strip().lower()
        #checks if password starts with letter
        #strings are just lists of characters; .isalpha() checks if the characters in a string are all letters
        while test_password[0].isalpha() != True:
            test_password = input("\nThat doesn't start with a letter. Try again.\n").strip().lower()
        passwordUnknown = True
        #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
        with open("mostCommonPasswords.txt","r") as f:
            for line in f:
                line1 = line.strip()

                #checks if password entered is line in text file + # up to current year (range needs to be 1 more than year)
                if line1 in test_password:
                    #checks for a password that ends with a number < 2019
                    for i in range(2019):
                        lineNum = line1 + str(i)
                        if lineNum == test_password:
                            print("\nYour password (",lineNum,") is weak; putting a number after a common password does not make it strong.")
                            passwordUnknown = False
                            break #breaks out of the second for loop going through the text file lines
                    if passwordUnknown == False:
                        break #breaks out of the first for loop going through the text file lines

                    #checks for a password that is two words in text file, includes " " + [word],
                    #which is actually faster than looking for the single word in the file b/c " " comes first 
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
        for i in range(len(mysteryWord)):
            displayedLetters += '_'

        while lives > 0:
            #asks user to guess
            print(displayedLetters)
            if lives == 1:
                guess = input("This is your last life.\nHere are the letters you have guessed:",guessedList,"\nGuess another letter.").strip().lower()
            else:
                guess = input("\nYou have",lives,"lives to guess the word.\nHere are the letters you have guessed:",guessedList,"\nGuess another letter.").strip().lower()

            if guess in mysteryWord:
                #detect correct letter's index
                for i in range(len(mysteryWord)):
                    #detect if correct guessed letter is in this item in the list
                    if guess == mysteryWord[i]:
                        #replace letter: {listName.insert(index,item)}
                        del displayedLetters[i]
                        displayedLetters.insert(i,guess)

                #if no more _ displayed: win and break out of loop and program will end.
                if "_" not in displayedLetters:
                    print(mysteryWord,"Congratulations! You won!")
                    break

            #if guess not in mysteryWord
            else:
                #check if the user inputted more than one letter (no penalty)
                if len(guess) > 1:
                    print("That was more than one letter, but you won't be penalized. Try again.")
                else:
                    lives -= 1
                    #check if letter was previously guessed
                    if guess in guessedList:
                        print("You already guessed that letter.")
                    else:
                        print(guess,"is not in the mystery word.")
                        guessedList.append(guess)
                    #lost game; the while loop will end
                    if lives == 0:
                        print("\nGame over! You lost.\nThe word was",mysteryWord)
                        doAgain = doAgainErrorCheck("\nDo you want to guess a new mystery word?\n")

#keeps asking until receives response in noList or yesList
def doAgainErrorCheck(doAgainQuestion):
    doAgain = 'yes'
    while True:
        doAgain = input(doAgainQuestion).strip().lower()
        if doAgain in yesList or doAgain in noList:
            #after return breaks out of function definition: if in yesList, function will loop again, and if in noList it will not loop
            return(doAgain)
        else:
            defaultError()

def defaultError():
    print("Error. You answer was not understood. Try again.")

#main program
def main():
    userInput = input("Welcome to Katie's random collection of programs!\nWhat's your name?\n")
    print("\nHi, " + userInput +'!')
    while True:
        userInput = input("\nType 'kpop' to generate a kpop band name,\ntype 'password' to test a password's strength,\ntype 'guessWord',\nor type 'quit' to end the program.\n").strip().lower()
        if userInput == "password":
            testPassword()
        elif userInput == "kpop":
            kpopBandNameGenerator()
        elif userInput == "guessword":
            guessTheWord()
        elif userInput == 'quit':
            break
        else:
            defaultError()

#Setup code that runs your main() function. They need to be at the bottom of all of your programs.
#The main program starts if this file is the main file being run, rather than having been imported from another module (file consisting of Python code).
if __name__ == "__main__":
  main()