#for i in range(1,11):
#   print(i)
#for i in range(1000,2001):
#   print(i)
#for i in range(1000,-1,-1):
#    print(i)
#for i in range(0,101,2): #to print even numbers
#    print(i, end=" ")
'''
num=int(input("enetr number: "))
for i in range(1,11):
    print("2 ",num*i)
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
num = int(input("Enter number: "))

for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num*i))
    '''
'''
num = int(input("Enter number: "))

for i in range(1, 11):
    print("{2} x {1} = {0}".format(num, i, num*i))
'''
'''
num = int(input("Enter number: "))
for i in range(20,-1,-1):
    print("{} x {} = {}".format(num, i, num*i))
    '''
'''
for i in range(65, 91):
    print(chr(i))
for i in range(97, 123):
    print(chr(i))
'''
'''
for i in range(1,11):
    if i%2!=0:
        print("odd nums: ",i)
'''
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "- FizzBuzz")
    elif i % 3 == 0:
        print(i, "- Buzz")
    elif i % 5 == 0:
        print(i, "- Fizz")
    else:
        print(i)
