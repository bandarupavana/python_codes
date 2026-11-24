'''
x=[1,2,3,4,5]
y=(1,2,3,4,5,6)
z={1,2,3,4,5,6,7}
for i in x,y,z:
    print(i, end=" ")
print()
a={'name':'pav','age':22}
for i in a.keys():
    print(i,end=" ")#defaultly prints keys alone
    print()
for i in a.values():
    print(i,end=" ")
'''
'''
x=[1,2,3,4,5]
for i in x:
    print(i,end=" ")#to get output side by side
'''
'''#travelling using range()
x=[10,20,30]
for i in range(len(x)): #which means travels from 0 to 3 [(0,4)]
    #print(x[i])
    print(i)
y=(10,20,30)
for i in range(len(y)):
    print(y[i],end="")
z={10,20,30}              #for SET it gives error as not subscriptable
for i in range(len(z)):
    print(z[i],end="")

a={'name':'pav','age':22}
for i in range(len(a)):
    print(i.values(),end=" ")#this gives error too becoz of numerical indexing is deniable in dict

#set traveling using range() func
numbers = {10, 20, 30, 40}
numbers = list(numbers)

for i in range(len(numbers)):
    print(numbers[i]) #so for set we convert into list and travel thru indexing
#dict traveling using range() func
student = {
    "name": "Pavana",
    "age": 22,
    "course": "CSE"
}

keys = list(student.keys())

for i in range(len(student)):
    print(student[keys[i]])
'''
'''
x=[1,2,3,4,5,7,9,11]
for i in x:
    if i%2!=0:
        print(i,end=" ")
x=[1,2,3,4,5,7,9,11]
for i in x:
    if i%2==0:
        print(i,end=" ")
'''
'''
x=[10,20,30]
my_list=list(x)
for i in my_list:
    print(i)
print(my_list)

#or it can aslo be done using an empty list
x=[10,20,30]
my_list=[]
for i in x:
    my_list.append(i)
'''
'''
x = [1, 2, 4, 0, 5, 9, 8, 10]

even_index_odd_value = []
odd_index_odd_value = []
odd_index_even_value = []

for i in range(len(x)):
    # Even index, odd value
    if i % 2 == 0 and x[i] % 2 != 0:
        even_index_odd_value.append(x[i])

    # Odd index, odd value
    if i % 2 != 0 and x[i] % 2 != 0:
        odd_index_odd_value.append(x[i])

    # Odd index, even value
    if i % 2 != 0 and x[i] % 2 == 0:
        odd_index_even_value.append(x[i])

print(even_index_odd_value)
print(odd_index_odd_value)
print(odd_index_even_value)
'''
'''
names=["a","b","c","d","e"]
string=""
#to convert even index values to uppercase
for i in range(len(names)):
    if i%2==0:
        string+=names[i].upper()
print(string)
'''
#names=["a","b","c","d","e"]
#results=[]
#string=""
'''
for i in name:
    results.insert(0,i)
print(i)#this also gives reverse string but this is not crt method
'''
'''
for i in range(len(names)-1,-1,-1):
    results.append(names[i])
print(results)
'''
'''
for i in range(len(names)-1,-1,-1):
    string+=names[i]
print(string)
'''
'''
for i in names:
    string=i+string
print(string)
'''
#Convert lowercase to uppercase and uppercase to lowercase without using (Swapcase)
'''
a=["A","b","C","d","e","F","G"]
res=[]
for i in range(len(a)):
    if a[i].islower():
        res.append(a[i].upper())
    elif a[i].isupper():
        res.append(a[i].lower())
print(res)
'''
#find vowels and consonants in a string
'''
x="hello"
res=""
for i in range(len(x)):
    if x[i] in "aeiou":
        res+=x[i]
print(res)
x="hello"
res=""
for i in x:
    if i not in "aeiou":
        res += i
print(res)
'''
#to print students marks
d = {"john": 500, "hari": 600, "sai": 300, "ram": 250}
for name,marks in d.items():
    print(name,marks)
#to print students grades based on marks
d = {"john": 500, "hari": 600, "sai": 300, "ram": 250}
res={}
for name,marks in d.items():
    if marks>500:
        res[name]="A"
    elif marks>400:
        res[name]="B"
    elif marks>300:
        res[name]="C"
    else:
        res[name]="FAIL"
print(res)    
    
