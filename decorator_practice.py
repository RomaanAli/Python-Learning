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