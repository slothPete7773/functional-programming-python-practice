# Reference:
# https://www.geeksforgeeks.org/function-composition-in-python/


# V1:
# Simple function composition
def add(x):
    return x + 2


def multiply(x):
    return x * 2


print("Adding 2 to 5 and multiplying the result with 2: ", multiply(add(5)))


# V2:
# Dedicated composing function with lambda for handle later execution
def composite_function(f, g):
    return lambda x: f(g(x))


def add(x):
    return x + 2


def multiply(x):
    return x * 2


add_multiply = composite_function(multiply, add)

print("Adding 2 to 5 and multiplying the result with 2: ", add_multiply(5))


# V3:
# Composing N functions
# But the composing function can only handle 2 function each time.
def composite_function(f, g):

    return lambda x: f(g(x))


def add(x):
    return x + 2


def multiply(x):
    return x * 2


def subtract(x):
    return x - 1


add_subtract_multiply = composite_function(composite_function(multiply, subtract), add)
print(
    "Adding 2 to 5, then subtracting 1 and multiplying the result with 2: ",
    add_subtract_multiply(5),
)


# V4:
# Composing N function 1 time with reduce function

from functools import reduce


# composite_function accepts N
# number of function as an
# argument and then compose them
def composite_function(*func):

    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)


# Function to add 2
def add(x):
    return x + 2


# Function to multiply 2
def multiply(x):
    return x * 2


# Function to subtract 2
def subtract(x):
    return x - 1


# Here add_subtract_multiply will
# store lambda x : multiply(subtract(add(x)))
add_subtract_multiply = composite_function(multiply, subtract, add)

print(
    "Adding 2 to 5, then subtracting 1 and multiplying the result with 2: ",
    add_subtract_multiply(5),
)
