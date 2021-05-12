"""
1. Loop through all (start from second element).
    a) Continually, if preceding element > current, shift (not swap) it into current one's place.
        (This is done towards the beginning of the array, until either array's end
        or a smaller element is encountered.)
    b) Replace last swapped element with the one which value was being used to shift elements.

NOTE:
    j >= 0 and array[j] > inserted, not array[j] > inserted and j >= 0
    as array[j] will throw when j is < 0.

    Inserted element is placed at j + 1 instead of j to compensate
    for j's decrementation occurring in the while loop.

O(n²)
stable
in-place
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
