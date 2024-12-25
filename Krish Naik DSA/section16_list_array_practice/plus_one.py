def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    digit = 0 
    for i in range(0, len(digits)):
        idx = -(i+1)
        digit += digits[idx] * (10 ** i) 
    
    digit += 1 
    new_digit = str(digit)
    
    new_digits = []
    
    for c in new_digit:
        new_digits.append(int(c))
    
    # print(digits)
    return new_digits
            

print(plus_one([9,9,9]))