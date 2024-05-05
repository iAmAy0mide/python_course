

# In Operator | in Lists | in Substrings
text = "Hello, world"
my_list = [1, 2, 3, 4, 5, 6]
sentence = "Python is powerful"
result = "o" in text
result2 = "E" in my_list
result3 = "power" in sentence

print(result)
print(result2)
print(result3)



#  while loop
"""
my_list = [1, 2, 3, 4, 5, 6]
index = 0
new_list = []

while index < len(my_list):
    add = my_list[index] * 4
    new_list.append(add)
    index += 1

print(new_list)
"""


#  for loop
"""

my_list = [1, 2, 3, 4, 5, 6]
new_list = []

for i in my_list:
    add = i * 2
    new_list.append(add)

print(new_list)
"""