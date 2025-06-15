

def power_set(my_list):
    if len(my_list) == 0:
        return [[]]
    
    print(f'length of my_list: {len(my_list)}')
    power_set_without_first = power_set(my_list[1:])
    
    print(f'power_set_without_first: {power_set_without_first}')
    
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    print(f'with_first: {with_first}')
    print(f'with_first + power_set_without_first: \n{with_first + power_set_without_first}')
    return with_first + power_set_without_first

if __name__ == "__main__":
    lst = ['a','b','c']
    power_set(lst)