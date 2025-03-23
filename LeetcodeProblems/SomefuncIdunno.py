
# Zip

ExampleL = [1, 2, 3]
ExampleL2 = [4, 5, 6]

def zip(a, b):
    return list(zip(a, b))

print(zip(ExampleL, ExampleL2))
#output [(1, 4), (2, 5), (3, 6)] 

# Map

def map(a, b):
    return list(map(lambda x, y: x*y, a, b))

print(map(ExampleL, ExampleL2))
#output [4, 10, 18]


# Filter

def filter(a):
    return list(filter(lambda x: x%2==0, a))

print(filter(ExampleL))
#output [2]

# Reduce

def reduce(a):
    return reduce(lambda x, y: x+y, a)

print(reduce(ExampleL))
#output 6

# Sort

def sort(a):
    return sorted(a)

print(sort(ExampleL))
#output [1, 2, 3]

# Reverse

def reverse(a):
    return a[::-1]

print(reverse(ExampleL))
#output [3, 2, 1]

# Count

def count(a):
    return len(a)

print(count(ExampleL))
#output 3

