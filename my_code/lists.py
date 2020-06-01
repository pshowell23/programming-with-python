# Use a for-loop to convert the string “hello” into a list of letters:
# ["h", "e", "l", "l", "o"]

letters = []
for char in 'hello':
    letters.append(char)
print(letters)

# Use slicing to access only the last four characters of a string or entries of a list.
string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"],
                    ["chlorine", "Cl"],
                    ["bromine", "Br"],
                    ["iodine", "I"],
                    ["astatine", "At"]]

def return_last_four(input):
    print(input[-4:])

return_last_four(string_for_slicing)
return_last_four(list_for_slicing)

# Use the step size argument to create a new string that contains only every other character in the string “In an octopus’s garden in the shade”

every_other = 'In an octopus’s garden in the shade'
print(every_other[0::2])