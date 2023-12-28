
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

def recursiveBinarySearch(list, item):
    """ recursive binary search algorithm """
    if len(list) == 0:
        return None

    mid = int(len(list) / 2)
    guess = list[mid]

    if guess == item:
        return mid

    if guess > item:
        return recursiveBinarySearch(list[:mid], item)

    else:
        return recursiveBinarySearch(list[mid + 1:], item)


# testing
assert binary_search([1, 2, 3, 4, 5], 5) == 4, "binary search algorithm failed, should return 4"
assert binary_search([], 3) == None
assert binary_search([1, 3, 5, 7, 9], 3) == 1
assert binary_search([1, 3, 5, 7, 9], 9) == 4

assert recursiveBinarySearch([1, 2, 3, 4, 5], 3) == 2
assert recursiveBinarySearch([], 2) == None
assert recursiveBinarySearch([1, 3, 5, 7, 9], 3) == 1
assert recursiveBinarySearch([1, 3, 5, 7, 9], 9) == 4
