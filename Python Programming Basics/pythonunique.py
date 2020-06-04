names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
newlist=names1+names2

mylist = list(dict.fromkeys(newlist))
print(mylist)
