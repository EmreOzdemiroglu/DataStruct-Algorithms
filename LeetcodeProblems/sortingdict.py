
# Sorting a Dictionary by Value

def sort_dict_by_value(dict):
    return sorted(dict.items(), key=lambda x: x[1])

# More Lambda Functions to Grasp Better

# Basic Lambda Function

# Lambda with simple arithmetic
add = lambda x, y: x + y
multiply = lambda x, y: x * y
square = lambda x: x ** 2

# Lambda with conditionals
is_even = lambda x: x % 2 == 0
get_sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

# Lambda with list operations
get_first = lambda lst: lst[0] if lst else None
sum_list = lambda lst: sum(lst)

# Lambda with string operations
capitalize_words = lambda s: ' '.join(word.capitalize() for word in s.split())
reverse_string = lambda s: s[::-1]

# Lambda with multiple arguments and complex logic
calculate = lambda x, y, operation: {
    'add': x + y,
    'subtract': x - y,
    'multiply': x * y,
    'divide': x / y if y != 0 else "Cannot divide by zero"
}.get(operation, "Invalid operation")

# Lambda with map and filter
double_all = lambda numbers: list(map(lambda x: x * 2, numbers))
only_evens = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))



# Sorting a Dictionary by Key

def sort_dict_by_key(dict):
    return sorted(dict.items(), key=lambda x: x[0])

# Sorting a Dictionary by Value and Key

def sort_dict_by_value_and_key(dict):
    return sorted(dict.items(), key=lambda x: (x[1], x[0]))
