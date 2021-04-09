"""
NOTE:
    j >= 0 and array[j] > inserted, not array[j] > inserted and j >= 0
    as array[j] will throw when j is < 0.

    Inserted element is placed at j + 1 instead of j to compensate
    for j's decrementation occurring in the while loop.
"""


def sort(array):
    for i in range(1, len(array)):
        inserted = array[i]

        j = i - 1
        while j >= 0 and array[j] > inserted:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = inserted

    return array


print(sort([3, 2, 11, -1, 0]))
