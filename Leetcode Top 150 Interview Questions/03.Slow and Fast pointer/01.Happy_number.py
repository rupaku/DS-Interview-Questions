#https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

# O(logn) O(1)

class Solution:
    def sum_of_sq_digit(n):
        total_sm =0
        while n > 0:
            n, rem = divmod(n,10)
            total_sm = total_sm + rem ** 2
        return total_sm

    def isHappy(self, n: int) -> bool:
        slow=n
        fast = Solution.sum_of_sq_digit(n)
        while fast != 1 and slow != fast:
            slow = Solution.sum_of_sq_digit(slow)
            fast = Solution.sum_of_sq_digit(Solution.sum_of_sq_digit(fast))

        if fast == 1:
            return True
        return False


        
