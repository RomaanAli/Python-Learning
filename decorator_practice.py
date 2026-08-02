def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

greet = outer()

greet()


def multiply_by(n):

    def multiply(x):
        return x * n

    return multiply

double = multiply_by(2)

triple = multiply_by(3)

print(double(5))
print(triple(5))

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()

print(c())
print(c())
print(c())

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(5, 6)

from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} --------Finished---------")

        return result

    return wrapper






@logger
def hello():
    print("Hello")

hello()