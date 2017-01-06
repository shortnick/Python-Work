#This is a guess the number game
import random

print("Hi! What's your name?")
name = input()

print("Ok,"+name+", I'm thinking of a number between 1 and 20. What is it?")
sekritNum = random.randint(1,20)



for guesses in range(1, 7):
	print("Take a guess.")
	attempt = int(input())

	if attempt < sekritNum:
		print("That was too low.")
	elif attempt > sekritNum:
		print("That was too high.")
	else:
		break # for correct guess

if attempt == sekritNum:
	print("Good job," + name+ "! You guessed my number in "+str(guesses)+" guesses.")
else: 
	print("Ooooo, sorry "+name+". I was thinking of "+str(sekritNum)+".")
