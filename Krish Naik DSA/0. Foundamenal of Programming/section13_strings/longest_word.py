def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    # Your code here
    max_count = 0 
    curr_count = 0
    space_count = 0
    for char in s:
        if char != ' ':
            curr_count += 1 
        else:
            space_count += 1 
            if curr_count > max_count:
                max_count = curr_count 
            curr_count = 0 
    if space_count > 0:
        return max_count
    else:
        return curr_count
    
print(longest_word_length('helloworld'))
    
