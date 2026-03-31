"""class car:
    def __init__(self,model,colour,brand):
        self.model=model
        self.colour=colour
        self.brand=brand
    def display_details(self):
        print(f"Car Model: {self.model}")
        print(f"Car Colour: {self.colour}")
        print(f"Car Brand: {self.brand}")
c1=car("2007","red","BMW")
c1.display_details()
print(c1.model)"""

"""class student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
    def display(self):
        self.marks+=10
        print("updated students marks:",self.marks)
s1=student("hemanth",80)
s2=student("nithya",70)
s3=student("muttu",85)
s1.display()
s2.display()
s3.display()"""

"""class banck_account:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def display(self):
        print("self balance :",self.__balance)
b1=banck_account(50004)
b1.deposit(1000)
b1.withdraw(1014)
b1.display()"""

"""class person:
    def __init__(self,name):
        self.__name=name
class employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.__salary=salary
    def display(self):
        print("person salary is :",self.__salary)
p1=employee("Mutuu",5000)
p2=employee("Poorna chandra",45000)
p1.display()
p2.display()"""

"""class bike:
    def speed(self):
        print("bike speed is 69")
class car:
    def speed(self):
        print("car speed is 120")
objects=[bike(),car()]
for obj in objects:
    obj.speed()"""





    


