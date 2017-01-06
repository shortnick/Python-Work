#! python3

import xlrd, bs4, requests, sys, re
#http://stackoverflow.com/questions/3597480/how-to-make-python-3-print-utf8
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False); 

spells = []
fileName = r'C:\Users\user\Documents\Warlock Spells.xls'
wb = xlrd.open_workbook(fileName)
#bob = wb.sheet_names()
#print(wb)
#print(bob)

sheet = wb.sheet_by_index(1)

#cell(y,x), where y is how many rows down, x how many columns over
#print(sheet.cell(3,0).value) 

for i in range(1,sheet.nrows):    
	spells.append(str.lower(sheet.cell(i,0).value))

for i,s in enumerate(spells):
	spells[i]=str.replace(s, " ", "-")


#open webpage
res = requests.get('https://www.dnd-spells.com/spells',
	headers={ "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" })

res.raise_for_status()


soup= bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.find_all('tr')
pursueAddy = []

def regexNpursue(goAfterTheseList,bs4In,searchTerms):
	#takes output list, BeautifulSoup object, list of strings
	#if searchTerm item is in BS4 hyperlink, link is appended to ouput list
	for i,s in enumerate(bs4In):
		address = re.compile(r'<a href=\"(.+)\" ')
		holder=str(bs4In[i].find('a'))
		obj = address.findall(holder)
		if len(obj) > 0:
			for i in searchTerms:
				if i in obj[0]:
					goAfterTheseList.append(obj[0])
		else:

			pass
	#print(goAfterTheseList)

regexNpursue(pursueAddy, elems, spells)


#open webpage
res = requests.get(pursueAddy[1],
	headers={ "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" })

res.raise_for_status()


soup= bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.find_all('p','.col-md-12')
print(elems)
#follow address, pull that page, take spell details 

#put details in columns of .xls


#wb.save(file)