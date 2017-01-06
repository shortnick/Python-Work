#! python3
import os

TotalSize=0
folder = r'C:\Users\user\Documents\Python Data Structures Work\AutomateBoringStuff'
for filename in os.listdir(folder):
		if not os.path.isfile(os.path.join(folder, filename)):
			continue
		TotalSize = TotalSize + os.path.getsize(os.path.join(folder, filename))
print(TotalSize)