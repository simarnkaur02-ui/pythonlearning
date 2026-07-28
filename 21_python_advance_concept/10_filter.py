#def is_greater_then_9(x):
#    if x>9:
#        return True
#    else:
#        return False
a = [1, 3, 5, 243, 34, 32, 6548, 23, 2, 5, 7, 9]  

new = list(filter(lambda x: x>9, a))
print(new)