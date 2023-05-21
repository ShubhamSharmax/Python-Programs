#creating functions

def function_name(): #function definition
  #statements
  print('hello from the function function_name()')

function_name() #calling the function


#python functions
var = 'apple'
var1 = 'ORANGE'

print(var) #prints the value
print(len(var)) #len() returns length of the variable
print(type(var)) #returns variable type
print(pow(4,3)) #pow() calculates power of the given value pow(a,b) is equivalent to a**b
print(abs(-50)) #abs() returns absolute value


#string functions
text = 'THis is AN exAmple OF STrinG'

print(text.upper()) #converts string to uppercase
print(text.lower()) #convert string to lowercase
print(text.capitalize()) #whole test lowercase and fist letter capital
print(text.find('an')) #finds the given string in text variable and return location
#-1 because the text has 'AN' i.e written in uppercase
print(text.find('AN'))
print(text.replace('exAmple' , 'line')) #replace(old , new) replace old string with new