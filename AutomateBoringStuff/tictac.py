import pprint

theBoard = {'top-l':' ', 'top-m':' ', 'top-r':' ', 
'mid-l':' ', 'mid-m':' ', 'mid-r':' ', 
'low-l':' ', 'low-m':' ', 'low-r':' '}

def printBoard(printme):
	pprint.print(printme('top-l')+'|'+printme('top-m')+'|'+printme('top-r'))
	pprint.print('-----')
	pprint.print(printme('mid-l')+'|'+printme('mid-m')+'|'+printme('mid-r'))
	pprint.print('-----')
	pprint.print(printme('low-l')+'|'+printme('low-m')+'|'+printme('low-r'))


