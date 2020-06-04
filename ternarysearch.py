# Python3 program to illustrate 
# recursive approach to ternary search 
import math as mt 
  
# Function to perform Ternary Search 

ar =[1,4,2,5,2,4,2,4,5,4,5,6,7,7,8,8,9]
ar.sort()

l=1
r=len(ar)

print(r)

def ternarySearch(l, r, key, ar): 
  
    if (r >= l): 
  
        # Find the mid1 and mid2 
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
  
        # Check if key is present at any mid 
        if (ar[mid1] == key):  
            return mid1 
          
        if (ar[mid2] == key):  
            return mid2 
          
        # Since key is not present at mid, 
        # check in which region it is present 
        # then repeat the Search operation 
        # in that region 
        if (key < ar[mid1]):  
  
            # The key lies in between l and mid1 
            return ternarySearch(l, mid1 - 1, key, ar) 
          
        elif (key > ar[mid2]):  
  
            # The key lies in between mid2 and r 
            return ternarySearch(mid2 + 1, r, key, ar) 
          
        else:  
  
            # The key lies in between mid1 and mid2 
            return ternarySearch(mid1 + 1,  
                                 mid2 - 1, key, ar) 
          
    # Key not found 
    return -1


print(ternarySearch(l,r,3,ar))
   
   def bubblesort(itmelist):
       pass