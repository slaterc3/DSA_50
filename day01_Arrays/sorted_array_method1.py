def sorted_array(array):
    n = len(array)
    if n <= 0:
        return 
    # making a new 
    new = [0] * n 
    for i in range(n):
        new[i] = array[i] ** 2 
    new.sort() 
    return new 

print(sorted_array([-1, -2, 3, 5, 7]))
    