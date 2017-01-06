#! python3

import webbrowser, sys, pyperclip
sys.argv # 'mapit.py', '870', 'Valencia', 'St.'
#these are passed in from command line, each space breaks into new string

#Check if comand line arguments were passed
if len(sys.argv) > 1:
	address = '+'.join(sys.argv[1:]) #creates string, with spaces of things following .py element
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place'+address)

