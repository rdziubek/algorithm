"""
1. Return (let go) if none to sort
2. Divide
3. Repeat recursively
4. Sort by overwriting (by a reference) original

O(n log n)
stable
out-of-place
"""


def sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    left = []
    for i in range(mid):
        left.append(array[i])

    right = []
    for i in range(mid, len(array)):
        right.append(array[i])

    i = 0
    j = 0
    k = 0

    sort(left)
    sort(right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array
