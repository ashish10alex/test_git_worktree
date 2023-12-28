
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


def algo_addition(a, b, c):
    """ weird addition """
    return multiply_three_numbers(a, b, c) + add_three_numbers(a, b, c)

def binary_search(list, item):
    """Binary search algorithm."""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None

def recursive_binary_search(list, item):
    """ recursive binary search algorithm """
    if len(list) == 0:
        return None

    mid = int(len(list) / 2)
    guess = list[mid]

    if guess == item:
        return mid

    if guess > item:
        return recursive_binary_search(list[:mid], item)

    else:
        return recursive_binary_search(list[mid + 1:], item)
