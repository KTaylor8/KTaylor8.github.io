# Update this text to match your story.
start = '''
You wake up one morning and find that you are lying in the grass in a small clearing.
You stand up and approach one of the three walls surrounding you.
A sign is hanging from the ivy: "You have one hour to get out of the maze. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print("""
start
""")


print("Type 'left' to go left or 'right' to go right. (Case-sensitive)")
user_input = input()

#leftRightErrorCheck
while (user_input != 'left' or 'right'):
    print ("Error! Re-enter your answer, and remember that this adventure is case-sensitive.")
    user_input = input()

#left
if user_input == "left":
    print("You decide to go left and ")

    while (input() != 'left' or 'right'):
        print ("Error! Re-enter your answer, and remember that this adventure is case-sensitive.")

    

#right
elif user_input == "right":
    print("You choose to go right and ...")
