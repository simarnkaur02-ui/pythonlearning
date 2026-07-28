class Animal:  # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
        
 
    def speak(self):
        print("Speaking now......")

class Dog(Animal): #Thise is how inheritance is done in python
    def speak(self):
        super().speak()# we are using the speak function of the parent class
        
        print("Woof!")        


#a = Animal("Dog")      
#a.speak()  
d = Dog("JOJO") 
d.speak()
print(d.location)