def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # TODO: Implement this function
    # pass
    lst = [0] * len(ARR)
    for i in range(len(ARR)):
        lst[(i-D)] = ARR[i]
    return lst 
    
print(rotate_left([1,2,3,4,5], 2))