# Python List vs Python Tuple

#Python list is ordered and changeble
# We can edit python list and it is slow compare to tuple
#We can't edit python tupes and it is fast compare to list

#Python List
pythonlist = ["Ashish","Name","Salary"]
print(pythonlist) # Print the list
print(pythonlist[1])#print the element index start 0
print(pythonlist[-1])#Reverse Print . Print last element
print(pythonlist[0:2])#Print element with index starting with 0 . Exclude uperbound

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #Print element 4 element
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

if "Ashish" in pythonlist:
    print ("Name present in the list")

print(len(pythonlist))




#del(pythonlist(len(pythonlist)-2)




#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)


#Python Tuple


mytuple = ("Ashish","Ramesh","Neralwar")

print(mytuple) # Same as list
print(mytuple[1])
print(mytuple[-1])

#Joining the tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



