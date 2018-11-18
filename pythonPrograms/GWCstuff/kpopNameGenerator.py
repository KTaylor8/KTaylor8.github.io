def main():
    #isupper() checks whether letters in string are upper case
    #imports the ability to get a random number (we will learn more about this later!)
    from random import *
    #Create the list of words you want to choose from
    #(I need to do some fixing with grammar by making order rules for parts of speech)
    wordList = ["Best", "Quality", "Idol", "Perfect", "Ubiquitous", "Majestic", "Mystical", "Awesome", "Super"]

    print("""
Welcome to the Kpop band name generator!""")

    while True:
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
            print("That's boring. :( Good bye.")
            break

        else:
            print("Error! You got no jams.")

# DON'T TOUCH! Setup code that runs your main() function. They need to be at the bottom of all of your programs.
if __name__ == "__main__":
  main()
