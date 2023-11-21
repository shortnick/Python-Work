#! python3

"""
sets - VAR = {a, b, c} or set() with the first for a populated example and the second for an empty set - only store unique values, and are unordered
adding an element that already exists in a set does nothing
"""

import random

def menu():
	userInput = getPlayerNumbers()
	generated = generateLottoNumbers()
	results(userInput,generated)


def getPlayerNumbers():
	number_csv = input("Pick 6 numbers from 1 to 20 and enter them, separated by commas. ")
	numberList= number_csv.split(",")
	guesses = {int(number) for number in numberList}
	return guesses

def generateLottoNumbers():
	winningNumbs = set()
	while len(winningNumbs)<6:
		winningNumbs.add(random.randint(1,20))
	return winningNumbs

def results(x,y):
	x=set(x)
	y=set(y)
	matches = x.intersection(y)
	ouptut={}
	if len(matches) == 0:
		output = "No matching numbers."
	else:
		output = matches
	#print("You guessed {}.".format(x))
	print("You matched {} numbers with the lottery drawing. {}".format(len(matches), output))
	print("Winning numbers were {} and you won ${}.".format(y,100**len(matches)))


menu()

#print(winningNumbs.intersection(guesses))