import streamlit as st

st.title("🐍 Python OOP Practice - 5 Minute Friendly")
st.subheader("Created by Sofia Ibrahim")
st.caption("Designed for students to learn fast with clear examples.")

questions = [
    ("1. Student Class", """
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student("Ali", 101)
print(s1.name, s1.roll_no)
"""),

    ("2. Car Class with Constructor", """
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota", "Corolla")
print(c1.brand, c1.model)
"""),

    ("3. Book Class with display()", """
class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Title:", self.title)

b1 = Book("Python 101")
b1.display()
"""),

    ("4. Animal Class with speak()", """
class Animal:
    def speak(self):
        print("Animal speaks")

a = Animal()
a.speak()
"""),

    ("5. Circle Class with area()", """
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area())
"""),

    ("6. Employee Class Constructor", """
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Sara", 50000)
print(e.name, e.salary)
"""),

    ("7. Laptop Class Print Details", """
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

l = Laptop("HP", "8GB", 70000)
print(l.brand, l.ram, l.price)
"""),

    ("8. Movie Class with Constructor", """
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

m = Movie("Inception", 9.0)
print(m.title, m.rating)
"""),

    ("9. Inheritance: Person & Teacher", """
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Miss Zara", "Math")
print(t.name, t.subject)
"""),

    ("10. Inheritance: Vehicle → Bike", """
class Vehicle:
    pass

class Bike(Vehicle):
    def __init__(self):
        self.wheels = 2

b = Bike()
print(b.wheels)
"""),

    ("11. Inheritance: Bird → Parrot", """
class Bird:
    pass

class Parrot(Bird):
    def fly(self):
        print("Parrot can fly")

p = Parrot()
p.fly()
"""),

    ("12. Method Overriding: Shape → Rectangle", """
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(4, 5)
print(r.area())
"""),

    ("13. Method Overriding: Animal → Dog", """
class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

d = Dog()
d.make_sound()
"""),

    ("14. Encapsulation: BankAccount", """
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(10000)
acc.show_balance()
"""),

    ("15. Encapsulation: Student Marks", """
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(85)
print(s.get_marks())
"""),

    ("16. Polymorphism: Bird & Airplane fly()", """
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def test_fly(flier):
    flier.fly()

test_fly(Bird())
test_fly(Airplane())
"""),

    ("17. Polymorphism: describe(Dog/Cat)", """
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def describe(animal):
    animal.speak()

describe(Dog())
describe(Cat())
"""),

    ("18. Class Method: Student count", """
class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def total_students(cls):
        return cls.count

s1 = Student()
s2 = Student()
print(Student.total_students())
"""),

    ("19. Static Method: is_even", """
class Math:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(Math.is_even(10))
print(Math.is_even(7))
"""),

    ("20. Real-life Mini Shop", """
class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Items in shop:", self.items)

s = Shop()
s.add_item("Book")
s.add_item("Pen")
s.show_items()
""")
]

for title, code in questions:
    with st.expander(title):
        st.code(code, language="python")