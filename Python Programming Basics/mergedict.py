from itertools import *

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for i in chain(list1,list2 ):
    print(i)