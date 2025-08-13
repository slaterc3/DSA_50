def i_sort(lst):
    
    for i in range(1, len(lst)):
        # start i at 2nd idx position
        # 1st index is sorted with itself
        j = i - 1
        while (j >= 0) and (lst[j] > lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j -= 1 
        
    return lst 
            
if __name__ == "__main__":
    lst = [5,4,3,2,1]
    new_lst = i_sort(lst)
    print(new_lst)