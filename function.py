"""def check(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
check(4)"""
"""def cube (n):
    return n*n*n
x=cube(5)
print(x)"""

"""def cube(n):
    print(n*n*n)
cube(12) """
"""def sub (a,b):
    return(a-b)
x=sub (abs(1),abs(5))
print(abs(x))"""

"""def mul(a,b):
    return a*b

print(mul(5,6))"""
"""def div(a,b):
    if b==0:
        return "undefined"
    else:
        return a/b
print(div(10,0))"""
"""def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(check(10))"""
"""def max(a,b):
    if a>b:
        return  a
    elif b>a:
        return b
    else:
        return "both are equal"
print(max(3,9))"""

"""def min(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c

print(max(9,3,4))"""

"""def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return c
    else:
        return c
print(max(9,3,5))"""

"""def cube(n):
    return n**3
print(cube(5))"""

"""def len(s):
    count=0
    for i in s:
        count+=1
    return count
print(len("hello world"))"""

"""def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))"""
"""def reverse(a):
        return(a[::-1])
print(reverse("hello ranganath gowda"))"""

"""def reverse(s):
    reverse=""
    for ch in s :
        reverse=ch+reverse
    return reverse
print(reverse("hello sier i am ranganath gowda"))"""
"""def vowels(s):
    count=0
    for  ch in s:
        if ch in "aeiou":
            count+=1
    return count
print(vowels("hello ranganath you were name please"))"""
"""def palindromic(s):
    if s==s[::-1]:
        return "palindromic"
    else:
        return "not pallindromic"
print(palindromic("madam"))"""

"""def check(n):
    if n>1:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"

print(check(0-1))"""

"""def F_C(n):
    F=(n*1.8)+32
    return F
print(F_C(8))"""
"""def c_F(n):
    C=(n-32)/1.8
    return C
print(c_F(99))"""

"""def factorial(n):
    factorial=1
    for i in range(1,n+1):
         factorial=factorial*i
    return factorial
print(factorial(3))"""

"""def sum(n):
    sum=0
    total=0
    for i in range(1,n+1):
        sum=sum+i
        total+=sum
    return total
print(sum(10))"""

"""def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(16,19))"""

"""def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
print(lcm(12,18))"""
"""def sum(n):
    total=0
    for i in range(1,n+1):

        total+=i
    return total
print(sum(10))"""

def set(s):
    unique=set()
    for i in range(s):
        unique.add(i)
    return unique
print(set([1,2,3,4,4,5,5,6]))





