def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    lst = [0] * n 
    curr = 1 
    for i in range(1, n+1):
        row = ' '.join(str(curr + j) for j in range(i))
        lst[i-1] = row 
        curr += i 
    return lst 
    
    
    
    # first = 1 
    # s = '1'
    # lst = [0] * n 
    # lst[0] = s 
    # for i in range(1, n):
    #     first += i 
    #     s = str(first)
    #     for j in range(1, i+1):
    #         s += ' ' + str(first+j)
    #     lst[i] = s 
    # return lst 
    
    # triangle = []
    
    # # Initialize the first number to be used in the triangle
    # current_num = 1
    
    # # Loop through each row from 1 to n
    # for i in range(1, n + 1):
    #     # Create a row by collecting the next i numbers
    #     row = ' '.join(str(current_num + j) for j in range(i))
    #     # Append the row to the list
    #     triangle.append(row)
    #     # Update the current number for the next row
    #     current_num += i
    
    # # Return the list of rows
    # return triangle
    
print(generate_floyds_triangle(3))



# Floyds Triangle
# Problem Description:

# You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.



# Input:

# A single integer n, where 1 <= n <= 100.



# Output:

# A list of strings where each string represents a row in Floyd's Triangle.



# Example:

# Input: 5
# Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
 
# Input: 3
# Output: ['1', '2 3', '4 5 6']