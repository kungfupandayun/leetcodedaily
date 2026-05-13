"""
URL: https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
Title: Minimum Moves to Make Array Complementary
Difficulty: Medium

Problem:
You are given an integer array nums of even length n and an integer limit.
In one move, you can replace any integer from nums with another integer between
1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed),
nums[i] + nums[n - 1 - i] equals the same number.
For example, [1,2,3,4] is complementary because nums[i] + nums[n-1-i] = 5 for all i.

Return the minimum number of moves required to make nums complementary.

Constraints:
- n == nums.length
- 2 <= n <= 10^5
- 1 <= nums[i] <= limit <= 10^5
- n is even

Source: LeetCode GraphQL API (activeDailyCodingChallengeQuestion)
"""

from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        Difference array approach: O(n + limit).

        For each symmetric pair (a, b) = (nums[i], nums[n-1-i]), the target sum T
        can range from 2 to 2*limit. We classify each T by how many moves the pair needs:
          - 0 moves if T == a + b  (already correct)
          - 1 move  if T in [min(a,b)+1, max(a,b)+limit]  (replace the "wrong" element)
          - 2 moves otherwise

        We start every pair at cost 2, then subtract 1 over the 1-move range, and
        subtract 1 more at exactly T = a+b. A difference (delta) array lets us do all
        range updates in O(1) and recover the actual costs in one prefix-sum pass.
        """
        n = len(nums)
        # delta array indexed from 0; valid targets are [2, 2*limit]
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
            s = a + b

            # Add 2 for all targets [2, 2*limit]
            delta[2] += 2
            delta[2 * limit + 1] -= 2

            # Subtract 1 over the range where 1 move suffices: [lo+1, hi+limit]
            delta[lo + 1] -= 1
            delta[hi + limit + 1] += 1

            # Subtract 1 more at T = s (0 moves needed)
            delta[s] -= 1
            delta[s + 1] += 1

        # Prefix sum to find cost at each target; return the minimum
        ans = float('inf')
        curr = 0
        for t in range(2, 2 * limit + 1):
            curr += delta[t]
            ans = min(ans, curr)

        return ans


if __name__ == "__main__":
    s = Solution()

    # Example 1: change nums[2] from 4 to 2 → all pairs sum to 4
    assert s.minMoves([1, 2, 4, 3], 4) == 1, "example 1"

    # Example 2: must change both outer elements → 2 moves
    assert s.minMoves([1, 2, 2, 1], 2) == 2, "example 2"

    # Example 3: already complementary (all pairs sum to 3)
    assert s.minMoves([1, 2, 1, 2], 2) == 0, "example 3"

    # Extra: single pair already equal, limit allows no other target with 0 moves
    assert s.minMoves([3, 3], 5) == 0, "extra 1 — pair sums to 6, already complementary"

    # Extra: must change one element in each pair
    assert s.minMoves([1, 1, 1, 1], 2) == 0, "extra 2 — all pairs already sum to 2"

    print("All assertions passed!")
