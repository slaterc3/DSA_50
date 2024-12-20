def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    seen = set()
    final = []
    for letter in s:
        if letter not in seen:
            seen.add(letter)
            final.append(letter)

    return "".join(final)
    

print(remove_duplicates('programming')) #returns programin