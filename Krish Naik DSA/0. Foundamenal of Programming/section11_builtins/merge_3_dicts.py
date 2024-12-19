def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    # if len(dict1) != len(dict2) != len(dict3):
    #     return False 
    keys = []
    vals = []
    merged_dict = {}
    for d in [dict1, dict2, dict3]:
        for k, v in d.items():
            keys.append(k)
            vals.append(v)
    
    for i in range(len(keys)):
        merged_dict[keys[i]] = vals[i]
        
    return merged_dict
x, y, z = {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}
print(merge_three_dictionaries(x,y,z))

"""def merge_three_dictionaries(dict1, dict2, dict3):
    # Create a new dictionary that starts with the content of dict1
    merged_dict = dict1.copy()
    
    # Add the key-value pairs from dict2
    for key, value in dict2.items():
        merged_dict[key] = value
    
    # Add the key-value pairs from dict3
    for key, value in dict3.items():
        merged_dict[key] = value
    
    return merged_dict"""

"""Merge Multiple Dictionaries
Merge Three Dictionaries

Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

Parameters:

dict1 (Dictionary): The first dictionary to be merged.

dict2 (Dictionary): The second dictionary to be merged.

dict3 (Dictionary): The third dictionary to be merged.

Returns:

A single dictionary containing all key-value pairs from the three input dictionaries.

Example:

Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}"""