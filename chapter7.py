#USER INPUT AND WHILE LOOPS
#input() function
"""
The input() function pauses your program and waits for the user to enter some text.
Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.
"""
message=input("Tell me something, and I will repeat it back to you: ")
print(message)
#Using int() to Accept Numerical Input
"""
When you use input() function, Python interprets everything the user enters as a string.
When you try to use the input to do a numerical comparison, Python produces an error because it can't compare a string to an integer.
"""
age=input("How old are you? ") #String
# age>=18 # TypeError: '>=' not supported between instances of 'str' and 'int'
"""
We can resolve this issue by using the int() function, which converts the input string to a numerical value.
"""
age=input("How old are you? ")
age=int(age)
if age>=18:
    print(age>=18)#True

#The Modulo Operator
"""
A useful tool for working with numerical information is the modulo operator(%), which divides one number by another number and returns the remainder:
"""
print(4%3)#1
print(6%3)#0

#TRY IT YOURSELF
#7.1
rental_car=input("What kind of rental car do you want ? ")
print(f"Let me see if I can find you a/an {rental_car}.")
#7.2
people=int(input("How many people will be in dinner group? "))
if people>8:
    print("Your group will have to wait for a table.")
else:
    print("Table is ready.")    
#7.3
number=int(input("Enter a number: "))    
if number%10==0:
    print(f"The {number} is a multiple of 10.")
else:
    print(f"The {number} is not a multiple of 10.")    
#While Loops
"""
The for loop takes a collection of items and executes a block of code once for each item in the collection.
In contrast, the while loop runs as long as, or while, a certain condition is true.
"""    
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
#Letting the User Choose When to Quit
"""
We'll define a quit value and then keep the program running as long as the user has not entered the quit value:
"""
prompt="\nTell me something, and I will repeat it back to you:"   
prompt+="\nEnter 'quit' to end the program. " 
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
#Using a Flag
"""
For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
This variable, called a flag, acts as a signal to the program.
"""
prompt="\nTell me something, and I will repeat it back to you:"   
prompt+="\nEnter 'quit' to end the program. " 
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)    
#Using break to Exit a Loop
"""
To exit a while loop immediately without running any remaining code in the loop, regardless of the result of any conditional test, use the break statement.
The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't.
"""     
prompt="\nTell me something, and I will repeat it back to you:"   
prompt+="\nEnter 'quit' to end the program. " 
while True:
    city=input(prompt)
    if city=='quit':
        break      
    else:
        print(f"I'd love to go to {city.title()}!")
# Note: You can use the break statement in any of Python's loop.

#Using continue in a Loop
"""
Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return the beggining of the loop,
based on the result of the conditional test.
"""
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)
#TRY IT YOURSELF
#7.4
while True:
    topping=input("What topping would you like to add?\nEnter quit to end the program: ")  
    if topping=="quit":
        break
    else:
        print(f"I will add {topping} on your pizza.")  
#7.5
prompt="How old are you?"
prompt+="\nEnter 'quit' to end the program: "
while True:
    age=input(prompt)
    if age=='quit':
        break
    else:
        if int(age)<3:
            price=0
        elif int(age)<13:
            price=10
        else:
            price=15
        print(f"The ticked price is ${price}.")            
#7.6
prompt="How old are you?"
prompt+="\nEnter 'quit' to end the program: "
active=True
while active:
    age=input(prompt)
    if age=='quit':
        break
    else:
        if int(age)<3:
            price=0
        elif int(age)<13:
            price=10    
        elif int(age)==65:
            active=False
            continue
        elif int(age)>13:
            price=15
        print(f"The ticked price is ${price}.") 

#Using a while Loop with Lists and Dictionaries
#Moving Items from One List to Another

#Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#Display all confirmed users.    
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())    

#Removing All Instances of Specific Values from a List
"""
In Chapter 3, we used remove() to remove a specific value from a list.
The remove() function worked because the value we were interested in appeared only once in the list.
But what if you want to remove all instances of a value from a list?
To remove all instances of that value, you can run a while loop until instances of that value are no longer in the list.
"""
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Filling a Dictionary with User Input
"""
You can prompt for as much input as you need in each pass through a while loop.
"""

responses={}
# Set a flag to indicate that polling is active.
polling_active=True
while polling_active:
    #Promp for the person's name and response.
    name=input("\nWhat is your name?")#Key
    response=input("Which mountain would you like to climb someday? ")#Value
#Store the response in dictionary
    responses[name]=response

#Find out if anyone else is going to take the poll.
    repeat=input("Would you like to let another person respond? (yes/no) ")
    if repeat=='no':
        polling_active=False

#Polling is complete. Show the results.
print("\n--- Pool Results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")

#TRY IT YOURSELF
#7.8
sandwich_orders=['Reuben','Porilainen','Bauru','Cemita']   
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)    

print("\nThe following sandwiches are ready to eat:")
for sandwich in finished_sandwiches:
    print(sandwich)    
#7.9    
sandwich_orders=['Reuben','Pastrami','Porilainen','Pastrami','Bauru','Cemita','Pastrami']
finished_sandwiches=[]
while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
print("Deli has run out of Pastrami.")   
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches are ready to eat:")
for sandwich in finished_sandwiches:
    print(sandwich)        
#7.10
responses={}
polling_active=True
while polling_active:
    name=input("What is your name? ")#Key
    place=input("If you could visit one place in the world, where would you go? ")#Value 
    responses[name]=place   
    repeat=input("Would you like to let another person respond? (yes/no) ")
    if repeat=='no':
        polling_active=False

print("\n--- Poll Results ---")
for name,place in responses.items():
    print(f"{name.title()} would like to go {place.title()}.")