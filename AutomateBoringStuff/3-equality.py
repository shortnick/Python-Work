#! python3
import pyperclip, re

text = pyperclip.paste()

obj = re.compile(r'[A-Z]{2}\w[A-Z]{2}')

result = obj.search(text)

print(result.group())