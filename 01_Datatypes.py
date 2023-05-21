#Data Types in Python 

#integer
a = 5;
print(type(a))  #prints <class 'int'>

#float
b = 5.5;
print(type(b))  #prints <class 'float'>

#string
c = "Hello World!"
print(type(c))  #print <class 'str'>


#variable Declaration in Python
variable_name = 'value'

print(variable_name) #print function returns the value of the given variable in our case 'value' would be the answer

#examples of variable declaration

x = 5;
y = 7.5;
z = "Hello"

print(x,'is a integer',y,'is a float',z,'is a String')  #Output => 5 is a integer 7.5 is a float Hello is a String


#int to string
user = 'Shubham Sharma '
num = 2
space = ' ' #this is a string containg single space
emptystring = '' #this is a emptystring 
result = user + 'have' + space + str(num) + space + 'laptops.' #here str() function changes the num from interger to string
print(result)