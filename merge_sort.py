def sort(array, left, right):
    if right - left <= 1:
        return

    middle = (left + right) // 2

    sort(array, left, middle)
    sort(array, middle, right)

    merge(array, left, middle, right)

    return array


def merge(array, left, middle, right):
    i = left
    j = middle

    merged = []

    while i < middle and j < right:
        if array[i] <= array[j]:
            merged += [array[i]]
            i += 1
        else:
            merged += [array[j]]
            j += 1

    while i < middle:
        merged += [array[i]]
        i += 1

    while j < right:
        merged += [array[j]]
        j += 1

    for i in range(len(merged)):
        array[left + i] = merged[i]


array = [3, 2, 11, -1, 0]
print(sort(array, 0, len(array)))
