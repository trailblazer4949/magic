# definig a list
b = [3, 4, 4, 234, 234, 234, 234, 234, 4, 234, 3]

# to sort a list
b.sort()
print(b)

# Reversing a list
b.reverse()
print(b)

# Appending or adding a string to right
b.append(34)
print(b)

# counting how many times 234 appeared
c = b.count(234)
print(c)

# checking index of 3
d = b.index(3)
print(d)

# copying  or returning a shallow copy
cs = b.copy()
print(cs)

Delete all records from string
b.clear()
print(b)
