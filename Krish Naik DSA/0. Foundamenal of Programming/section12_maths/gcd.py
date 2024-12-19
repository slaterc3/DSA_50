def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    biggest = 0
    if n < m:
        big, small = m, n
        
    else:
        big, small = n, m 
    
    if big % small == 0:
        return small 
    
    for i in range((small//2) + 1, 1, -1):
        if big % i == 0 and small % i == 0:
            return i 
    return 1

    
print(gcd(48, 18))
    