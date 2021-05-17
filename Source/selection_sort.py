"""
Each iteration, smallest element is found (and hence the quadratic big O).

NOTE:
    Looping through `len() - 1` avoids redundant last call
    swapping the last element with itself.

O(n²)
not stable
in-place
"""


def sort(array):
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array
