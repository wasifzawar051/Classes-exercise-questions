#  MUHAMMAD WASIF ZAWAR             FA24-BBD-053

#  QUESTION NUMBER 1 :
#  Create a class Person with attributes name, age, and city.
class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
p1=Person("Wasif",20,"Sheikhupura")
print(f"{p1.name} is {p1.age} years old. Living in {p1.city}")


#  QUESTION NUMBER 2 :
#  Create a class Car with attributes make, model, and year.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
c1=Car("audi",19,2024)
print(f"The car is {c1.make} and it's model is {c1.model}. And the current year is {c1.year}.")


#  QUESTION NUMBER 3 :
#  Create a class Circle with attributes radius and methods to calculate area and circumference.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        ar=3.14159*(self.radius**2)
        print(f"The area of the circle is {ar}.") 
    def get_circumference(self):
        circ=2*3.14159*(self.radius)
        print(f"The circumference of the circle is {circ}.") 
c1=Circle(4)
c1.get_area()
c1.get_circumference()


#  QUESTION NUMBER 4 :
#  Create a class Rectangle with attributes length and width and methods to calculate area and perimeter.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        ar=self.length*self.width
        print(f"The area of the rectangle is {ar}.") 
    def get_parameter(self):
        para=2*(self.length + self.width)
        print(f"The parameter of the rectangle is {para}.") 
r1=Rectangle(8,4)
r1.get_area()
r1.get_parameter()



#  QUESTION NUMBER 5 :
#  Create a class Student with attributes name, roll_number, and marks. Implement a method to calculate the average marks.
class Student:
    def __init__(self, name, roll_number, marks) :
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def get_average(self):
        if len(self.marks) > 0 :
            print(sum(self.marks)/len(self.marks) )
        else :
            print(0)
Student=Student("Wasif","FA24-BBD-053",80)
print(f"Name : {Student.name}")
print(f"Roll Number : {Student.roll_number}")
print(f"Average Marks : {Student.marks}")


#  QUESTION NUMBER 6 :
#  Create a class Book with attributes title, author, and publication_year.
class Book:
    def __init__(self,title, author, publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
B1=Book("The Alchemist", "Pulo Coelho", 1998)
print(f"{B1.title} was written by {B1.author} in {B1.publication_year}.")


#  QUESTION NUMBER 7 :
#   Create a class Employee with attributes name, salary and designation.
class Employee:
    def __init__(self, name, salary, designation):
        self.name=name
        self.salary=salary
        self.designation=designation
E1=Employee("Ahmed",150_000,"Soft Engineer")
print(f"{E1.name} is a {E1.designation} and earns {E1.salary}")


#  QUESTION NUMBER 8 :
#  Create a class Bank with attributes name, account_number, and balance. Implement methods to deposit and withdraw money.
class Bank:
    def __init__(self, name, account_number, balance=0.0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def deposit(self, amount):
        if amount > 0 :
         self.balance += amount
         print(f"Deposited {amount}. New balance: {self.balance}")
        else :
            print("Insufficant Balance")
    def withdraw(self, amount) :
        if amount > 0 :
            if amount <= self.balance :
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else :
                print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive")
    def __str__(self):
        return f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}"
acc = Bank("Ali", "123456789", 5000)
acc.deposit(2000)
acc.withdraw(6000)
print(acc)
            


















































    