#Name: Starbuzz.py

import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
text = page.read().decode("utf8")

hit=text.find("html")
print(int(hit))
print(text[int(hit):(int(hit)+200)])
