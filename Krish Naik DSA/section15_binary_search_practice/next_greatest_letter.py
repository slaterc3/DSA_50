def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic
    target_num = ord(target)
    start = 0 
    end = len(letters) - 1 
    while start <= end:
        mid = (start + end) // 2
        if target == letters[mid]:
            return letters[mid+1]
        elif target < letters[mid]:
            end = mid - 1 
        else:
            start = mid + 1 
    return letters[0]
    
    
    # if target not in letters:
    #     return letters[0]
    # else:
    #     return letters[letters.index(target) + 1]

print(next_greatest_letter(['c', 'f', 'j'], 'c'))