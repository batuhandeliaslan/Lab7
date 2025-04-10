def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
def power(x, y): return x ** y
def mod(x, y): return x % y

if _name_ == "_main_":
    print("Testing math_utils functions:")
    print("add(4, 5) =", add(4, 5))
    print("subtract(10, 3) =", subtract(10, 3))
    print("multiply(6, 7) =", multiply(6, 7))
    print("divide(8, 2) =", divide(8, 2))
    print("divide(8, 0) =", divide(8, 0))  # zero division test
    print("power(2, 3) =", power(2, 3))
    print("mod(10, 3) =", mod(10, 3))
