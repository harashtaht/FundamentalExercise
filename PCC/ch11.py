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
