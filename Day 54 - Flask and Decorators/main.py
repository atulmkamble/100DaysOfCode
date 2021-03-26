"""
This program implements decorator function
"""

import time


def main():
    def speed_calc_decorator(function):
        def wrapper_function():
            # Execute before function call
            start_time = time.time()
            function()
            # Execute after function call
            end_time = time.time()
            print(f'Executing {function.__name__} took {round(end_time - start_time, 2)} seconds')

        return wrapper_function

    @speed_calc_decorator
    def fast_function():
        for i in range(10000000):
            i * i

    @speed_calc_decorator
    def slow_function():
        for i in range(100000000):
            i * i

    fast_function()
    slow_function()


if __name__ == '__main__':
    main()
