students={
"s1":{"name":"ranga","age":18,"course":"computer science"},
"s2":{"name":"hema","age":19,"course":"electronics"},
"s3":{"name":"nithya","age":18,"course":"BSC in cs"}
}
"""print(students["s1"]["name"])
print(students["s3"]["name"])
students["s2"]["name"]="inchara"
print(students["s2"]["name"])
del students["s3"]["name"]
print(students["s3"])"""

"""students["s4"]={"name":"siri","age":18,"course":"BSC in cs"}
print(students["s4"])
print(students.keys())
print(students.values())
print(students.items())"""
"""print(students.get("s1"))
print(students.get("s1"),"student not found")"""

"""if "inchara" in students and "ranga" in students:
    print("ranga loves inchara and both are marrying themselves")
else:
    print("inchara loves ranga and ranga loves nithya")"""
"""def add(a,b,c):
    return a+b+c
a, b, c="inchara",  "loves",  "ranga"
print(add(a,b,c))"""
print(len(students))
dictionary={}

dictionary["name"]="chaya"
print(dictionary)





