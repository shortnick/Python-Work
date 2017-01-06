def div42by(divider):
	try:
		return 42/divider
	except ZeroDivisionError:
		print("Error: Can't divide by 0.")
print(div42by(22))
print(div42by(42))
print(div42by(0))
print(div42by(100))

print("How many cats do you have?")
numCats = input()
try:
	if int(numCats)>=4:
		print("Woah. Lotta gatos you got there.")
	else: 
		print("That's not so many cats.")
except ValueError: 
	print("That wasn't a number.")
