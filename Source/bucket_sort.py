"""
1. Determine max value.
2. Make buckets.
3. Put into buckets.
4. Sort each bucket.
5. Print buckets.

NOTE:
    `array[i] / size` is not floored (by floor division, as opposed to
    the used integer cast from a real division) so as not to
    encounter rounding errors caused by truncating instead of
    rounding float numbers down.

    `j` figures actual bucket's index out.

    Elements 'overflowing' the bucket size are put into the last container.

    `max_value` parameter is dependent on the array though its calculation should not be reliant
    on the algorithm, hence the separation.

complexity and stability depends on sort used
"""

import insertion_sort


def sort(array, max_value):
    span = max_value / len(array)

    buckets = []
    for _ in range(len(array)):
        buckets += [[]]

    for i in range(len(array)):
        j = int(array[i] / span)
        if j != len(array):
            buckets[j] += [array[i]]
        else:
            buckets[j - 1] += [array[i]]

    for i in range(len(array)):
        insertion_sort.sort(buckets[i])

    result = []
    for i in range(len(array)):
        result += buckets[i]
    return result
