#year=int(input())
'''
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not a leap year")
'''
'''#
find the grade of a student based on marks:
90-100 A
80-90 B
60-80 C
LESS THAN 40 FAIL
'''
'''
marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 60 and marks < 80:
    print("Grade C")
elif marks < 40:
    print("fail")
else:
    print("invalid")
'''
#given num is less than 0 print -ve
#= to 0 equal
#greater than 0 +ve
'''
num = int(input("Enter num: "))
if num < 0:
    print("Negative")
elif num == 0:
    print("Equal to zero")
else:
    print("Positive")
    
x,y,z=3,2,1
if x>y:
    print(x)
elif y>z:
    print(y)
elif z>x:
    print(z)
else:
    print("not valid")
################
#take multiple values and multiple variables to compare
a, b, c = map(float, input("Enter three numbers separated by spaces: ").split())

if a >= b and a >= c:
    print(f"{a} is the greatest")
elif b >= a and b >= c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
'''
#take empty dict, take 2 inputs from user 1. username 2. password, add username as a key and passwordas a value
'''d = {}
username = input("Enter username: ")
password = input("Enter password: ")
d[username] = password
print(d)
'''
'''
#to chk user input with the given input in code and says valid if matches
data={'john':23456,'sai':34567,'raju':87654}
username = input("Enter username: ")
password = int(input("Enter password: "))
if username in data.keys() and password in data.values():
    print("valid")
else:
    print("invalid")
'''
'''
mens=["pants","shirts","shorts"]
womens=["tops","dupata","dreeses"]
option=int(input("1.mens 2.womens:"))

if option==1:
    print(mens)
    choose=int(input("select size:"))
    if choose>=32 and choose<=38:
        print("avaialble")
    else:
        print("not avialble")

else:
    print(womens)
    choose=int(input("1.size 2. colors: "))
    colors=["red","blue","green"]
    if choose==1:
        size=int(input("enter size: "))
        if size>=32 and size<=38:
            print("avaialble")
    else:
        print(colors)
'''
'''
# added children set
mens=["pants","shirts","shorts"]
womens=["tops","dupata","dreeses"]
children=["frocks","chudidhar","night set"]
option=int(input("1.mens 2.womens 3.children: "))

if option==1:
    print(mens)
    choose=int(input("select size:"))
    if choose>=32 and choose<=38:
        print("avaialble")
    else:
        print("not avialble")

elif option == 2:
    print(womens)
    choose=int(input("1.size 2. colors: "))
    colors=["red","blue","green"]
    if choose==1:
        size=int(input("enter size: "))
        if size>=32 and size<=38:
            print("avaialble")
    else:
        print(colors)
else:
    print(children)
    age=int(input("enter age: "))
    if age<=5:
        print("only frocks available")
    elif age>5 and age<=12:
        print("all are avilable")
    else:
        print("invalid age")
        
'''
'''
#username is username exists then ask password
#if username doesnt exist then say username not found and password wrong
data={'john':23456,'sai':34567,'raju':87654}
username = input("Enter username: ")
if username in data.keys():
    password = int(input("Enter password: "))
    if password in data.values():
        print("password matched")
    else:
        print("password mismatched")
else:
    print("username doesnt exist")
'''
#electricity bill
#name,units
#1-100 units then per unit 5rs
#101-2002 units then per unit 6rs
#201-500 units then per unit 10rs
print("ELECTRICITY BILL : TELANGANA")
print("----------------------------")
name=input("enter owner name: ")
units=int(input("no.of units used: "))
print("------------------------------")
print("electricity units usage: \n 1-100 units then per unit 5rs \n 101-200 units then per unit 6rs \n 201-500 units then per unit 10rs \n >500 units then per unit 15 rs")
print("------------------------------")   
if units>=1 and units<=100:
    print("1-100 units then per unit 5rs")
    bill= units * 5
    print(f"total bill amt {bill} rs")
elif units>=101 and units<=200:
    print("101-200 units then per unit 6rs")
    bill= units * 6
    print(f"total bill amt {bill} rs")
elif units>=201 and units<=500:
    print("201-500 units then per unit 6rs")
    bill= units * 10
    print(f"total bill amt {bill} rs")
else:
    print(">500 then per unit 15rs")
    bill= units * 15
    print(f"total bill amt {bill} rs")
