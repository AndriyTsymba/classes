# теорія класи
class Student:
    count = 0
    print("hi!")
    def __init__(self,height = 150): # кунструктор класу
        self.height = height
        Student.count += 1
    def breating(self, height):#  методи класів
        return self.height - 10
oleg = Student() # об"єкт б екзимпляр класу
print(oleg.height)
masha = Student(height= 200)
print(masha.height)
print(Student.count)
print(type(1))
print(masha.breating())

