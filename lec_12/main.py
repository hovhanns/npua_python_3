# # A simple lambda function that adds 10 to the input
# def add_10_f(x):
#     return x / 10

# add_10 = lambda x, y: x / 0 + y
# print(type(add_10)) 
# print(type(add_10_f))
# print(add_10_f(5)) 
# print(add_10(5, 10)) 

#print(add_10(5))  # Output: 15

# # A lambda function that multiplies two numbers
# multiply = lambda x, y: x * y
# print(multiply(2, 3))  # Output: 6

# # A lambda function that returns the maximum of two numbers
# maximum = lambda x, y: x if x > y else y
# print(maximum(4, 7))  # Output: 7





# # Using map to apply a function to all items in a list
# def f_square(x):
#     return x ** 2

numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x**2, numbers)
# print(squared_numbers) 
# print(type(squared_numbers))
# # print(list(squared_numbers))
# for i in squared_numbers:
#     print(i)


# # Using filter to filter out items from a list
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbers)
# print(even_numbers)  # Output: [2, 4]


# from functools import reduce
# # Using reduce to apply a function to all items in a list and reduce the list to a single value
# print(numbers)
# numbers = []
# sum_of_numbers = reduce(lambda x, y: x + y, numbers, 10)
# print(sum_of_numbers)  # Output: 15



# import time
# def execution_time_decorator(func):
#     print("Decorator created")
#     def wrapper(*args, **kwargs):
#         print(f"Executing {func.__name__}")
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper

# @execution_time_decorator
# def example_function(a, b):
#     time.sleep(2)
#     print("Function complete")
#     return a + b

# print(example_function(10, 2))






# A simple generator function that yields numbers from 1 to 3
def simple_generator():
    yield "aaaaa"
    yield "bbbbb"
    yield "ccccc"

# for i in simple_generator():
#     print(i)


# gen = simple_generator()
# print(gen)
# print(type(gen))
# print(next(gen))  
# print(next(gen))  
# print(next(gen))  


# Using iter to create an iterator from a list
numbers = [10, 20, 30, 40]
numbers_iter = iter(numbers)
print(numbers_iter)
print(type(numbers_iter))

print(next(numbers_iter))  # Output: 10
print(next(numbers_iter))  # Output: 20
print(next(numbers_iter))  # Output: 30
print(next(numbers_iter))  # Output: 40

# # A generator function that yields the squares of numbers up to a given limit
# def square_numbers(limit):
#     for i in range(1, limit + 1):
#         yield i * i

# squares = square_numbers(5)
# for square in squares:
#     print(square)  # Output: 1, 4, 9, 16, 25