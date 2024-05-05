# Removing / Deleting Items

# Using remove() 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.reverse()
my_list.remove(4)
my_list.remove(10)
print(my_list)


# Using del
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del my_list[2:9:3]
print(my_list)
print(my_list[2:9:3])
"""





# Updating Items
"""
my_list = [1, 2, 3, 4, 5, 6, 7]
my_list[3] = 30
print(my_list)
"""


"""
slices [start:end:step]
"""

# Using slices
"""
my_list = [1, 2, 3, 4, 5]
subset = my_list[1:3]
print(subset)
"""



# Accessing Items
"""
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])
"""