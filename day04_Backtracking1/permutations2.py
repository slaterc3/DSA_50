def permuteUnique(nums):
    res = [] 
    def helper(idx):
        if idx == len(nums) - 1:
            res.append(nums[:]) # get copy in res list
            return 
        hash_map = {}
        for j in range(idx, len(nums)):
            if nums[j] not in hash_map:
                hash_map[nums[j]] = True 
                nums[idx], nums[j] = nums[j], nums[idx]
                helper(idx + 1)
                nums[idx], nums[j] = nums[j], nums[idx]
    helper(0)
    return res 
    
print(permuteUnique([1,1,2]))