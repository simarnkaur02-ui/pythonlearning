def  remove_duplicates (numbers):
    return list(set(numbers))
num = [1,2,3,4,8,9,5,6,8,9,7]
 
print("orignal list: ", num)
print("without duplicates:", remove_duplicates(num))