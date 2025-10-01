class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])

        dp = [[10000]*m for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1,n):
            for j in range(i):
                dp[i][j]=triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])


        return min(dp[n-1])
