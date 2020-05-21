import numpy as np
import time as t

data = np.loadtxt(fname="../swc-python/data/inflammation-01.csv", delimiter=',')

print(type(data))

#Getting a value
print('first value in data:', data[0,0])
print('middle value in data:', data[30, 20])

# Getting a slice
print(data[0:4, 0:10])

# Getting mean
print('The mean is:', np.mean(data))

print(t.ctime())

maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
print('Maximum inflamtion:', maxval)
print('Minimum inflamtion:', minval)
print('Standard diviation:', stdval)

patient_0 = data[0] #Tutorial says to equate the value to data[0, :], but this seems needless to me
print('Maximum inflamtion of patient 0:', np.max(patient_0))

# Slicing strings
element = 'oxygen'
print(element[:4]) # returns oxyg
print(element[4:]) # returns en
print(element[-2]) # returns e
print(element[1:-1]) #returns xyge

# How can we rewrite the slice for getting the last three characters of element, so that it works even if we assign a different string to element?
def print_last_three(el):
    print('The last three characters of', el, 'are:', el[-3:])

print_last_three(element)
print_last_three('carpentry')
print_last_three('clone')
print_last_three('hi')