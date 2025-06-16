def binary_helper(num, width):
    """
    simpler way is to use built in python bin(<digit>)[2:]
    
    this returns a string representation of the binary with same width and length of list
    """
    return f"{num:0{width}b}"
    
    
def power_set(lst):
    """Will get power set of list based on:
        * size of power set is 2^n 
        * we can get an iterative solution by looking at the binary representation of each number 0 => n
            ** if  for ['a', 'b', 'c'], 101 (5) would yield ['a', 'c'], 010 (2) would yield ['b']
    """
    length_lst = len(lst)
    power_set_size = 2 ** length_lst
    result = [] # all subsets will go here
    for n in range(power_set_size):
        subset = [] # establish new subset
        binary = binary_helper(n, length_lst)
        for idx in range(length_lst):
            if binary[idx] == '1':
                subset.append(lst[idx])
        print(f'subset: {subset}')
        result.append(subset)
        print(f'result: {result}')
            # print(binary)
            
        
if __name__ == "__main__":
    power_set(['a', 'b', 'c'])