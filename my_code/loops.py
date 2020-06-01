# Using range, write a loop that uses range to print the first 3 natural numbers
for n in range(1,4):
    print(n)

# Given the following loop:
# word = 'oxygen'
# for char in word:
#    print(char)
# How many times is the body of the loop executed?
# 3 times
# 4 times
# 5 times
# 6 times
#
# Answer: 6 times


# Write a loop that calculates the same result as 5 ** 3 using multiplication (and without exponentiation).
number = 5
for ex in range(1,3):
    number = number * 5
print('5^3 ==',number)

# Knowing that two strings can be concatenated using the + operator, write a loop that takes a string and produces a new string with the characters in reverse order, so 'Newton' becomes 'notweN'.
def string_reverse(string):
    new_string = ''
    for char in string:
        new_string = char + new_string
    print(new_string)
string_reverse('Newton')
# solved with a function, cause I can!

# Write a loop using enumerate(coefs) which computes the value y of any polynomial, given x and coefs.
x = 5
coefs = [2, 4, 3]
y = 0
for index, cof in enumerate(coefs):
    y = y + cof * x**index
print(y)