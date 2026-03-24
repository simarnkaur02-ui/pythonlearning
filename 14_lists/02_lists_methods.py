# marks = [5, 2, 21, 5, 7]
# extra_marks = [53, 25, 31]

#print(marks)

#marks.append(55) # THIS WILL CHANGE THE ORIGINAL LIST 
#marks.pop()
#marks.remove(21)
#marks.extend(extra_marks)
#print(marks)

# name =[1,2,2,2,4,5]
# name2 =[x if x != 2 else 300 for x in name if x < 4]

# print(name2)
 
# import copy


# list2 = [1, 2, 3, 4, 5,[100, 200, 300]]
# list3 = list(list2)
# list4 = copy.deepcopy(list3)
# list2[5][2] = 500   
# print(list2)
# print(list3)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# five = [x for x in num if x<5]
# print(five)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 8,]
UniqueNumbers = []
for x in list2:
    if x not in UniqueNumbers:
        UniqueNumbers.append(x)
print(UniqueNumbers)