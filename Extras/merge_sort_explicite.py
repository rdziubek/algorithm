def sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = sort(array[:middle])
    right = sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


print(sort([3, 2, 11, -1, 0]))
