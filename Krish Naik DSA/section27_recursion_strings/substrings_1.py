def find_substrings(s):
    """
    Function to find all substrings of a given string using recursion.

    Parameters:
    s (str): The input string.

    Returns:
    list of str: A list containing all substrings of the input string.
    """
    # Base case: if the string is empty, return an empty list
    if len(s) == 0:
        return []
    
    # Recursive case: get substrings of the rest of the string
    smaller_substrings = find_substrings(s[1:])
    
    # Generate substrings starting with the first character
    current_substrings = [s[:i+1] for i in range(len(s))]
    
    # Combine current substrings with the substrings from the recursive call
    return current_substrings + smaller_substrings

# Example usage
print(find_substrings("abc"))