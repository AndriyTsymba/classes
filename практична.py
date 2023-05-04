#1
class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"імя {self.name}, Bik {self.age}")
studednt = Student("Andriy",15)
studednt.info()