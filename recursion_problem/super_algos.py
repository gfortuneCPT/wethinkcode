
def find_min(element):
    """finds minimum element in a list
    Args:
        element (list): list of int
    Returns:
        (int): smallest int in elements
    """
    if  not element or all(isinstance(item, int) for item in element) == False:
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        if element[0] < find_min(element[1:]):
            del element[1]
            return  find_min(element)
        else:
            del element[0]
            return  find_min(element)


def sum_all(element):
    """sum all elements of a list
    Args:
        element (list): list of int
    Returns:
        (int): sum of all int in list
    """
    if  not element or all(isinstance(item, int) for item in element) == False:
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        return element[0] + sum_all(element[1:])


def find_possible_strings(character_lst, n):
    """
    returns all permutations of character_lst of n length
    Args:
        character_lst (list): list of characters
        n (int): length of permutation of characters
    Returns:
        (list): list of permutations
    """
    out = []
    if  all(isinstance(item, str) for item in character_lst) == False:
        return []
    elif n == 1:
        return character_lst
    elif n > 1:
        for item in character_lst:
            for perm in find_possible_strings(character_lst, n-1):
                out += [item + perm]
    else:
        return []
    return out
