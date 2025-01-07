def findMinSubArrayBruteForce(s, arr):
    n = len(arr)
    min_length = float('inf')
    
    # Iterate over all possible starting points
    for i in range(n):
        _sum = 0
        # Iterate over all possible ending points for each start
        for j in range(i, n):
            _sum += arr[j]
            if _sum >= s:
                min_length = min(min_length, j - i + 1)
                break  # Stop further expansion since we found a valid subarray
    
    return min_length if min_length != float('inf') else 0