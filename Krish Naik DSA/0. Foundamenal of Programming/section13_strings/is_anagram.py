def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    hash1 = {}
    hash2 = {}
    if len(s) != len(t):
        return False 
    for i in range(len(s)):
        if s[i] not in hash1:
            hash1[s[i]] = 1 
        else:
            hash1[s[i]] += 1 
        if t[i] not in hash2:
            hash2[t[i]] = 1 
        else:
            hash2[t[i]] += 1
    
    return hash1 == hash2
    
print(is_anagram("anagram", "nagaram"))