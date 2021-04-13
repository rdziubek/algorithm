"""
1. Loop through all.
    a. Loop through all, swapping, omitting already swapped.

O(n^2) ; depends on sort used
"""


def order(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array


print(order(['aab', 'aaa', 'aa', 'aaa']))
