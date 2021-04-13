"""
1. Determine max value.
2. Make buckets.
3. Put into buckets.
4. Sort each bucket.
5. Print buckets.

NOTE:
    `array[i] / size` is not floored (by integer division, as opposed to
    the used integer cast) so as not to hinder negative value handling

O(n²)
"""

import insertion_sort


def sort(array, max_value):
    size = max_value / len(array)

    buckets = []
    for _ in range(len(array)):
        buckets += [[]]

    for i in range(len(array)):
        j = int(array[i] / size)
        if j != len(array):
            buckets[j] += [array[i]]
        else:
            buckets[len(array) - 1] += [array[i]]

    for i in range(len(array)):
        insertion_sort.sort(buckets[i])

    result = []
    for i in range(len(array)):
        result = result + buckets[i]
    return result


array = [3, 2, 11, -1, 0]
print(sort(array, max(array)))
