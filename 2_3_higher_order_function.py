# -------------------------------------------------------------
# Higher order function
# -------------------------------------------------------------
def apply_operation(operation, x, y):
    return operation(x, y)


# Binary operation functions
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


# V1:
# Usage of the higher-order function
result_addition = apply_operation(add, 3, 4)
result_multiplication = apply_operation(multiply, 3, 4)


def compose(f, g):
    """Compose two functions, f and g."""
    return lambda x: f(g(x))


def plus_one(x):
    return x * 2


def square(x):
    return x**2


# Compose the functions double and square
composed_function = compose(plus_one, square)
print(type(composed_function))

# Test the composed function
result = composed_function(3)
print(result)


# V2:
def compose(*functions):
    """
    Compose multiple functions: f(g(...(h(x))))
    """

    def composed_function(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result

    return composed_function


# Set of unary functions
def square(x):
    return x**2


def add_one(x):
    return x + 1


def double(x):
    return x * 2


def to_s(s):
    return f"final result {str(s)}"


# ----Compose functions to create a pipeline------
pipeline = compose(to_s, square, add_one, double)
# ------------------------------------------------

# Run It
result = pipeline(3)
print(f"Result: {result}")
