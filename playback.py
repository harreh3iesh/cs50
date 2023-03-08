'''
Lesson: 002
Playback
03/06/2023
https://www.w3schools.com/python/ref_string_replace.asp


Requirements:
In a file called playback.py, implement a program in Python that
1. prompts the user for input
2. outputs that same input,
3. replacing each space with ... (i.e., three periods).
'''

text = input("Enter any text ") # passing a str of your own as an argument to input.

replacement = text.replace(" ", "...")

print(replacement)
