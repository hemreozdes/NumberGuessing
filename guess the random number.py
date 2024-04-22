import random
guess=-1
i=0
pcnum=random.randint(1,99)
while(guess!=pcnum):
    guess=int(input("Your guess: "))
    i=i+1
    if(guess>pcnum):
        print("You must enter smaller number!")
    if(guess<pcnum):
        print("You must enter bigger number!")
print("You got it on the %d. guess"%i)