#! python3

import csv, bs4, requests, sys, re

#http://stackoverflow.com/questions/3597480/how-to-make-python-3-print-utf8
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False); 

spells = [] #basis of search/scrape, pulled from spreadsheet
fileName = r'C:\Users\user\Documents\xxxxxxx.xls' # the spreadsheet
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

takenSpells.append(make_spell('Hurting','0','cOMBAT','ALLMINUTES','WORLDS','ELECTICAL','TIMELESS','IT HURTS!!'))

csvFile = open('WarlockSpells.csv','r', newline='')
reader = csv.reader(csvFile)
output= open('WarlockGrimoire.csv','w', newline='')
writer = csv.writer(output, delimiter=',', lineterminator='\n')

temp=[]
for x in takenSpells:
	for y in ['lvl', 'school', 'castTime', 'range_', 'components',	'duration', 'desc']:
		temp.append(x.y)
	print(temp)	
	'''
       for row in csvRows:
           csvWriter.writerow(row)
       csvFileObj.close()
'''

		#name, lvl, school, castTime, range_, components, duration, desc

