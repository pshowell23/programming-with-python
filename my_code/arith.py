import sys

# Write a command-line program that does addition and subtraction:

def main():
    operation = sys.argv[1]
    numbers = sys.argv[2:]

    assert len(numbers) > 1, 'Plese use more numbers'
    if operation == 'add' or operation == 'sum':
        print('The answer is:', sum(numbers))
    elif operation == 'sub' or operation == 'diff':
        print('The answer is:', difference(numbers))
    elif operation == 'multiply':
        print('The answer is:', product(numbers))
    elif operation == 'divide':
        print('The answer is:', divide(numbers))

def sum(nums):
    total = 0
    for num in nums:
        num = int(num)
        total = total + num
    return format_number(total)

def difference(nums):
    total = 0
    for num in nums:
        num = int(num)
        if total == 0:
            total = num
        else:
            total = total - num
    return format_number(total)

def product(nums):
    total = 1
    for num in nums:
        num = int(num)
        total = total * num
    return format_number(total)

def divide(nums):
    total = 1
    for num in nums:
        num = int(num)
        if total == 1:
            total = num
        else:
            total = total / num
    return format_number(total)

def format_number(number):
    return "{:,}".format(number)

if __name__ == '__main__':
    main()