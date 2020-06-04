#In Python Exception handling is done by Try Except Else

#Finally if specificed (optional) executed in any case

try:
    #raise Exception('A very specific bad thing happened.') #Raising the error
    x = 10
    y = 0
    z = x/y

except Exception as e:

    print(e)

except ZeroDivisionError:
    print("Specific Error")


else:
    print("No Error")
finally:
    print("finally- Ashish Neralwar")
    




    