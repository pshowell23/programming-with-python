import numpy as np

# Suppose you are writing a funciton called 'average' that calculates the average of the numbers in a list. What pre-conditions and post-conditions would you write for it? Compare your answer to your neighbor's: can you think of a funciton that will pass your tests but not his/hers or vice versa?

def average(nums):
    assert isinstance(nums, list), 'not a list'
    total = 0
    amount_of_numbers = len(nums)
    for num in nums:
        total += num
    avg = total / amount_of_numbers
    assert avg == np.average(nums), 'Average doesn\'t work'
    print('The average is:', avg)

average([1,4,6,7,4,2,4,1,6,0,1,4,3])

# Given a sequence of a number of cars, the function get_total_cars returns the total number of cars.
#
# get_total_cars([1, 2, 3, 4]) >> 10
# 
# get_total_cars(['a', 'b', 'c']) >> ValueError: invalid literal for int() with base 10: 'a'
#
# Explain in words what the assertions in this function check, and for each one, give an example of input that will make that assertion fail.
#
# def get_total(values):
#    assert len(values) > 0
#    for element in values:
#        assert int(element)
#    values = [int(element) for element in values]
#    total = sum(values)
#    assert total > 0
#    return total
#
# My Answer: The first assertion insures that there is something passed into the get_total function,
#   failed call would be get_total()
# then the second assertion insures that each element is an integer
#   failed call would be get_total('a') as 'a' is a string
#       get_total(4.0) as 4.0 is a float
# The third assertion insures that the total of all numbers is actually being added