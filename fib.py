'''
calculates the fibonacci sequence using 3 different algorithms
'''


def __fib_recur(n):
    '''
    brute force fiboncacci solution
    '''
    # initial condition
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursion
    result = __fib_recur(n-1) + __fib_recur(n-2)

    return result


def fib_recursive(n):
    '''
    slow recursive solution
    '''
    # students should write code to calculate the fibonacci number

    total = 0
    for i in range(n+1):
        total += __fib_recur(i)

    return total


def __fib_recursive_dp(n, cache):
    '''
    fast recursive w/ dynamic programming (cache
    of results)
    '''
    # return the answer if we know it already (dynamic programming)
    if n in cache:
        return cache[n]

    # initial condition
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursion
    result = __fib_recursive_dp(n-1, cache) + __fib_recursive_dp(n-2, cache)

    # cache (save) the result
    cache[n] = result

    return result


def fib_recursive_dp(n):
    '''
    iterative solution
    '''
    total = 0
    cache = dict()
    for i in range(n+1):
        total += __fib_recursive_dp(i, cache)
    return total


def fib_iterative_dp(n):
    '''
    iterative dynamic programming solution with cached computations
    save the result in a list to save unnecessary calculations
    '''

    # edge case
    if n == 0:
        return 0

    # create a list to store pre-calculated values
    fib = [0] * (n+1)

    # initial condition
    fib[0] = 0
    fib[1] = 1

    # calc the first two values
    total = fib[0] + fib[1]
    # calculate the remaining values up to n
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        total += fib[i]

    return total
