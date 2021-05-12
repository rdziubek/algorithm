def kadane(array):
    max_so_far = 0
    max_ending_here = 0

    for i in array:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


"""EVALUATION"""
kadane(
    array=[0, 1, -10, 1, 2, 3]
)
