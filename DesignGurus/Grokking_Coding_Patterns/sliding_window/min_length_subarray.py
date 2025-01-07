
def findMinSubArray(s, arr):
    # TODO: Write your code here
    _sum = 0 
    min_length = float('inf')
    l = 0 
    for r in range(len(arr)):
        _sum += arr[r]
        while _sum >= s:
            min_length = min(min_length, (r-l+1))
            _sum -= arr[l]
            l += 1 

    return min_length if min_length != float('inf') else 0

print(findMinSubArray(10,[1,1,1]))

print(findMinSubArray(7, [2,3,5,2,3,1]))

