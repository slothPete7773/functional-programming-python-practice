# V1:
# Just Either Monad

from pymonad.either import Left, Right


def divide(a, b):
    return Right(a / b) if b != 0 else Left("Error: Division by zero")


# Example usage
result = divide(10, 2)  # Result: Right(5.0)
result = divide(10, 0)  # Result: Left('Error: Division by zero')

print(result)

# V2:
# Either Monad + Curry Func

from pymonad.either import Left, Right
from pymonad.tools import curry


@curry(2)
def divide(a, b):
    print(f"A: {a} || B: {b}")
    return Right(a / b) if b != 0 else Left("Error: Division by zero")


# What happen here is that,
# 1. Create Right monad supplied with value=10
# 2. then, function `divide()` is called and partially applied with parameter `a`= 2.
#   # 2.1 `divide()` compute and return Right(0.2), because 2/10=0.2`
# 3. then, another function `divide()` is called and partially applied with param `a`=5
#   # 3.1 and the function compute to return a{5} / b{0.2} = 25.0
result = Right(10).then(divide(2)).then(divide(5))
print(result)

# print((10 / 2) / 5)
