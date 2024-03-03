'''from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers_list = [2, 3, 4, 5]
result = multiply(numbers_list)
print(result)
'''

'''
def count_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

input_string = "Hello World"
upper_count, lower_count = count_case_letters(input_string)
print(upper_count, lower_count)
'''
'''
import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    return result

input_number = int(input())
milliseconds = int(input())

result = calculate_square_root(input_number, milliseconds)

print(f"Square root of {input_number} after {milliseconds} milliseconds is {result}")
'''

'''
tuple_1 = (True, True, True)
tuple_2 = (False, True, True)

print(all(tuple_2))
'''


