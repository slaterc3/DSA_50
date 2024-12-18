def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    lst = [0] * (2*n-1)
    
    for i in range(n):
        spaces = i * ' '
        stars = (((2*n)-1) - (2*i)) * '*'
        # print(f"{i}: {spaces}, {stars}, {lst[i]}")
        lst[i] = spaces + stars + spaces 
        lst[-(i+1)] = lst[i]
        
    return lst 
    
print(generate_sandglass(5))