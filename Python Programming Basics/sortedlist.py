list1 =[555555,6666,44,44,1,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9,9]

revisedlist = set()

for i in list1:
    if i not in revisedlist:
        revisedlist.add(i)



print(revisedlist)

