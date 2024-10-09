#CLASSES
"""
In object-oriented programming, you write classes that represent real-world things and situations, and you create objects based on these classes.
When you write a class, you define the general behovior that a whole category of objects can have.
When you create individual objects from the class, each objects is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire.
Making an object from a class is called 'instantiation', and you work with 'instances' of class.
"""
#Creating and Using a Class
"""
You can model almost anything using classes.
Let's start by writing a simple class, Dog, that represents a dog-not one dog in particular,but any dog.
What do we know about pet dogs? Well, they have all a name and an age. We also know that most dogs sit and roll over.
Those two pieces of information (name and age) and those behaviors(sit and roll over) will go in our Dog class because they're common to most dogs.
This class will tell Python how to make an object representing a dog.
"""
#Creating the Dog Class
"""
Each instance created from the Dog class will store a name and an age,and we'll give each dog the ability to sit() and roll_over():
"""
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name=name
        self.age=age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")    
"""
Capitalized names refer to classes in Python.
There are no parentheses in the class definition becuase we're creating this class from scratch.
"""        
#The __init__() Method
"""
The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class.
Make sure to use two underscores on each side of __init()__.

We define the __init__() method to have three parameters:self,name and age.
The self parameter is required in the method definition, and it must come first, before the other parameters.
It must be included in the definition because when Python calls ths method later (to create an instance of Dog), the method call will automatically pass the self argument.
Every method call associated with an instance automatically passes self, which is reference to the instance itself; it gives the individual instance acces to the attributes and methods in the class.
When we make an instance of Dog, Python will call the __init__() method from  the Dog class.
We'll pass Dog() a name an age as arguments; self is passed automatically, so we don't need to pass it.
Whenever we want to make an instance from the Dog class, we'll provide values for only the last two parameters, name and age.

The two variable defined in the body of the __init__() method each have the prefix self.
Any variable prefixed with self is available to every method in the class, and we'll also be able to acces these variables through any instance created from the class.
The line self.name=name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created.
The same process happens with the self.age=age. 
Variables that are accessible through instances like this are called 'attributes'.

The Dog class has two other methods defined: sit() and roll_over().
Because these methods don't need additional information to run, we just define them to have one parameter, self.
The instances we create later will have acces to these methods. In other words, they'll be able to sit and roll over.
For now, sit() and roll_over() don't do much. They simply print a message saying the dog is sitting or rolling over.
But the concept can be extented to realistic situations:if these class were part of a computer game, these methods would contain code to make an animated dog sit and roll over.
If this class written to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.
"""

#Making Instances from a Class
"""
Think of a class as a set of instructions for how to make an instance.
The Dog class is a set of instructions that tells Python how to make individual instances representing specific dog.

Let's make an instance representing a specific dog:
"""
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name=name
        self.age=age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")   

my_dog=Dog('Willie',6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

"""
Here, we tell Python to create a dog whose name is 'Willie' and whose age is 6.
When Python reads this line, it calls __init()__ method in Dog with the arguments 'Willie' and 6.
The __init()__ method creates an instance representing this particular dog and sets the name and age attributes using the values we provided.

Python then returns an instance representing this dog. We assign that instance to the variable my_dog.
The naming convention is helpful here; we can usually assuma that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.
"""

#Accessing Attributes
"""
To acces the attributes of an instance, you use dot notation. We acces value of the my_dog's attribute name by writing: 
my_dog.name

This syntax demonstrates how Python finds an attribute's value.Here, Python looks at the instance my_dog and then finds the attribute name associated with my_dog.
This is the same attribute referred to as self.name in the class Dog. We use the same approach to work with the attribute age.

Output:
My dog's name is Willie.
My dog is 6 years old.
"""

#Calling Methods
"""
After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
Let's make our dog sit and roll over:
"""
my_dog=Dog('Willie',6)
my_dog.sit()
my_dog.roll_over()
"""
To call a method, give the name of instance (in this case,my_dog) and the method you want to call, separated by a dot.
When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code. Python interprets the line my_dog.roll_over() in the same way.
Now Willie does what we tell him to:

Willie is now sitting.
Willie rolled over!

This syntax is quite useful. 
When attributes and methods have been given appropriately desriptive names like name,age,sit(), and roll_over(),we can easily infer what a block of code, even one we've never seen before, is supposed to do.
"""

#Creating Multiple Instances
"""
You can create as many instances from a class as you need. Let's create a second dog called your_dog:
"""
my_dog=Dog('Willie',6)
your_dog=Dog('Lucy',3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
"""
In this example we create a dog named Willie and a dog named Lucy.
Each dog is a separate instance with its own set of attributes, capable of the same set of actions:

My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.

Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class.
You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.
"""
print("\n\n")
#TRY IT YOURSELF
#9.1
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")   
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.") 

restaurant_1=Restaurant('Gold Oven','Ottoman')

print(f"{restaurant_1.restaurant_name}")
print(f"{restaurant_1.cuisine_type}")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print("\n\n")
#9.2
french_restaurant=Restaurant("Paris Streets","French")
turkish_restaurant=Restaurant("Ottoman Kebab","Turkish-Ottoman")
german_restaurant=Restaurant("Spelien","German")
french_restaurant.describe_restaurant()
print("\n")
turkish_restaurant.describe_restaurant()
print("\n")
german_restaurant.describe_restaurant()
print("\n")
#9.3
class Users:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, your age is {self.age} and gender is {self.gender}.")   

first_user=Users("Micheal","George","18","Male")
second_user=Users("Lara","Kelan","25","Female")
first_user.describe_user()
print("\n")
second_user.describe_user()
print("\n\n")
first_user.greet_user()
print("\n")
second_user.greet_user()            
print("\n\n")
#Working with Classes and Instances
"""
You can use classes to represent many real-world situations. Once you write a class, you'll spend most of your time working with instances created from that class.
One of the first tasks you'll want to do is modify the attributes associated with a particular instance.
You can modify the attributes of an instance directly or write methods that update attributes in specific ways.
"""
#The Car Class
"""
Let's write a new class representing a car. 
Our class will store information about the kind of car we're working with, and it will have a method that summarizes this information:
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())# 2024 Audi A4 
print("\n")
#Setting a Default Value for an Attribute
"""
When an instance is created, attributes can be defined without being passed in as parameters.
These attributes can be defined in the __init__() method, where they are assigned a default value.

Let's add an attribute called odometer_reading that always starts with a value of 0.
We'll also add a method read_odometer() that help us read each car's odometer.
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")    

my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print("\n")
"""
This time, Python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes, like it did in the previous example.
Then Python creates a new attribute called odometer_reading and sets its initial value to 0.
We also have a new method called read_odometer() that makes it easy to read a car's mileage.
"""
#Modifying Attribute Values
"""
You can change an attribute's value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method.
"""
#Modifying an Attribute's Value Directly
"""
The simplest way to modify the value of an attribute is to acces the attribute directly through an instance.
Here we set the odometer reading to 23 directly:
"""
my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
print("\n")
"""
We use dot notation to acces the car's odometer_reading attribute, and set its value directly.
This line tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23:

2024 Audi A4
This car has 23 miles on it
"""
#Modifying an Attribute's Value Through a Method
"""
It can be helpful to have methods that update certain attributes for you.
Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")    

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""    
        self.odometer_reading=mileage

my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
print("\n")
""" 
The only modification to Car is the addition of update_odometer().
This method takes in a mileage value and assigns it to self.odometer_reading.
Using the my_new_car instance, we call update_odometer() with 23 as an argument.
This sets the odometer reading to 23, and read_odometer() prints the reading:

2024 Audi A4
This car has 23 miles on it.

We can extend the method update_odometer() to do additional work every time the odometer reading is modified.
Let's add a little logic to make sure no one tries to roll back the odometer reading:
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")    

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage>=self.odometer_reading:   
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!") 

my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(-1)# You can't roll back an odometer!
my_new_car.read_odometer()# This car has 0 miles on it.
print("\n")

"""
Now update_odometer() checks that the new reading makes sense before modifying the attribute.
If the value provided for mileage is greater than or equal to the existing milage, self.odometer_reading, you can update the odometer reading to the new mileage.
If the new mileage is less than the existing mileage, you'll get a warning that you can't roll back an odometer.
"""            
#Incrementing an Attribute's Value Through a Method
"""
Sometimes you'll want to increment an attribute's value by a certain amount, rathen than set an entirely new value.
Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it.
Here's a method that allows us to pass this incremental amount and add that value to the odometer reading:
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")    

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage>=self.odometer_reading:   
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading+=miles

my_used_car=Car('subaru','outback',2019)       
print(my_used_car.get_descriptive_name())# 2019 Subaru Outback

my_used_car.update_odometer(23_500)
my_used_car.read_odometer() #This car has 23500 miles on it.

my_used_car.increment_odometer(100) 
my_used_car.read_odometer() #This car has 23600 miles on it.

"""
The new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading.
First, we create a used car, my_used_car.
We set its odometer to 23.500 by calling a update_odometer() and passing it 23_500.
Finally, we call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it:


2019 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.

You can modify this method to reject negative increments so no one uses this function to roll back an odometer as well.
"""
print("\n")
#TRY IT YOURSELF
#9.4
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")   
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.") 

    def set_number_served(self,number_of_customers):
        self.number_served=number_of_customers

    def increment_number(self,number):
        self.number_served+=number    

    def read(self):
        print(f"The number of customers that have been served is {self.number_served}.")    

my_restaurant=Restaurant('La Santo','Spanish')
print(my_restaurant.number_served)# 0
my_restaurant.number_served=10
print(my_restaurant.number_served)# 10

my_restaurant.set_number_served(25)
my_restaurant.read() # The number of customers that have been served is 25.

my_restaurant.increment_number(100)
my_restaurant.read() # The number of customers that have been served is 125.

#9.5
print("\n")
class Users:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, your age is {self.age} and gender is {self.gender}.")   

    def increment_login_attempts(self):
        self.login_attempts+=1    

    def reset_login_attempts(self):
        self.login_attempts=0
    

user1=Users('George','Lara','19','Male')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The number of attempts: {user1.login_attempts}") #The number of attempts: 3
user1.reset_login_attempts()
print(f"The number of attempts: {user1.login_attempts}") #The number of attempts: 0
print("\n\n")

#Inheritance
"""
You don't always have to start from scratch when writing a class.
If the class you're writing is a specialized version of another class you wrote, you can use inheritance.
When one class inherits from another, it takes on attributes and methods of the first class.
The original class is called the parent-class, and the new class is the child class.
The child class can inherit any or all of the attributes and methods of its parent class,but it's also free to define new attributes and methods of its own.
"""
#The __init__() Method for a Child Class
"""
When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the parent class.
This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.

As an example, let's model an electric car. 
An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class we wrote earlier.
Then we'll only have to write code for the attributes and behaviors specific to electric cars.

"""
class Car:
    """A simple attemp to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""    
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")        

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading=miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles.""" 

    def __init__(self,make,model,year):
        """Initialize attriubes of the parent class."""
        super().__init__(make,model,year)    
 

my_leaf=ElectricCar('nissan','leaf','2024')  
print(my_leaf.get_descriptive_name())
print("\n\n")
"""
The name of the parent class must be included in parentheses in the definition of a child class.
The __init__() method takes in the information required to make a Car instance.

The super() function is a special function that allows you to call a method from the parent class.
This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.
The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

We test whether inheritance is working properly by trying to create an electric car with the same kind of information we'd provide when making a regular car.
We make an instance of the ElectricCar class and assign it to my_leaf.
This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car.
We provide arguments 'nissan','leaf',and'2024'

Aside from __init__(), there are no attributes or method yet that are particular to an electric car.
At this point we're just making sure the electric car has the appropriate Car behaviors:

2024 Nissan Leaf

The ElectricCar instance works just like an instance of Car, so now we can begin defining attributes and methods specific to electric cars.
"""
#Defining Attributes and Methods for the Child Class
"""
Once you have a child class that inherits from a parent class, you can add any new attributes and methods necesssary to differentiate the child class from the parent class.
Let's add an attribute that's specific to electric cars (a battery,for example) and a method to report on this attribute.
"""

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""  

    def __init__(self,make,model,year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)# From parent class.
        self.battery_size=40# It's a child class attribute.

    def describe_battery(self):# It's a child class method
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf=ElectricCar('nissan','leaf','2024')
print(my_leaf.get_descriptive_name())#Parent class method
my_leaf.describe_battery() #Child class method
print("\n\n")

"""
We add a new attribute self.batter_size and set its initial value to 40.
This attribute will be associated with all instances created from the 'ElectricCar' class but won't be associaed with any instances of 'Car'.

We also add a method called describe_battery() that prints information about the battery.
When we call this method, we get a description that is clearly specific to an electric car:


2024 Nissan Leaf
This car has a 40-kWh battery.

There's no limit to how much you can specialize the ElectricCar class.
You can add as many attributes and methods as you need to model an electric car to whatever degree of accuracy you need.

"""

#Overriding Methods from the Parent Class
"""
You can override any method from the parent class that doesn't fit what you're trying to model with the child class.
To do this, you define a method in the child class with the same name as the method you want to override in the parent class.
Python will disregard the parent class method and only pay attention to the method you define in the child class.

Say the class Car had a method called fill_gas_tank().
This method is meaningless for an all-electric vehicle, so you migh want to override this method.
"""

class Car:
    """A simple attemp to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""    
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")        

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading=miles

    def fill_gas_tank(self):
        print("Filling the gas tank...")


class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        


    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't have a gas tank")

car=Car('nissan','leaf',2024)
my_electric_car=ElectricCar('nissan','leaf',2024)
car.fill_gas_tank()#Filling the gas tank...
my_electric_car.fill_gas_tank()#This car doesn't have a gas tank.
print("\n\n")

"""
Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car amd run this code instead.
When you use inheritace, you can make your child classes retain what you need and override anything you don't need from the parent class.
"""
#Instances as Attributes
"""
When modeling something from the real world in code, you may find that you're adding more and more detail to a class.
You'll find that you have a growing list of attributes and methods and that your files are becoming lengthy.

In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together, this approach is called composition.
For example, if we continue adding detail to the ElectricCar class, we might notice that we're adding many attributes and methods specific to the car's battery
When we see this happening, we can stop and move those attributes and methods to a separate class called Battery.
Then we can use a Battery instance as an attribute in the ElectricCar class:
"""
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")    

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery=Battery()

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())       
my_leaf.battery.describe_battery() #Instance as Attribute

"""
We define a new class claled Battery that doesn't inherit from any other class.
The __init__() method has one parameter, battery_size, in addition to self.
This is an optional parameter that sets the battery's size to 40 if no value is provided.
The method describe_battery() has been moved to this class as well.

In the ElectricCar class, we now add an attribute called self.battery.
This line tells Python to create a new instance of Battery(with a default size of 40, because we're not specifiying a value) and assign that instance to the attribute self.battery.
This will happen every time the __init__() method is called; any ElectricCar instance will now have a Battery instance created automatically.

We create an electric car and assign it to the variable my_leaf.
When we want to describe the battery, we need to work through the car's battery attribute.
"""
my_leaf.battery.describe_battery()

"""
This line tells Python to look at the instance my_leaf, find its battery attribute, and call the method describe_battery() that's associated with the Battery instance assigned to the attribute.

2024 Nissan Leaf
This car has a 40-kWh battery

Let's add another method to Battery that reports the range of the car based on the battery size:
"""

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery") 

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225

        print(f"This car can go about {range} miles  on a full charge.")  

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery=Battery(65)         

print("\n\n")
my_leaf=ElectricCar('nissan','leaf',2024)      
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print("\n\n")
"""
The new method get_range() performs some simple analysis.
If the battery's capacity is 40 kWh, get_range() sets the range to 150 miles, and if the capacity is 65 kWh, it sets the range to 225 miles.
It then reports this value. When we want to use this method, we again have to call it through the car's battery attribute.


2024 Nissan Leaf
This car has a 65-kWh battery
This car can go about 225 miles  on a full charge.
"""
print("\n\n")
#TRY IT YOURSELF
#9.6
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")   
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.") 

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors    

    def display_flavors(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"-{flavor}")    

my_icecream=IceCreamStand("Haka Lan","Ice Cream",["cherry","lemon"])
my_icecream.display_flavors()
print("\n\n")
#9.7
class Users:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, your age is {self.age} and gender is {self.gender}.")   

class Admin(Users):
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges=['can add post','can ban user','can delete post','can shutdown a server','can kick user']

    def show_privileges(self):
        print("Administor's set of privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")     

my_admin=Admin('Hale','Davidson','29','Male')
my_admin.show_privileges()
print("\n\n")
#9.8
class Users:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, your age is {self.age} and gender is {self.gender}.")

class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        print("Administor's set of privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")    

class Admin(Users):
    def __init__(self,first_name,last_name,age,gender,privileges):
        super().__init__(first_name,last_name,age,gender)
        self.privileges=Privileges(privileges)

admin=Admin('Lara','Croft','23','Female',['can add post','can ban user','can delete post','can shutdown a server','can kick user'])
admin.privileges.show_privileges()      
print("\n\n")
#9.9
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size):
        """Initialize the battery's attributes."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery") 

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225

        print(f"This car can go about {range} miles  on a full charge.") 

    def upgrade_battery(self):
        if self.battery_size!=65:
            self.battery_size=65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year,battery_size=40):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery=Battery(battery_size)

electric_car=ElectricCar('nissan','leaf',2024)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()

print("\n\n")


#Importing Classes
"""
As you add more functionality to your classes, your files can get long, even when you use inheritance and composition properly.
In keeping with the overall philosophy of Python, you'll want to keep your files as uncluttered as possible.
To help, Python lets you store classes in modules and then import the classes you need into your main program.
"""
#Importing a Single Class
"""
Let's create a module containing just the Car class.

We include a module-level docstring that briefly describes the contents of this module.
You should write a docstring for each module you create.

Now we make a separate file called my_car.py. This file will import the Car class and then create an instance from that class.
"""
from car9 import Car
my_new_car=Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
print("\n\n")
"""
The import statement tells Python to open the car module and import the class Car. Now we can use the Car class as if it were defined in this file.
The output is the same as we saw earlier:

2024 Audi A4
This car has 23 miles on it.
"""

#Storing Multiple Classes in a Module
"""
You can store as many classes as you need in a single module, although each class in a module should be related somehow.
The classes Battery and ElectricCar both help represent cars, so let's add them to the module.
"""
from car9v2 import ElectricCar

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print("\n\n")
"""
This has the same output as we saw earlier, even though most of the logic is hidden away in a module:

2024 Nissan Leaf
This car has a 40-kWh battery
This car can go about 150 miles  on a full charge.
"""

#Importing Multiple Classes from a Module
"""
You can import as many classes as you need into a program file. 
If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar.
"""
from car9v2 import Car,ElectricCar

my_mustang=Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
print("\n\n")
"""
You import multiple classes from a module by separating each class with a comma. 
Once you've imported the necessary classes, you're free to make as many instances of each class as you need.

2024 Ford Mustang
2024 Nissan Leaf
"""
#Importing an Entire Module
"""
You can also import an entire module and then acces the classes you need using dot notation.
This approach is simple and results in code that is easy to read. Because every call that creates an instance of class includes the module name, you won't have naming conflicts with any names used in current file.
"""
import car9v2

my_mustang=car9v2.Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf=car9v2.ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

print("\n\n")

#Importing All Classes from a Module
"""
You can import every class from a module using the following syntax:
"""
from car9v2 import *
"""
This method is not recommended.
If you need to import many classes from a module, you're better of importing the entire module and using the module_name.ClassName syntax.
"""
#Importing a Module into a Module
"""
Sometimes you'll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module.
When you store your classes in several modules, you may find that a class in one module depends on class in another module.
When this happens, you can import the required class into the first module.

For example, let's store Car class in one module (car9.py) and the ElectricCar and Battery classes in a separate module (car9v3.py).

The class ElectricCar (car9v3.py) needs acces to its parent class Car, so we import Car directly into the module. 
If we forgot this line, Python will raise an error when we try to import car9v3.py module.

Now we can import from each module (car9 and car9v3) separately and create whatever kind of car we need:
"""
from car9 import Car
from car9v3 import ElectricCar

my_mustang=Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

print("\n\n")
"""
Output:

2024 Ford Mustang
2024 Nissan Leaf

"""

#Using Aliases
"""
As you saw in Chapter 8, aliases can be quite helpful when using modules to organize your project's code.
You can use aliases when importing classes as well.

As an example, consider a program where you want to make a bunch of electric cars.
It might get tedious to type (and read) ElectricCar over and over again.
You can give ElectricCar an alias in the import statement.
"""

from car9v3 import ElectricCar as EC

my_leaf=EC('nissan','leaf',2024)

"""
You can also give a module an alias.
"""
import car9v3 as car
my_leaf=car.ElectricCar('nissan','leaf',2024)

print("\n\n")
#TRY IT YOURSELF
#9.10
from restaurant9 import Restaurant
restaurant=Restaurant("Kebab Palace","Kebab-Doner")
restaurant.describe_restaurant()
print("\n\n")
#9.11
from admin9 import Admin
admin=Admin('Lara','Croft','23','Female',['can add post','can ban user','can delete post','can shutdown a server','can kick user'])
admin.privileges.show_privileges()
print("\n\n")
#9.12
from admin9v3 import Admin
admin=Admin('Lara','Croft','23','Female',['can add post','can ban user','can delete post','can shutdown a server','can kick user'])
admin.privileges.show_privileges()
print("\n\n")

#The Python Standard Library
"""
One interesting function from the random module is randint(). 
This function takes two integer arguments and returns a randomly selected integer between (and including) those numbers.
"""
from random import randint
print(randint(1,6))
"""
Another useful function is choice(). 
This function takes in a list or tuple and returns a randomly chosen element:
"""
from random import choice
players=['charles','martina','michael','florence','eli']
first_up=choice(players)
print(first_up)

print("\n\n")
#TRY IT YOURSELF
#9.13
import random
class Die:

    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_die(self):
        for i in range(10):
            print(random.randint(1,self.sides))

six_sided=Die()
ten_sided=Die(10)
twenty_sided=Die(20)
six_sided.roll_die()
print()
ten_sided.roll_die()
print()
twenty_sided.roll_die()
print("\n\n")
#9.14
from random import choice
random_list=[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
print("Any ticket matching these 4 numbers or letters won the prize:")
for i in range(4):
    print(choice(random_list))
print("\n\n")
#9.15
my_ticket=[5,'a','d',8]
winner_ticket=[]
count=0
while True:
    rand=choice(random_list)
    winner_ticket.append(rand)
    count+=1
   
    if winner_ticket==my_ticket:
        break
    
    if len(winner_ticket)==4:
        winner_ticket=[]
    

print(f"{count} times the loop had to run to give me a winning ticket.")