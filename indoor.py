'''
Indoor Voice
03/06/2023
https://cs50.harvard.edu/python/2022/psets/0/indoor/
Requirements:
In a file called indoor.py, implement a program in Python that
    1. Prompts the user for input
    2. Outputs that same input in lowercase.
Note: Punctuation and whitespace should be outputted unchanged.
'''


name = input("Enter any text ") # passing a str of your own as an argument to input.

lowerCase = str.lower(name)

print(lowerCase)
