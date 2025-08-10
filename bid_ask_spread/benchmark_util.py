# benchmark_util.py

import time

"""
Usage: @log_execution_time in any function
"""


def log_execution_time(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fn.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper
