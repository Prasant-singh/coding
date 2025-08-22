# # A basic decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()




# Decorators: Write a decorator timer that measures the execution time of a function and prints the duration.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timer
def example_function(n):    
    total = 0
    for i in range(n):
        total += i
    return total

n = 1000000
result = example_function(n)    
print(f"Result: {result}")