Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
n="codegnan: is my first choice"
n.split("n")
['codeg', 'a', ': is my first choice']
n.split("c")
['', 'odegnan: is my first ', 'hoi', 'e']
help()
Welcome to Python 3.13's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.13/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> str.ljust
Help on method_descriptor in str:

str.ljust = ljust(self, width, fillchar=' ', /) unbound builtins.str method
    Return a left-justified string of length width.

    Padding is done using the specified fill character (default is a space).

help> str.casefold()
No Python documentation found for 'str.casefold()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
help(str.casefold)
Help on method_descriptor:

casefold(self, /) unbound builtins.str method
    Return a version of the string suitable for caseless comparisons.

a="π"
a.casefold()
'π'
>>> n="srujana"
>>> print(f{n} "thinnavara")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f" {n} thinnavara")
 srujana thinnavara
>>> print("The capital of {country} is {city}.".format(country="France", city="Paris"))
... 
The capital of France is Paris.
>>> name="srujana"
>>> name2="arjun"
>>> print(name,"i got 10 lpa job, thank you very much",name2)
srujana i got 10 lpa job, thank you very much arjun
>>> print("{1} i got 10 lpa job, thank you very much {0}".format(name,name2))
arjun i got 10 lpa job, thank you very much srujana
>>> print(f"good morning {name}")
good morning srujana
>>> name3=99
>>> print("%s i got a job %d"%(name,name3))
srujana i got a job 99
>>> x=["phone","laptop","keyboard"]
>>> x[0]
'phone'
>>> x[::-1]
['keyboard', 'laptop', 'phone']
>>> x[2::-1]
['keyboard', 'laptop', 'phone']
>>> x=["phone","laptop","keyboard","laptop"]
>>> x
['phone', 'laptop', 'keyboard', 'laptop']
>>> x=["phone","laptop","keyboard","1","0.01","False"]
>>> x[::-1]
['False', '0.01', '1', 'keyboard', 'laptop', 'phone']
>>> x[0::1/2]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x[0::1/2]
TypeError: slice indices must be integers or None or have an __index__ method
