# Chapter 11: Testing Your Code

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\nNeatly formatted name: " + formatted_name + '.')

'''
A unit test verifies that one specific aspect of a function's behavior is correct.
A test case is a collection of unit tests that together prove that
a function behaves as it's supposed to, within the full range of situations you
expect it to handle.
'''

# Testing a Function
# in 'test_name_function.py'

'''
The method name must start with test_ so the method runs automatically when we run test_name_function.py. 
We name the method to make it clear which behavior of get_formatted_name() we’re testing.
As a result, if the test fails, we know right away what kinds of names are affected. 
It’s fine to have long method names in your TestCase classes. 
They need to be descriptive so you can make sense of the output when your tests fail, and 
because Python calls them automatically, you’ll never have to write code that calls these methods.
'''

# Testing a Class

# Assert Methods Available from the unittest Module

'''
assertEqual(a, b)       ->  Verify that a == b
assertNotEqual(a, b)    ->  Verify that a != b
assertTrue(x)           ->  Verify that x is True
assertFalse(x)          ->  Verify that x is False
assertIn(item, list)    ->  Verify that item is in list
assertNotIn(item, list) ->  Verify that item is not in list
'''

# Testing a Class
# can be found in survey.py
