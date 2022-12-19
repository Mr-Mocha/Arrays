import array
"""
@pre - 
@post - Return array in ascending order
"""
def sortArray(array):
    if array[0] > array[1]:
        # Store 2nd element in a variable
        num = array[1]
        # Store 1st element in 2nd element
        array[1] = array[0]
        #Store variable in the 1st element
        array[0] = num
    return array

myArray = array.array('i', [8, 4])

myArray = sortArray(myArray)
print(myArray)
