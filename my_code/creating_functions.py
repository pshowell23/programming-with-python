# I've already been doing this one, sorry SWC

import numpy as np

# “Adding” two strings produces their concatenation: 'a' + 'b' is 'ab'. Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:
#
# print(fence('name', '*'))

def fence(original, wrapper):
    return wrapper + original + wrapper
print(fence('name', '*'))

# Note that return and print are not interchangeable. print is a Python function that prints data to the screen. It enables us, users, see the data. return statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:
#
# def add(a, b):
#   print(a + b)
#
# Question: What will we see if we execute the following commands?
# A = add(7, 3)
# print(A)
# 
# Answer: Prints 10, then None

# If the variable s refers to a string, then s[0] is the string’s first character and s[-1] is its last. Write a function called outer that returns a string made up of just the first and last characters of its input. A call to your function should look like this:
#
# print(outer('helium'))
def outer(s):
    return s[0] + s[-1]

print(outer('helium'))

# Write a function rescale that takes an array as input and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0. (Hint: If L and H are the lowest and highest values in the original array, then the replacement for a value v should be (v-L) / (H-L).)

def rescale(arr):
    rescaled_arr = []
    L = np.min(arr)
    H = np.max(arr)
    for item in arr:
        new_val = (item - L) / (H - L)
        rescaled_arr.append(new_val)
    return rescaled_arr

list_to_be_scaled = [10, 5, 6, 18, 49, 82, 4, 20, 9, 65]
print(rescale(list_to_be_scaled))

# Run the commands help(numpy.arange) and help(numpy.linspace) to see how to use these functions to generate regularly-spaced values, then use those values to test your rescale function. Once you’ve successfully tested your function, add a docstring that explains what it does.
# help(np.linspace)

