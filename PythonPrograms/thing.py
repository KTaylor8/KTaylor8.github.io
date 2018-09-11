def greeting(name):
    print ("Hi, " + name + "!")

def is_even(num):
    return num % 2 == 0

def calc_total(intList):
    sum = 0
    for i in range(len(intList)):
        sum += intList[i]
    return sum

def main():
    answer = input("What's your name? ")
    greeting(answer)

    num = input("Give me a number and I'll check to see if it's even!: ")
    print(is_even(int(num))

    intList = []
    answer = "yes"
    while answer != 'no':
        int = input("Type a integer to add: ")
        intList.append(int(int))
        answer = input("""Do you want to add another number?
(Type 'no' when ready to calculate)
""")
    sum = calc_total(intList)
    print("Here's your sum:", sum)


if __name__ == "__main__":
    main()
