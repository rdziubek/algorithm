"""

O(n²)
stable
in-place
"""


def sort(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array
