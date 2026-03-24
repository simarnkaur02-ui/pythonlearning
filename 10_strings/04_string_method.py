s = "hello world565 " # string are immutable
# s[0] = "r" # you cannot do this

# a = len(s)
# print(a)
#print(s.upper(), s)
# print(s.lower())
#print(s.upper())
# print(s.capitalize())
#print(s.title())
#print(s.count("hello"))  # Output: 3
#print(s.find('world'))  # Output: 6
#print(s.index('heee'))  # Output: 6
#print(s.endswith("hello "))  # Output: True
#print(s.startswith("llo"))  # Output: True


text = " India is a great country "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world"
#print(text.partition("are"))""
print(text.split('a' ))

# text = "Python is fun"
# print(text.find("is"))   # Output: 7
# print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

# text = "apple,banana,orange"
# fruits = text.split(",")
# print(fruits)  # Output: ['apple', 'banana', 'orange']

# new_text = " - ".join(fruits)
# print(new_text)  # Output: "apple - banana - orange"

#text = "python123"
#print(text.isalnum())   # Output: True
'''
def isalnum():
    if text.isalpha() or text.isdigit():
        return True
    else:
        return False

print(isalnum())  '''
#text = "Python Code" 
# print(text.isalpha())  # Output: False
# print(text.isdigit())  # Output: False
#print(text.isalnum())  # Output: True
#print(text.isspace())  # Output: False
#print(text.isupper())  # Output: False
#print(text.islower())  # Output: False
#print(text.istitle())  # Output: True