#! python3
import re

message = "Hello my name is bob. You've got my machine. My cell is 222-896-5555 if you need me urgently."

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo =phoneNumRegex.search(message)
#can also use phoneNumRegex.findall(message)
print("Found number "+mo.group())

batRegex= re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search ("Batmobile lost a wheel when Batgirl lost control.")

print(mo.group())