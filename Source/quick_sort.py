"""
1. Arrange elements relative to the pivot.
2. Execute quick-sort on left and right sides of the array (pivot denotes the middle).

NOTE:
    `left < j` and `right > i` checks make sure there is something to further sort.
    `right` is inclusive.

    Recursive calls use `j` and `i` indices instead of a middle index (used in merge-sort).

O(n²)
not stable
"""


def sort(array, left, right):
    i = left
    j = right

    pivot = array[(left + right) // 2]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if left < j:
        sort(array, left, j)
    if right > i:
        sort(array, i, right)

    return array
