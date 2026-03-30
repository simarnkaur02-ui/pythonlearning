s = {34, 23, 1, 3, 22}

# print(s)

# s.add(32)
# s.add(322)
# s.remove(1)
# s.remove(58231)# Throws an error
# s.discard(58231)
# s.pop()#Remove random element
# print(s)

# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs) #Note: Frozensets are immutable, so methods like add() or remove() cannot be used. They are also hashable, which allows them to be used as dictionary keys.
  