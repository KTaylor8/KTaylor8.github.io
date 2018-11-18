print("Can your password survive a dictionary attack?")

redoWords = ["yes","yeah","sure","correct","indeed","okay","ok","yep","yeet","ye"]
redo = "yes"
#Write logic to see if the password is in the dictionary file below here:
while redo in redoWords:
    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type a trial password that starts with a letter: ").strip().lower()
    passwordUnknown = True
#When the "with" statement finishes, the text file closes and so you can start on the first line on the next iteration
    with open("commonPasswords.txt","r") as f:
        for line in f:
            line1 = line.strip()
            if line1 == test_password:
                print("\nYour password (",test_password,") is weak; it's too common.")
                passwordUnknown = False
                break #breaks out of nearest loop
            #checks if password entered is real word + # up to current year (range needs to be 1 more than year)
            if line1 in test_password:
                for i in range(2019):
                    lineNum = line1 + str(i)
                    if lineNum == test_password:
                        print("\nYour password (",test_password,") is weak; it's too common.")
                        passwordUnknown = False
                        break #breaks out of nearest loop
            #checks for a password that is two real words
            if line1 in test_password:
                with open("commonPasswords.txt","r") as f:
                    for line in f:
                        line2 = line.strip()
                        line12 = line1 + line2
                        if line12 == test_password:
                            print("\nYour password (",test_password,") is weak; it's too common.")
                            passwordUnknown = False
                            break #breaks out of the nearest loop it's in

    if passwordUnknown == True:
        print("\nGood! Your password is strong.")

    redo = input("Do you want to test another password?: ").strip().lower()
    print("")

print("Program complete.")
