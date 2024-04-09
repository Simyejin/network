class People:
    def __init__(self, age = 0, name = None):
        self.__age = age
        self.__name = name
    def introMe(self):
        print("name : ", self.__name, "age : ", str(self.__age))
class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.school = school
    def showSchool(self):
        print("my school is ", self.school)
    

class Student(People):
    def __init__(self, age = 0, name = None, grade=None):
        super().__init__(age, name)
        self.__grade = grade
    def introMe(self):
        super().introMe()
        print("grade : ", self.__grade)