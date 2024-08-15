# https://leetcode.com/problems/group-anagrams/description/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        #{('a','b','t'): ["bat","tab"]} sorted string key
        for i in strs:
            x="".join(sorted(i))
            if x in res:
                res[x].append(i)
            else:
                res[x]=[i]
                
        return list(res.values())
        