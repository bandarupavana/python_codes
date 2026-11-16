Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 10**2*10
1000
>>> 10%2
0
>>> 10//2
5
>>> 10/2
5.0
\
>>> 10**2%4//2*3**2
0
>>> 10**2%4+2*3
6
>>> a=10
>>> b=1
>>> c=2
>>> d=3
>>> a+=b
>>> a
11
>>> a-=b
>>> a
10
>>> a**=2
>>> a
100
>>> x=5
>>> x+=x+10
>>> x
20
>>> x=3
>>> x*=2%4
>>> x
6
>>> x*=10%2
>>> x
0
>>> x**=1+5//3
>>> x
0
>>> x=3
>>> x**=1+5//3
>>> x
9
>>> x=2
x%=2**1//3
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x%=2**1//3
ZeroDivisionError: integer modulo by zero
s="1"
m="b"
s+m
'1b'
s*b
'1'
s*3
'111'
s*m
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s*m
TypeError: can't multiply sequence by non-int of type 'str'
s+m*2
'1bb'
s**3
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s**3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
s/s
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s/s
TypeError: unsupported operand type(s) for /: 'str' and 'str'
s+3
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s+3
TypeError: can only concatenate str (not "int") to str
s+"3"
'13'
s*"3"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s*"3"
TypeError: can't multiply sequence by non-int of type 'str'
x
2
x="b"
x+"alayya"
'balayya'
10.0*2
20.0
x*5
'bbbbb'
10.4<10.0
False
a=10
b=11
x+=10<20
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x+=10<20
TypeError: can only concatenate str (not "bool") to str
x=10<20
x
True
x!=False
True
x=False+1
x
1
x=True+True*2
x
3
"a">"b"
False
1<2<3
True
1<2>3
False
