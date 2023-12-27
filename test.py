
def add_three_numbers(a, b, c):
    """Add three numbers together."""
    return a + b + c

def multiply_three_numbers(a, b, c):
    """Multiply three numbers together."""
    return a * b * c

def algo_division(a, b, c):
    """ weird division """
    return multiply_three_numbers(a, b, c) / add_three_numbers(a, b, c)

def algo_substraction(a, b, c):
    """ weird substraction """
    return multiply_three_numbers(a, b, c) - add_three_numbers(a, b, c)


