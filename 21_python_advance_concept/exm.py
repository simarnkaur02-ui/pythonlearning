class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

       # static method 
@staticmethod
def sum (a, b):
        return  a+b 
    
print(sum(5, 8))   