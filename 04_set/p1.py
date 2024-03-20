# set is unordered
# set will not maintain an insertion order
# set will not allow duplicates
# set will not do indexing and slicing

# s1 = set
# print(s1)  # <class 'set'>

# s1 = set()
# print(s1)  # set()

# s1 = {10, 20, 30, 40, 50}
# print(s1, type(s1))

# s2 = {10, 20, 30, 40, 50, 10, 20, 30, 40}
# print(s2, type(s2))

# print(s1 + s2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# print(s1 * 2)  # TypeError: unsupported operand type(s) for *: 'set' and 'int'

# print(dir(set))

# add', 'clear', 'copy', 'discard', 'pop', 'remove', 'update'

# s1 = {10}
# s1.add(20)
# s1.add(30)
# s1.add(40)
# s1.add(50)
# s1.add(10)
# print(s1)  # {40, 10, 50, 20, 30}
#
# s1.clear()
# print(s1)  # set()

# copy()
# s1 = {10, 20, 30, 40, 50}
# print(s1)
# print(s1.copy())

# remove()
# s1 = {10, 20, 30, 40, 50}
# s1.remove(300)
# print(s1)  # KeyError: 300

# discard()
# s1 = {10, 20, 30, 40, 50}
# s1.discard(300)
# print(s1)

# s1 = {10, 20, 30, 40, 50}
# print(s1)
# l1 = list(s1)
# print(l1)
# l1.sort()
# print(l1)

# s1 = {10, 10, 20}
# print(s1)
#
# s1.remove(10)
# print(s1)

s1 = {10, 20, 30, 40, 50, 10.1}
print(s1)