#comment
countDown = 5
print ("Hello, world!")
print ("My evil robot army's deployment is imminent!")
while (countDown != 0):
    print (countDown)
    countDown -= 1
print ("I will now take over the world! MWAHAHA!!")
answer = input ("Wait, is there pizza near you? I'm almost out of pizza energy...\n")
if (answer == "Yes" or answer == "yes"):
    print ("Ha! Then here I come!")
elif (answer == "No" or answer == "no"):
    print ("Argh you've foiled me! I need pizza!")
else:
    print ("Error! Eh I'll just stay here. No world domination today.")
