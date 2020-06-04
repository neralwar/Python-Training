def generatorfunc(): #Lambda functional generator generates values
    for i in range(10):
     yield (lambda a:a*2)(i)

for value in generatorfunc():
    print(value)

help()
