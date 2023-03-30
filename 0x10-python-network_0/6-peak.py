#!/usr/bin/python3
"""A peak finding function"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak in the list of integers.
    """

    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    # Initialize left and right pointers
    left = 0
    right = len(list_of_integers) - 1

    # Loop while left pointer is less than right pointer.
    while left < right:

        # Find the middle index between left and right pointers.
        mid = (left + right) // 2

        # Compare element at mid index with its right neighbor at mid+1.
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Peak must be to the right of mid. Update left pointer to mid+1.
            left = mid + 1
        else:
            # Peak must be to the left of mid or at mid itself.
            right = mid

    # Return peak element at left pointer.
    return list_of_integers[left]
