#WORKING WITH LISTS

#Looping Through an Entire List
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
"""
Tells Python to pull name from the list magicians, and associate it with the variable magician. Next, we tell Python to print the name that's just been assigned to magician.
Output: 
alice
david
carolina    
"""
#Doing More Work Within a for Loop
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
"""
The only difference in this code is where we compose a message to each magician, starting with that magician's name.
Output:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
"""
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
"""
Output:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
"""

#Doing Something After a for loop
"""
Any lines of code after the for loop that are not indented are executed once without repetition.
"""
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

"""
The first two calls to print() are repeated once for each magician in the list, as you saw earlier. However, because the last line is not indented, it's printed only once:

Output:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
"""    
#Avoiding Indentation Errors
"""
Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.
"""
#Forgetting to Indent
#Always indent the line after the for statement in a loop. If you forget, Python will remind you:

magicians=['alice','david','carolina']
#for magician in magicians:
#print(magician)
"""
The call to print() should be indented, but it's not.
When Python expects an indented block and doesn't find one, it lets you know which line it had a problem with:

IndentationError: expected an indented block after 'for' statement on line 73
"""

#Forgetting to Indent Additional Lines
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")   
"""
The second call to print() is supposed to be indented, but because Python finds at least one indented line after the for statement, it doesn't report an error.
As a result, the first print() call is executed once for each name in the list because it is indented. The second print() call is not indented, so it is executed only once after the loop has finished running.

Output:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
"""
#Indenting Unnecessarily
"""
If you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indent:
"""
message="Hello Python World!"
#   print(message)
""" 
We don't need to indent the print() call, because it isn't part of a loop; hence, Python reports that error:
IndentationError: unexpected indent
"""

#Indenting Unnecessarily After the Loop
"""
If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. Sometimes this prompts Python to report an error, but often this will result in a logical error.
"""
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")   

"""
Output:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you, everyone. That was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you, everyone. That was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
"""

#Forgetting the Colon
"""
The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.
"""
magicians=['alice','david','carolina']
#for magician in magicians
    #print(magician)
#SyntaxError: expected ':'


#TRY IT YOURSELF
#4.1
pizzas=['Sicilian','California ','Margherita']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza} pizza.\n")
print("I like pizza so much.")
print("\n")    
#4.2
animals=['hawk','eagle','falcon']
for animal in animals:
    print(animal)
    print(f"The {animal} is a scout animal.\n")
print("They are really good at scouting.")


#Making Numerical Lists
#Using the range() Function
for value in range(1,5):
    print(value)#1 to 4
"""
The output never contains the end value.
"""
for value in range(1,6):
    print(value)
#This time the output starts at 1 and ends at 5.

"""
You can also pass range() only one argument, and it will start the sequence of numbers at 0.
"""
for value in range(6):
    print(value)# 0 1 2 3 4 5

#Using range() to Make a List of Numbers
"""
When you wrap list() around a call to the range() function, the output will be a list of numbers.
"""    
numbers=list(range(1,6))
print(numbers)
#[1, 2, 3, 4, 5]
"""
We can also use the range() function to tell Python to skip numbers in a given range. 
If you pass third argument to range(), Python uses that value as a step size when generating numbers.
"""
even_numbers=list(range(2,11,2))
print(even_numbers)
#The range() function starts with the value 2 and thenww adds 2 to that value. It passes the end value,11, and produces this result:
#[2, 4, 6, 8, 10]

#You can create almost any set of numbers you want to using the range() function.
squares=[]
for value in range(1,11):#1 to 10. 11 is an end value.
    square=value**2 #exponents.
    squares.append(square)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Alternative
squares=[]
for value in range(1,11):#1 to 10. 11 is an end value.
    squares.append(value**2)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Simple Statistics with a List of Numbers
"""
A few Python functions are helpful when working with lists of numbers. 
For example, you can easily find the minimum, maximum, and sum of a list of numbers:
"""
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))#0
print(max(digits))#9
print(sum(digits))#45

#List Comprehensions
"""
A list comprehension combines the for loop and the creating of new elements into one line, and automatically appends each new element.
Note that no colon is used at the end of the for statement.
"""
squares=[value**2 for value in range(1,11)]
print(squares)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#TRY IT YOURSELF
#4.3
for value in range(1,21):
    print(value)
#4.4
numbers=list(range(1,1000001))
print(numbers)
#4.5
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#4.6
for value in range(1,21,2):
    print(value)
#4.7
values=[]
for value in range(3,31):
    value*=3
    values.append(value)
print(values)
#4.8
cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#4.9
cubes=[value**3 for value in range(1,11)]
print(cubes)#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#Working with Part of a List
#Slicing a List
"""
To make a slice, you specify the index of the first and last element you want to work with.
As with the range() function, Python stops one item before the second index you specify.
"""
players=['charles','martina','micheal','florence','eli']
print(players[0:3])#['charles', 'martina', 'micheal']

#You can generate any subset of a list.
print(players[1:4])#['martina', 'micheal', 'florence']

#If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4])#['charles', 'martina', 'micheal', 'florence']

#A similar syntax works if you want a slice that includes the end of a list.
print(players[2:])#['micheal', 'florence', 'eli']

#This syntax allows you to output all of the elements from any point in your list to the end, regardless of the length of the list.
#Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list.
print(players[-3:])#['micheal', 'florence', 'eli']
#This prints the name of the last three players and will continue to work as the list of players changes in size.

"""
Note:
You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip betweem items in the specified range.
"""

#Looping Through a Slice
"""
You can use a slice in a for loop if you want to loop through a subset of the elements in a list.
"""
players=['charles','martina','micheal','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
"""
Output:
Here are the first three players on my team:
Charles
Martina
Micheal
"""    

#Copying a List
"""
To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index([:]).
This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
"""
my_foods=['pizza','falafel','carrot cake']
friends_food=my_foods[:]
print("My favorite foods are:")
print(my_foods)#['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friends_food)#['pizza', 'falafel', 'carrot cake']

"""
To prove that we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's favorite foods:
"""
my_foods=['pizza','falafel','carrot cake']
friends_food=my_foods[:]
my_foods.append('cannoli')
friends_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)#['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friends_food)#['pizza', 'falafel', 'carrot cake', 'ice cream']


"""
If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.
So now, both variables point to the same list.
"""
my_foods=['pizza','falafel','carrot cake']
friends_food=my_foods
my_foods.append('cannoli')
friends_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)#['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

print("\nMy friend's favorite foods are:")
print(friends_food)#['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']


#TRY IT YOURSELF
#4.10
countries=['Germany','Italy','Turkey','Poland','Russia','Spain','Japan']
print("The first three items in the list are:")
print(countries[:3])
print("\nThree items from the middle of the list are:")
print(countries[2:5])
print("\nThe last three items in the list are:")
print(countries[4:])
#4.11
my_pizzas=['pepperoni','california','texas']
friend_pizzas=my_pizzas[:]
my_pizzas.append('margarita')
friend_pizzas.append('marinara')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")    
for pizza in friend_pizzas:
    print(pizza)
"""
Output:

My favorite pizzas are:
pepperoni
california
texas
margarita

My friend's favorite pizzas are:
pepperoni
california
texas
marinara
"""
#4.12
print()
my_foods=['pizza','falafel','carrot cake']
friend_foods=['pasta','hamburger','taco']
print("My favorite foods are:")
for food in my_foods:
    print(food)
print()
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)
    
#Tuples
"""
Python refers to values that cannot change as immutable, and an immutable list is called tuple.
"""
#Defining a Tuple

#Once you define a tuple, you can acces individual elements by using each item's index, just as you would for a list.
#For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn't change by putting the dimensions into a tuple:
dimensions=(200,50)
print(dimensions[0])#200
print(dimensions[1])#50

#If you try to change one of the items in tuple, we will get error.
#dimensions[0]=250
#TypeError: 'tuple' object does not support item assignment

"""
Note:
Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable.
If you want to define a tuple with one element, you need to include a trailing comma.
It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.
"""
my_t=(3,)

#Looping Through All Values in a Tuple

#We can loop tuple ,just as we did with a list.
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

#Writing Over a Tuple
"""
Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple.
Python doesn't raise any errors this time, because reassigning a variable is valid:
"""
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#TRY IT YOURSELF
#4.13
buffet=('pizza','pasta','hamburger','taco','sushi')
for food in buffet:
    print(food)    
#buffet[0]='pancake' #It will give error.
print()    
buffet=('pizza','risotto','hamburger','taco','paella')
for food in buffet:
    print(food)    