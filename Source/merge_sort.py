"""
NOTE:
    'right' is exclusive.


O(n log n)
stable
out-of-place
"""


def merge(array, left, middle, right):
    i = left
    j = middle

    merged = []

    while i < middle and j < right:
        if array[i] <= array[j]:
            merged.append(array[i])
            i += 1
        else:
            merged.append(array[j])
            j += 1

    while i < middle:
        merged.append(array[i])
        i += 1

    while j < right:
        merged.append(array[j])
        j += 1

    for i in range(len(merged)):
        array[left + i] = merged[i]


def sort(array, left, right):
    if right - left <= 1:
        return

    middle = (left + right) // 2

    sort(array, left, middle)
    sort(array, middle, right)

    merge(array, left, middle, right)

    return array
