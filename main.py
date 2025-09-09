import fib
import time

NANOSECONDS_TO_SECONDS = 1000000


def print_result(result, start, stop, n):
    diff = (stop - start) * NANOSECONDS_TO_SECONDS
    print(f'the slow implementation runs in {diff:.1f} nanoseconds')
    print(f'the total sum of fib({n}) = {result}')
    print()


def main():

    user_input = input('Enter a number: ')
    n = int(user_input)

    # brute-force recursively calculate the fibonacci number
    print('slow brute-force recursive solution')
    start = time.perf_counter()
    slow_total = fib.fib_recursive(n)
    stop = time.perf_counter()
    print_result(slow_total, start, stop, n)

    # recursively calculate the fibonacci number sum by saving/caching
    # previous computations
    print('fast recursive solution with cached computations')
    start = time.perf_counter()
    fast_total = fib.fib_recursive_dp(n)
    stop = time.perf_counter()
    print_result(fast_total, start, stop, n)

    # iterative solution, using dp array by saving/caching previous
    # computations
    print('fastest iterative solution with cached computations')
    start = time.perf_counter()
    fastest_total = fib.fib_iterative_dp(n)
    stop = time.perf_counter()
    print_result(fastest_total, start, stop, n)


main()
