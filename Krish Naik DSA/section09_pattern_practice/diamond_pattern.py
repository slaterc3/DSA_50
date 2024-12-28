def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Initialize an empty list to store the rows of the diamond
    diamond = []
    
    # Generate the upper part of the diamond (including the middle row)
    for i in range(1, n + 1):
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        diamond.append(spaces + stars + spaces)
    
    # Generate the lower part of the diamond (mirrored upper part without the middle row)
    for i in range(n - 1, 0, -1):
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        diamond.append(spaces + stars + spaces)
    
    # Return the list of diamond rows
    return diamond

"""my solution:
   if n == 1:
        return ['*']
        
    lst = [0] * ((2*n)-1)
    
    # print(lst)
    for i in range((n)):
        spaces = (n - (i+1)) * ' '
        stars = (2*(i+1)-1) * '*'
        lst[i] = spaces + stars + spaces 
        lst[-(i+1)] = lst[i]
    return lst"""


# Diamond Pattern
# Problem Description:

# You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.



# Input:

# A single integer n, where 1 <= n <= 100.



# Output:

# A list of strings where each string represents a row in the diamond pattern.



# Example:

# Input: 3
# Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
# Input: 5
# Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']