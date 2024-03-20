
# diff b/w list and tuple
# list are unsafe / mutable
# l1 = [10, 20, 30, 40, 50]
# l1[0] = 100
# print(l1)

# tuple are safe / immutable
# t1 = (10, 20, 30, 40, 50)
# t1[0] = 100
# print(t1)  # TypeError: 'tuple' object does not support item assignment

# tuple
# we can create tuple using parameters ()
# tuple will maintain insertion order and allows duplicates
# tuple is immutable
# tuple have only two methods

t1 = ()
print(t1, type(t1))

t1 = (10, 20, 30, 40, 50, 10, 20, "NameOne", True)
print(t1, type(t1))

t1 = 10
print(t1, type(t1))

t1 = 10,
print(t1, type(t1))

# count()
t1 = (10, 20, 30, 40, 50, 10, 20, "NameOne", True)
print(t1.count(40))

# index()
t1 = (10, 20, 30, 40, 50, 10, 20, "NameOne", True, 10, 20, 30)
print(t1.index("NameOne"))

# index(value, start, end)
print(t1.index(10, 6, 10))

# add (concat)
t1 = (10, 20)
t2 = (30, 40)
print(t1 + t2)  # (10, 20, 30, 40)

# rep
print(t1 * 3)  # (10, 20, 10, 20, 10, 20)

# print(t1 * t2)  # TypeError: can't multiply sequence by non-int of type 'tuple'
print(t1)
