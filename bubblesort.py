#Bubble Sort

def bubblesort(itmelist):
  for i in range(len(itmelist)):  
    for i in range(0,len(itmelist)-i-1):
         if itmelist[i] > itmelist[i+1]:
             itmelist[i],itmelist[i+1] = itmelist[i+1],itmelist[i]
  print(itmelist)

listitem = [1,4,3,6,15,18,19,0,17]
bubblesort(listitem)