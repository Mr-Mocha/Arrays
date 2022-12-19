import array

"""
@pre - Array initialized with numbers
@post - Double 1st element in array and display array elements
"""
# Passing an array as an argument
def DoubleNumbers(array):
    array[0] = array[0] * 2
    for number in array:
        print(number)
    #return array

# Created an array of 3 integers
myArray = array.array('i', [1, 2, 3])

# Created a list of 3 integers
myList = []

myList.append(5)
myList.append(3)
myList.append(7)

print(len(myList))
print(sum(myList))
print(sum(myList) / len(myList))
print(max(myList))
print(min(myList))
"""
# Pass myArray as an argument
newArray = DoubleNumbers(myArray)

print(newArray[1])
# Use an index to access values of the array
print(myArray[0])

# Modify an element using an index as well
myArray[0] = 5

for x in myArray:
    print(x)
"""