## function that takes in a string and reverses it.

## function that takes in a string and return it in all caps.



def flipit(string):
    newstring = ''
    for n in string:
        newstring = n + newstring
    return newstring
print(flipit("hello"))




def shout(string):
    return string.upper()
