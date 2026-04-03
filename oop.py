"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)
s1=student("hemanth",[85,90,78,92])
s2=student("ramu",[90,60,67.80])
print(s1.average())
print(s2.average())"""


"""class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def display(self):
        print("area",self.area())
        print("perimeter",self.perimeter())
r1=rectangle(12,13)
r2=rectangle(14,29)
r1.display() 
r2.display() """

"""class car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    def display(self):
        print("Car details:",self.brand,self.model,self.color)
c1=car("BMW",2018,'white')
c1.display()"""


"""class employee:
    def __init__(self,name,new_salary,old_salary,percentage):
        self.name=name
        self.new_salary=new_salary
        self.old_salary=old_salary
        self.percentage=percentage
    def salary(self):
        percentage_hike=((self.new_salary-self.old_salary)/self.old_salary)*100
        added_salary=(self.old_salary*self.percentage/100)+self.old_salary
        return percentage_hike,added_salary
e1=employee("hemanth",56000,50000,12)
e2=employee("thomas",40000,3000,14)
print(e1.salary())
print(e2.salary())"""

class banckaccount:
    def __init__(self,balanc):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient balance")
        else:
            print("sucessfully withdraw")
b1=banckaccount(200)
b1.set__balance(5000)
b1.get__balance(7000)
b1.withdraw(2000)
print(b1.banckaccount)

    
    






    
    
        

