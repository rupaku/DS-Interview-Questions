'''
https://leetcode.com/explore/interview/card/google/67/sql-2/3045/
https://www.youtube.com/watch?v=r2I7KIqHTPU
https://leetcode.com/explore/interview/card/google/67/sql-2/3045/discuss/217981/JavaC++Python-DP-using-Map-or-Stack
'''
class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher=  [0] * n
        next_lower =  [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        # print(stack) # [4]

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        # print(stack) #[4, 3, 2, 0]

        higher= [0] * n
        lower = [0] * n
        higher[-1] = 1
        lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
        