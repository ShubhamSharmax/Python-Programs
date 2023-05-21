#LIST

studentName = ['Shubham' , 'Sumant', 'gorav']
print(studentName)

#printing list element by its index
print(studentName[0])

# list[0] returns first element 
# list[-1] returns last element

print(studentName[-2]) #returns second last from the list

# list[start : end] will let you chose index range from start to end
print(studentName[:2]) #prints element from start to 2 
print(studentName[1:2]) #prints elsement from 1 to 2
print(studentName[1:]) #prints element from 1 to end

#list functions
from types import EllipsisType
#list functions
#empty list
emptyList = []

#append()
emptyList.append('hello') #appends a new element in the list  
print(emptyList)

#insert()
emptyList.insert(1, 'hey') #inserts new element into the list at index one
print(emptyList)

#extend()
emptyList.extend([1,2,3]) #allows to concat several lists together
print(emptyList)

#remove()
emptyList.remove('hey') #removes the matching element from list
print(emptyList)

#del()
del emptyList[3] #deletes the element on behalf of its index number
print(emptyList)

#Dictionary
studentData = {
    'name' : 'Shubham sharma', 
    'marks' : 94
}

print(studentData)
print(studentData['name'])
print(studentData['marks'])

#adding new element
studentData['Grade'] = 'A'
print(studentData)

#Tuple
#tupple is similar to list but tuples are ordered and immutable
#The main difference is that once a tuple has been declared, it cannot be modified. It is then said that it is immutable.
data = (2, 3, 45, 70)
print(data)

data[4] = 50


