print((lambda x,y,z,c : x+y*z*c)(1,2,3,4))

#Python lambda function are anonymus
#It can take any number of arguments but single expression or statement
#No return value
#Lambda functions are inline

#Application of Lambda function

#Filter Function along with Lambda function inline

ages = [5, 12, 17, 18, 24, 32]
adults = list(filter(lambda x: x < 18 , ages))
print(list(filter(lambda x: x < 18 , ages)))
print(adults)

#map() functional applies to  each item in Iterable list Tuple and set
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)



