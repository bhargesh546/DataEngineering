import time
from functools import wraps
import random

def timer(func):
    fastest = None
    slowest = None

    @wraps(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start

        if fastest == None or duration < fastest:
            fastest = duration
        if slowest == None or duration > slowest:
            slowest = duration
        
        print(f"{func.__name__} ran in {duration:.2f} seconds.")
        print(f"Fastest: {fastest:.2f} and Slowest: {slowest:.2f}")

        return result
    return wrapper

@timer
def random_sleep():
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    return delay

