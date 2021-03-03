def parse(combination):
    result = ""
    for i in range(len(combination)):
        result += str(combination[i])
        if i < len(combination) - 1:
            result += " + "
    return result

def parse_multiple(combinations):
    result = [] 
    for i in combinations:
        result.append(parse(i))
    return result

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix
