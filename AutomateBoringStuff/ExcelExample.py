#! python3

import openpyxl, os

workingDir = os.getcwd()

workbook = openpyxl.load_workbook('example.xlsx')
#workbook.get_sheet_names() - returns all sheet titles
sheet1=workbook.get_sheet_by_name('Sheet1')
#equivalent calls follow this
currentCell = sheet1['C1']
currentCell = sheet1.cell(row=1, column=3) #counting starts @1!, not zero
#these both return a Cell Object.
# use cell.value to get what's inside the cell