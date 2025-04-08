def fib_tab(n):
    dp = [0] * (n + 1)
    
    if n > 0:
        dp[1] = 1 
    
    count = 1
    while count < n:
        count += 1 
        dp[count] = dp[count-1] + dp[count-2]
    print(dp)
    return dp[n]

print(fib_tab(5))