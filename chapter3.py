#INTRODUCING LIST

"""
A list is a collection of items in a particular order.

You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don't have to be related in any particular way.
Because a list usually contains more than one element, it's a good idea to make the name of your list plural, such as letters, digits, or names.

In Python, square brackets([]) indicate a list, and invdividual elements in the list are seperated by commas.
"""
bicycles=['trek','cannodale','redline','specialized']
print(bicycles)
#If you ask Python to print a list, Python returns it representation of the list, including the square brackets:
#Output: ['trek','cannodale','redline','specialized']


#Accessing Element in a List
"""
List are ordered collections, so you can acces any elements in a list by telling Python the position, or index, of the item desired.

To acces an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
"""

bicycles=['trek','cannodale','redline','specialized']
print(bicycles[0])

#When we ask for a single item from a list, Python returns just that element without square brackets:
#Output: trek

"""
You  can also use the string methods from Chapter 2 on any element in the list. For example, you can format the elemenet 'trek' to look more presentable by using the title() method:
"""
bicycles=['trek','cannodale','redline','specialized']
print(bicycles[0].title()) #Output: Trek



#Index Positions Start at 0, Not 1

"""
Python considers the first item in a list to be at position 0, not position 1.

The second item in a list has an index of 1. Using this counting system, you can get any element you want from a list by substracting one from its position in the list.
"""
bicycles=['trek','cannodale','redline','specialized']
print(bicycles[1])
print(bicycles[3])
# This code returns the second and fourth bicycles in the list:
#cannodale
#specialized

#Special syntax for accessing the last element in a list. If you ask for the item at index -1 , Python always returns the last item in tthe list:
bicycles=['trek','cannodale','redline','specialized']
print(bicycles[-1]) #specialized

#This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.
print(bicycles[-2]) #redline
print(bicycles[-3]) #cannodale



#Using Individual Values from a List

"""
You can use individual values from a list just as you would any other variable. 
For example, you can use f-strings to create a message based on a value from a list.
"""
bicycles=['trek','cannodale','redline','specialized']
message=f"My first bicycle was a {bicycles[2].title()}."
print(message)
#Output
# My frist bicycle was a Redline.
#We build a sentence using the value at bicycles[2] and assign it to the variable message.


#TRY IT YOURSELF
#3.1
names=["Martin","Emma","Paul","Anna"]
print(names[0]) #Martin
print(names[1]) #Emma
print(names[2]) #Paul
print(names[3]) #Anna

#3.2
names=["Martin","Emma","Paul","Anna"]
print(f"Hi {names[0]}, welcome to the Python World.")
print(f"Hi {names[1]}, welcome to the Python World.")
print(f"Hi {names[2]}, welcome to the Python World.")
print(f"Hi {names[-1]}, welcome to the Python World.")

#3.3
cars=['Mercedes','Audi','BMW','Fiat']
print(f"I would like to have an {cars[1]} car.")
print(f"{cars[2]} is better than {cars[-1]}.")
print(f"{cars[0]} has a lot of variety in the transportation field, such as air,land, and sea.")


#Modifying, Adding, and Removing Elements.
"""
Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements from it as your program runs its course.
"""

#Modifying Elements in a List

#To change an element in a list, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles) # Now output is ['ducati','yamaha','suzuki']

#Adding Elements to a List
#Appending Elements to the End of a List
"""
When you append an item to a list, the new element is added to the end of the list.
"""
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
#Here the append() method adds 'ducati' to the end of the list, without affecting any of the other elements in the list:

#Before: ['honda','yamaha','suzuki']
#After:  ['honda','yamaha','suzuki','ducati']

"""
The append() makes it easy to build list dynamically.
For example, you can start with an empty list and then add items to the list using a series of append() calls. 
Using an empty list, let's add the elements 'honda','yamaha' and 'suzuki' to the list.
"""
motorcycles=[]
print(motorcycles) #[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles) # ['honda','yamaha','suzuki']

#Inserting Elements into a List
'''
You can add a new element at any position in your list by using the insert() method.
'''
motorcycles=['honda','yamaha','suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles) #['ducati','honda','yamaha','suzuki']
# This operation shifts every other value in the list one position to the right.


#Removing Elements from a List
"""
You can remove an item according to its position in the list or according to its value.
"""
#Removing an Item Using the del Statement
"""
If you know the position of the item you want to remove from a list, you can use the del statement:
"""
motorcycles=['honda','yamaha','suzuki']
print(motorcycles) #['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles) #['yamaha','suzuki']

#You can remove an item from any position in a list using the del statement if you know its index.
motorcycles=['honda','yamaha','suzuki']
print(motorcycles) #['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles) #['honda','suzuki']

#In both examples, you can no longer acces the value that was removed from the list after the del statement is used.



#Removing an Item Using the pop() Method
"""
The pop() method removes the last item in a list, but it lets you work with that item after removing it.
"""
motorcycles=['honda','yamaha','suzuki']
print(motorcycles) # We printed all list: ['honda','yamaha','suzuki']
popped_motorcycles=motorcycles.pop() #Now we popped the last item in the lise and assigned it to the varaible.
print(motorcycles) #We printed the list without 'suzuki' : ['honda','yamaha']
print(popped_motorcycles) #We printed the popped item. Item=suzuki

"""
Imagine that the motorcycles in the list are stored in chronological order, according to when we owned them.
If this is the case, we can use the pop() method to print a statement about last motorcycle we bought:
"""
motorcycles=['honda','yamaha','suzuki'] #Chronological order
last_owned=motorcycles.pop() #We popped suzuki
print(f"The last motorcycle I owned was a {last_owned.title()}.")
#Output: The last motorcycle I owned was a Suzuki.


#Popping Items from Any Position in a List
"""
You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses:

"""
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0) #We popped honda
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#Output: The first motorcycle I owned was a Honda.

"""
Remember that each time you use pop(), the item you work with is no longer stored in the list.

When you want to delete an item from a list and not use that item in any way, use the del statement;
If you want to use an item as you remove it , use the pop() method.
"""

#Removing an Item by Value
"""
If you only know the value of the item you want to remove, you can use remove() method.
"""
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)#['honda','yamaha','suzuki','ducati'] 
motorcycles.remove('ducati') #We removed ducati from the list.
print(motorcycles)#['honda','yamaha','suzuki']
"""
You can also use the remove() method to work with a value that's being removed from a list.
"""
motorcycles=['honda','yamaha','suzuki','ducati']
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.")
#Output: A Ducati is too expensive for me.

#Note: The remove() method deletes only first occurrence of the value you specify. 
# #If there's a possibility the value appers more than once in a list, you'll need to use a loop to make sure all occurences of the value are remove.

#TRY IT YOURSELF
#3.4
guests=['Martin','Emma','Anna']
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")

#3.5
guests=['Martin','Emma','Anna']
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")
print(f"{guests[-1]} can't make it.")
guests.remove('Anna')
guests.insert(2,'Paul')
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")

#3.6
guests=['Martin','Emma','Anna']
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")
print(f"{guests[-1]} can't make it.")
guests.remove('Anna')
guests.insert(2,'Paul')
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")
print("I found a bigger table so we can invite more people.")
guests.insert(0,'Micheal')
guests.insert(2,'Oba')
guests.append('Oliver')
print(f"Hi {guests[0]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[1]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[2]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[3]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[4]}, would you like to join us to eat dinner ?")
print(f"Hi {guests[-1]}, would you like to join us to eat dinner ?")

#3.7
print(f"Dear {guests[-1]},we don't have enough seats for dinner, sorry for that problem.")
guests.pop(-1)
print(f"Dear {guests[4]},we don't have enough seats for dinner, sorry for that problem.")
guests.pop(4)
print(f"Dear {guests[3]},we don't have enough seats for dinner, sorry for that problem.")
guests.pop(3)
print(f"Dear {guests[2]},we don't have enough seats for dinner, sorry for that problem.")
guests.pop(2)
print(f"Hi {guests[0]},you're still invited.")
print(f"Hi {guests[1]},you're still invited.")
del guests[1]
del guests[0]
print(guests) # []

#Organizing a List
#Sorting a List Permanently with the sort() Method
"""
Python's sort() method makes it relatively easy to sort a list.
Imagine we have a list of cars and want to change the order of the list to store them alphabetically.
To keep the task simple, let's assume that all the values in the list are lowercase:
"""
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
"""
The sort() method changed the order of list permanently.
We can never revert to the original order:
"""
#Output:['audi', 'bmw', 'subaru', 'toyota']
"""
You can aslo sort this list in reverse-alphabetical order by passing the argument reverse=True to the sort() method.
The list of cars in reverse-alphabetical order:
"""
cars.sort(reverse=True)
print(cars)
#Again, the order of the list permanently changed:
#Output:['toyota', 'subaru', 'bmw', 'audi']

#Sorting a List Temporarily with the sorted() Function
"The sorted() function lets you display your list in a particular order, but doesn't affect the actual order of the list."
cars=['bmw','audi','toyota','subaru']
print("\nHere is the original list:")
print(cars) #['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
print("\nHere is the original list again:")
print(cars) #['bmw', 'audi', 'toyota', 'subaru']
"""
Notice that the list still exists in its original order after the sorted() function has been used.
The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.
"""
print(sorted(cars,reverse=True))#['toyota', 'subaru', 'bmw', 'audi'] 

"""
Note:
Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.
There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time.
However, most approaches to sorting will build directly on what you learned in this section.
"""

#Printing a List in Reverse Order
"""
To reverse the original order of a list, you can use the reverse() method.
"""
cars=['bmw','audi','toyota','subaru']
print(cars) #['bmw','audi','toyota','subaru'] 
cars.reverse()
print(cars) #['subaru','toyota','audi','bmw']
#Notice that reverse() doesn't sort backward alphabetically; it simply reverses the order of the list.
#The reverse method changes the order of a list permanently,but you can revert to the original order anytime by applying reverse() to the same list a second time.


#Finding the Length of a List
"""
You can quickly find the length of a list by using the len() function.
"""
cars=['bmw','audi','toyota','subaru']
print(len(cars)) #The list has 4 elements so length is 4.
#Note: Python counts the items in a list starting with one,so you shouldn't run into any off-by-one errors when determining the length of a list.

#TRY IT YOURSELF
#3.8
places=['Madrid','Rome','London','Moscow','Berlin']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#3.9
guests=['Martin','Emma','Anna']
print(len(guests))
#3.10
countries=['Turkey','USA','Russia','UK','Spain','Hungary','Italy','Japan','Brazil']
countries.append('Mexico')
countries.insert(1,'Bosnia')
del countries[2]
countries.pop()
countries.pop(3)
countries.remove('Japan')
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print(sorted(countries))
print(sorted(countries,reverse=True))
countries.reverse()
print(countries)
print(len(countries))

#Avoiding Index Error When Working with Lists
"""
Let's say you have a list with three items, and you ask for the fourth item:
"""
motorcycles=['honda','yamaha','suzuki']
print(motorcycles[3])
#This example results in an index error: 
#IndexError: list index out of range
"""
An index error means Python can't find an item at the index you requested.
If an index error occurs in your program, try adjusting the index you're asking for by one.
"""
#If the list is empty and if you ask for motorcycles[-1], it will cause an error.
motorcycles=[]
print(motorcycles[-1])
#IndexError: list index out of range
#No items are in motorcycles, so Python returns another index error.
