
# l1 = [int, float, complex, bool]
# print(l1)
# l1 = [int(), float(), complex(), bool()]
# print(l1)

# Memory
# l1 = [10, 10, 10, 10, 10,  100]
# #      0   1   2   3   4,   5
# print(l1)
#
# print(id(l1[0]), id(l1[1]), id(l1[2]), id(l1[3]), id(l1[4]), id(l1[5]))

# add the list
# l1 = [10, 20, 30, 40, 50]
# l2 = [10, 20, 30, 40, 50]
# print(l1 + l2)  # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# repetition
# l1 = [10, 20, 30, 40, 50]
# print(l1 * 5)

# unpacking
a, *b, c, d = [10, 20, 30, 40, 50]
print(a)
print(b)
print(c)
print(d)  # ValueError: too many values to unpack (expected 4)
