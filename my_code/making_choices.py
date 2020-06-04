import numpy as np
import glob

filenames = filenames = sorted(glob.glob('../swc-python/data/inflammation*.csv'))

for filename in filenames:
    data = np.loadtxt(fname=filename, delimiter=',')

    max_inflammation_0 = np.max(data, axis=0)[0]
    max_inflammation_20 = np.max(data, axis=0)[20]

    if max_inflammation_0 == 0 and max_inflammation_20 == 20:
        print(filename, ': Suspicious looking maxima!')
    elif np.sum(np.min(data, axis = 0)) == 0:
        print(filename, ': Minima add up to zero!')
    else:
        print(filename, ': Seems OK!')

# Write some conditions that print True if the variable a is within 10% of the variable b and False otherwise. Compare your implementation with your partner’s: do you get the same answer for all possible pairs of numbers?
a = 10
b = 100

if a <= (b * .1):
    print('True')
else:
    print('False')

# Write some code that sums the positive and negative numbers in a list separately, using in-place operators. Do you think the result is more or less readable than writing the same without in-place operators?
nums_list = [4, 6, -4, 10, -68, 54, 3, -5, -7, 2, 1, -19]
positive_sum = 0
negative_sum = 0

for num in nums_list:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
print(positive_sum)
print(negative_sum)

# 1. Write a loop that counts the number of vowels in a character string.
# 2. Test it on a few individual words and full sentences.
# 3. Once you are done, compare your solution to your neighbor’s. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?

def find_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print('Vowels in string:', count)

find_vowels('Oh no! I did not think about the letter y')
find_vowels('Today is awesome')
find_vowels('I gotta be better')