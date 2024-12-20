def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    vowels = 'aeiou'
    
    vowel_count = 0
    
    for letter in list(s):
        if letter in vowels:
            vowel_count += 1 
            
    return vowel_count
    
print(count_vowels('Hello, World!'))