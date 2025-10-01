# Day 1 , One person discovers  secret.
# Delay: Each person will share the secret with a new person every day, starting from the day after they discover the secret.
# Forget: Each person will forget the secret forgetLimit days after they discover it. Forget day is not subject to share.
# n: Return the number of people aware of the secret at the end of day n. Return it modulo 10^9 + 7.

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        total = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                total += dp[day - delay]
            if day - forget >= 1:
                total -= dp[day - forget]
            dp[day] = total % MOD

        return sum(dp[n - forget + 1:n + 1]) % MOD
