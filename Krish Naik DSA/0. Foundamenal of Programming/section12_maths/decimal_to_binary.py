def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n == 0:
        return '0'
    s = ''
    curr = abs(n) 
    while curr >= 1:
        binary_digit = str(curr%2)
        curr = curr//2
        s = s + binary_digit
    # print(s)
    if n < 0:
        s = '-' + s
    return s 
    
print(int_to_binary(-5))