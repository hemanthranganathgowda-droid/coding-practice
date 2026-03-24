
#code to calculate the electricity bill on the basis of units used 

"""units=int(input("enter the units of current used:"))

if units <= 100:                                               
    bill=units*1
elif units <= 200:
    bill=100*1+(units-100)*2
else:
    bill=100*1+100*2+(units-200)*3
print("Bill",bill)""" 


#code for login to maintain security
"""username=input("enter the name of the user:")
passward=int(input("enter the passward:"))
if username=='admin' : 
    if passward==12345:
        print("loged sucessfully")
    else :
        print("wrong password")
else:
    print("user not found, Try again!")"""



# python code to calculte the balance like an ATM machine

"""amount=int(input("enter the amount :")) 
intial_balance=10000
if amount<=intial_balance:
    if amount%10000!=0:
        print("Transaction sucessfully.")
        balance=intial_balance-amount
        print("Balance",balance)

    else:
        print("entered amount is multiple of 100")
else:
   
    print("insufficient balance")"""

# code acts like a calculator 
"""num1=int(input("enter the num1"))
num2=int(input("enter the num2:"))
print("1.addition:")
print("2.substraction:")
print("3.multiplication")
print("4.division")
choice=int(input("enter the choices:(1/2/3/4/5):"))
if choice ==1:
    result=num1+num2
    print("R",result)
elif choice==2:
    result=num2-num2
    print("R",result)
elif choice==3:
    result=num1*num2
    print("R",result)
elif choice==4:
    if num2!=0:
        print(("Result"),num1/num2)
    else:
        print("denominated shoud not be zero")
else:
    print('invalid choice')"""



#  Ekart discount calculator


amount=int(input("enter the total amount of the product :"))
if  amount>5000:
    print("20 % discount")
    discount_applied = amount*(20/100)
    final_amount = amount-discount_applied
    print("Dicount",discount_applied)
    print("Final_amount",final_amount)

elif amount>2000:
    print("10% discount")
    discount_applied = amount*(10/100)
    final_amount = amount-discount_applied
    print("Dicount",discount_applied)
    print("Final-amount",final_amount)
else:
    print("No discount  is their for this price ! you need to  pay acutual price")




   


