#imports the ability to get a random number (we will learn more about this later!)
from random import *
#static lists that apply to whole program for checking many user responses that share a single intent:
yesList = ['yes','yeah','sure','okay','ok','why not', 'why not?','yeet','yep','yup','si','affirmative','of course', 'definitively', 'definitely', 'always']
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
        #prints name acronym; I wanted it to be in the same line; it should work for any length name below the max
        print("\nHere is your band name:")
        #turns list of strings into one string; map({function},{sequence to apply function to})
        name_str = ' '.join(map(str, nameList))
        #Turns one string into acronym & prints
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
        while test_password[0].isalpha != True:
            test_password = input("\nThat doesn't start with a letter. Try again.\n").strip().lower()
        passwordUnknown = True
        #When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
        with open("mostCommonPasswords.txt","r") as f:
            for line in f:
                line1 = line.strip()

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

                    #checks for a password that is two words in text file, includes " " + [word], which is actually faster than looking for the single word in the file b/c " " comes first 
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
    print("Error. You userInput was not understood. Try again.")

# --- Put your main program below! ---
def main():
    userInput = input("Welcome to Katie's random collection of programs!\nWhat's your name?\n")
    print("\nHi, " + userInput +'!')
    while True:
        userInput = input("Type 'kpop' to go to the Kpop Band Name Generator,\n or type 'password' to test the strength of a password.").strip().lower()
        if userInput == "password":
            testPassword()
        elif userInput == "kpop":
            kpopNameGenerator()
        else:
            defaultError()

# DON'T TOUCH! Setup code that runs your main() function. They need to be at the bottom of all of your programs.
if __name__ == "__main__":
  main()