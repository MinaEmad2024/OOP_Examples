### abstract class is like a template for building other classes 

from abc import ABC, abstractmethod

class abstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass 

class Dog(abstractAnimal):
    def speak(self):
        print("Boww boww")  
    
dog = Dog()
print(dog.speak())    