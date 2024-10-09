#Functions

#Defining a Function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user() #Hello!
"""
Keyword def to inform Python that you're defining a function.
The parentheses hold that information.
The text on the second line is a comment called a docstring, which describes what function does.
A function call tells Python to execute the code in the function.
To call a function, you write the name of the function, followed by parentheses.
"""

#Passing Information to a Function
def greet_user(username):
    print(f"Hello,{username.title()}!")
greet_user('jesse')
"""
By adding username between parentheses,you allow the function to accept any value of username you specify.
The function now expects you to provide a value for username each time you call it.
"""

#Arguments and Parameters
"""
The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
The value 'jesse' in greet_user('jesse') is an example of an argument.
An argument is a piece of information that's passed from a function call to a function.
"""
#Note:
"""
People sometimes speak of arguments and parameters interchangeably.

Don't be suprised if you see the variables in function definition referred to as arguments or
the variables in a function call referred to as parameters.
"""

#TRY IT YOURSELF

#8.1
def display_message():
    print("I'm learning functions.")
display_message()    

#8.2
def favorite_book(title):
    print(f"One of my favorite book is {title.title()}.")
favorite_book("Animal Farm")

#Passing Arguments
"""
You can pass arguments to your functions in a number of ways.

You can user positional arguments, which need to be in the same order the parameters were written;
keyword arguments, where each argument consists of a variable name and a value; and list and dictionaries of values.
"""

#Positional Arguments
"""
Python must match each argument in the function call with a parameter in the function definition.
The simplest way to do this is based on the order of the arguments provided.
Values matched up this way are called positional arguments.
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

"""
In the function call, the argument 'hamster' is assigned to the parameter animal_type and the argument 'harry' is assigned to the parameter pet_name.
"""

#Multiple Function Calls
"""
You can call a function as many times as needed.
Describing a second, different pet requires just one more call to describe_pet():
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

#Order Matters in Positional Arguments
"""
You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments:
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry','hamster')
"""
Output:
I have a harry.
My harry's name is Hamster.
"""    

#Keyword Arguments
"""
A keyword argument is a name-value pair that you pass to a function.
You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion.
Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
"""
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='harry')

"""
When Python reads the function call, it knows to assign the argument 'hamster' to the parameter animal_type and the argument 'harry' to pet_name.
The order of keyword arguments doesn't matter because Python knows where each value should go.
"""
#The following two function calls are equivalent:
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
"""
Note:
When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.
"""

#Default Values
"""
If an argument for a parameter is provided in the function call, Python uses the argument value.
If not, it uses the parameter's default value.
"""
def describe_pet(pet_name,animal_type='dog'): #Default value:'dog'
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie') #keyword argument #the order of the parameters don't matter.
"""
Note that the order of the parameters in the function definition had to be changed.
Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet's name.
Python still interprets this as positional argument.
This is the reason the first parameter needs to be pet_name:

If the function called with just a pet's name, that argument will match up with the first parameter listed in the function's definition.
"""
describe_pet('willie') #positional argument #same output as the previous example. #the order of the parameters matter.


"""
To describe an animal other than a dog, you could use a function call like this:
Because an explicit argument for animal_type is provided, Python will ignore the parameter's default value.
"""
describe_pet(pet_name='harry',animal_type='hamster')#keyword argument
#or
describe_pet('harry','hamster')#positional argument
"""
Same output:
I have a hamster.
My hamster's name is Harry.

I have a hamster.
My hamster's name is Harry.
"""

#Note:
"""
When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values.
This allows Python to continue interpreting positional arguments correctly.
"""

#Equivalent Function Calls
"""
Because positional arguments,keyword arguments,and default values can all be used together, you'll often have several equivalent ways to call a function.
"""
# def describe_pet(pet_name,animal_type='dog'):
"""
With this definition, an argument always need to be provided for pet_name, and this value can be provided using the positional or keyword format.
If the animal being described is not a dog, an argument for animal_type must be included in the call and this argument can also be specified using the positional or keyword format.
"""
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
"""
Each of these function calls would have the same output as the previous examples.
It doesn't really matter which calling style you use.
"""

#Avoiding Argument Errors
"""
Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.
"""
def describe_pet(pet_name,animal_type): #Default value:'dog'
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet() #we will get error becuase arguments are missing
# TypeError: describe_pet() missing 2 required positional arguments: 'pet_name' and 'animal_type'

#TRY IT YOURSELF
#8.3
def make_shirt(size,message):
    shirt=f"The size of the shirt is {size} and the message printed on the shirt is '{message}'."
    print(shirt)
make_shirt("XL","Hello World")
make_shirt(message="Peace",size="M")
#8.4
def make_shirt(size="L",message="I love Python"):
    shirt=f"The size of the shirt is {size} and the message printed on the shirt is '{message}'."
    print(shirt)
make_shirt()
make_shirt(size="M")
make_shirt("S","I love C")  
#8.5
def describe_city(city,country="Turkey"):
    sent=f"{city.title()} is in {country.title()}."
    print(sent)
describe_city("Ankara")    
describe_city("istanbul")
describe_city("amasya")
describe_city("Moscow","Russia")


#Return Values
"""
The value the function returns is called a return value.
The return statement takes a value from inside a function and sends it back to the line that called the function.
"""
#Returning a Simple Value

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

#Making an Argument Optional

"""
Sometimes it makes sense to make an argument optional, so that people using the function can choose to provide extra information only if they want to.
You can use default values to make an argument optional.
"""

def get_formatted_name(first_name,middle_name,last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('john','lee','hooker')#If you don't write ur mid name , you will get an error.
print(musician)    


def get_formatted_name(first_name,last_name,middle_name=''):#mid name is optional because we used default a value as a empty string.
    """Return a full name, neatly formatted."""
    if middle_name:#Checks for string is empty or not.
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"    
    return full_name.title()


musician=get_formatted_name('jimi','hendrix')#If you don't write mid name here, you will not get an error.
print(musician)   #Mid name is optional. If you want to add, you can write ur mid name in function call.
                  # If you don't want to add, just leave it blank.
musician=get_formatted_name('john','lee','hooker')
print(musician)

#Returning a Dictionary
"""
A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.
"""
def build_person(first_name,last_name):
    """Return a dictionary of information about a person."""
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('jimi','hendrix')
print(musician) #{'first': 'jimi', 'last': 'hendrix'}

"""
We add a new optional parameter age to the function definition and assign the parameter the special value None, which is used when a variable has no specific value assigned to it.
You can think of None as a placeholder value.
In conditional tests, None evaluates to False.
If the function call includes value for age, that value is stored in the dictionary.
"""
def build_person(first_name,last_name,age=None): # age is optional parameter.
    """Return a dictionary of information about a person."""
    person={'first':first_name,'last':last_name}
    if age: #Controlling age is empty or not.
        person['age']=age    
    return person

musician=build_person('jimi','hendrix',27)
print(musician)#{'first': 'jimi', 'last': 'hendrix', 'age': 27}



#Using Function with a while Loop
"""
You can use functions with all the Python structures you've learned about so far.
For example, let's use the get_formatted_name() function with a while loop to greet user more formally.
"""
def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your full name:")
    print("(enter 'q' at any time to quit)")

    f_name=input("First name: ")
    if f_name=="q":
        break

    l_name=input("Last name: ")
    if l_name=="q":
        break
    
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")


#TRY IT YOURSELF
#8.6
def city_country(city,country):
    area={city:country}
    for key,value in area.items():
        print(f"{key.title()}, {value.title()}")

city_country("Ankara","Turkey")
city_country(country="USA",city="ohio")
city_country("moscow",country="russia") #Note: Positional arguments must come before keyword arguments. For example:
# city_country(city="Germany","berlin") ----> SyntaxError: positional argument follows keyword argument.
#8.7
print("\n")
def make_album(artist,album_title,number_of_songs=None):
    if number_of_songs:
        album={"Name of Artist":artist,"Album title":album_title,"Number of songs":number_of_songs}
    else:
        album={"Name of Artist":artist,"Album title":album_title}    
    for key,value in album.items():
        print(f"{key}: {value}")
    print("\n")     
make_album("Neon Streets","City lights")
make_album("Soulcraft","Broken Mirrors")
make_album("Echo Mind","Fragments")
make_album("Sky Wanderer","Daydreams",10)
    #8.8
while True:
    print("\nEnter your favorite album's informations:")
    print("(enter q at any time to quit.)\n")
        
    artist_n=input("Enter the Artist name: ")
    if artist_n.lower()=="q":
        break
    album_t=input("Enter the title of the Album: ")
    if album_t.lower()=="q":
        break
    number_of_songs=None
    choice=input("Would you like to enter the number of songs in the album (Yes/No): ")
    if choice.lower()=="yes":
        number_of_songs=input("Enter the number of songs in the album: ")
        if number_of_songs.lower()=="q":
            break
        number_of_songs=int(number_of_songs)
    print("\nThe details of your favorite album:\n")
    make_album(artist_n,album_t,number_of_songs)
    
#Passing a List
"""
You'll often find it useful to pass a list to a function, whether it's a list of names, numbers, or more complex objects, such as dictionaries.
"""    
def greet_users(names):
    """Print a simple greeting to  each user in the list."""
    for name in names:
        msg=f"Hello, {name.title()}"
        print(msg)

usernames=['hannah','ty','margot']
greet_users(usernames)

#Modifying a List in a Function
"""
When you pass a list to a function, the function can modify the list. 
Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you're dealing with large amount of data.
"""
print("\n")
def print_models(unprinted_designs,completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    show_completed_models(completed_models)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['phone case','robot pendant', 'dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)

#Preventing a Function from Modifying a List
"""
Sometimes, you'll want to prevent a function from modifying a list.
In this case, you can adress this issue by passing the function a copy of the list, not the original.
Any changes the function makes to the list will affect only copy, leaving the original list intact.
"""
print_models(unprinted_designs[:],completed_models)
"""
The slice notation [:] makes a copy of the list to send to the function.
"""

#TRY IT YOURSELF
#8.9
print("\n")
def show_messages(messages):
    for message in messages:
        print(message)

texts=['hello','python','crash','course']
show_messages(texts)
print("\n")
#8.10
def send_messages(messages,sent_messages):
    while messages:
        printing=messages.pop()
        print(f"Sending... : {printing}")
        sent_messages.append(printing)
    print("\nThe list of messages have sent:\n")    
    for message in sent_messages:   
         print(message)

texts=['hello','python','crash','course']
sent_messages=[]
send_messages(texts,sent_messages)
print(texts)# now is []
print(sent_messages)# now is ['course', 'crash', 'python', 'hello']
#8.11
print("\n")
texts=['hello','python','crash','course']
sent_messages=[]
send_messages(texts[:],sent_messages)
print(texts)# now is ['hello', 'python', 'crash', 'course'] It doesn't change because we used copy of 'texts'.
print(sent_messages) # ['course', 'crash', 'python', 'hello']

#Passing an Arbitrary Number of Arguments
"""
Sometimes you won't know ahead of time how many arguments a function needs to accept.
Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.
"""
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
"""
The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all values this function receives.
Python can handle a function call with one value and a call with three values.
It treats different calls similarly.
Note that Python packs the arguments into a tuple, even if the function receives only one value:
"""
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')

"""
Now we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:
"""
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
"""
Output:

Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

This syntax works no matter how many arguments the function receives.
"""
#Mixing Positional and Arbitrary Arguments
"""
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be places last in the function definition.
Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
"""
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
In the function definition, Python assigns the first value it receives to the parameter size.
All other values that come after are stored in the tuple toppings.
"""
#Note:
"""
You'll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
"""

#Using Arbitrary Keyword Arguments
"""
Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of information will be passed to the function.
You can write functions that accepts as many key-value pairs as the calling statement provides.
"""
def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('albert','einstein',
                          location='priceton',
                          field='physics')
print(user_profile)#{'location': 'priceton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
"""
The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want.
The double asterisks before the parameter **user_info cause Python to create a dictionary called user_info containing all extra name-value pairs the function receives.
The function will work no matter how many additional key-value pairs are provided in the function call.
"""

#Note:
"""
-You'll often see the parameter name **kwargs used to collect nonspecific keyword arguments.

-*args becomes before **kwargs
-positional arguments becomes before *args and **kwargs.
-keyword argument becomes after *args and positional arguments and becomes before **kwargs.
"""
#For example:
def example_func(pos1, pos2, *args, kwarg1=None, kwarg2='default', **kwargs):
    pass    
"""
First and second ---> positional
Third ---> arbitrary positional argument
Fourth and Fifth ---> keyword argument
Sixth ---> arbitrary keyword argument
"""
"""
We dont' use asterisks in print function.
print("args:",args)
print("kwargs:",kwargs)
"""

#TRY IT YOURSELF
#8.12
def make_sandwich(*ingridents):
    print("\nMaking a sandwich with the following ingridents:")
    for ingrident in ingridents:
        print(f"- {ingrident}")

make_sandwich('cheese')
make_sandwich('tomato','lettuce','olive')
make_sandwich('honey','jam')
#8.13
def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('Samed','Tevin',age=20,nationallity='Turkish',hobby='computer games')
print(user_profile)
#8.14
def make_car(manufacturer,model_name,default_tires=True,**details):
    details['manufacturer']=manufacturer
    details['model_name']=model_name
    details['default tires']=default_tires
    return details
car=make_car('nissan','sedan',False,color='blue',model=2020)
print(car)    

#Storing Your Functions in Modules
"""
You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program.
An import statement tells Python to make the code in module available in the currently running program file.
Storing your functions in a separate file allows you to hide the details of your program's code and focus on its higher-level logic.
It also allows you to reuse functions in many different programs.
"""
#Importing an Entire Module
"""
A module is a file ending in .py that contains the code you want to import into your program.

Our module is pizzacp8.py
"""
import pizzacp8
pizzacp8.make_pizza(16,'pepperoni')
pizzacp8.make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
Output:
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
"""

"""
This is first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program.
If you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax:
"""
#module_name.function_name()#


#Importing Specific Functions
"""
You can also import a specific function from a module. Here's the general syntax for this approach:
"""
# from module_name import function_name #
"""
You can import as many functions as you want from a module by separating each function's name with a comma:
"""
# from module_name import function_0,function_1,function2 #

from pizzacp8 import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
With this syntax, you don't need to use the dot notation when you call a function.
Because we've explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.
"""

#Using as to Give a Function an Alias
"""
If the name of function you're importing might conflict with an existing name in your program, or if the function name is long, you can use a short,unique alias-an alternate name similar to a nickname for the function.
You'll give the function this special nickname when you import the function.
"""
from pizzacp8 import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

"""
The import statement shown here renames the function make_pizza() to mp() in this program.
Anytime we want to call make_pizza() we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file.

The general syntax for providing an alias is:
"""
# from module_name import function_name as fn #

#Using as to Give a Module an Alias
"""
You can also provide an alias for a module name.
Giving a module a short alias, like p for pizzacp8, allows you to call the module's functions more quickly.
"""
import pizzacp8 as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
The module pizza is given the alias p in the import statement, but all of the module's functions retain their original names.
"""
# import module_name as mn #

#Importing All Functions in a Module
"""
You can tell Python to import every function in a module by using the asterisk (*) operator:
"""
from pizzacp8 import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
The asterisk in the import statement tells Python to copy every function from the module pizzacp8 into this program file.
Because every function is imported, you can call each function by name without using the dot notation.

However, it's best not to use this approach when you're working with larger modules that you didn't write:
if the module has a function name that matches an existing name in your project, you can get unexpected results.
"""
# from module_name import * #

#TRY IT YOURSELF
#8.15
import printing_models8
unprinted_designs=['phone case','robot pendant', 'dodecahedron']
completed_models=[]
printing_models8.print_models(unprinted_designs,completed_models)

#8.16
import hello_world8
hello_world8.hello('Samet')
from hello_world8 import hello
hello('Samet')
from hello_world8 import hello as hl
hl('Samet')
import hello_world8 as hl8
hl8.hello('Samet')
from hello_world8 import *
hello('Samet')