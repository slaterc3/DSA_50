def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = [0] * n 
    
    for i in range(1, n+1):
        
        idx = i-1 
        if i == 1:
            lst[idx] = '*'
        elif i > 1 and i < n:
            spaces = (i - 2) * ' '
            lst[idx] = '*' + spaces + '*'
        else:
            lst[idx] = '*' * n
    return lst 
    

print(generate_hollow_right_angled_triangle(5))