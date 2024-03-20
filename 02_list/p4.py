
# slicing
# syntax: l1[start : end(-1) : step-over(1)]
# syntax: l1[start : end(-1) : step-over(-1)]
# l1 = [10, 20, 30, 40, 50, 60, 70, 80]
# #      0   1   2   3   4   5   6   7
# print(l1[1:5])
#
# print(l1[1:])
#
# print(l1[:5])
#
# print(l1[:])

# l1.reverse()
# print(l1)

# print(l1[::-1])
#
# print(l1[::-2])
#
# print(l1[::-4])

l1 = [10, 20, 30, 40, 50, 60, 70, 80]
#      0   1   2   3   4   5   6   7
#     -8  -7  -6  -5  -4  -3  -2   -2
print(l1[::-1])
print(l1[::1])

print(l1[-7:-2:1])
