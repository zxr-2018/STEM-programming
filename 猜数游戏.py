import random
import sys
import time
time =1
while time == 1:
    secret = random.randint(1,99)
    guess = 0
    tries = 0
    print("Hello!My name is Xirui Zhu ,\nand I have a guess game.\n ")
    print("It is a number from 1  to 99.   I will give you 8 tries.\n ")
    name = raw_input("What's your name?")
    print("\n")
    while guess != secret and tries < 8:
        tries = tries + 1
        guess = input("What's your guess, "+ name + " ?")
        print"\n"
        if not guess : break
        if guess < secret:
            print('The '+ str(guess) + " was too low, try again! Spend " + str(tries) + " times.")
            print"\n"
        elif guess > secret:
            print('The '+ str(guess) + " was too high, try again! Spend " + str(tries) + " times.")
            print"\n"
    if guess == secret:
        print("Great! " + name +", you are win!")
        print"\n"
    else :
        print"Sorry," + name + ", you are fail. The number is ", + secret
        print"\n"
    would = raw_input("Whould you want play again?(Y/N)")
    if would == 'Y' or would == 'y':
       print"OK! Please wait.",
    else:sys.exit()
    print("\n\n\n\n\n\n\n\n----------------------------------------------------")
