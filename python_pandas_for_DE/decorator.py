## Timing Decorator
# Function decorator that times execution
from time import time

def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper

# the decorator function syntax
@timer
def sum_nums():
    result = 0
    for x in range(1000000):
        result += x

sum_nums()

## Logging Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Ran {func.__name__} with args: {args}, and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def sub(x, y):
    return x - y

add(10, 20)
sub(30, 20)

## Caching Decorator
import functools

def cache(func):
    cache_data = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in cache_data:
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]
    return wrapper

import time
@cache
def expensive_func(x):
    start_time = time.time()
    time.sleep(2)
    print(f"{expensive_func.__name__} ran in {time.time() - start_time:.2f} secs")
    return x

%time print(expensive_func(1))

%time print(expensive_func(1))

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)

## Delay
import time
from functools import wraps

def delay(seconds):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} seconds before running {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return inner

@delay(seconds=3)
def print_text():
    print("Hello World")

print_text()

