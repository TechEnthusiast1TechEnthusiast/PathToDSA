def uniquePaths(m,n):
    dp=[1]*n
    for _ in range(1,m):
        for j in range(1,n):
            dp[j]+=dp[j-1]
    return dp[-1]
print(uniquePaths(4,7))

