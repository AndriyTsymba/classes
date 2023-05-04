# теорія класи
class Student:
    print("hi!")
    def __init__(self,height = 150):
        self.height = height
oleg = Student() # об"єкт б екзимпляр класу
print(oleg.height)
masha = Student(height= 200)
print(masha.height)



