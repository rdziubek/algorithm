"""
1. Loop through all.
    a. Loop through all, swapping, omitting already swapped.

O() depends on sort used
"""

import bubble_sort


def order(array):
    return bubble_sort.sort(array)


print(order(['aab', 'aaa', 'aa', 'aaa']))
