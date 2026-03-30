"""employee={
    "name":"john",
    "age":25,
    "course":"python",
    "country":"india",
    "experience":"15 years",
    "hobbies":"cricket, Mastuburation,watching corns,raging",}"""

#print(employee["name"])
#print(employee["hobbies"])
"""for key,value in employee.items():
    print(f"{key}: {value}")"""
"""total=len(employee.values())
print(total)"""


"""numbers={
"one":1,
"two":2,
"three":3,
"four":4,
"five":5,
"six":6,
"seven":7,
"eight":8,
"nine":9,
"ten":10,
"eleven":11}
print(min(numbers.values()))

merge={**employee,**numbers}
print(merge)"""

keys=["name","age","course","country","rating"]
values=["meha",25,"python","south african",9]
d=dict(zip(keys,values))
print(d)