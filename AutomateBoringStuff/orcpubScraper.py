#! python3

import xlrd, xlwt, bs4, requests, sys, re

#http://stackoverflow.com/questions/3597480/how-to-make-python-3-print-utf8
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False); 

spells = [] #basis of search/scrape, pulled from spreadsheet
fileName = r'C:\Users\user\Documents\Warlock Spells.xls' # the spreadsheet
ends=[] # will be website subaddress of spell page
spelladdy= []# will contain actual webaddresses of spells
takenSpells = [] # spellObj place holder



class spellObj(object):
	name = ''
	lvl = ''
	school = ''
	castTime = ''
	range_ = ''
	components = '' 
	duration= ''
	desc = ''

	def __init__(self, name, lvl, school, castTime, range_, components, duration, desc):
		self.name = name
		self.lvl = lvl
		self.school = school
		self.castTime = castTime
		self.range_ = range_
		self.components = components
		self.duration = duration
		self.desc = desc

def make_spell(name, lvl, school, castTime, range_, components, duration, desc):
    name = spellObj(name, lvl, school, castTime, range_, components, duration, desc)
    return name



wb = xlrd.open_workbook(fileName)
sheet = wb.sheet_by_index(1)
#cell(y,x), where y is how many rows down, x how many columns over
#print(sheet.cell(3,0).value) 

for i in range(1,sheet.nrows):    
	spells.append(str.lower(sheet.cell(i,0).value))


for i,s in enumerate(spells):
	spells[i]=str.replace(s, " ", "-")


def getSpells(productUrl):
	#set user-agent to get around bot/scraping filters
	#http://docs.python-requests.org/en/master/user/quickstart/
	res = requests.get(productUrl,
		headers={ "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" })

	res.raise_for_status()
	''' Example of a single item of things trying to parse on this page:
	<a href="/dungeons-and-dragons/5th-edition/spells/wind-wall"><div class="lv-item media">
	<div class="pull-left"><span class="list-image-fallback media-object">WW</span></div>
	<div class="lv-title p-t-10" itemProp="itemListElement" itemScope="itemScope" itemType="http://schema.org/ListItem">
	<div><strong itemProp="name">Wind Wall</strong></div><em>Evocation</em><meta content="303" itemProp="position" />
	<link href="/dungeons-and-dragons/5th-edition/spells/wind-wall" itemProp="url" /><span class="m-l-5">3</span></div></div>
	'''

	soup= bs4.BeautifulSoup(res.text, 'lxml-xml') #can replace string with 'lxml' for fast/lenient html, 'lxml-xml' for xml
	#print(res.text)
	#{"data-reactid": re.compile("\.a\.2\.3\.0\.0\.1:\$.+\d")} <<<for whatever reason, none of the parsers are reading react elements
	elems = soup.find_all(itemProp="url")
	
	for i in elems:
		ends.append(str(i).split()[1][47:-1])#converts item into string, splits on space, grabs 2nd element, strips to just final / portion
	del ends[0]
	#print(ends[0:10])
	#print(spells)
	for s in spells:
		if s in ends:
			spelladdy.append("http://www.orcpub.com/dungeons-and-dragons/5th-edition/spells/"+s)
	

	for i in range(0,len(spelladdy)):
		spellChars=[]
		res = requests.get(spelladdy[i],
			headers={ "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" })
		page = bs4.BeautifulSoup(res.text,'lxml-xml')
		

		spellChars.append(str.replace(spelladdy[i][62:], "-", " "))
		chas = page.find_all(class_="m-b-10")
		spellChars.append(chas[1].string[0])#gets spell level
		spellChars.append(chas[1].string[10:])# and school
		
		bob = page.find_all(class_="m-l-5")
		for i in range(1,len(bob)):
			spellChars.append((bob[i].string))# gets casting time, range, components, and duration

		dylan = page.find(class_="description-paragraph").string #gets spell description
		spellChars.append(dylan)
		
		#print(len(spellChars))
		#print(spellChars)
		takenSpells.append(make_spell(*spellChars))

	for i in takenSpells[0:10]:
		wbWrtr = xlwt.Workbook(fileName)
		sheet = wb.sheet_by_index(1)
		row = str(takenSpells.index(i)+2)
		#zip together as dict, use with dir(takenSpells[2])
		colsUsed = ['B','C','D','E','F','G','H']
		colNames = ['lvl', 'school', 'castTime', 'range_', 'components', 'duration', 'desc']
		destinations = dict(zip(colNames,colsUsed))
		for n in colNames:
			#destinations[str(n)]+row
			#i.n doesn't get passed around right
	
	
	#match i in takenSpells with rows in .xls (+2 offset)
	#write each element of spell into cell (same row, increasing col)
	#save sheet

		

getSpells('http://www.orcpub.com/dungeons-and-dragons/5th-edition/spells')
