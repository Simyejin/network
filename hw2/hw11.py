class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    
    def getName(self): 
        return self.name 
    
    def getAge(self): 
        return self.age 

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        return self.employeeID

employee = Employee("IoT", 65, 2018)

print(employee.getName())
print(employee.getAge())
print(employee.getID())