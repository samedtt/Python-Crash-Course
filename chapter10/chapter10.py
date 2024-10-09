#FILES AND EXCEPTIONS

#Reading from a File

#Reading the Contents of a File
"""
Let's start with a file that contains pi to 30 decimal places, with 10 decimal places per line:
3.1415926535
  8979323846
  2643383279

Here's a program that opens this file, reads it, and prints the contents of the file to the screen:
"""
from pathlib import Path
path=Path('pi_digits10.txt')
contents=path.read_text()
print(contents)
"""
To work with the contents of a file, we need to tell Python the path to the file.
A path is the exact location of a file or folder on a system.
Python provides a module called pathlib that makes it easir to work with files and directories, no matter which operating system you or your program's users are working with it.

Once we have a Path object representing pi_digits10.txt, we use the read_text() method to read the entire contents of the file.
The contents of the file are returned as a single string, which we assign to the variable contents.

The only difference between output and original file is the extra blank line at the end of the output.
The blank line appears because read_text() returns an empty string when it reaches the end of the file; this empty string shows up as blank line.

We can remove the extra blank line by using rstrip() on the contents string:

"""
from pathlib import Path
path=Path('pi_digits10.txt')
contents=path.read_text()
contents=contents.rstrip()
print(contents)
"""
Recall from Chapter 2 that Python's rstrip() method removes, or strips, any whitespace characters from the right side of a string.
Now the output matches the contents of the original file exactly:
3.1415926535
  8979323846
  2643383279
We can strip the trailing newline character when we read the contents of the file, by applying the rstrip() method immediately after calling read_text():
"""
content=path.read_text().rstrip()
"""
This line tells Python to call the read_text() method on the file we're working with.
Then it applies the rstrip() method to the string that read_text() returns.
The cleaned-up string is then assigned to the variable contents. 
This approach is called method chaining, and you'll see it used often in programming.
"""
#Relative and Absolute File Paths
"""
There are two main ways to specify paths in programming. 
A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored.
Since text_files folder is inside python_work folder, we need to build a path that starts with the directory text_files, and ends with the filename.
Here's how to build this path:
"""
path=Path('text_files/filename.txt')
"""
You can also tell Python to exatly where the file is on your computer, regardless of where the program that's being executed is stored.
This is called an absolute_file path.
You can use an absolute path if a relative path doesn't work.
Absolute paths are usually longer than relative paths, because they start at your system's root folder:
"""
path=Path('/home/eric/data_files/text_files/filename.txt')

#Note:
"""
Windows systems use a backslash (/) instead of forwards slash (\) when displaying file paths, but you should use forward slashes in your code, even on Windows.
The pathlib library will automatically use the correct representation of the path when it interacts with your system, or any user's system.
"""

#Accessing a File's Lines
"""
When you're working with a file, you'll often want to examine each line of the line.
You might be looking for certain information in the file, or you might want to modify the text in the file in some way.

For example, you might want to read through a file of wheather data and work with any line that includes the word 'sunny' in the description of that day's weather.
In a news report, you might look for any line with tag <headline> and rewrite that line with a specific kind of formatting.

You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time:
"""
print()
from pathlib import Path

path=Path('pi_digits10.txt')
contents=path.read_text()

lines=contents.splitlines()
print(lines)#['3.1415926535', '  8979323846', '  2643383279']
print()
for line in lines:
    print(line)
"""
We start out by reading the entire contents of the file, as we did earlier.
If you're planning to work with the individual lines in a file, you don't need to strip any whitespace when reading the file.
The splitlines() method returns a list of all lines in the file, and we assign this list to the variable lines.
We then loop over these lines and print each one:
3.1415926535
  8979323846
  2643383279
Since we haven't modified any of the lines, the output matches the original text file exactly.  
"""
#Working with a File's Contents
"""
After you've read the contents of a file into memory, you can do whatever you want with that data, so let's briefly explore the digits of pi.
First, we'll attempt to build a single string containing all the ditis in the file with no whitespace in it:
"""
print()
from pathlib import Path

path=Path('pi_digits10.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line

print(pi_string)
print(len(pi_string))
"""
We create a variable, pi_string, to hold the digits of pi. 
We write a loop that adds each line of digits to pi_string
We print this string, and also show how long the string is:

3.1415926535  8979323846  2643383279
36

The variable pi_string contains whitespace that was on the left side of the digits in each line, but we can get rid of that by using lstrip() on each line:
"""
print()
pi_string=""
for line in lines:
    pi_string+=line.lstrip()

print(pi_string)
print(len(pi_string))
print()
"""
Now we have a string containing pi to 30 decimal places. 
The string is 32 characters long because it also includes the leading 3 and a demical point:

3.141592653589793238462643383279
32
"""
#Note:
"""
When Python reads from a text file, it interprets all text in the file as a string.
If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the int() function or a float using the float() function.
"""

#Large Files: One Million Digits
"""
If we start with a text file that contains pi to 1,000,000 decimal places, instead of just 30, we can create a single string containing all these digits.
We don't need to change our program at all, except pass it a different file.
We'll also print just the first 50 decimal places, so we don't have to watch a million digits scroll by in the terminal:
"""
from pathlib import Path

path=Path('pi_million_digits10.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=""
for line in lines:
    pi_string+=line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
print()
"""
The output shows that we do indeed we have a string containing pi to 1,000,000 decimal places:
3.14159265358979323846264338327950288419716939937510...
1000002

Python has no inherent limit to how much data you can work with; you can work with as much data as your system's memory can handle.
"""
#Is Your Birthday Contained in Pi?
"""
Let's use the program we just wrote to find out if someone's birthday appers anywhere in the first fifty digits of pi.
We can do this by expressing each birthday as a string of digits and seeing if that string appers anywhere in pi_string:
"""
from pathlib import Path

path=Path('pi_million_digits10.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=""
for line in lines:
    pi_string+=line.lstrip()

birthday=input("Enter your birthday, in the form mmddyy:\n")
if birthday in pi_string:
    print("Your birthday appers in the first fifty digits of pi.")
else:
    print("Your birthday does not appear in the first fifty digits of pi.")    
print()
#TRY IT YOURSELF
#10.1
from pathlib import Path
path=Path('my_learning10.txt')
contents=path.read_text()
lines=contents.splitlines()
print(contents)
print()
for line in lines:
    print(line)
print()    
#10.2
"""
You can use the replace() method to replace any word in a string with different word.
For example:
message="I really like dogs."
message.replace('dog','cat')
I really like cats.
"""    
from pathlib import Path
path=Path('my_learning10.txt')
contents=path.read_text()
print(contents.replace('Python','C++'))
print()
#10.3
from pathlib import Path
path=Path('my_learning10.txt')
contents=path.read_text()
for line in contents.splitlines():
    print(line)
print()   

#Writing to a File

#Writing a Single Line
"""
Once you have a path defined, you can write to a file using the write_text() method.
To see how this work, let's write a simple message and store it in a file instead of printing it to the screen:
"""
from pathlib import Path

path=Path('programming10.txt')
path.write_text('I love programming.')
"""
The write_text() method takes a single argument: the string that you want to write to the file.
This program has no terminal output, but if you open the file programming.txt, you'll see one line:

I love programming.

This file  behaves like any other file on your computer. 
You can open it, write new text in it, copy from it, paste to it, and so forth.
"""
#Note:
"""
Python can only write strings to a text file. 
If you want to store numerical data in a text file, you'll have to convert the data to string format first using the str() function.
"""

#Writing Multiple Lines
"""
The write_text() method does a few things behind the scenes. 
If the file that path points to doesn't exist, it creates a file. Also, after writing the string to the file, it makes sure the file is closed properly.
Files that aren't closed properly can lead to missing or corrupted data.

To write more than one line to a file, you need to build a string containing the entire contents of the file, and then call write_text() with that string.
"""
from pathlib import Path

contents="I love programming.\n"
contents+="I love creating new games.\n"
contents+="I also love working with data.\n"

path=Path('programmingv2-10.txt')
path.write_text(contents)
"""
You can also use spaces, tab characters, and blank lines to format your output, just as you've been doing with terminal-based output.
There's no limit to length of your strings, and this is how many computer-generated documents are created.
"""
#Note
"""
Be careful when calling write_text() on a path object. 
If the file already exists, write_text() will erase the current contents of the file and write new contents to the file.
Later in this chapter, you'll learn to check whether a file exists using pathlib.
"""

#TRY IT YOURSELF
#10.4
from pathlib import Path

path=Path('guest.txt')
name=input("Enter your name: ")
path.write_text(name)

#10.5
pathv2=Path('guest_book.txt')
guest_list=""
while True:
    name=input("Enter the name(press q-Quit): ")
    if name.lower()=='q':
        break
    guest_list+=name
    guest_list+="\n"
pathv2.write_text(guest_list) 

#Exceptions
"""
Python uses special objects called exceptions to manage errors that arise during a program's execution.
Whenever an error occures that makes Python unsure of what to do next, it creates an exception object.

Exceptions are handled with try-except block.
A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.
When you use try-except blocks, your program will contniue running even if things start to go wrong.
Instead of tracebacks, which can be confusing for users to read, users will see friendly error message that you've written.
"""

#Handling the ZeroDivisionError Exception
"""
Let's look at a simple error that causes Python to raise an exception.
You probably know that it's impossible to divide a number by zero, but let's ask Python to do it anyway:

print(5/0)

Traceback (most recent call last):
  File "/Users/samedtevin/Desktop/Python/chapter10.py", line 325, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero

The error reported in the traceback, ZeroDivisionError, is an exception object.
Python creates this kind of object in response to a situation where it can't do what we ask it to.
When this happens, Python stops the program and tells us to the kind of exception that was raised.
We can use this information to modify our program.
"""
#Using try-except Blocks
"""
When you think an error may occur, you can write a try-except block to handle the exception that might be raised.
You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception.
Here's what a try-except block for handling the ZeroDivisionError exception looks like:
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")    
"""
If the code in a try block works, Python skips over the except block.
If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised, and runs the code in that block.

If more code followed the try-except block, the program would continue running because we told Python how to handle the error.
Let's look at an example where catching an error can allow a program to continue running.
"""    
#Using Exceptions to Prevent Crashes
"""
Handling errors correctly is especially important when the program has more work to do after the error occurs.
This happens often in programs that prompt users for input.
If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing.
"""
print("Give me two numbers, and I'll divide them.")
print("Enter q to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number=='q':
        break
    second_number=input("\nSecond number:")
    if second_number=='q':
        break
    answer=int(first_number)/int(second_number)
    print(answer)
"""
This program does nothing to handle errors, so asking it to divide by zero causes it to crash.
"""
print("\n\n")
#The else Block
"""
We can make this program more error resistant by wrapping the line that might produce errors in a try-except block.
The error occurs on the line that performs the divison, so that's where we'll put the try-except block.
This example also includes an else block. Any code that depens on the try block executing succesfully goes in the else block:
"""
print("\n\nGive me two numbers, and I'll divide them.")
print("Enter q to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
print("\n\n")
"""
The only code that should go in a try block is code that might cause an exception to be raised.
Sometimes you'll have additional code that should run only if the try block was succesful; this code goes in the else block.
The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block.
"""

#Handling the FileNotFoundError Exception
"""
One common issue when working with files is handling missing files.
The file you're looking for might be in a different location, the filename might be mispelled, or the file might not exist at all.
You can handle all of these situations with try-except block.

The following program tries to read in the contents of Alice in Wonderland, but I haven't saved the file alice.txt in the same directory as alice.py:

from pathlib import Path

path=Path('alice.txt')
contents=path.read_text(encoding='utf-8')

Note that we're using read_text() in a slightly different way here than what you saw earlier.
The encoding argument is needed when your system's default encoding doesn't match the encoding of the file that's being read.
This is most likely to happen when reading from a file that wasn't created on your system.

Python can't read from a missing file, so it raises and exception:

Traceback (most recent call last):
  File "/Users/samedtevin/Desktop/Python/chapter10.py", line 413, in <module>
    contents=path.read_text(encoding='utf8')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/pathlib.py", line 1027, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

On the last line, we can see that a FileNotFoundError exception was raised.
This is important because it tells us what kind of exception to use in the except block that we'll write.

Looking back near the beggining of the traceback, we can see that the error occured at line 413 in the file.
The next line shows the line of code that caused the error.
The rest of the traceback shows some code from the libraries that are involved in opening and reading from files.

To handle the error that's being raised, the try block will begin with the line that was identified as problematic in the tracebook.
"""
from pathlib import Path
path=Path('alice.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
print("\n\n")    
"""
In this example, the code in the try block produces a FileNotFoundError, so write an except block that matches that error.
Python then runs the code in that block when the file can't be found, and the result is a friendly error message instead of traceback:

Sorry, the file alice.txt does not exist.
"""
#Analyzing Text
"""
Let's pull in the text of Alice in Wonderland and try to count the number of words in the text.
To do this, we'll use the string method split(), which by default splits a string whever it finds any whitespace:
"""
from pathlib import Path

path=Path('alicev2-10.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")    
else:
    #Count the approximate number of words in the file:
    words=contents.split()
    num_words=len(words)
    print(f"The file {path} has about {num_words} words.")

print("\n\n")
"""
We take the string contents, which now contains the entire text of Alice in Wonderland as one long string, and use split() to produce a list of all the words in the book.
Using len() on the list gives us a good approximation of the number of words in the original text.
Lastly, we print a statement that reports how many words were found in the file.
This code is placed in the else block because it only works if the code in the try block was executed succesfully.

The output tells us how many words are in alicev2-10.txt:

The file alicev2-10.txt has about 1616 words.

"""

#Working with Multiple Files
"""
Let's add more books to analyze, but before we do, let's move the bulk of this program to a function called count_words().
This will make it easier to run the analysis for multiple books:
"""
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words=contents.split()
        num_words=len(words)
        print(f"The file {path} has about {num_words} words.")        
path=Path('alicev2-10.txt')        
count_words(path)
print("\n\n")

"""
Most of this code is unchanged. It's only been indented, and moved into the body of count_words().
It's a good habit to keep comments up to date when you're modifiyng a program, so the comment has also been changed to a docstring and reworded slightly.

Now we can write a short loop to count the words in any text we want to analyze.
We do this by storing the names of the files we want to analyze in a list, and then we call count_words() for each file in the list.
We'll try to count the words for Alice in Wonderland, Siddhartha, Moby Dick and Little Women.

I've intentionally left sidhartha-10.txt out of directory containing word_count.py, so we can see how well our program handles a missing file:
"""
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words=contents.split()
        num_words=len(words)
        print(f"The file {path} has about {num_words} words.")        

filenames=['alicev2-10.txt','siddhartha-10.txt','moby_dick-10.txt',
           'little_women-10.txt']

for filename in filenames:
    path=Path(filename)
    count_words(path)

print("\n\n")
"""
The names of the files are stored as simple strings. Each string is then converted to a Path object, before the call to count_words().
The missing siddhartav2-10.txt has no effect on the rest of the program's execution:

The file alicev2-10.txt has about 1616 words.
Sorry, the file siddhartha-10.txt does not exist.
The file moby_dick-10.txt has about 611 words.
The file little_women-10.txt has about 505 words.

Using the try-except block in this example provides two significant advantages.
We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it's able to find.
If we don't catch the FileNotFoundError that siddhartha-10.txt raises, the user would see a full traceback, and the program would stop running after trying to analyze Siddharta.
It would never analyze Moby Dick or Little Women.
"""
#Failing Silently
"""
In the previous example, we informed our users that one of the files was unavailable.
But you don't need to report every exception you catch.
Sometimes, you'll want the program to fail silently when an exception occurs and continue on as if nothing happened.

To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in except block.
Python has a pass statement that tells it to do nothing in a block:
"""
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words=contents.split()
        num_words=len(words)
        print(f"The file {path} has about {num_words} words.")        

filenames=['alicev2-10.txt','siddhartha-10.txt','moby_dick-10.txt',
           'little_women-10.txt']

for filename in filenames:
    path=Path(filename)
    count_words(path)

print("\n\n")
"""
Now when a FileNotFoundError is raised, the code in except block runs, but nothing happens.
No traceback is produced, and there's no output in response to the error that was raised.
Users see the word counts for each file that exists, but they don't see any indication that a file wasn't found:

The file alicev2-10.txt has about 1616 words.
The file moby_dick-10.txt has about 611 words.
The file little_women-10.txt has about 505 words.

The pass statement also acts as a placeholder. It's reminder that you're choosing to do nothing at a specific point in your program's execution and that you might want to do something there later.
For example, in this program we might decide to write any missing filenames to a file called missing_files.txt. Our users wouldn't see this file, but we'd be able to read the file and deal with any missing texts.
"""
#TRY IT YOURSELF
#10.6
try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
except ValueError:
    print("\nYou have entered non-numerical input\n")
else:
    print(f"\nTotal is {num1+num2}.\n")        
#10.7
print("\n\nEnter two numbers to add them.\n")
print("Enter 'q' to end the program.\n")
while True:
    num1=input("Enter the first number: ")
    if num1=='q':
        break
    num2=input("Enter the second number: ")
    if num2=='q':
        break
    try:
        num1=int(num1)
        num2=int(num2)
    except ValueError:
        print("\nYou have entered non-numerical input.\n\n")
    else:
        print(f"\nTotal is {num1+num2}.\n\n")
#10.8
print("\n\n")
from pathlib import Path


path=Path('dog.txt')
try:
    contents=path.read_text(encoding='utf-8') 
except FileNotFoundError:
    print(f"{path} is missing.") 
else:
    print("Dog names are:")
    print(contents,"\n\n")


path=Path('cat.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"{path} is missing.") 
else:
    print("Cat names are:")
    print(contents)

print("\n\n")

#10.9

from pathlib import Path


path=Path('dog.txt')
try:
    contents=path.read_text(encoding='utf-8') 
except FileNotFoundError:
    pass 
else:
    print("Dog names are:")
    print(contents,"\n\n")


path=Path('cat.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass 
else:
    print("Cat names are:")
    print(contents)

print("\n\n")

#10.10
"""
You can use the count() method to find out how many times a word or phrase appers in a string. 
For example, the following code counts the number of times 'row' appears in a string:
"""
line="Row,row,row your boat"
print(line.count('row'))# 2
print(line.lower().count('row'))# 3
"""
Notice that converting string to lowercase using lower() catches all appearances of the word you're looking for, regardless of how it's formatted.
"""
print("\n")
from pathlib import Path

path=Path('10.10.txt')
contents=path.read_text()
print(f"The count of the is {contents.lower().count('the')}.\n") #195
print(f"The count of the is {contents.lower().count('the ')}.\n") #136
print("The first count is higher than second becase it will count 'there' and 'then' as 'the' so we used 'the ' with one space in the string to get real data.\n\n")


#Storing Data
"""
Many of your programs will ask users to input certain kinds of information.
You might allow users to store preferences in a game or provide data for a visualization.
Whatever the focus of your program is, you'll store the information users provide in data structures such as lists and dictionaries.
When users close a program, you'll almost always want to save the information they entered.

A simple way to do this involves storing your data using the json module.
The json module allows you to convert simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs.
You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages.
It's a useful and portable format, and it's easy to learn.
"""
#Using json.dumps() and json.loads()
"""
Let's write a short program that stores a set of numbers and another program that read these numbers back into memory.
The first program will use json.dumps() to store the set of numbers, and the second program will use json.loads()

The json.dumps() function takes one argument: a piece of data that should be converted to the JSON format.
The function returns a string, which we can then write to a data file:
"""
from pathlib import Path
import json

numbers=[2,3,5,7,11,13]

path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)
"""
We first import the json module, and then create a list of numbers to work with.
Then we choose a filename in which to store the list of numbers. It's customary to use the file extension .json to indicate that the data in the file is stored in the JSON format.
Next, we use the json.dumps() function to generate a string containing the JSON representation of the data we're working with.
Once we have this string, we write it to the file using the same write_text() method we used earlier.

This program has no output, but let's open the file numbers.json and look at it. The data is stored in a format that looks just like Python:
[2,3,5,7,11,13]

Now we'll write a separate program that uses json.loads() to read the list back into memory:
"""
from pathlib import Path

path=Path('numbers.json')
contents=path.read_text()
numbers=json.loads(contents)

print(numbers)
print("\n\n")
"""
We make sure to read from the same file we wrote. Since the data file is just a text file with specific formatting, we can read it with the read_text() method.
We then pass the contents of the file to json.loads() . This function takes in a JSON-formatted string and returns a Python object(in this case, a list) which we assign to numbers.
Finally, we print the recovered list of numbers and see that it's the same list:

[2, 3, 5, 7, 11, 13]

This is a simple way to share data between two programs.
"""
#Saving and Reading User-Generated Data
"""
Saving data with json is useful when you're working with user-generated data, because if you don't store your user's information somehow, you'll lose it when the program stops running.
Let's look at an example where we prompt the user for their name the first time they run a program and then remember their name when they run the program again.
"""
from pathlib import Path
import json

username=input("What is your name? ")

path=Path('username.json')
contents=json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!\n")

"""
We first prompt for a username to store. Next, we write the data we just collected to a file called username.json .
Then we print a message informing the user that we've stored their information:

What is your name? Eric
We'll remember you when you come back, Eric!


Now let's write a new program that greets a user whose name has already been stored:
"""
from pathlib import Path
import json

path=Path('username.json')
contents=path.read_text()
username=json.loads(contents)

print(f"Welcome back, {username}!\n\n")
"""
We read the contents of the data file and then use json.loads() to assign the recovered data to the variable username.
Since we've recovered the username, we can welcome the user back with a personalized greeting:

Welcome back, Eric!

We need to combine these two programs into one file. 
When someone runs program, we want to retrieve their username from memory if possible; if not, we'll prompt for a username and store it in username.json for next time.
We could write a try-except block here to respond appropriately if username.json doesn't exist, but instead we'll use a handy method from the pathlib module:
"""
from pathlib import Path
import json

path=Path('username.json')
if path.exists():
    contents=path.read_text()
    username=json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username=input("What is your name? ")
    contents=json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")    
print("\n\n")
"""
There are many helpful methods you can use with Path objects.
The exists() method returns True if a file or folder exists and False if it doesn't.
Here we use path.exists() to find out if a username has already been stored.
If username.json exists, we load the username and print a personalized greeting to the user.

If the file username.json doesn't exist, we prompt for a username and store the value that user enters.
We also print the familiar message that we'll remember them when they come back.
Whichever block executes, the result is a username and an appropriate greeting. If this is the first time the program runs, this is output:

What is your name? Eric
We'll remember you when you come back, Eric!

Otherwise:

Welcome back, Eric!

This is the output you see if the program was already run at least once. 
Even though the data in this section is just a single string, the program would work just as well with any data that can be converted to a JSON-formatted string.
"""

#Refactoring
"""
Often, you'll come to a point where your code will work, but you'll recognize that you could improve the code by breaking it up into a series of function that have specific job
This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.
"""
from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path=Path('username.json')
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username=input("What is your name? ")
        contents=json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")  

greet_user()
print("\n\n")
"""
Because we're using a function now, we rewrite the comments as a docstring that reflects how the program currently works.
The file is a little cleaner, but the function greet_user() is doing more then just greeting the user- it's also retrieving a stored username if one exists and prompting for a new username if one doesn't.

Let's refactor greet_user() so it's not doing so many different tasks. We'll stary by moving the code for retrieving a stored username to separate function:
"""
from pathlib import Path
import json


def get_stored_name(path):
    """Get stored username if available."""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def greet_user():
    """Greet the user by name."""    
    path=Path('username.json')
    username=get_stored_name(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username=input("What is your name? ")
        contents=json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")    

greet_user()
print("\n\n")
"""
We should factor one more block of code out of greet_user(). 
If the username doesn't exist, we should move the code that prompts for a new username to a function dedicated to that purpose:
"""
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""   
    username=input("What is your name? ")
    contents=json.dumps(username)
    path.write_text(contents)
    return username 

def greet_user():
    """Greet the user by name."""
    path=Path('username.json')
    username=get_stored_name(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username=get_new_username(path)  
        print(f"We'll remember you when you come back, {username}!")  

greet_user()
print("\n\n")
"""
Each function in this final version has a single, clear purpose.
We call greet_user(), and that function prints an appropriate message: it either welcomes back an existing user or greets a new user.
It does this by calling get_stored_name() which is responsible only for retrieving a stored username if one exists.
Finally, if necessary, greet_user() calls get_new_username(), which is responsible only for getting a new username and storing it.
This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend
"""
#TRY IT YOURSELF
#10.11

from pathlib import Path
import json
path=Path('fav_num.json')
fav_num=int(input("What is your favorite number? "))
contents=json.dumps(fav_num)
path.write_text(contents)
print(f"I will remember your favorite number, It's {fav_num}.")
contents=path.read_text()
your_fav_num=json.loads(contents)
print(f"I know your favorite number, It's {your_fav_num}.")

print("\n\n")
#10.12
from pathlib import Path
import json
path=Path('fav_numv2.json')
try:
    contents=path.read_text()
except FileNotFoundError:
    fav_num=int(input("What is your favorite number? "))
    content=json.dumps(fav_num)
    path.write_text(content)
    print(f"I know your favorite number, It's {fav_num}.")
else:
    your_fav_num=json.loads(contents)
    print(f"I know your favorite number, It's {your_fav_num}.")

print("\n\n")

#10.13
from pathlib import Path
import json

def get_stored_name(path):
    """Get stored username if available."""
    if path.exists():
        contents=path.read_text()
        user_info=json.loads(contents)
        return user_info
    else:
        return None
    
def greet_user():
    """Greet the user by name."""    
    path=Path('user_info.json')
    user_info=get_stored_name(path)
    if user_info:
        print(f"Welcome back, {user_info['username']} and your age is {user_info['age']} !")
    else:
        username=input("What is your name? ")
        age=int(input("What is your age? "))
        user_info={'username':username,'age':age}
        contents=json.dumps(user_info)
        path.write_text(contents)
        print(f"We'll remember you when you come back, username: {user_info['username']}, age: {user_info['age']} !")    

greet_user()

#10.14
print("\n\n")
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""   
    username=input("What is your name? ")
    contents=json.dumps(username)
    path.write_text(contents)
    return username 

def greet_user():
    """Greet the user by name."""
    path=Path('usernamev2.json')
    username=get_stored_name(path)
    if username:
        answer=input(f"Hello, is the username: {username} (y/n)? ")
        if answer.lower()=='y':    
            print(f"Welcome back, {username}!")
        else:
            username=get_new_username(path)  
            print(f"We'll remember you when you come back, {username}!")
    else:
        username=get_new_username(path)  
        print(f"We'll remember you when you come back, {username}!")  

greet_user()

