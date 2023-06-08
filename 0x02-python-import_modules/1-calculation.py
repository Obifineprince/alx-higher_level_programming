#!/usr/bin/python3
# Import functions from calculator_1.py
import calculator_1

# Define variables a and b
a = 10
b = 5

# Call each imported function with arguments a and b
result_add = calculator_1.add(a, b)
result_subtract = calculator_1.subtract(a, b)
result_multiply = calculator_1.multiply(a, b)
result_divide = calculator_1.divide(a, b)

# Print the results
result_message_add = "The sum of " + str(a) + " and " + str(b) + " is " + str(result_add)
result_message_subtract = "The difference between " + str(a) + " and " + str(b) + " is " + str(result_subtract)
result_message_multiply = "The product of " + str(a) + " and " + str(b) + " is " + str(result_multiply)
result_message_divide = "The division of " + str(a) + " and " + str(b) + " is " + str(result_divide)

print(result_message_add)
print(result_message_subtract)
print(result_message_multiply)
print(result_message_divide)

