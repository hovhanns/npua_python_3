# A simple lambda function that adds 10 to the input
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# A lambda function that returns the maximum of two numbers
maximum = lambda x, y: x if x > y else y
print(maximum(4, 7))  # Output: 7






from functools import reduce
# Using map to apply a function to all items in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using filter to filter out items from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using reduce to apply a function to all items in a list and reduce the list to a single value
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15





import time
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time_decorator
def example_function():
    time.sleep(2)
    return "Function complete"

print(example_function())  # Output: Execution time of example_function: 2.0xxxx seconds






# A simple generator function that yields numbers from 1 to 3
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Using iter to create an iterator from a list
numbers = [10, 20, 30, 40]
numbers_iter = iter(numbers)
print(next(numbers_iter))  # Output: 10
print(next(numbers_iter))  # Output: 20
print(next(numbers_iter))  # Output: 30
print(next(numbers_iter))  # Output: 40

# A generator function that yields the squares of numbers up to a given limit
def square_numbers(limit):
    for i in range(1, limit + 1):
        yield i * i

squares = square_numbers(5)
for square in squares:
    print(square)  # Output: 1, 4, 9, 16, 25