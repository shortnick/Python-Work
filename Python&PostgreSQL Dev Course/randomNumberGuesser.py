#! python3 

import random 



def askAndCheckfunc():
	user_number=int(input("Enter a number from 0 to 9 --  "))
	if user_number not in magic_numbers:
		return "Your number is not in here. \n"

	else:
		return "Congrats! That's the number."

def runGuessesXtimes(repetitions):
	for attempt in range(repetitions):
		print("Atttempt {} of {}. \n".format(str(attempt+1), str(repetitions)))
		message = askAndCheckfunc()
		print(message)

magic_numbers=[random.randint(0,9),random.randint(0,9)]
chancesToGuess = int(input("How many guesses will you need to guess the correct number? Enter a number from 1 to 10.  "))

runGuessesXtimes(chancesToGuess)


"""

minimum = 100
for index in range(10):
	random_num = random.randint(0,100)
	print("The number generated is {}".format(random_num))
	if random_num <= minimum:
		minimum = random_num
	print("Minimum was {}".format(minimum))
"""	
