'''
https://leetcode.com/problems/longest-absolute-file-path/submissions/
https://www.youtube.com/watch?v=Ad9Qqhy43fE
'''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxLength=0
        depth_map={0:0}
        lines=input.split("\n")
        for line in lines:
            path=line.split("\t")[-1]
            depth=len(line)-len(path)
            if '.' in path:
                maxLength=max(maxLength,depth_map[depth]+len(path))
            else:
                depth_map[depth+1]= depth_map[depth]+len(path)+1
            
        return maxLength
                
        
        