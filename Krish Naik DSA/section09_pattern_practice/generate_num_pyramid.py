def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    lst = [0] * n 
    # curr = 1 
    for i in range(1, n+1):
        # row = ' '.join(str(curr + j) for j in range(i))
        spaces = ' ' * (n-i)
        nums = ' '.join(str(j) for j in range(1, i+1))
        row = spaces + str(nums) + spaces
        # print(type(nums))
        lst[i-1] = row 
        # curr += i 
    return lst 

print(generate_number_pyramid(4))