

def permute(nums):
    n = len(nums)
    # using helper function
    res = []
    def helper(idx):
        if idx == n-1:
            # appending copy of `nums`
            res.append(nums[:])
            return # simply return here
        for j in range(idx, n):
            # swapping the first time
            nums[idx], nums[j] = nums[j], nums[idx]
            # call the helper with idx incremented 1
            helper(idx+1)
            # the backtracking step to get to square one
            nums[idx], nums[j] = nums[j], nums[idx]
    helper(0)
    return res 
    
print(permute([1,2,3]))