
# what are datatypes
# int float complex bool, list, set, map, tuple, frozenset, bytes, bytearray, str, dict

# list is datatype, and it is a class, and it is an object
# using square brackets we can create a list
# list will maintain insertion order and it will allow duplicate
# list is unsafe

# syntax: [element/item, element/item, element/item, element/item...]
l1 = [10, 20, 30, 40, 50]
#      0   1   2   3   4  - index
#      1   2   3   4   5  - length
print(l1)  # [10, 20, 30, 40, 50]

l1 = [10, 20, 30, 40, 50, 10, 20, 30, 60, 70]
print(l1)  # [10, 20, 30, 40, 50, 10, 20, 30, 60, 70]

# list is unsafe
l2 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
l2[2] = 200
print(l2)  # [10, 20, 200, 40, 50]

# tuple is safe
# l2 = (10, 20, 30, 40, 50)
# #      0   1   2   3   4
# l2[2] = 200
# print(l2)  #  # TypeError: 'tuple' object does not support item assignment
