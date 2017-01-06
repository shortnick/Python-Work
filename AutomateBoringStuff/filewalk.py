#! python3
import os
bob = os.getcwd()
for folderName, subFolders, filenames in os.walk(bob):
	print('The folder is '+folderName)
	print('Containing '+'\n'.join(subFolders))
	print('Containing '+ '\n'.join(filenames))

"""
for subFolder in subFolders:
	if 'fish' in subFolder:
		os.rmdir(subFolder)

for file in filenames:
	if file.endswith('.py'):
		shutil.copy(os.join(folderName,file), os.join(folderName,file+'.backup'))
		"""