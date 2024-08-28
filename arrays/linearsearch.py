import array

my_array1 = array.array('i',[1,2,3,4,5,6,7,8,9,10])

def linear_search():
    for i in range(len(my_array1)): #time complexity is O(n)
        if my_array1[i] == 5:
            return "Found at index: " + str(i)
    return -1
print(linear_search())