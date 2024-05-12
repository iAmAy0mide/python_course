# Iterating Over Tuple
friends = ('alex', 'micheal', 'jordan')

for friend in friends:
    print(friend)

# weird things about tuple
# 1
a_tuple = 12, 3, 4, 56
not_tuple = (3)
another_tuple = (5,)
# print(type(a_tuple), type(not_tuple), type(another_tuple))



my_tuple = (1, 2, 3, "hello", 3.34)

# Creating a new tuple with modified content

new_tuple = my_tuple + (5, "World")
# print(new_tuple)


# my_tuple[3] = 4

# print(my_tuple)
# print(my_tuple[3])
# print(type(my_tuple))