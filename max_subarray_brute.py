def force_find(array):
    biggest = array[0]

    for i in range(len(array)):
        current = array[i]

        for j in range(len(array) - i):
            current += array[j] 
        
        biggest = current if current > biggest else biggest
    
    return biggest


print(force_find([0, 1, 0, 1, 2, 3]))
