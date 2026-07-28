a = {1, 2, 3}
b = {3, 4, 5}
''''
c = a.union(b)
print(c)

d = a.intersection(b)

print(d)

e = a.difference(a - b)
print(e)
'''

union = a.union(b)
intersection = a.intersection(b)

difference = a. difference(b)

print(union, intersection, difference)