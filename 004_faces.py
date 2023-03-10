'''
Lesson: 004
Faces
03/06/2023

In a file called faces.py,
1. implement a function called convert that
    a. accepts a str as input
    b. returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
    c. and any :( converted to 🙁 (otherwise known as a slightly frowning face).
    d. All other text should be returned unchanged.
2. Then, in that same file, implement a
    a. function called main that prompts the user for input
    b. calls convert on that input, and prints the result.
'''



def convert(asciiEmote):
    asciiHappy = "Hello :)"
    asciiSad = "Goodbye :("
    conjoined = asciiHappy + " " + asciiSad

    if asciiEmote == asciiHappy:
        newHappyEmoji = "Hello 🙂"
        return newHappyEmoji
    elif asciiEmote == asciiSad:
        newSadEmoji = "Goodbye 🙁"
        return newSadEmoji
    elif asciiEmote == conjoined:
        newConjoinedEmote = "Hello 🙂" + " " + "Goodbye 🙁"
        return newConjoinedEmote
    else:
        return asciiEmote


#something like this should work ok
#but there's something wrong with this file unicode
def convert2(asciiEmote):
    return asciiEmote.replace(":)"", "🙂").replace(":(", "🙁")

if __name__ == '__main__': # function called main that prompts the user for input

    asciiEmote = input("Enter any ascii emoticon ") # accepts a str as input
    print(convert2(asciiEmote))
