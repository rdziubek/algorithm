def force_find(array):
    biggest = array[0]
    biggest_start = 0
    biggest_end = 0

    for i in range(len(array)):
        current = 0

        for j in range(i, len(array)):
            current += array[j]

            if current > biggest:
                biggest = current
                biggest_start = i
                biggest_end = j

    return biggest, biggest_start, biggest_end


"""EVALUATION"""
force_find(
    array=[0, 1, -10, 1, 2, 3]
)
