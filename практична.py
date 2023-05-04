#1
class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"імя {self.name}, Bik {self.age}")
studednt = Student("Andriy",15)
studednt.info()
#2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(10)
print(circle.area())
#3
def sound (self):
    print("варинка видає звук")
class Dog:
    def sound(self):
        print("Гав"," афуф")
my_dog = Dog()
my_dog.sound()
