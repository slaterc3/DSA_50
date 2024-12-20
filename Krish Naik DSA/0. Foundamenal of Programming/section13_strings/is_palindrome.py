def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    
    string_list = s.split(" ")
    flat_string = "".join(string_list)
    flat_string = flat_string.lower()
    for i in range(len(flat_string)//2):
        if flat_string[i] != flat_string[-(i+1)]:
            return False 
    
    return True

print(is_palindrome('A man a plan a canal Panama'))