from functools import lru_cache

def fast_double(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return fib(n)[0]

@lru_cache(maxsize=50)
def fib(n):
    if n == 0:
        return (0, 1)

    f_n, f_n_minusOne = fib(n // 2)
    f_2n = f_n * (2 * f_n_minusOne - f_n)
    f_2n_minusOne = f_n ** 2 + f_n_minusOne ** 2 
    if n % 2 == 0:
        return (f_2n, f_2n_minusOne)
    return (f_2n_minusOne, f_2n + f_2n_minusOne)

def fib_list(num):
    i, results = 2, [0, 1]
    while results[-1] < num:
        results.append(fast_double(i))
        i += 1 
    return results 

def fib_which_term(num):
    list_of_fib = fib_list(num)
    if num not in list_of_fib:
        return "Not a fibonacci number"
    return len(fib_list(num)) - 1

def is_fib(num):
    return num in fib_list(num)
