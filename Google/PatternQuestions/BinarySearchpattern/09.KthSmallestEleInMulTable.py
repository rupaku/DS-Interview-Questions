'''https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/submissions/960427132/'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num) -> bool:
            count = 0
            for val in range(1, m + 1):  # count row by row
                add = min(num // val, n)
                if add == 0:  # early exit
                    break
                count += add
            return count >= k                

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left 