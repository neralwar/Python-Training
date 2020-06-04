def factorial(n):
    if n == -1:
        return 0
    elif n==0:
        return 1
    else:
        fact = 1
        while(n>1):
            fact = fact * n
            n=n-1
        return fact

def factorial1(n): 

    return 1 if (n==1 or n==0) else n * factorial1(n - 1)

factans = factorial(3)
print(factans)

factans = factorial1(3)
print(factans)







