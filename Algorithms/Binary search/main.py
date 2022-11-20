def linear_search(given_list, value_to_find):
    for index, value in enumerate(given_list):
        if value == value_to_find:
            return index
    return -1


def binary_search(given_list, value_to_find):
    left_index = 0
    right_index = len(given_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = given_list[mid_index]
        if mid_value == value_to_find:
            return mid_index
        if mid_value < value_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(given_list, value_to_find, left_index=0, right_index=1):
    """
    This function is a recursive funciton
    :param given_list: Int list (already transformed :D)
    :param value_to_find: int value
    :param left_index: int (0) by default
    :param right_index: int (1) by default
    :return: the function returns the index of the given value or -1 by default if the value wasn't found
    """
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(given_list) or mid_index < 0:
        return -1

    mid_value = given_list[mid_index]
    if mid_value == value_to_find:
        return mid_index
    if mid_value < value_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(given_list, value_to_find, left_index, right_index)


given_list = input('Enter your list given_list separated by space "sorted or un-sorted it does not matter :P\n')
given_list_split_str = given_list.split(" ")
given_list_split = [int(item) for item in given_list_split_str]
given_list_split.sort()
value_to_find = int(input())

number_index = binary_search_recursive(given_list_split,value_to_find,right_index=len(given_list_split))
print(number_index)
