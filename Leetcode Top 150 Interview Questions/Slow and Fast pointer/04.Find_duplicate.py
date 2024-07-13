#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-find-the-duplicate-number

#O(n) O(1)
def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow == fast:
            break
    slow=nums[0]

    while slow != fast:
        slow=nums[slow]
        fast=nums[fast]

    return fast