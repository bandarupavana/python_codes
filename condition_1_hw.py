'''n=int(input("enter a number:"))
if n==10:
    print("equal")
if n>=10:
    print("greater")
if n<=100:
    print("possible")
#print("done")
'''
'''
#1. Arithmetic Operator (+)
if 10 + 5 == 15:
    print("The sum of 10 and 5 is 15")

#2. Arithmetic Operator (-)
if 20 - 10 == 10:
    print("The difference between 20 and 10 is 10")

#3. Arithmetic Operator (*)
if 5 * 4 == 20:
    print("The product of 5 and 4 is 20")

#4. Arithmetic Operator (/)
if 20 / 5 == 4:
    print("20 is exactly divisible by 5")

#5. Arithmetic Operator (//)
if 17 // 5 == 3:
    print("The quotient of 17 divided by 5 is 3")

#6. Arithmetic Operator (%)
if 15 % 4 == 3:
    print("The remainder when 15 is divided by 4 is 3")

#7. Arithmetic Operator (**)
if 2 ** 3 == 8:
    print("2 raised to the power of 3 is 8")

#8. Arithmetic Operators (+, *)
if (5 + 5) * 2 == 20:
    print("The total value after addition and multiplication is 20")


#9. Assignment Operator (+=)
x = 10
x += 5
if x == 15:
    print("The value becomes 15 after adding 5")

#10. Assignment Operator (-=)
x = 20
x -= 5
if x == 15:
    print("The value becomes 15 after subtracting 5")

#11. Assignment Operator (*=)
x = 5
x *= 3
if x == 15:
    print("The value becomes 15 after multiplying by 3")

#12. Assignment Operator (/=)
x = 20
x /= 4
if x == 5:
    print("The value becomes 5 after division by 4")

#13. Assignment Operator (//=)
x = 17
x //= 5
if x == 3:
    print("The floor division result is 3")

#14. Assignment Operator (%=)
x = 17
x %= 5
if x == 2:
    print("The remainder stored in x is 2")

#15. Assignment Operator (**=)
x = 2
x **= 3
if x == 8:
    print("The value of x becomes 8 after raising it to power 3")


#16. Logical Operator (and)
if 10 > 5 and 20 > 15:
    print("Both numbers satisfy their respective conditions")

#17. Logical Operator (or)
if 10 > 20 or 15 > 10:
    print("At least one number is greater than the specified value")

#18. Logical Operator (not)
if not 10 < 5:
    print("10 is not less than 5")

#19. Logical Operators (and, or)
if (10 > 5 and 20 < 30) or 5 == 5:
    print("The given logical conditions are satisfied")

#20. Logical Operators (not, and)
if not (10 < 5) and 20 == 20:
    print("10 is not less than 5 and 20 is equal to 20")


#21. Membership Operator (in)
if 5 in [1, 3, 5, 7, 9]:
    print("5 is present in the given list")

#22. Membership Operator (not in)
if 10 not in [1, 2, 3, 4, 5]:
    print("10 is not present in the given list")

#23. Membership Operator (in)
if "a" in "apple":
    print("The letter a is present in the word apple")

#24. Membership Operator (not in)
if "z" not in "python":
    print("The letter z is not present in the word python")

#25. Membership Operator (in)
if "name" in {"name": "Pavana", "age": 22}:
    print("The key name exists in the dictionary")

#26. Membership Operator (not in)
if 100 not in (10, 20, 30, 40):
    print("100 is not present in the given tuple")


#27. Identity Operator (is)
a = None
if a is None:
    print("The variable a has no assigned value")

#28. Identity Operator (is not)
a = None
if a is not 10:
    print("The variable a is not the integer object 10")

#29. Identity Operator (is)
a = True
if a is True:
    print("The variable a refers to the True object")

#30. Identity Operator (is not)
a = False
if a is not True:
    print("The variable a does not refer to the True object")


#31. Bitwise Operator (&)
if 5 & 3 == 1:
    print("The bitwise AND result of 5 and 3 is 1")

#32. Bitwise Operator (|)
if 5 | 3 == 7:
    print("The bitwise OR result of 5 and 3 is 7")

#33. Bitwise Operator (^)
if 5 ^ 3 == 6:
    print("The bitwise XOR result of 5 and 3 is 6")

#34. Bitwise Operator (~)
if ~5 == -6:
    print("The bitwise NOT result of 5 is -6")

#35. Bitwise Operator (<<)
if 5 << 1 == 10:
    print("Left shifting 5 by 1 position gives 10")

#36. Bitwise Operator (>>)
if 10 >> 1 == 5:
    print("Right shifting 10 by 1 position gives 5")

#37. Bitwise Operators (&, |)
if (6 & 3) | 4 == 6:
    print("The combined bitwise AND and OR result is 6")

#38. Bitwise Operators (^, &)
if (7 ^ 3) & 5 == 4:
    print("The combined bitwise XOR and AND result is 4")


#39. Comparison Operators (==, >=)
if 10 == 10 and 20 >= 15:
    print("The first value is equal to 10 and the second value is at least 15")

#40. Comparison Operators (!=, <=)
if 15 != 10 and 5 <= 10:
    print("15 is not equal to 10 and 5 is less than or equal to 10")

'''
'''
n=int(input("enter the value: "))
if n>10:
    print(">10")
if n>20:
    print(">20")
if 50 <= n <= 60:
    print("half")
if n>=50 and n<=60:
    print("half")
'''
'''
password=input()
if password.isalpha():
    print("valid")
if password.isnumeric():
    print("valid")
    '''
'''
# painadhi kuuda crt but that is not more correct to do, need to use OR operator
password=input()
if password.isalpha() and password.isnumeric():
    print("valid")

else:
    print("invalid")
    
password=input()
if password.isaplha() or password.isnumeric():
    print("valid")
else:
    print("invalid")
'''
'''
password = input("Enter password: ")

#if password.isalpha() or password.isnumeric():
 #   print("Invalid Password")
if password in "@#$%*":
    print("Valid Password")
else:
    print("Invalid Password")
'''
'''
password=input()

if not(password.isalnum()):
    print("valid")
else:
    print("invalid")
    
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")
'''
'''
x=["pardhu","john","balayya","sampu"]
n=input("give input: ")
if n not in x:
    #x.append(n)
    x.insert(0,n)
    print("valid")
    print(x)
else:
    print("invalid")
'''
'''
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("bus")
if num%3==0:
    print("fizz")
if num %3==0 and num%5==0:
    print("fizzbuzz")
else:
    print("wrong")
'''
'''
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("bus")
elif num%3==0:
    print("fizz")
elif num %3==0 and num%5==0:
    print("fizzbuzz")
else:
    print("wrong")
'''
age=int(input())
if age>=6 and age<=12:
    print("child")
elif age>=13 and age<=18:
    print("teen")
elif age>=19 and age<=26:
    print("youth")
else:
    print("not valid")
