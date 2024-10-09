#DICTIONARIES
"""
A dictionary in Python is a collection of key-value pairs.
Each key is connected to a value, and you can use a key to acces the value associated with that key.
A key's value can be a number, a string, a list or even another dictionary.
In fact, you can use any object that you can create in Python as a value in dictionary.
A dictionary is wrapped in braces({}) with a series of key-value pairs inside the braces.
"""
alien_0={'color':'green','points':5}

"""
When you provide a key, Python returns the value associated with that key.
"""

#Accessing Values in a Dictionary
"""
To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.
"""
alien_0={'color':'green'}
print(alien_0['color'])#green

#Adding New Key-Value Pairs
"""
Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets, along with new value.
"""
alien_0={'color':'green'}
print(alien_0)#{'color': 'green'}
#add statement
alien_0['x position']=0
alien_0['y position']=25
print(alien_0)#{'color': 'green', 'x position': 0, 'y position': 25}

#Starting with an Empty Dictionary
"""
To start filling an empty dictionary, define a dictionary with an epmty set of braces and then add each key-value pair on its own line.
"""

alien_0={}#Empty
alien_0['color']='green'
alien_0['points']=5

print(alien_0)#{'color': 'green', 'points': 5}

#Modifying Values in a Dictionary
"""
To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
"""
alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}.")#green
alien_0['color']='yellow'
print(f"The alien color is now {alien_0['color']}.")#yellow

#Removing Key-Value Pairs
"""
You can use del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to remove.
Be aware that the deleted key-value pair is removed permanently.
"""
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)#{'color': 'green'}

#A dictionary of Similar Objexts
"""
The previous example involved storing different kinds of information about one object, an alien in game.
You can also use a dictionary to store one kind of information about many objects.

For example a poll of favorite programming languages:
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phill':'python',#comma doesn't need for last key-value pair but its good because you are ready to add new key-value pair on the next line.
}

langauge=favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {langauge}.")

#Using get() to Acces Values
"""
Using keys in square brackets to retrieve the value you're interested in from a dictionary might cause one problem:
IF KEY DOESN'T EXISTS, YOU WILL GET AN ERROR

For example:
"""
alien_0={'color':'green','speed':'slow'}
# print(alien_0['points']) #Error : KeyError: 'points'

"""
You can use the get() method to set a value that will be returned if the requested key doesn't exist.

The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist.
"""
alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point value assigned.')
color_value=alien_0.get('color','No color value assigned.')
print(color_value) # it exists so value is 'green'
print(point_value)# it doesn't exist so value is 'No point value assigned.'
"""
If the key exist in the dictionary, you will get the corresponding value.
If it doesn't, you get the default value.
"""

"""
If there's a chance the key you're asking for might not exist, consider using get() method instead of the square bracked notation.

Note:
If you leave out second argument in the call to get() and the key doesn't exist, Python will return the value None.
None means 'no value exists'.
This is not an error: it's a special value meant to indicate the absence of a value.
"""
alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points')
print(point_value)#None

#TRY IT YOURSELF
#6.1
person={'first_name':'Martin','last_name':'Victor','age':'22','city':'London'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
#6.2
fav_num={
    'Martin':5,
    'Lara':2,
    'Polly':6,
    'Clara':1,
    'Samuel':9
}
print(fav_num)
#6.3
dictionary={
    'data':'a set of informations',
    'AI':'Artifical Intelligence',
    'loop':'Iteration',
    'Syntax':'Grammar of the code',
    'input':'Gets value from user'

}
print()
print(f"Data: {dictionary['data']}.\n")
print(f"AI: {dictionary['AI']}.\n")
print(f"Loop: {dictionary['loop']}.\n")
print(f"Syntax {dictionary['Syntax']}.\n")
print(f"Input: {dictionary['input']}.")

#Looping Through a Dictionary
#Looping Through All Key-Value Pairs
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
"""
If you want to see everything stored in dictionary, you could loop through the dictionary using a for loop.
The method items(), which returns a sequence of key-value pairs.
The for loop then assigns each of these pairs to the two variables provided.
"""
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
"""
Output:

Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
"""    
#Looping Through All the Keys in a Dictionary
"""
The keys() method is useful when you don't need to work with all of the values in a dictionary.
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
for name in favorite_languages.keys():
    print(name.title())
"""
Output:
Jen
Sarah
Edward
Phil
"""
print()
"""
You can choose to use keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.
"""
for name in favorite_languages:
    print(name.title())
"""
Output:
Jen
Sarah
Edward
Phil
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
"""
The keys() method isn't just for looping: it actually returns a sequence of all the keys.
You can also use the keys() method to find out if a particular person was polled.
"""
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our pool.")

#Looping Through a Dictionary's Keys in a Particular Order
"""
Looping through a dictionary returns the items in the same order they were inserted.
You can use sorted() function to get a copy of the keys in order.
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
"""
Sorted Output:
Erin, please take our pool.
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
"""    
#Looping Through All Values in a Dictionary
"""
You can use the values() method to return a sequence of values without any keys.
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
"""
Output:
The following languages have been mentioned:
Python
C
Rust
Python
"""
print()

"""
To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique:
"""
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

"""
When you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items.
The result is nonrepetitive list of languages that have been mentioned by people taking the pool:

The following languages have been mentioned:
Rust
C
Python
"""

#Note:
"""
You can build a set directly using braces and separating the elements with commas:
"""
languages={'python','rust','python','c'}
print(languages) #Output: {'c', 'rust', 'python'}
"""
It's easy to mistake set for dictionaries becuase they're both wrapped in braces.
When you see braces but no key-value pairs, you're probably looking at a set.
Unlike list and dictionaries, sets do not retain items in specific order.
"""
#TRY IT YOURSELF
#6.4
print()
dictionary={
    'data':'a set of informations',
    'AI':'Artifical Intelligence',
    'loop':'Iteration',
    'Syntax':'Grammar of the code',
    'input':'Gets value from user',
    'integer':'whole numbers',

}
for key,value in dictionary.items():
    print(f"{key.title()}: {value}")

print()

#6.5
rivers={
    'nile':'egypt',
    'amazon':'brazil',
    'lena':'russia',
}
for key,value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")
print()   
for river in rivers.keys():
    print(river)
print()
for country in rivers.values():
    print(country)    
print()    
#6.6
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
people=['jen','sarah','edward','phil','michael','william','emma']
for person in people:
    if person in favorite_languages.keys():
        print(f"Dear {person.title()},thank you for joining our pool.")
    else:
        print(f"Dear {person.title()}, would you like to join our pool?")    
#Nesting
"""
You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.
"""
#A List of Dictionaries
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
print()
"""
A more realistic example:
"""
#Make an empty list for storing aliens.
aliens=[] #We are storing dictionaries(about aliens) in list.
#Make 30 green aliens.
for alien_number in range(30):
    new_alien={'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]: #modifying some aliens.
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")    
"""
It's common to store a number of dictionaries in a list,
when each dictionary contains many kinds of information about one object.
"""
#A List in a Dictionary
"""
You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key in a dictionary.
"""
#Store information about a pizza being ordered.
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
#Summarize the order
"""
When you need to break up a long line in a print() call, choose an appropriate point at which to break the line being printed, and end the line with a quotation mark.
Python will automatically combine all of the strings it finds inside the parentheses.
"""
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

print()
"""
In the earlier example of favorite programming languages, if we were to store each person's responses in a list, people could choose more than one favorite language.
"""    
favorite_languages={
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    if len(languages)>1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
#A Dictionary in a Dictionary
"""
You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.
The value associated with each key is a dictionary that includes each user's first name, last name, and location.
"""
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcruie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#TRY IT YOURSELF
#6.7
print()
person_1={'first_name':'Martin','last_name':'Victor','age':'22','city':'London'}
person_2={'first name':'Emma','last name':'Thunder','age':'45','city':'New York'}
person_3={'first name':'Robert','last name':'Oldan','age':'63','city':'Rome'}
people=[person_1,person_2,person_3]
for person in people:
    for key,value in person.items():
        print(f"{key}: {value}")
    print()
#6.8
pet_1={'kind':'cat','owner':'emma'}
pet_2={'kind':'dog','owner':'robert'}
pet_3={'kind':'fish','owner':'martin'}
pets=[pet_1,pet_2,pet_3]
for pet in pets:
    for key,value in pet.items():
        print(f"{key.title()}:{value.title()}")
    print()    
#6.9    
places=[]
favorite_places={
    'Robert':['moscow','ohio','rome'],
    'Martin':['barcelona','madrid','sofia'],
}
print("Emma, could you suggest me three cities?")
for i in range(3):
    place=input("")
    places.append(place)
print()
favorite_places['Emma']=places
for key,values in favorite_places.items():
    print(f"{key}'s favorite places are:")
    for value in values:
        print(f"{value.title()}")
    print()
#6.10
fav_num={
    'Martin':[2,3,6],
    'Lara':[9,4,1],
    'Polly':[8,5,0],
    'Clara':[7,9,2],
    'Samuel':[5,6,1]
}
for key,values in fav_num.items():
    print(f"{key}'s favorite numbers are: {values}")
#6.11
print()
cities={
    'london':{
        'country':'uk',
        'population':'9.5 million',
        'one fact':'london has 170 museums'
    },
    'ankara':{
        'country':'turkey',
        'population':'5.1 million',
        'one fact':'Ankara became the capital of Turkey in 1923.'
    },
    'berlin':{
        'country':'germany',
        'population':'3.8 million',
        'one fact':'Berlin has over 180 museums.'
    }

}    
for key,value in cities.items():
    print(f"Some informations about {key.title()}:")
    for key,information in value.items():
        print(f"{key}: {information.title()}")
    print()





    





    
