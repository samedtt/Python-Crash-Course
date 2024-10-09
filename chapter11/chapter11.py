#TESTING YOUR CODE
"""
In this chapter, you'll learn to test your code usig pytest.
The pytest library is a collection of tools that will help you write your first tests quickly and simply, while supporting your tests as they grow in complexity along with your project.
Python doesn't include pytest by default, so you'll learn to install external libraries.
"""
#Installing pytest with pip
#Updating pip
"""
Python includes a toll called pip that's used to install third-party packages.
Because pip helps install packages from external resources, it's updated often to adress potential security issues.
So, we'll start by updating pip.

$ python -m pip install --upgrade pip

The first part of this command, python -m pip, tells Python to run the module pip.
The second part, install --upgrade, tells pip to update a package that's already been installed.
The last part, pip, specifies which third-party package should be updated.

The output shows that my current version of pip, version 24.0, was replaced by the latest version at the time of this writing, 24.2

You can use this command to update any third-party package installed on your system:
$ python -m pip install --upgrade package_name

#Note: $ is comment so we don't need to add this symbol on our code and you can use 'python3 m -pip' if 'python m -pip' doesn't work.
"""
#Installing pytest
"""
Now that pip is up to date, we can install pytest:

$ python -m pip install --user pytest

We're still using the core command pip install, without the --upgrade flag this time.
Instead, we're using the --user flag, which tells Python to install this package for the current user only.

You can use this command to install many third-party packages:
$ python -m pip install --user package_name
"""

#Testing a Function
"""
To learn about testing, we need cote to test.
Here's a simple function that takes in a first and last name, and returns a neatly formatted full name:

def get_formatted_name(first,last):
    'Generate a neatly formatted full name.'
    full_name=f"{first} {last}"
    return full_name.title()

The function get_formatted_name() combines the first and last name with a space in between to complete a full name, and then capitalizes and returns the full name.
To check that get_formatted_name() works, let's make a program that uses this function.
The program lets users enter a first and last name, and see a neatly formatted full name:
"""
from name_function11 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first=input("\nPlease give me a first name: ")
    if first=='q':
        break
    last=input("Please give me a list name: ")
    if last=='q':
        break

    formatted_name=get_formatted_name(first,last)    
    print(f"\nNeatly formatted name: {formatted_name}")

"""
We can see that names generated here are correct. But say we want to modify get_formatted_name() so it can handle middle names.
As we do so, we want to make sure we don't break the way the function handles names that have only a first and last name.
We could test our code by running program and entering a name like Janis Joplin every time we modify get_formatted_name(), but that would become tedious.

Fortunately, pytest provides an efficient way to automate the testing of a function's output.
If we automate the testing get_formatted_name(), we can always be confident that the function will work when given the kinds of names we've written test for.
"""

#Unit Tests and Test Cases
"""
There is a wide variety of approaches to testing software. One of the simplest kind of test is a unit test.

A unit test verifies that one specific aspect of a function's behavior is correct.
A test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle.

A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations.
A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.
"""

#A Passing Test
"""
With pytest, writing your first unit test is pretty straightforward.
We'll write a single test function. The test function will call the function we're testing, and we'll make an assertion about the value that's returned.
If our assertion is correct, the test will pass; if the assertion is incorrect, the test will fail.

Here's the first test of the function get_formatted_name():

!!!The code is  in test_name_function.py!!!
!!! We are using the code which is in name_function11.py !!!

"""
from name_function11 import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name=get_formatted_name('janis','joplin')
    assert formatted_name=='Janis Joplin'

"""
The name of a test file is important; it must start with test_.
When we ask pytest to run the tests we've written, it will look for any file that begins with test, and run all of the tests it finds in that file.

In the test file, we first import the function what we want to test: get_formatted_name().
Then we define a test function: in this case, test first_last_name.
This is a longer function name when we've been using, for a good reason.
First, test functions need to start with the word test, followed by an underscore. Any function that starts with test_ will be discovered by pytest, and will be run as part of the testing process.

Also, test names should be longer and more descriptive than a typical function name.
You'll never call the function yourself; pytest will find the function and run it for you.

Next, we call the function we're testing. Here we call get_formatted_name() with the arguments 'janis' and 'joplin', just like we used when ran program.
We assign the return value of this function to formatted_name.
Finally, we make an assertion. 
An assertion is a claim about a condition. Here we're claiming that the value of formatted_name should be 'Janis Joplin'.
"""
#Running a Test
"""
If you run the file directly, you won't get any output because we never called the test function. Instead, we'll have pytest run the test file for us.
To do this, open a terminal window and navigate to the folder that contain the test file.
In the terminal window, enter the command pytest. Here's what you should see:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_name_function.py .                                                                                                                                           [100%]

=========================================================================== 1 passed in 0.00s ===========================================================================

Most importantly, we can see which versions of Python, pytest, and other packages are being used to run the test.
Next, we see the directory where the test is being run from: in my case, Desktop/Python.

We can see that pytest found one test to run, and we can see the test file that's being run.
The single dot after the name of the file tells us that a single test passed, and the %100 makes it clear that all of the tests have been run.
A large project can have hundreds or thousands of tests, and the dots and percentage-complete indicator can be helpful in monitoring the overall progress of the test run.

The last line tells us that one test passed, and it took less than 0.01 seconds to run the test.
This output indicated that function get_formatted_name() will always work for names that have a first and last name, unless we modify the function.
When we modify get_formatted_name(), we can run this test again. If the test passes, we know the function will still work for names like Janis Joplin

#Note:
If you see a message that the pytest command was not found, use the command python -m pytest instead. (Also, you can use python3 -m pytest )
"""
#A Failing Test
"""
What does a failing test look like? Let's modify get_formatted_name() so it can handle middle names, but let's do so in a way that breaks the function for names with just a first and last name, like Janis Joplin.

Here's a new version of get_formatted_name() that requires a middle name argument:

!!!The code is in name_function11v2.py!!!
!!!Also, The test is in test_name_functionv2.py!!!
"""
def get_formatted_name(first,middle,last):
    """Generate a neatly formatted full name."""
    full_name=f"{first} {middle} {last}"
    return full_name.title()

"""
This version should work for people with middle names, but when we test it, we see that we've broken the function for people with just a first and last name.
This time, running pytest gives the following output:

========================================================================== test session starts ==========================================================================
--snip--
test_name_functionv2.py F                                                                                                                                         [100%]

=============================================================================== FAILURES ================================================================================
_________________________________________________________________________ test_first_last_name __________________________________________________________________________

    def test_first_last_name():
        ""Do names like 'Janis Joplin' work?""
>       formatted_name=get_formatted_namev2('janis','joplin')
E       TypeError: get_formatted_namev2() missing 1 required positional argument: 'last'

test_name_functionv2.py:5: TypeError
======================================================================== short test summary info ========================================================================
FAILED test_name_functionv2.py::test_first_last_name - TypeError: get_formatted_namev2() missing 1 required positional argument: 'last'
=========================================================================== 1 failed in 0.01s ===========================================================================


The first item of note in the output is a single F, which tells us that one test failed.
We then see a section that focuses on FAILURES, because failed tests are usually the most importanat thing to focus on in a test run.
Next, we see that test_first_last_name() was the test function that failed.
An angle bracket (>) indicates the line of code that caused the test to fail.
The E on the next line shows the actual error that caused the failure: a TypeError due to a missing required positional argument, last.

The most important information is repeated in a shorter summary at the end, so when you're running many tests, you can get a quick sense of which tests failed and why.
"""

#Responding to a Failed Test
"""
Assuming you're checking the right conditions, a passing test means the function is behaving correctly and a failing test means there's an error in the new code you wrote.
So when a test fails, don't change the test. If you do, your tests might pass, but any code that calls your function like the test does will suddenly stop working.
Instead, fix the code that's causing the test to fail. Examine the changes you just made to the function, and figure out how those changes broke the desired behavior.

In this case, get_formatted_name() used to require only two parameters; a first name and a last name. Now it requires a first name, middle name, and last name.
The addition of that mandatory middle name parameter broke the original behavior of get_formatted_name().
The best option here is to make the middle name optional. Once we do, our test for names like 'Janis Joplin' should pass again, and we should be able to accept middle names as well.

Let's modify get_formatted_name() so middle names are optional and then run the test case again.
If it passes, we'll move on to making sure the function handles middle names properly.

To make middle names optional, we move the parameter middle to the end of the parameter list in the function definition and give it an empty value.
We also add an if test that builds the full name properly, depending on whether a middle name is provided:

!!!The code is in name_function11v3.py!!!
!!!Also, The test is in test_name_functionv3.py!!!
"""
def get_formatted_name(first,last,middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name=f"{first} {middle} {last}"
    else:
        full_name=f"{first} {last}"    
    
    return full_name.title()

"""
In this version of get_formatted_name(), the middle name is optional.
If a middle name is passed to the function, the full name will contain a first, middle and last name.
Otherwise, the full name will consist of just a first and last name.
Now the function should work for both kinds of names.
To find out if the function still works for names like Janis Joplin, let's run the test again:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_name_functionv3.py .                                                                                                                                         [100%]

=========================================================================== 1 passed in 0.01s ===========================================================================


The test passes now. This is ideal; it means the function works for names like Janis Joplin again, without us having to test the function manually.
Fixing our function was easier because the failed test helped us identify how the new code broke existing behavior.
"""
#Adding New Tests
"""
Now that we know get_formatted_name() works for simple names again, let's write a second test for people who include a middle name.
We do this by adding another test function to the file test_name_functionv4.py:

!!!We will use name_function11v3 in this code!!!
!!!The test code is in test_name_functionv4.py!!!
"""
from name_function11v3 import get_formatted_namev3

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name=get_formatted_namev3('janis','joplin')
    assert formatted_name=='Janis Joplin'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadues Mozar' work?"""
    formatted_name=get_formatted_namev3('wolfgang','mozart','amadues')
    assert formatted_name=='Wolfgang Amadeus Mozart'

"""
We name this new function test_first_last_middle_name().
The function name must start with test_ so the function runs automatically when we run pytest.
We name the function to make it clear which behavior of get_formatted_name() we're testing.
As a result, if the test fails, we'll know right away what kind of names are affected.

To test the function, we call get_formatted_name() with a first, last, and middle name, and then we make an assertion that returned full name matches the full name (first, middle, and last) that we except.
When we run pytest again, both tests pass:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 2 items                                                                                                                                                       

test_name_functionv4.py ..                                                                                                                                        [100%]

=========================================================================== 2 passed in 0.00s ===========================================================================

The two dots indicate that two test passed, which is also clear from the last line of output.
This is great! We now know that the function still works for names like Janis Joplin, and we can be confident that it will work for names like Wolfgang Amadeus Mozart as well.
"""
#TRY IT YOURSELF
#11.1
"""
The function is in city_functions.py
The test is in test_cities.py
The test passed:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_cities.py .                                                                                                                                                  [100%]

=========================================================================== 1 passed in 0.00s ===========================================================================
"""
#11.2
"""
The first function is in city_functionsv2.py
The first test function is in test_citiesv2.py

Test failed:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_citiesv2.py F                                                                                                                                                [100%]

=============================================================================== FAILURES ================================================================================
__________________________________________________________________________ test_city_countryv2 __________________________________________________________________________

    def test_city_countryv2():
        ""Do city, country names like 'Santiago, Chile' work?""
>       city_country=get_city_countryv2('santiago','chile')
E       TypeError: get_city_countryv2() missing 1 required positional argument: 'population'

test_citiesv2.py:5: TypeError
======================================================================== short test summary info ========================================================================
FAILED test_citiesv2.py::test_city_countryv2 - TypeError: get_city_countryv2() missing 1 required positional argument: 'population'
=========================================================================== 1 failed in 0.01s ===========================================================================


The second function is in city_functionsv3.py
The second test function is in test_citiesv3.py

Test passed:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_citiesv3.py .                                                                                                                                                [100%]

=========================================================================== 1 passed in 0.00s ===========================================================================
"""

#Testing a Class
"""
In the first part of this chapter, you wrote tests for a single function. Now you'll write tests for a class.
If you have passing tests for a class you're working on, you can be confident that improvements you make to the class won't accidentally break its current behavior.
"""
#A Variety of Assertion
"""
So far, you've seen just one kind of assertion: a claim that a string has a specific value.
When writing a test, you can make any claim that can be expressed as a conditional statement.

Table 11-1 shows some of the most useful kinds of assertions you can include in your initial tests.

Table 11-1: Commonly Used Assertion Statement in Tests

Assertion                                Claim
-----------------------------------------------------------------
assert a==b                 Assert that two values are equal

assert a!=b                 Assert that two values are not equal

assert a                    Assert that a evaluates to True

assert not a                Assert that a evaluates to False

assert element in list      Assert that an element is in a list

assert element not in list  Assert that an element is not in a list
-------------------------------------------------------------------

There are just a few examples; anything that can be expressed as a conditional statement can be included in a test.
"""

#A Class to Test
"""
Testing a class is similar to testing a function, because much of the work involves testing the behavior of the methods in the class.
However, there are few differences, so let's write a class to test.
Consider a class that helps administer anonymous surveys:

!!! The class is in survey.py!!!
"""
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self,question):
        """Store a question, and prepare to store respones."""
        self.question=question
        self.responses=[]

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self,new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)        

    def show_results(self):
        """Show all the responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

"""
This class starts with a survey question that you provide and includes an empty list to store responses.
The class has methods to print the survey question, add a new response to the response list, and print all the responses stored in the list.
To create an instance from this class, all you have to provide a question.
Once you have an instance representing a particular survey, you display the survey question with show_question(), store a response using store_response(), show the result with show_results().

To show that the AnonymousSurvey class works, let's write a program that uses the class:
"""
from survey import AnonymousSurvey

#Define a question and make a survey
question='What language did you first learn to speak?'
language_survey=AnonymousSurvey(question)

#Show the question, and store responses to the question.
language_survey.show_question()
print("\n\nEnter 'q' at any time to quit.\n")
while True:
    response=input("Language: ")
    if response=='q':
        break
    language_survey.store_response(response)

#Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

"""
This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with that question.
The program calls show_question() to display the question and then prompts for responses.
Each response is stored as it received. When all responses have been entered (the user input q to quit), show_results() prints the survey results.
"""

#Testing the AnonymousSurvey Class
"""
Let's write a test that verifies one aspect of the way AnonymousSurvey behaves.
We'll write a test to verify that a single response to the survey question is stored properly:

!!! The test is in test_survey.py !!!
"""
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question="What language did you first learn to speak?"
    language_survey=AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

"""
We start by importing the class we want to test, AnonymousSurvey.
The first test function will verify that when we store a response to the survey question, the response will end up in the survey's list of responses.
A good descriptive name for this function is test_store_single_response()
If this test fails, we'll know from the function name in the test summary that there was a problem storing a single response to the survey.

By default, running the command pytest with no arguments will run all the tests that pytest discovers in the current directory.
To focus on the test in one file, pass the name of the test file you want to run. 
Here we'll run just the one test we wrote for AnonymousSurvey:

$ python3 -m pytest ----> to run all test files

$ python3 -m pytest file_name.py -----> to run specific test file

Test passed:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 1 item                                                                                                                                                        

test_survey.py .                                                                                                                                                  [100%]

=========================================================================== 1 passed in 0.00s ===========================================================================

This is a good start, but a survey is useful only if it generates more than one response.
Let's verify that three responses can be stored correctly. 
To do this, we add another method to TestAnonymousSurvey:

!!! The test is in test_surveyv2.py !!!
"""
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question="What language did you first learn to speak?"
    language_survey=AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question="What language did you first learn to speak?"
    language_survey=AnonymousSurvey(question)
    responses=['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses 

"""
We call the new function test_store_three_response(). We create a survey object just like we did in test_store_single_response().
We define a list containing three different responses, and then we call store_response() for each of these responses.
Once the responses have been stored, we write another loop and assert that each response is now in language_survey.responses

When we run the test file again, both tests(for a single response and for three responses) pass:
========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 2 items                                                                                                                                                       

test_surveyv2.py ..                                                                                                                                               [100%]

=========================================================================== 2 passed in 0.01s ===========================================================================

This works perfectly. However, these tests are a bit repetitive, so we'll use another feature of pytest to make them more efficient.
"""  
#Using Fixtures
"""
In test_survey.py and test_surveyv2.py , we created a new instance of AnonymousSurvey in each test function.
This is fine in the short example we're working with it, but in a realistic world project with tens or hundreds of tests, this would be problematic.

In testing, a fixture helps set up a set environment. Ofthen this means creating a resource that's used by more than one test.
We create a fixture in pytest by writing a function with the decorator @pytest.fixture.
A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves.

Let's use a fixture to create a single survey instance that can be used in both test functions in test_surveyv2.py:

!!! The test is in test_surveyv3.py !!!
"""
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question= "What language did you first learn to speak?"
    language_survey=AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses=['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses 
"""
We need to import pytest now, because we're using a decorator that's defined in pytest.
We apply @pytest.fixture decorator to the new function language_survey().
This function builds an AnonymousSurvey object and returns the new survey.

Notice that the definitions of both test functions have changed; each test function now has a parameter called language_survey.
When a parameter in a test function matches of a function with @pytest.fixture decorator, the fixture will run automatically and the return value will be passed to the test function.
In this example, the function language_survey() supplies both test_store_single_response() and test_store_three_response() with a language_survey instance.

There's no new code in either of the test functions, but notice that two lines have been removed from each function : the line that defined a question and the line that created an AnonymousSurvey object.
When we run the test file again, both tests still pass. These tests would be particularly useful when trying to expand AnonymousSurvey to handle multiple respones for each person.

Both tests passed:
========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 2 items                                                                                                                                                       

test_surveyv3.py ..                                                                                                                                               [100%]

=========================================================================== 2 passed in 0.01s ===========================================================================



When you want to write a fixture, write a function that generates the resource that's used by multiple test functions.
Add @pytest.fixture decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource.

Your test will be shorter and easier to write and maintain from that point forward.
"""
#TRY IT YOURSELF
#11.3
class Employee:

    def __init__(self,first_name,last_name,annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.annual_salary=annual_salary

    def give_raise(self,addition=5000):
        self.annual_salary+=addition


"""
The first test which named as Employee_test.py:

Tests are passed:

========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 2 items                                                                                                                                                       

Employee_test.py ..                                                                                                                                               [100%]

=========================================================================== 2 passed in 0.01s ===========================================================================





The second test which named as Employee_testv2.py (We used fixtures @pytest.fixture):

Tests are passed:



========================================================================== test session starts ==========================================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/samedtevin/Desktop/Python
collected 2 items                                                                                                                                                       

Employee_testv2.py ..                                                                                                                                             [100%]

=========================================================================== 2 passed in 0.01s ===========================================================================

"""

