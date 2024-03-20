
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort
# append(element): adds the element at the end of the list
# task 1
# l1 = [10, 20]
# l1.append(30)
# l1.append(40)
# l1.append(50)
# print(l1)  # [10, 20, 30, 40, 50]

# Note: append 1 behaviour

# task 2
# l1 = [10, 20]
# l2 = [30, 40]
# l1.append(l2)
# print(l1)

# task 4
# l2 = [10, 20, 30]
# l2.extend([100, 200, 300, 400, 500])
# print(l2)  # [10, 20, 30, 100, 200, 300, 400, 500]

# Note: append 2 behaviour

# l1 = []
# l1.extend("SaiKiran")
# print(l1)  # ['S', 'a', 'i', 'K', 'i', 'r', 'a', 'n']

# l1 = []
# l1.extend(["SaiKiran"])
# print(l1)  # ['SaiKiran']

# l1 = ["NameOne", "NameTwo"]
# l1.extend([10, 20, 30, 40, 50])
# print(l1)  #  ['NameOne', 'NameTwo', 10, 20, 30, 40, 50]

# task 5
# pop(element) method will remove the element from the end of the list
# 2 behaviours
# l1 = [10, 20, 30, 40, 50]
# print("see it was deleted: ", l1.pop())
# print(l1)

# pop(index)
# l2 = [10, 20, 30, 40, 50]
# #      0   1   2   3   5
# l2.pop(2)
# print(l2)  # [10, 20, 40, 50]

# task 6
# remove(element)
# l1 = [10, 20, 30, 40, 50, 20, 60]
# l1.remove(20)
# print(l1)  # [10, 30, 40, 50]

# task 7
# index(element)
# l1 = [10, 20, 30, 40, 50, 10, 30, 40, 20, 10, 60, 70]
# #      0   1   2   3   4   5   6   7   8   9  10  11
# print(l1.index(10))
# print(l1.index(50))
#
# # index(element, start, stop)
# print(l1.index(10, 9, 15))

# task 8
# clear()
# l1 = [10, 20, 30, 40, 50]
# print(l1)
# l1.clear()
# print(l1)


# task 8
# insert(index, element)
# l1 = [10, 20, 30, 40, 50]
# #      0   1   2   3   4
# print(l1)
# print(len(l1))
# l1.insert(3, 300)
# print(l1)
# print(len(l1))

# task 9
# copy()
# l1 = [10, 20, 30, 40, 50]
# print(l1)
# print(l1.copy())
# print(l1[:])

# task 10
# reverse()
# l1 = [10, 20, 30, 40, 50]
# l1.reverse()
# print(l1)

# task 11
# sort()
# l1 = [30, 10, 40, 20, 70, 90, 60, 50, 80]
# print(l1)
#
# l1.sort(reverse=False)
# print(l1)
#
# l1.sort(reverse=True)
# print(l1)
#
# l1 = ['D', 'A', 'C', 'B']
# l1.sort()
# print(l1)

# task 12
# count()
l1 = [10, 20, 30, 40, 50, 10, 30, 10, 10]
print(l1.count(20))

# task 13
# diff b/w uni and asi
# build in methods
# b1 = bin(10)
# print(b1)
#
# h1 = hex(10)
# print(h1)
#
# o1 = oct(10)
# print(o1)
#
# l1 = 'A'
# print(ord(l1))

# l2 = 65
# print(chr(l2))
