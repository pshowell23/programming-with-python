weight_kg = 60.0
weight_kg_text = 'weight in kilograms:'

print(weight_kg_text, weight_kg)

weight_kg = 65.0
print('now', weight_kg_text, weight_kg)

weight_lb = 2.2 * weight_kg
print(weight_kg_text, weight_kg, 'and in pounds:', weight_lb)

weight_kg = 100.0
print(weight_kg_text, weight_kg, 'and in pounds:', weight_lb)

#Check understanding
mass = 47.5
age = 122
mass = mass * 2.0
age = age - 20
print(mass, age) #prints 95.0 102

# Sorting Out References
first, second = 'Grace', 'Hopper'
third, fourth = second, first
print(third, fourth) #prints Hopper Grace