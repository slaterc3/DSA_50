def sorted_array(array):
    n = len(array)
    i, j = 0, n-1
    # creating the new array
    new = [0] * n 
    for k in reversed(range(n)):
        if array[i] ** 2 < array[j] ** 2:
            new[k] = array[j] ** 2 
            j -= 1 
        else:
            new[k] = array[i] ** 2 
            i += 1 
    return new 

x = sorted_array([-1,-2,3,4,9])
print(x)