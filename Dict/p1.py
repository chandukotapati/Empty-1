
# dict
# assign position to the dict

# Note: Not possible in list
# l1 = [10]
# print(len(l1))
# l1[1] = 100  # IndexError: list assignment index out of range
# print(l1)

# d1 = {}
#
# d1['a'] = 10
# d1['b'] = 20

# print(d1)  # {'a': 10, 'b': 20}
#
# d1 = {'a': 10, 'b': 20}
# print(d1)

# length of the key
# print(len(d1))

# length of the elements
# l1 = [10, 20]
# print(len(l1))

#  length of the characters
# s1 = "saikiran"
# print(len(s1))

# create a dict with key and values
# d1 = {1: 10, 2: 30, 3: 30, 4: 40, 5: 50}
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())

# del keyword
# d1 = {1: 10, 2: 30, 3: 30, 4: 40, 5: 50}
# del[d1[1]]
# print(d1)
#
# l1 = [10, 20, 30, 40, 50]
# del[l1[0]]
# print(l1)

# update
# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# d1.update({"e": 20})
# print(d1)

# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# d2 = {1: 10, 2: 20, 3: 30, 4: 40}
# d1.update(d2)
# print(d1)

# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# d1.update({"b": 100})
# d1["e"] = 10
# print(d1)

# pop()
# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# print(d1)
# print(d1.pop("b"))
# print(d1)

# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# print(d1)
# del(d1["a"])
# print(d1)

# Modify the key
# d1 = {"a": 10, "b": 10, "c": 10, "d": 10}
# d1[0] = d1.pop("d")
# print(d1)

data = {

    "employeeNames": ["Sai Kiran", "Sai Ram", "Sai Vamsi", "Sai Krisha", "Vishal"],

    "age": 28,

    "jobs": {
        "role_1": "Devops Engineering", "role_2": "Fullstack Developer"
    }

}


print(data)

print(data["employeeNames"][0], ' age ', data["age"], ' he is ',  data["jobs"]["role_2"])

data["employeeNames"][0] = "Sai Kumar"
print(data["employeeNames"][0])

print(data)


#  ordered : safe(tuple) and unsafe(list)
#  unordered : safe(frozenset) and unsafe(set)
#  key and values: dict
