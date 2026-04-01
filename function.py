"""class student:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def display_details(self):
        print("name",self.name)
        print("age",self.age)
s1=student("ranganath",18)
s1.display_details()
print(s1.name)"""
"""class car:
    def __init__(self,start):
        self.start=start
    def start_engine(self):
        print("engine started",self.start)
c1=car("yes")
c1.start_engine()"""

"""class rectangle:
    def __init__(self,length,width):
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width
r1=rectangle(2,3)
r1.area()
print(r1.area())"""

"""class circle:
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*3.14*self.radius
c1=circle(5)
print(c1.circumference())"""

"""class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name",self.name)
        print("salary",self.salary)
e1=employee("ramu",50000)
print(e1.name)
print(e1.salary)"""
"""class banckaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def display_balance(self):
        print("Balance",self.balance)
b1=banckaccount(500)
b1.deposit(1078)
b1.withdraw(205)
b1.display_balance()"""

"""class animal:
    def __init__(self,sound):
        self.sound=sound
class dog(animal):
    def __init__(self,sound):
        super().__init__(sound)
d1=dog("bark")
print(d1.sound)"""

"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("Nmae",self.name)
        print("Age",self.age)
class teacher(person):
    def __init__(self,subject,age,name):
        
        super().__init__(name,age)
        self.subject=subject
    def display_teacher(self):
        self.display_person()
        print("subjects",self.subject)
t1=teacher("muttu",20,"maths")
t1.display_teacher()"""











