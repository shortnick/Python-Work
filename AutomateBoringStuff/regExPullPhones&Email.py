#! python 3

import re, pyperclip

#TODO regex for phone nums
phoneRegex = re.compile(r""" 
# with/without area code, parenthetical area code or dashed in
(			#open paren for total group
((\d\d\d)|(\(\d\d\d\)))? #area codes, optional
(\s|-|\.) #separators
\d\d\d #phone prefix
(-|\s|\.)		#separators
\d\d\d\d #last 4 phone digits
((ext(\.)?\s?|x)?	#optional extension
(\d{2,5}))?		#optional extension numbers
) # close paren for total group
""", re.VERBOSE)
#TODO regex for emails
emailRegex = re.compile(r"""
[a-zA-Z0-9_.+]+ #chars for name/address, 
				#all alphanumeric plus the last three symbols
@				#separator
[a-zA-Z0-9_.+]+ #domain name chars
""", re.VERBOSE)


# TODO Get text from clipboard
text = pyperclip.paste()

#TODO Extract regex objs from text
extractPhone = phoneRegex.findall(text)

allPhoneNumbers = []
for PhoneNumber in extractPhone:
	allPhoneNumbers.append(PhoneNumber[0])

extractEmail = emailRegex.findall(text)
#TODO Copy extracts to clipboard
results = '\n'.join(allPhoneNumbers)+'\n' + '\n'.join(extractEmail)

pyperclip.copy(results)