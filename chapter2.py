#VARIABLES
message="Hello Python world!"
print(message)
message="Hello Python Crash Course world!"
print(message)


#TRY IT YOURSELF
#2.1
newmessage="Bye"
print(newmessage)
#2.2
newmessage="Bye Python Crash Course world!"
print(newmessage)

#STRINGS
#A string is a series of characters.
"This is a string"
'This is also a string'

#You can use "" or '' around your strings.
#This flexibility allows you to use "" and '' within your strings:
'I told my friend, "Python is my favorite language!"'
"One of the Python's strengths is its 'diverse and supportive' community."

#Changing Case in a String with Methods
name="ada lovelace"
print(name.title()) #The output will be like this: "Ada Lovelace"
#A method is an action that Python can perform on a piece of data.
#The title() method changes each word to title case, where each word begins with a capital letter.

#You can change a string to all uppercase or all lowercase letters.
name="Ada Lovelace"
print(name.lower())#ada lovelace
print(name.upper())#ADA LOVELACE

#Using Variables in Strings
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)#ada lovelace
#These strings are called f-strings.

#You can do a lot with f-strings. For example, you can use f-strings to compose complete messages using the information associated with a variable, as shown here:
first_name="martin"
last_name="key"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")#Hello, Martin Key!

#You can also use f-strings to compose a message, and then assign the entire message to a variable:
message=f"Hello, {full_name.title()}!"
print(message)#Hello Martin Key!


#Adding Whitespace to Strings with Tabs or Newlines
#Whitespace refers to any nonprinting characters, such as spaces,tabs, and end-of-line symbols.

#To add a tab to your text, use \t
print("Python")# ---->Python
print("\tPython")# ---> Python

#To add a newline in a string, use \n
print("Languages:\nPython\nJava\nC")
'''
Languages:
Python
Java
C
'''

#Stripping Whitespace
# 'Python' and 'Python ' is totally different for computer but for programmers , they look pretty much the same.
#Extra whitespace can be confusing in much situations. Python makes it easy  to eliminate extra whitespace from data that people enter.
#Python can look for extra whitepsace on the right and left sides of a string.

#To ensure that no whitepsace exist on the right side of a string, use rstrip() method.
language='Python '
print(language.rstrip())
'''
Output:
'Python' instead of 'Python '

'''

#However, its removed temporarily. To remove the whitespace from the string permanently, you have to assign the value a variable.
language=language.rstrip()
print(language)

#You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip().
language=' Python '
print(language)# ' Python '
print(language.rstrip())# ' Python'
print(language.lstrip())# 'Python '
print(language.strip())# 'Python'


#Removing Prefixes

#Consider a URL with the common prefix https://:. We want to remove  this prefix, so we can focus on just the part of URL that users need to enter into an address bar. 
#Here's how to do that:
nostarch_url='https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

#Its removed temporarily. To remove string permanently, you have to reassign  it to the original variable or new variable.
simple_url=nostarch_url.removeprefix('https://')
print(simple_url)

#Avoid Syntax Error with Strings
#Here's how to use single and double quotes correctly.
message="One of Python's strengths is its diverse community."
print(message)
#No trouble reading the string correctly.

#However if you use single quotes,  Python can't identify where the string should end:
"""
message= 'One of Python's strengths is its diverse community.'
print(message)

Error will occur.
"""


#TRY IT YOURSELF
#2.3
message="Hello Mark, welcome to the Python world."
print(message)
#2.4
name="mark"
print(name.lower())
print(name.upper())
print(name.title())
#2.5
famous_quote='The slogan "Peace at home, peace in the world" was first pronounced by Mustafa Kemal Atatürk.'
print(famous_quote)
#2.6
famous_name="Mustafa Kemal Atatürk"
famous_quote='"Peace at home, peace in the world"'
print(f"The slogan {famous_quote} was first pronounced by {famous_name}.")
#2.7
name="\n\tMark\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#2.8
#Python has removesuffix() method that works exactly like removeprefix()
filename='python_notes.txt'
print(filename.removesuffix(".txt"))# Output:python_notes


#NUMBERS

#Integers
'''
You can add(+),substract(-),multipy(*), and divide (/) integers in Python.

>>> 2+3
5
>>> 3-2
1
>>> 2*3
6
>>> 3/2
1.5

Python uses two multiplication symbols to represent exponents:

>>> 3 ** 2
9
>>> 3 ** 3
27

Python supports the order of operations. 
>>> 2 + 3*4
14

You can also use parentheses to modify the order of operations.
>>> (2+3)*4
20

'''
#Floats
'''
>>> 0.1 + 0.1
0.2
>>> 2 * 0.1
0.2

However, be aware that you can sometimes get an arbitrary number of decimal places in your answers.

>>> 0.2 + 0.1
0.30000000000004
>>> 3 * 0.1
0.30000000000004

Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers interally.
'''
#Integers and Floats

'''
When you divide any two numbers, even if they are integers that result in a whole number, you'll always get float:

>>> 4/2
2.0

If you mix an integer and a float in any other operation, you'll get a float as well:

>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0

'''

#Underscores in Numbers

'''
When you're writing long numbers, you can group digits using underscores.
'''
universe_age=14_000_000_000
print(universe_age) # 14000000000

#Python ignores the underscores when storing these kinds of values.

#Even if they don't group the digits in threes, the value will still be unaffected.
#To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature works for both integers and floats.


#Multiple Assignment

#You can assign values to more than one variable using just a single line of code.

x,y,z=0,0,0
#Now, x=0, y=0, and z=0

#Constans
'''
Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:
'''
MAX_CONNECTIONS=500


#TRY IT YOURSELF

#2.9
print(5+3)
print(10-2)
print(4*2)
print(16/2)
#2.10
fav_num=8
message=f"My favorite number is {fav_num}."
print(message)

#Comments
"""
In Python, the hash mark(#) indicates a comment. Anything following a hash mark in your code is ignored by the Python interpreter.
"""
# Say hello to everyone.
print("Hello Python people!")

#Python ignores the first line and executes the second line.

#TRY IT YOURSELF
#2.11

num1=5
num2=6
sum=num1+num2
print(sum) #This program adds num1+num2 and assigns it to the sum variable. Then the program will show the result of the sum on the screen.


#The Zen of Python
import this

"""
Brief set of principles for writing good Python code by Tim Peters.

When you run your program , you will acces these outputs about good Python Code.

Output:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""