#! python3

import xlrd, xlwt, bs4, requests, sys, re

#http://stackoverflow.com/questions/3597480/how-to-make-python-3-print-utf8
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False); 

spells = [] #basis of search/scrape, pulled from spreadsheet
fileName = r'C:\Users\user\Documents\xxxxxx.xls' # the spreadsheet
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


takenSpells.append(make_spell('Banishment', '4', 'proj', '2 min', '10 feet', 'VSM', ' hours', 'blah balh blah blah'))

takenSpells.append(make_spell('Astral Projection', '4', 'proj', '2 min', '10 feet', 'VSM', ' hours', 'blah balh blah blah'))
for i in takenSpells[0:1]:
	wbWrtr = xlwt.Workbook(fileName)
	trythis= xlrd.open_workbook(fileName)
	gored = wbWrtr.sheet_by_index(0)
	row = takenSpells.index(i)+2
	#zip together as dict, use with dir(takenSpells[2])
	colsUsed = ['B','C','D','E','F','G','H']
	colNames = ['lvl', 'school', 'castTime', 'range_', 'components', 'duration', 'desc']
	destinations = dict(zip(colNames,colsUsed))
	for n in colNames:
		#print(getattr(i,n))
		#print(destinations[str(n)])
		
		gored.row(3).write(2,'B3')
		
		#i.n doesn't get passed around right

	
	#match i in takenSpells with rows in .xls (+2 offset)
	#write each element of spell into cell (same row, increasing col)
	#save sheet
