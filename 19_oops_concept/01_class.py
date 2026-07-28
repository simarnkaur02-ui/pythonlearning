# Class: class is a blueprint or a temple. eg. from for an exxm that contains name, age, elective, father's name etc 

# OBJECT: specific instance created from the template (class.). eg. from which contains the data john doe

class Employee: 
    company = "Hp"

    def get_salary(self): #self is imp here because self is a way to refernce the object of the class which is being created
        
        return 34000
    

e1 = Employee() # An object of class employee is created here 
print(e1.get_salary()) #Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)