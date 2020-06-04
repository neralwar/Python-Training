def getMissingNo(A):
    B=A
    A.sort()
    lastelmindex=len(A)-1

    for i in range(1,A[lastelmindex]):
        if i not in B:
            print(i)
    
    #n = len(A) 
    #total = (n + 1)*(n + 2)/2
    #sum_of_A = sum(A) 
    #return total - sum_of_A 
  
# Driver program to test the above function 
A = [1,15,2,6,4,9,11,3,5,7,8,10,12,13] 
miss = getMissingNo(A) 
