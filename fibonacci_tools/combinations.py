from .fib_term import fib_list

def next_closest_fib(num, list_of_fib):
    for value in reversed(list_of_fib):
        if value <= num:
            return value

def solve_helper(num, fibonacci_list):
    result = []
    while num > 0:
        temp = next_closest_fib(num, fibonacci_list)
        num -= temp
        result.append(temp)
    return result 

def solve(num):
    if (num <= 1):
        return [num] 
    return solve_helper(num, fib_list(num))

def solve_all_combinations(num):
    if (num <= 1):
        return [num]
    combinations, list_of_fib = [], fib_list(num)
    while len(list_of_fib) > 0:
        result = solve_helper(num, list_of_fib)
        fibonacci_list = filter_all_after(list_of_fib, result[0])
        if len(set(result)) == len(result):
            combinations.append(result)
        else:
            break
    return combinations

def filter_all_after(list_to_filter, num):
    target = list_to_filter
    for i in list_to_filter:
        if i >= num:
            target.remove(i)
    return target
