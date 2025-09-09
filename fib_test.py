'''
unit tests
'''
import pytest
import random
import fib


def test_success_base_conditions():
    '''
    test base conditions
    '''
    assert fib.fib_recursive(0) == 0
    assert fib.fib_recursive(1) == 1


def test_success_n_greater_1():
    '''
    test 3 values, where n>1
    '''
    assert fib.fib_recursive(3) == 4
    assert fib.fib_recursive(10) == 143
    assert fib.fib_recursive(15) == 1596


def test_success_fib_all():
    '''
    test all, and checks 3 values
    '''
    for f in [fib.fib_recursive, fib.fib_recursive_dp, fib.fib_iterative_dp]:
        assert f(3) == 4
        assert f(10) == 143
        assert f(15) == 1596


def test_success_fib_match():
    '''
    test all, and checks 5 random values match
    '''
    for n in range(5):
        val = random.randrange(0, 20)
        match = fib.fib_recursive(val) == fib.fib_recursive_dp(val) \
            == fib.fib_iterative_dp(val)
        assert (match)


def test_failure():
    '''
    test for raising an exception
    '''
    with pytest.raises(Exception):
        result = fib.fib_iterative_dp(-5)
        print(result)
