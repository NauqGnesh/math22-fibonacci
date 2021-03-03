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

