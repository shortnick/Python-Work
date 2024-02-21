import random


success=0
tries=3
secretNumber=random.randint(0,10)
while tries>0:
    g=input("Guess the number:")
    tries=tries-1
    guess=int(g)
    if guess==secretNumber:
        success=1
        print("You win. Congrats!")
        exit()
    elif secretNumber-guess<=0:
        print("That's too high.")
    else:
        print("That's too low.")
print("Ooooo. Wrong again. Too many guesses. Sorry!")  
