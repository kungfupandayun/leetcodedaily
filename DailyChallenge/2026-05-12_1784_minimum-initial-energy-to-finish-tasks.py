"""
LeetCode 1784. Minimum Initial Energy to Finish Tasks  (Hard)
Daily Challenge: 2026-05-12 (UTC)
Link: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/?envType=daily-question&envId=2026-05-12
Topics: Greedy, Array, Sorting

==============================  PROBLEM  ==============================

You are given an array `tasks` where `tasks[i] = [actual_i, minimum_i]`:

  - actual_i  is the actual amount of energy you spend to finish the i-th task.
  - minimum_i is the minimum amount of energy you require to begin the i-th task.

For example, if the task is [10, 12] and your current energy is 11, you cannot
start this task. However, if your current energy is 13, you can complete this
task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all tasks.

------------------------------- Examples -------------------------------

Example 1
  Input:  tasks = [[1,2],[2,4],[4,8]]
  Output: 8
  Explanation: Start with 8, do tasks in order 3, 2, 1.
               Starting with 7 fails because you can't start the 3rd task.

Example 2
  Input:  tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
  Output: 32

Example 3
  Input:  tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
  Output: 27

----------------------------- Constraints -----------------------------

  1 <= tasks.length <= 10^5
  1 <= actual_i <= minimum_i <= 10^4

==============================  APPROACH  =============================

Greedy + sorting.

Sort tasks by (minimum_i - actual_i) DESCENDING -- the bigger the "buffer" a
task demands, the earlier we should do it. Walk the sorted list, keeping a
running `energy`; whenever it dips below the current task's `minimum`, top up
the starting energy by the shortfall, then spend `actual` to finish the task.

Time:  O(n log n) for the sort.
Space: O(1) extra (ignoring the sort).
"""
from typing import List


# ==============================  SOLUTION  =============================

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        start = 0
        energy = 0
        for actual, minimum in tasks:
            if energy < minimum:
                start += minimum - energy
                energy = minimum
            energy -= actual
        return start


# ==============================   TESTS   =============================

if __name__ == "__main__":
    s = Solution()
    assert s.minimumEffort([[1, 2], [2, 4], [4, 8]]) == 8
    assert s.minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]) == 32
    assert s.minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]) == 27
    print("All sample tests passed.")
