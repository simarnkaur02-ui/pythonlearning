# string formating

template = "Dear {}, you are awsome. Take this {}$ bag "

a = "JOHN"
a1 = 10000
b = "JACK"
b1 = 100000
c = "MARIE"
c1 = 200

s1 = template.format(c, c1)
print(s1)

print(f"{c} you are and take this {c1}$ bag")