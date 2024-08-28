import array

my_array = array.array("i", [1, 2, 3, 4, 5])

#when we delete 1 from the above array then the output will be [2, 3, 4, 5], 2 will move to index 0, 3 will move to index 1, 4 will move to index 2, 5 will move to index 3. and index 4 wil be empty


my_array.remove(1) #deletes the first occurence of 1 and tme complexity is O(n)
my_array.pop(0) #deletes the element at index 0 and time complexity is O(1)
my_array.pop() #deletes the last element and time complexity is O(1)
my_array.clear() #deletes all the elements and time complexity is O(1)
my_array.pop(3) #deletes the element at index 3 and time complexity is O(1)
print(my_array)