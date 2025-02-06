def is_balanced(S):
    #Write down your code here
    hashmap = {
        "}": "{", 
        ")": "(",
        "]": "["
    }
    stk = []
    for c in S:
        if c not in hashmap:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != hashmap[c]:
                    return False 
    
    return not stk 
    
print(is_balanced("({}"))