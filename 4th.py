"""total=0
for i in range(1,101):
    total+=i
    print(total)"""

"""num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("palindromic")
else:
    print("not a palindromic")"""


"""num=int(input("enter a number :"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
    else:
        print("prime number")
else:
    print("not a prime number")"""


"""print(15%3)
print(17%5)"""
"""n=20
if n%4==0:
    print("yes divisible by 4")"""

"""num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
        else:
            print("yes it is a prime number")
            break"""




"""amount=int(input("enter the total amount:"))
if amount%100!=0:
    print("invalid balance")
else:    
    n2000=amount//2000
    amount=amount%2000
    n500=amount//500
    amount=amount%500
    n100=amount//100

print("500notes",n500)
print("2000notes",n2000)
print("n100notes",n100)"""


"""total=0
count=0
while True:
    amount=int(input("enter the amount:"))
    if amount==0:
        break
    total+=amount
    count+=1
print('total amount:',total)
print("number of depositers",count)"""

"""num=int(input("enter the number:"))
temp=num
sum=0
while num>0:
    digit=num%10 
    sum=sum+digit**3
    num=num//10
if sum==temp:
    print("Armstrong number:")
else:
    print("not an armstrong number")"""

n=int(input("enter the limit:"))
for num in range(1,n+1):
    original =num
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==original:
        print("Armstrong number",original)

