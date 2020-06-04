#Linerat Search 
#Binary Search -- Sortted elements


#Items Sets for Linear Search
listitem = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

listitem.sort()


def binary_Search(listitem,itemkey):
    low=0
    high = len(listitem)
    
    print(listitem)
    
    while low <= high:
        mid = int((low+high)/2)
       
        if (listitem[mid] < itemkey):
     
            low=mid+1
     
        elif(listitem[mid] > itemkey):
     
            high=mid-1
     
        else:
            return mid
    return -1 


pos = binary_Search(listitem,10)

if (pos == -1):
    print("ITEM NOT FOUND")
else:
    print("ELEMENT FOUND AT POSITION--BINARY SEARCH")

