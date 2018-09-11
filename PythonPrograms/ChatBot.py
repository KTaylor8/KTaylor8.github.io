##imports the ability to get a random number (we will learn more about this later!)
from random import *
import time

def intro():
    print("I'm your personal chatbot, Billy Bob Joe Bob Joe the 18th.")
    print("What's your name?")
    answer = input()
    print("Hi, " + answer +'!')

def process_input(prompt):
    prompt = prompt.lower()
#ERROR HERE w/ referencing the greetingList
    greetingList = ["hi","hello","sup","hey","greetings",'yo']
    if greet(prompt, greetingList) == True:
        print(prompt, ' back!')
    else:
        print("Greeting error!")
    elif prompt == "calculator":
        calc()
    elif prompt == "kpop":
        kpopNameGenerator()
    elif prompt == "rps" or prompt == "rock paper scissors":
        rps()
    elif prompt == "evenorodd":
        num = input("Give me a number and I'll check to see if it's even!: ")
        print(is_even(int(num)))
    elif prompt == "guessTheWord":
        guessTheWord()
    else:
        default()

def greet(user_greeting, greetingList):
    return(user_greeting in greetingList)

def calc():
    print("Would you like to do summation (+), subtraction (-), multiplication (*), or division (/)?")
    answer = input()
    #summation
    if answer == '+':
        intList = []
        answer = "yes"
        int = input("Type the first number in the summation: ")
        intList.append(float(int))
        while answer != 'no':
            int = input("Type a number to add: ")
            intList.append(float(int))
            answer = input("""Do you want to add another number?
(Type 'no' when ready to calculate)
""")
        sum = summation(intList)
        print("Here's your sum:", sum)

    elif answer == '-':
        num1 = input("1st number: ")
        num2 = input ('2nd number: ')
        print(float(num1) - float(num2))

    elif answer == '*':
        num1 = input("1st number: ")
        num2 = input ('2nd number: ')
        print(float(num1) * float(num2))

    elif answer == '/':
        num1 = input("Dividend: ")
        num2 = input ('Divisor: ')
        print(float(num1) / float(num2))

    else:
        print("Error")

def summation(numList):
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
    return sum

def kpopNameGenerator():

    wordList = ["Best", "Quality", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]

    print("""
Welcome to the Kpop band name generator!""")
    answer = "yes"

    while answer != "no":
        #creates empty list for name
        name = []
        print ("""
Do you want to generate a new group name? ('yes' or 'no')""")
        answer = input()
        answer = answer.lower()
        if answer == 'yes':
            #chooses reasonable name length
            while len(name) < randint(3,7):
                #chooses name parts (doesn't show) w/o repeating words; first Generates a random integer to choose words.
                randIndex = randint(0, len(wordList)-1)
                if wordList[randIndex] not in name:
                    name.append(wordList[randIndex])
            #prints name acronym (tuple?); I wanted it to be in the same line; it should work for any length name below the max
            print("""
Your band's name is ready!:""")
            #turns list strings into one string; map({function},{sequence to apply function to})
            name_str = ' '.join(map(str, name))
            #Turns one string into acronym & prints (I don't 100% understand how it works)
            print(''.join(i[0] for i in name_str.split() if i[0].isupper()))
            #apparently this also works but idk why: print(''.join(x[0] for x in name_str.split()))
            print("""
This stands for...""")
            #prints full form of acronym
            print(name_str)

        elif answer == 'no':
            print("That's boring. :( Good bye. \n")
            break

        else:
            print(answer, "Error! You got no jams.")

def rps():
    answer = ("Do you want to play Rock Paper Scissors? ('yes' or 'no')")
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

def is_even(num):
    return num % 2 == 0

def default():
    print("Error. I don't understand what you want. Try again.")


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
            print("""
    This is your last life.
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
