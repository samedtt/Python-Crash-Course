# IF STATEMENTS
"""
Python uses the values True and False to decide whether the code in an if statement should be executed.
True=Execute
False=Ignore
"""
#Checking for Equality
"""
Most conditional tests compare the current value of a variable to a specific value of interest.
= is equal sign
== is equality operator and it returns true or false due to statements.
"""
car='bmw'
if car=='bmw':
    print(True)
else:
    print(False)
#Ignoring Case When Checking for Equality
"""
Testing for equality is case sensitive in Python. For example:
>>car='Audi'
>>car=='audi'
False

If case matters, this behavior is advantageous. But if case doesn't matter and instead you just want to test the value of a variable, you can convert
the variable's value to lowercase before doing the comparison:

This test will return True no matter how the value 'Audi' is formatted becuase the test is now case insensitive.
car.lower() doesn't change the actual value that stored in variable.
"""
car='Audi'
if car.lower()=='audi':
    print(True)
else:
    print(False)

#Checking for Inequality

"""
When you want to determine whether two values are not equal, you can use the inequality operator(!=).

If these two values don't match, the code will be executed.
If these two values match, the code won't be executed.
"""
requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")

#Numerical Comparisons

#Testing numerical values is pretty straightforward.
age=18
if age==18:
    print(True)
#You can also test to see if two numbers are not equal.
answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")

"""
You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:

>> age=19
>> age<21
True
>> age<=21
True
>> age>21
False
>> age>=21
False
"""
#Using and to Check Multiple Conditions
"""
To check whether two conditions are both True simultaneously, use the keyword 'and' to combine the two conditional tests.
If each test passes, the overall expression evaluates to True.
If either test fails or if both tests fail, the expresion evaluates to False.
"""    
age_0=22
age_1=18
if age_0>=21 and age_1>=21:
    print(True)
else:
    print(False) #false
age_1=22
if age_0>=21 and age_1>=21:
    print(True) #true
else:
    print(False)    

#Using or to Check Multiple Conditions
"""
The keyword 'or' allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass.
An 'or' expression fails only when both individual tests fail.
"""    
age_0=22
age_1=18
if age_0>=21 or age_1>=21:
    print(True) #true
else:
    print(False)    
age_0=18
if age_0>=21 or age_1>=21:
    print(True)
else:
    print(False) #false

#Checking Whether a Value Is in a List
"""
To find out whether a particular value is already in a list, use the keyword 'in'.
"""    
requested_topping=['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)#True
print('pepperoni' in requested_topping)#False

#Checking Whether a Value Is Not in a List
"""
Other times, it's important to know if a value does not appear in a list.
You can use the keyword 'not' in this situation.
"""
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#Boolean Expressions
"""
A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.
"""    
#TRY IT YOURSELF
#5.1
food='pizza'
print("Is food=='pizza'? I predict True")
print(food=='pizza')
print("\nIs food=='taco'? I predict False")
print(food=='taco')
#5.2
car=['audi','mercedes','BMW']
print(car[0]=='audi')
print(car[2].lower()=='bmw')

model1=1989
model2=2004

print(model1==1989)
print(model2!=2033)
print(model1>model2)
print(model1<model2)
print(model1>=model2)
print(model1<=model2)

if model1>1979 and model2<2009:
    print("Both statements are true.")
if model1>=1999 or model2==2004:
    print(True)

print('mercedes' in car)    
print('audi' not in car)

#if Statements

"""
if conditional_test:
    do something

If the conditional test is true, Python executes the code
If test is false, Python will ignore the code    
"""
age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else Statements
"""
An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.
"""
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain
"""
It runs each conditional test in order, until one passes.
When a test passes, the code following that test is executed and Python skips the rest of the tests.
"""    
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")        

#Using Multiple elif Blocks

age=12

if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"Your admission cost is ${price}.")               

#Omitting the else Block
"""
If you have a specific final condition you're testing for, consider using a final elif block and omit the else block.
"""

age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"Your admission cost is ${price}.")                

#Testing Multiple Conditions
"""
You should use a series of simple if statements with no elif or else blocks.
This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.
"""
requested_topping=['mushrooms','extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")    
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")    
print("\nFinished making your pizza!")

"""
Output:

Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
"""

requested_topping=['mushrooms','extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni.")    
elif 'extra cheese' in requested_topping:
    print("Adding extra cheese.")    
print("\nFinished making your pizza!")

"""
This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes.

In summary, if you want only one block of code to run, use an if-elif-else chain.
If more than one block of code needs to run, use a series of independent if statements.

Output:
Adding mushrooms.

Finished making your pizza!
"""

#TRY IT YOURSELF
#5.3
alien_color="green"
if alien_color=="green":
    print("You just earned 5 points")

if alien_color=="yellow":
    print(True)
else:
    print("You just earned 5 points")    
#5.4
alien_color="yellow"
if alien_color=="green":
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")

alien_color="green"
if alien_color=="green":
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")    

#5.5
alien_color=="red"    
if alien_color=="green":
    print("Player just earned 5 points.")
elif alien_color=="yellow":
    print("Player just earned 10 points.")    
else:
    print("Player just earned 15 points.")   
#5.6
age=15
if age<2:
    print("You are a baby.")     
elif age>=2 and age<4:
    print("You are a toddler.")    
elif age>=4 and age<13:
    print("You are a kid.")    
elif age>=13 and age<20:
    print("You are a teenager.")    
elif age>=20 and age<65:
    print("You are an adult.")    
else:
    print("You are an elder.")    
#5.7    
favorite_fruits=["apple","watermelon","cherry"]
print()
if "apple" in favorite_fruits:
    print("You really like apples!")
if "watermelon" in favorite_fruits:
    print("You really like watermelons!")    
if "cherry" in favorite_fruits:
    print("You really like cherries!") 
if "banana" in favorite_fruits:
    print("You really like bananas!")  
if "orange" in favorite_fruits:
    print("You really like oranges!")         

print()
#Using if Statements with Lists
# Checking for Special Items    
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=="green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")    
print("\nFinished making your pizza!")     
#Checking That a List Is Not Empty
"""
When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
"""
print()
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")    
else:
    print("Are you sure you want a plain pizza?") #Output: Are you sure you want a plain pizza?

#Using Multiple Lists
print()
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have  {requested_topping}.")    
print("\nFinished making your pizza")        
"""
Output:
Adding mushrooms.
Sorry, we don't have  french fries.
Adding extra cheese.

Finished making your pizza
"""
#TRY IT YOURSELF
#5.8
print()
usernames=['anonymus','lion','apples','bird','admin']
for username in usernames:
    if username=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")    
#5.9
print()
usernames=[]
if usernames:
    for username in usernames:
        if username=="admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.") 
else:
    print("We need to find some users!")
#5.10
print()
current_users=['admin','btr','lion','flower','moon']
new_users=['BTR','flower','LIGHT','Space','turtle']
for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Hello {new_user.title()}, you will need to enter a new username.")
        else:
            print(f"Hello {new_user.title()}, the username is available.")    
#5.11
print()
ordinal_nums=[1,2,3,4,5,6,7,8,9]
for number in ordinal_nums:
    if number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")            

#Styling if Statements
"""
PEP 8 provides for styling conditional tests is to use a single space around comparison operators.
"""

if age < 4:
    print()
#is better than    
if age<4:
    print()

#TRY IT YOURSELF
#5.12 - Styling if Statements
print("\nStyled if Statements.")
if age < 4:
    price=0
elif age < 18:
    price=25
elif age < 65:
    price=40
else:
    price=20
print(f"Your admission cost is ${price}.")   