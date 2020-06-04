from itertools import permutations

def allPermutations(str): 
       
     # Get all permutations of string 'ABC' 

     print(list(permutations(str)))
     permList = permutations(str)

     #print(list(permList))

     # print all permutations 
     for perm in list(permList): 
       print (''.join(perm)) 


allPermutations('Ash')



