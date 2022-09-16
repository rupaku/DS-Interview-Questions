''' https://leetcode.com/problems/unique-number-of-occurrences/submissions/ '''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store_freq= {}
        for i in arr:
            if i in store_freq:
                store_freq[i] += 1
            else:
                store_freq[i] = 1
        list_freq = list(store_freq.values())
        check_freq={}
        for i in list_freq:
            if i in check_freq:
                return False
            check_freq[i] =1
        return check_freq
        