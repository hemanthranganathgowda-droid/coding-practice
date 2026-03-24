#a=int(input("enter the angle of side1: "))
#b=int(input("enter the angle of side2: "))
#c=int(input("enter the angle of side3: "))
"""if a+b+c==180 and a>0 and b>0 and c>0:
    print("the triangle is valid")
else:
    print("the triangle is not valid")"""

"""if a==b and 0<=c<60:
    print("the triangle is isosceles")
elif a==b==c==60:
    print("the traiangle is equilateral")
else:
    print("the triangle is scalene")"""



"""year=int(input("enter the year:"))
if year%100==0:
    print("the given year is century year")
else:
    print("the given year is not a century year")"""
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))
if b>a and b<c:
    print("second largest number is",b)
elif  a>b and a<c:
    print("second largest is",a)
else:
    print("second largest",c)
