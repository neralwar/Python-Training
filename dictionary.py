import re
#Python Dictionary
dictionary={'Country':'India','Capital':'Delhi','PM':'Modi'}
print(dictionary['Country'])
print(dictionary)

#print(split('words', 'Words, words , Words'))

print(re.split('a',"Ashish Neralwardddd"))  #split string based on the charactors

print(re.sub('ash',"XXX","Neralwarash")) #Find and Replace

print(re.subn('ner',"XXX","neralwarner",2)) #Find and Replace .Number of replacement depends of number of instances to replace 

