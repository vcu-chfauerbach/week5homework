"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    # retval = max(incoming_list)
    # return retval
    retval = None

    #   1,2,3,4,5,1
    # MAGIC_LOWNUMBER,    1    -> STORE 1
    # 1              ,    2    -> STORE 2
    # 2,                 3    -> STORE 3
    # 3,                 4    -> STORE 4
    # 4,                 5    -> STORE 5
    # 5,                 1    ->  ????   nothing

    # for value in incoming_list:
    #     if not retval:
    #        retval = value
    #    if value > retval:
    #        retval = value

    # return retval

    if not incoming_list:
        return None

    sorted_list = sorted(incoming_list)
    retval = sorted_list[len(sorted_list) - 1]
    return retval


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    if not incoming_list:
        incoming_list = []

    retval = min(incoming_list)
    return retval


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    if incoming_list:  # if incoming_list is not None and len(incoming_list) > 0
        retval = sum(incoming_list)
    else:
        retval = 0
    return retval


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if not incoming_dict:
        return None

    all_keys = incoming_dict.keys()
    if not all_keys:
        return None
    key_with_longest_value = None
    for key in all_keys:
        if not key_with_longest_value:
            key_with_longest_value = key

        if len(incoming_dict[key]) > len(incoming_dict[key_with_longest_value]):
            key_with_longest_value = key
    return key_with_longest_value
