"""
NOTE:
    `left < j` and `right > i` checks make sure there is something to actually sort

O(n²)
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


array = [3, 2, 11, -1, 0]
print(sort(array, 0, len(array) - 1))
