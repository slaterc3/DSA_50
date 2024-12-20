def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    count = 0 
    in_word = False 
    for char in s:
        if char != ' ':
            if not in_word:
                in_word = True 
                count += 1 
        else:
            in_word = False 
    return count