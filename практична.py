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
#4
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Неприпустима сума для внесення!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Недостатньо коштів на рахунку!")
        else:
            print("Неприпустима сума для зняття!")

    def get_balance(self):
        return self.balance
account = BankAccount("Olga")
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())
account.withdraw(1000)
account.deposit(-100)

